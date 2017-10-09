#!/usr/bin/env python
# encoding: utf-8
import math
from common import mongo
import time
from operator import itemgetter
import requests
from requests.exceptions import ConnectionError, Timeout
from time import sleep
from common.logger import logging
import config
from pymongo.errors import NetworkTimeout, ServerSelectionTimeoutError

# NOW = time.time()
collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, "spiders")
CRAWLER_SERVERS_CONFIG = [
#     {'name_server':'crawl1', 'max_thread':25, 'free_thread':25, 'status':True},
#     {'name_server':'crawl2', 'max_thread':25, 'free_thread':25, 'status':True},
    {'name_server':'crawler', 'max_thread':40, 'free_thread':40, 'status':True},
    ]
SERVER_PORT = '6081'

def getAllValidSpiders():
    one_day_ago = time.time() - 24*60*60
    spiders = collection.find({"$and":[{"crawler_status.last_stop_time": {"$exists":1}},
                                       {'crawler_status.last_stop_time': {"$lt": one_day_ago}},
                                       {"$or":[{"doc.status": "1"},{"doc.status": 1}]},
                                       {"crawler_status.status":0}
                                       ]})
    return spiders

def calculateSpiderScore(priority, crawled_time, number_items, status):
#     crawled_time = (float(NOW) - time)  / 3600
    if number_items == 0 or number_items == 1: number_items = 1000
    if crawled_time is not None and crawled_time < 336:
        if number_items <= 0: number_items = 1000
        score = (-1)**int(status)*priority*crawled_time**2*math.log(math.fabs(number_items))
    else:
        score = (-1)**int(status)*priority*crawled_time**3*math.log(math.fabs(number_items))
        
    return score

def sortListSpiders(list_spiders):
    try:
        return sorted(list_spiders,key=itemgetter('score'),reverse=True)
    except (KeyError):
        return None

def buildListCrawlSpiders():
    validSpiders =  getAllValidSpiders()
    list_spiders = []
    now = time.time()
    spider = {}
    logging.info("=====>Please wait, we're building spider list...")
    try:
        for spi in validSpiders:
            try:        
                spider['name'] = spi['doc']['spider']
                crawled_time = (float(now) - spi['crawler_status']['last_stop_time'])  / 3600
                spider['score'] = calculateSpiderScore(spi['crawler_status'].get('priority', 1), crawled_time , spi['crawler_status'].get('items', 1000) , spi['crawler_status']['status']) 
                list_spiders.append(spider)
                spider = {}
            except KeyError:
                continue
    except NetworkTimeout, ServerSelectionTimeoutError:
        sleep(60)
    return sortListSpiders(list_spiders)


def chooseSpider(list_spiders):
    if list_spiders is not None and len(list_spiders) > 0:
        return list_spiders[0]
    return None


def getCrawlerServerConfig():
    return CRAWLER_SERVERS_CONFIG

def set_free_thread(server):
    if server['free_thread'] > 0:
        server['free_thread'] = server['free_thread'] - 1
    return server
        
def updateCrawlerServers(server, crawler_servers):
    crawler_servers[0] = server
    return crawler_servers

def getCrawlerServers():
    global spiders_running
    spiders_running = []
    config_servers = getCrawlerServerConfig()
    crawler_servers = []
    for server in config_servers:
        crawler = {}
        crawler['name_server'] = server['name_server']
        crawler['max_thread'] = server['max_thread']
        crawler['free_thread'] = server['free_thread']
        crawler['status'] = server['status']
        try:
            resp = requests.get('http://'+server['name_server']+'.localhost:'+SERVER_PORT+'/crawler/thread_count')
            data = resp.json()
            spiders_running.extend(data['running_spiders'])
            free_thread = server['max_thread'] - data['total_crawler_thread']
            if free_thread <= 0:
                crawler['free_thread'] = 0
            else:
                crawler['free_thread'] = free_thread
        except (Timeout, ConnectionError):
            logging.error("Connection error at %s", server['name_server'])
            crawler['status'] = False
        except:
            logging.error("Error at %s", server['name_server'])
            crawler['status'] = False
        crawler_servers.append(crawler)
    return crawler_servers
    
            
def sortCrawlerServers(list_crawler_server):
    return sorted(list_crawler_server, key=itemgetter('status','free_thread'), reverse=True)


def chooseCrawlerServer(list_crawler_server):
    list_crawler_server = sortCrawlerServers(list_crawler_server)
    server = None
    if list_crawler_server[0]['status'] == True and list_crawler_server[0]['free_thread'] > 0:
        server = list_crawler_server[0]
    return server, list_crawler_server

def startSpider(spider_name, crawler_server):
    if spider_name is not None:
        if spider_name in spiders_running:
            logging.error("Spider name \"%s\" running", spider_name)
            spider = collection.find_one({'doc.spider':spider_name})
            logging.info("Info spider: %s", spider['crawler_status'])
            return crawler_server
        try:
            requests.get('http://'+crawler_server['name_server']+'.localhost:'+SERVER_PORT+'/crawler/startcrawl?spider='+spider_name)
            crawler_server = set_free_thread(crawler_server)
            logging.info("Start spider \"%s\" successful at \"%s\"!", spider_name, crawler_server['name_server'])
        except (Timeout, ConnectionError):
            crawler_server['status'] = False
            logging.error("Start spider \"%s\" failed at \"%s\"!", spider_name, crawler_server['name_server'])
    else:
        logging.error("Spider is None!")
    return crawler_server

def startServiceMaster():
    logging.info("Start master-service!")
    list_crawler_servers = getCrawlerServers()
    list_spiders = buildListCrawlSpiders()
    count_start = 0
    if list_spiders is not None and len(list_spiders) > 0:
        for spider in list_spiders:
            crawler_server, list_crawler_servers = chooseCrawlerServer(list_crawler_servers)
            if crawler_server is not None:
                crawler_server = startSpider(spider['name'], crawler_server)
                list_crawler_servers = updateCrawlerServers(crawler_server, list_crawler_servers)
                count_start += 1
            else:
                logging.info("=======> All crawler servers were full!")
                break
        logging.info("Started %d spiders." % (count_start))
    else:
        logging.error("No result from MongoDb!")


def main():   
    startServiceMaster()
    
    
if __name__ == '__main__':
        main()
