#!/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 24, 2016

@author: Quyet
'''
from common import mongo
import requests
coll = mongo.connectCol('staging', 'crawler', 'spiders')


def getSpiderGood():
    spiders = coll.find({"crawler_status.last_stop_time": {"$exists":1}})
    print spiders.count()
    spider_names = []
    for spider in spiders:
        spider_names.append(spider['doc']['spider'])
    return spider_names


def generateSpiderGood():
    spider_names = getSpiderGood()
    count = 1
    for spider in spider_names:
        print "Generate: ", count, spider
        requests.get("http://localhost:6081/generate?spider=" + spider)
        count += 1
    print "Done!"

if __name__=="__main__":
    generateSpiderGood()
