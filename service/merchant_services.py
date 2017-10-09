# -*- coding: utf-8 -*-
import json
import requests
import time
import os
from common import mongo
import random

def connectDatabase(db_name):
    return mongo.connectCol("staging", "hello", db_name)

def getMerchantCompany(company_name):
    collection      = connectDatabase('merchants')
    res             = collection.find( {'merchant_name':  company_name}).count()
    return res

def getMerchantSite(company_site):
    collection      = connectDatabase('merchants')
    res             = collection.find( {'merchant_spider':  company_site}).count()
    return res

def getZone():
    collection      = connectDatabase('zone')
    res             = list(collection.find({}, {'_id':0}).sort("name"))
    output          = json.dumps(res)
    return output

def getDistrict(city_id):
    collection      = connectDatabase('district')
    res             = list(collection.find({'city_id':int(city_id)}, {'_id':0}).sort("district_name"))
    output          = json.dumps(res)
    return output

def addMerchant(data):
    collection      = connectDatabase('merchants')
    data            = json.loads(data)
    res             = collection.insert(data)
    return res

if __name__ == '__main__':
    getZone()