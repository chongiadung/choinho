#!/usr/bin/env python
# encoding: utf-8
"""
scraper_service.py

Created by Toan Vinh Luu on 2013-01-10.
Copyright (c) 2013 Chongiadung.vn Inc. All rights reserved.
"""

import os
import psutil
import subprocess
import time
import requests
import hashlib, urlparse
from common import mongo, util
from common.logger import logging
from common.util import getFileNameFromSpiderName
from scrapy import Selector
import config
import datetime
import codecs

def execute(commands):
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return '=====>OUTPUT:\n' + out + '\n=====>ERROR:\n' + err

def insertSpider(document):
    collection      = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, "spiders")
    data = {'doc': document,
            'last_modified': time.time()}
    
    data['doc']['_id'] = hashlib.md5(data['doc']['spider']).hexdigest()
    res = collection.update( {'doc.spider' : document['spider']} , {"$set":data}, upsert=False, multi=False)
    if not res['updatedExisting']:
        data['crawler_status.last_stop_time'] = time.time()-86400*14
        data['crawler_status.status'] = 0
        data['created'] = time.time()
        res = collection.update( {'doc.spider' : document['spider']} , {"$set":data}, upsert=True, multi=False)
    return res

def generateSpider(spider_name, over_write):  
    logging.info('generateSpider')
    commands = []
    commands.append(config.PYTHON)
    commands.append('generator/runner.py')
    commands.append('generator/generate.py')
    commands.append('--mongo_server')
    commands.append(config.MONGO_SERVER)
    commands.append('--spider_name') 
    commands.append(spider_name)
    commands.append('--spider_template')
    commands.append('generator/spider_template.django.py') 
    commands.append('--output_spider_py')
    commands.append('scraper/spiders/' + getFileNameFromSpiderName(spider_name))
    commands.append('--over_write')
    commands.append(str(over_write))
    commands.append('--storage_spider_template')
    commands.append('generator/storage_spider_template.django.py') 
    commands.append('--output_storage_py')
    commands.append('scraper/storage_spiders/' + getFileNameFromSpiderName(spider_name))
    logging.info(" ".join(commands))
    msg = execute(commands)
    return msg

def stopCrawl(spider_name):
    logging.info('stopCrawl')
    commands = 'ps -ef | grep python | grep ' + spider_name + '  | grep -v grep | awk \'{print $2}\' | xargs kill -2'
    logging.info(" ".join(commands))
    os.system(commands)
    return '/crawler/taillog?spider=' + spider_name

def stopAllSpider():
    logging.info('stopAllSpider')
    commands = 'ps -ef | grep python | grep scrapy | grep -v grep | awk \'{print $2}\' | xargs kill -2'
    logging.info(" ".join(commands))
    os.system(commands)
    return 'Done!'
    
def startCrawl(spider_name):
    logging.info('startCrawl')
    logFile = config.LOG_DIR + 'logs_crawl/' + spider_name + '.log'
    jobdir_crawl = config.LOG_DIR + 'crawls/' + spider_name
    #kill process
    commands = 'ps -ef | grep python | grep ' + spider_name + '  | grep -v grep | awk \'{print $2}\' | xargs kill -2'
    logging.info(" ".join(commands))
    os.system(commands)
    commands = 'scrapy crawl ' + spider_name + ' -s JOBDIR=' + jobdir_crawl + ' &> ' + logFile + ' &'
    logging.info(" ".join(commands))
    os.system(commands)

    return '/crawler/taillog?spider=' + spider_name

def tailLog(spider_name, number_lines, files=None):
    logging.info('tailLog')
    if files:
        logFile = config.LOG_DIR + "/" + spider_name + '_from_'+ files +'.log'
    else:   
        logFile = config.LOG_DIR + "/logs_crawl/" + spider_name + '.log'
    commands = []
    commands.append('tail')
    commands.append('-' + str(number_lines))
    commands.append(logFile)
    msg = execute(commands)
    return msg

def threadCount():
    collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, 'spiders')
    commands = 'ps -ef| grep scrapy'
    msg = subprocess.Popen(commands, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = msg.communicate()
    list_spiders = []
    output = {}
    p = psutil.Process(os.getpid())
    cpu_usage = psutil.cpu_percent(interval=1.0)
    memory_usage = p.memory_percent()
    
    list_res = out.split('\n')
    for item in list_res:
        if item.find("crawl") >0:
            start = item.find("crawl") + 6
            res = item[start:]
            spider_name = res.split(' ')[0]
            last_start = getLastStartSpider(collection, spider_name)
            if not last_start:
                continue
            spider_info = {'name': spider_name,
                           'last_start': last_start}
            list_spiders.append(spider_info)
    output['percent_cpu_usage'] = cpu_usage
    output['percent_mem_usage'] = round(memory_usage)
    output['total_crawler_thread'] = len(list_spiders) 
    output['running_spiders'] = list_spiders
    return output

def getLastStartSpider(collection, spider_name):
    spider = collection.find_one({"doc.spider": spider_name})
    if spider:
        time = spider['crawler_status'].get('last_start_time', 0)
        return datetime.datetime.fromtimestamp(int(time)).strftime('%d-%m-%Y %H:%M:%S')
    return None

def getAllSpidersRunning():
    collection      = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, "spiders")
    spiders = collection.find({"crawler_status.status":1})
    list_spiders = []
    for spider in spiders:
        list_spiders.append(spider['doc']['spider'])
    return list_spiders

