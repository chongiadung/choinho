#!/usr/bin/env python
# encoding: utf-8
"""
crawled_product_indexer.py

Created by Toan Vinh Luu on 2014-01-27.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""


import requests, json, time
from service import config

ES_SERVER = 'http://' + config.ES_SERVER + '/elastic'
CRAWLED_PRODUCTS = config.CRAWLED_PRODUCTS
COUCHBASE_SERVER = 'http://' + config.COUCHBASE_SERVER
COUCH_PORT = 8091
COUCH_USER = ''
COUCH_PWD = ''

def main():
    
    print 'Delete index...'
    print requests.delete(ES_SERVER  + '/' + CRAWLED_PRODUCTS + '/').text
    
    time.sleep(30)
    print 'Create index...'
    print requests.put(ES_SERVER  + '/' + CRAWLED_PRODUCTS).text
    
    print 'Create mapping...'
    mapping = {
        'doc' : {
            'properties' : {
                'source' : {
                    'index' : 'not_analyzed',
                    'type' : 'string'
                }
            }
        }
    }
    print requests.put(ES_SERVER + '/' + CRAWLED_PRODUCTS + '/couchbaseDocument/_mapping', data =  json.dumps({'properties' : mapping})).text  
        
    print 'Replication from couchbase to elasticsearch...'
    payload = {
        'fromBucket': CRAWLED_PRODUCTS,
        'toCluster' : 'index_chongiadung',
        'toBucket' : CRAWLED_PRODUCTS,
        'replicationType' : 'continuous',
        'type' : 'capi'
    }
    print requests.post(COUCHBASE_SERVER + '/controller/createReplication', data = payload, auth = (COUCH_USER, COUCH_PWD)).text

if __name__ == '__main__':
    main()

