    #!/usr/bin/env python
# encoding: utf-8

from common import mongo
import requests
import config

collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB,  "spiders")

API_WORKER = "http://localhost/crawler/thread_count"

def get_thread_workers():
    try:
        data_worker = requests.get(API_WORKER).json()
    except:
        data_worker = None
    return data_worker

def count_spiders(spiders):
    count = 0
    if spiders:
        for spider in spiders:
            count += 1
    return count

def get_list_spiders(spiders_data):
    try:
        if spiders_data['running_spiders']:
            spiders = []
            for source in spiders_data['running_spiders']:
                spiders.append(source['name'])
            return spiders
    except TypeError:
        spiders = []
        for spider in spiders_data:
            spiders.append(spider['doc']['spider'])
        return spiders
    
    
def get_total_spds():
    total_spiders = collection.find({"doc.images": {"$exists":1}})
    return total_spiders

def count_total_spiders(total_spiders):
    if total_spiders:
        return count_spiders(total_spiders)
    else:
        return 0

def get_spds_stt_pending():
    pending_spiders = collection.find({"$and": [{"doc.images": {"$exists":1}},
                                                {"crawler_status.last_stop_time": {"$exists":1}},
                                                {"crawler_status.status": 0},
                                                {"$or" : [{"doc.status": 1},
                                                          {"doc.status": "1"}]}]})
    return pending_spiders
   
    
def count_spds_stt_pending(pending_spiders):
    if pending_spiders:
        return count_spiders(pending_spiders)
    else:
        return 0
    
def get_spds_stt_running():
    spiders = collection.find({"crawler_status.status":1})
    running_spiders = []
    for spider in spiders:
        running_spiders.append(spider)
    return running_spiders

def count_spds_stt_running(running_spiders):
    if running_spiders:
        return count_spiders(running_spiders)
    else:
        return 0

def merge_spiders_on_workers(running_spiders_w1, running_spiders_w2):
    spd_run_on_wkers = []
    spd_run_on_wkers.extend(running_spiders_w1)
    spd_run_on_wkers.extend(running_spiders_w2)
    return spd_run_on_wkers

def get_spiders_not_running(spds_stt_running, spd_run_on_wkers):
    spiders_not_running = []
    if spds_stt_running:
        for spider in spds_stt_running:
            if spider not in spd_run_on_wkers:
                spiders_not_running.append(spider)
    return spiders_not_running

def get_spiders_missing(spds_stt_running, spd_run_on_wkers):
    spiders_missing = []
    for spider in spd_run_on_wkers:
        if spider not in spds_stt_running:
            spiders_missing.append(spider)
    return spiders_missing

def get_spiders_duplicate(running_spiders_w1, running_spiders_w2):
    spiders_dup = []
    for spider in running_spiders_w1:
        if spider in running_spiders_w2:
            spiders_dup.append(spider)
    return spiders_dup

def get_debugCrawler():
    debugCrawler = {}
    spiders_stt_running = get_spds_stt_running()
    spds_stt_running = get_list_spiders(spiders_stt_running)
    
    data_worker = get_thread_workers()
    spds_running = get_list_spiders(data_worker)
#     spds_merge = merge_spiders_on_workers(spds_running_w1, spds_running_w2)
    
    debugCrawler['not_running'] = get_spiders_not_running(spds_stt_running, spds_running)
    debugCrawler['missing'] = get_spiders_missing(spds_stt_running, spds_running)
#     debugCrawler['duplicate'] = get_spiders_duplicate(spds_running_w1, spds_running_w2)
    
    return debugCrawler

def fixBugSpiderNotRun(option):
    debugs = get_debugCrawler()
    if option == "" or option is None:
        json_update = {
                       'crawler_status.server_running' : None,
                       'crawler_status.status' : 0
                       }
        for spider_name in debugs['not_running']:
            collection.update({"doc.spider": spider_name} , {"$set":json_update},upsert=False, multi=False)
    return "Fixed!"
        
