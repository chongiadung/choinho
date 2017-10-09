#!/usr/bin/env python
# encoding: utf-8
"""
crawled_products_service.py

Created by Toan Vinh Luu on 2014-01-29.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""

import sys
import os
import time
import requests, json
import config

from common.logger import logging

def getItems(start, limit, sincedays = None, beforedays = None, source = None, facetsize = 100, missing = None, exists = None, expired = None,sort=None):
    ITEM_URL = 'http://' + config.ES_SERVER + ':' + config.ES_PORT + '/' + config.CRAWLED_PRODUCTS + '/timcho_item/_search'
    now = time.time()

    daySeconds = 60 * 60 * 24

    timeQuery = {}
    if beforedays is not None:
        dayThreshold = now - daySeconds * float(beforedays)
        timeQuery["lte"] = dayThreshold

    if sincedays is not None:
        dayThreshold = now - daySeconds * float(sincedays)
        timeQuery["gte"] = dayThreshold

    mustQuery = [
        {
            "range" : {
                "timestamp" : timeQuery
            }
        }
    ]

    if source is not None:
        mustQuery.append({"term" : { "source" : source }})

    if expired is not None:
        mustQuery.append({"term" : { "expired" : expired}})
    if sort is None:
        sortQuery = [{ "timestamp" : {"order" : 'desc'}}]
    else:
        sortQuery   = []
        fields      = sort.split(",")
        for field in fields:
            tokens      = field.split(" ")
            fieldName   = tokens[0]
            order       = tokens[1]
            sortQuery.append({fieldName:{"order":order}})

    dslQuery = {
        "query": {
            "bool" : {
                "must": mustQuery
            }
        },
        "aggs" : {
            "source" : {
                "terms" : {
                    "field" : "source",
                    "size" : facetsize,
                    "shard_size": facetsize * 2
                    
                }
            }
        },
        "sort" : sortQuery,
        "size" : limit,
        "from" : start
    }

#     if missing is not None:
#         fields = missing.split(',')
#         andFields = []
#         for missingField in fields:
#             missingQuery = {
#                 "missing" : {
#                     "field" : missingField,
#                     "existence" : True,
#                     "null_value" : True
#                 }
#             }
#             andFields.append(missingQuery)
# 
#         dslQuery['query']['filtered']['filter'] = {
#             "and": andFields
#         }
        
        
    if missing:
        fields = missing.split(',')
        existFileds = []
        for field in fields:
            existField = {
                "exists": {
                    "field": field
                }
            }
            existFileds.append(existField)
            
        dslQuery['query']['bool']['must_not'] = existFileds

    
#     if exists is not None:
#         fields = exists.split(',')
#         andFields = []
#         for existsField in fields:
#             existsQuery = {
#                 "exists" : {
#                     "field" : existsField,
#                 }
#             }
#             andFields.append(existsQuery)
#  
#         dslQuery['query']['filtered']['filter'] = {
#             "and": andFields
#         }
        
        
    if exists:
        fields = exists.split(',')
        existFileds = []
        for field in fields:
            existField = {
                "exists": {
                    "field": field
                }
            }
        existFileds.append(existField)
        
        dslQuery['query']['bool']['filter'] = existFileds
    
#     print json.dumps(dslQuery, indent=4, ensure_ascii=False)
#     print '====================================================\n'

    # print json.dumps(dslQuery)
    #  print ITEM_URL
    r = requests.get(ITEM_URL + '?fields=timestamp,url,source' , data = json.dumps(dslQuery))
    data =  json.loads(r.text)
#     print json.dumps(data, indent = 4)
#     print data
    response = {}
    response['start'] = start
    response['limit'] = limit
    response['sincedays'] = sincedays
    response['beforedays'] = beforedays
    response['sources'] = []
    if 'aggregations' in data:
        for source in data['aggregations']['source']['buckets']:
            response['sources'].append({'source': source['key'], 'count': source['doc_count']}) # key / doc_count
    response['num_sources'] =  len(response['sources'])
    response['total_items'] = data['hits']['total']
    response['hits'] = []
    for hit in data['hits']['hits']:
        timestamp = hit['fields']['timestamp']
        numDays = ((now - timestamp[0])/daySeconds)
        response['hits'].append({
                                'id' : hit['_id'], 
                                'time': time.ctime(timestamp[0]), 
                                'url' : hit['fields']['url'], 
                                'days' : numDays, 
                                'source' : hit['fields']['source']
                                })

    return response

def main():
    print json.dumps(getItems(0, 10, sincedays = 30, beforedays = None, source = None, facetsize = 100, missing = 'expired', expired = None,sort=None), indent = 4)


if __name__ == '__main__':
	main()