def delete_spider_mongo(spider_name):
    collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, "spiders")
    collection.delete_one({'doc.spider': spider_name})

def delete(spider_name, _type):
    if _type == "dir":
        commands = 'rm -rf ' + config.LOG_DIR + 'crawls/' + spider_name
    elif _type == "py":
        commands = 'rm -rf ' + config.CRAWL_DIR + 'scraper/spiders/' + getFileNameFromSpiderName(spider_name)
    elif _type == "all":
        delete_spider_mongo(spider_name)
        commands = 'rm -rf ' + config.LOG_DIR + 'crawls/' + spider_name
        commands += ' && rm -rf ' + config.CRAWL_DIR + 'scraper/spiders/' + getFileNameFromSpiderName(spider_name)
    logging.info(" ".join(commands))
    msg = os.system(commands)
    return msg

def parse_item(spider, req):
    item = {}
    item['source'] = spider['doc']['spider']
    fields = ['name', 'price', 'category', 'description', 'images', 'canonical', 'base_url', 'brand', 'in_stock', 'guarantee', 'promotion']
    xpath_dict = spider['doc']
    data = req.content
    hxs = Selector(text=data)
    for k, v in xpath_dict.iteritems():
        if k in fields and v != '':
            if k == "description":
                item["description"] = hxs.xpath(v.encode('ascii') + "/node()").extract()
            else:
                item[k] = util.cleanText(hxs.xpath(v.encode('ascii')).extract())
    return item

def get_requests(url):
    HDR = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
    try:
        req = requests.get(url, headers=HDR, allow_redirects=False, timeout = 20)
        return req
    except Exception as e:
        logging.exception(e)
        logging.info("Get content from %s null", url)
        return None

def get_xpath(spider_name):
    coll = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, 'spiders')
    spider = coll.find_one({'doc.spider' : spider_name})
    return spider

def get_spider_name_from_url(url):
    uri = urlparse.urlparse(url)
    return uri.netloc.replace('www.', '')

def check_parse_item(url):
    spider_name = get_spider_name_from_url(url)
    return parse_item(get_xpath(spider_name), get_requests(url))

def get_spider_history(spider_name):
    collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, 'stats')
    spider_history = collection.find_one({'spider': spider_name})
    if spider_history:
        return spider_history
    return None

def get_number_spiders_started(days):
    now = time.time()
    query = {'last_history.start_time': {'$gte': now - days*24*60*60}}
    collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, 'stats')
    results = collection.find(query)
    spiders = []
    if results:
        for spider in results:
            spiders.append(spider['spider'])
    return {'number_hit': len(spiders), 'hits': spiders}

def get_number_spiders_stopped(days):
    now = time.time()
    query = {'last_history.finish_time': {'$gte': now - days*24*60*60}}
    collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, 'stats')
    results = collection.find(query)
    spiders = []
    if results:
        for spider in results:
            spiders.append(spider['spider'])
    return {'number_hit': len(spiders), 'hits': spiders}

def get_number_spider_created(days):
    now = time.time()
    query = {'created': {'$gte': now - days*24*60*60}}
    collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, 'spider')
    results = collection.find(query)
    spiders = []
    if results:
        for spider in results:
            spiders.append(spider['spider'])
    return {'number_hit': len(spiders), 'hits': spiders}

def get_blacklist_category():
    coll = mongo.connectCol('proc', 'category', 'category_blacklist')
    results = coll.find()
    categories = []
    for cat in results:
        categories.append(cat['feature'])
    return categories

def update_category_blacklist():
    blacklist_file = codecs.open(config.CRAWL_DIR + '/service/category_blacklist.py', 'w+', 'utf-8')
    contents = '#!/usr/bin/env python\n# encoding: utf-8\nBLACKLIST = ['
    category_blacklist = get_blacklist_category()
    contents += '\'' + '\', \''.join(category_blacklist) + '\']'
    blacklist_file.write(contents)
    blacklist_file.close()

def main():
    pass


if __name__ == '__main__':
    main()
