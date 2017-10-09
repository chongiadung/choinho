#!/usr/bin/env python
# encoding: utf-8
"""
lab.py

Created by Toan Luu on 2012-09-30.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from pyes import *
from pyes.facets import *

TEST_INDEX = 'test'
TEST_TYPE = 'test'
# ES_SERVER = 'http://localhost:9200'
ES_SERVER = 'http://elastic.timkiem.mobi'

def createIndex():
    print 'Delete index...'
    esConn = ES(ES_SERVER, timeout = 30.0)
    try:
       esConn.delete_index(TEST_INDEX)
    except:
       print 'No index to delete'

    print 'Create index...'

    setting = {
       "settings": {
         "analysis": {
           "analyzer": {
             "myanalyzer": {
               "tokenizer": "letter",
               "filter": ["lowercase", "asciifolding", "concatenate"]
             }
           },
           "filter": {
             "concatenate": {
               "type": "com.chongiadung.analysis.ConcatenateTokenFilterFactory",
               "token_separator": "_"
             }
           }
         }
       }
    }

    esConn.create_index(TEST_INDEX, setting)
    return esConn
def indexDoc(esConn):
    doc = {'field1' : 'value1', 'field2' : 'value2'}
    esConn.index(doc, TEST_INDEX, TEST_TYPE, 1)
    doc = {'field1' : 'value1', 'field2' : 'value3'}
    esConn.index(doc, TEST_INDEX, TEST_TYPE, 2)
    doc = {'field1' : 'value1', 'field2' : 'value2'}
    esConn.index(doc, TEST_INDEX, TEST_TYPE, 3)
    esConn.refresh()
    
def testQuery():
    esConn = ES(ES_SERVER, timeout = 30.0)
    query = {
        "text" : {
            "_all" : {
                "query" : "value1 value3",
                "operator" : "and"
            }
        }
    }
    results = esConn.search(query=query, indices=[TEST_INDEX], doc_types=TEST_TYPE)
    for r in results: print r
    print results.total

def testExplain():
    esConn = ES(ES_SERVER, timeout = 30.0)
    query = {
        "text" : {
            "_all" : {
                "query" : "value1",
                "operator" : "and"
            }
        }
    }
    results = esConn.search(Search(query = query, size=2, start=1), explain=True, indices=[TEST_INDEX], doc_types=TEST_TYPE, model=lambda x,y:y)
    for r in results: print r
    print len([r for r in results])
    print results.total
    # print results

def testFields():
    esConn = ES(ES_SERVER, timeout = 30.0)
    query = {
        "text" : {
            "_all" : {
                "query" : "value1",
                "operator" : "and"
            }
        }
    }
    results = esConn.search(Search(query = query, size=2, start=1, fields = []), explain=True, indices=[TEST_INDEX], doc_types=TEST_TYPE, model=lambda x,y:y)
    for r in results:
        for k, v in r.items():
            print k, ':', v
    print len([r for r in results])
    print results.total
    
def testFacet():
    esConn = ES(ES_SERVER, timeout = 30.0)
    query = {
        "text" : {
            "_all" : {
                "query" : "value1",
                "operator" : "and"
            }
        }
    }

    search = Search(query = query, size=1)
    search.facet.add(TermFacet(field='field1', size = 1))
    search.facet.add(TermFacet(field='field2', size = 1))
    results = esConn.search(search, explain=True, indices=[TEST_INDEX], doc_types=TEST_TYPE, model=lambda x,y:y)
    
    for r in results: print r
    print 'SIZE:', len([r for r in results])
    print 'TOTAL:', results.total
    print 'FACETS:', results.facets

def testSort():
    esConn = ES(ES_SERVER, timeout = 30.0)
    query = {
        "text" : {
            "_all" : {
                "query" : "value1",
                "operator" : "and"
            }
        }
    }

    search = Search(query = query, size=3)
    print 'asc:'
    results = esConn.search(search, explain=True, sort = 'field2:asc', indices=[TEST_INDEX], doc_types=TEST_TYPE, model=lambda x,y:y)
    for r in results: print r['_source']
    print 'desc:'
    results = esConn.search(search, explain=True, sort = 'field2:desc', indices=[TEST_INDEX], doc_types=TEST_TYPE, model=lambda x,y:y)
    for r in results: print r['_source']

def testBoolQuery():
    esConn = ES('http://elastic.timkiem.mobi', timeout = 30.0)
    query = {
        "bool" : {
            "must" : [
            {        
                "field": {
                    "u_category" : { 
                        "query" : "Thoi trang, trang suc",
                        "boost" : 3.0
                    }
                }
            },
            {        
                "field": {
                    "u_name" : { 
                        "query" : "Tommy Hilfiger",
                        "boost" : 1.0
                    }
                }
            }]
        }   
    }

    search = Search(query = query, size=10)
    results = esConn.search(search, indices=['cdt_model'])
    print 'TOTAL:', results.total
    cnt = 0
    for r in results:
        cnt = cnt + 1
        print cnt, '======'
        print r 

def main():
    # esConn = createIndex()
    # indexDoc(esConn)
    # testQuery()
    # testExplain()
    # testFields()
    # queryFacet()
    # testSort()
    # testBoolQuery()
    pass
    


if __name__ == '__main__':
    main()




