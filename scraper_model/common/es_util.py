#!/usr/bin/env python
# encoding: utf-8
"""
es_util.py

Created by Cuong Pham on 2012-09-06.
Copyright (c) 2012 ChonGiaDung.vn. All rights reserved.
"""

from logger import logging
from pyes import *
import requests, json


def isOk(response):
    data  = json.loads(response)
    return 'acknowledged' in  data and data['acknowledged']

def createIndex(esServer = "localhost:9200", indexName = "test", indexType = "doctype", mapping = None, setting = None, clear = False):

    conn = ES(esServer)

    if clear:
        deleteIndex(esServer =  esServer, indexName =  indexName)

    logging.info('Create index %s ...', indexName)
    try:
        if setting:
            conn.indices.create_index(indexName, setting)
        else:
            conn.indices.create_index(indexName, None)
    except exceptions.IndexAlreadyExistsException:
        logging.warning('Index is already created: %s ...', indexName)

    if mapping is not None:
        logging.info('Put mapping...')
        conn.indices.put_mapping(indexType, mapping, [indexName])

    return True

def closeIndex(esServer = "http://localhost:9200", indexName = "test"):

    esIndex = esServer  + '/' + indexName

    logging.info('Close index %s ...', esIndex)
    response = requests.post(esIndex + '/_close').text
    logging.info(response)
    if isOk(response):
        return True
    else:
        return False

def openIndex(esServer = "http://localhost:9200", indexName = "test"):

    esIndex = esServer  + '/' + indexName

    logging.info('Open index %s ...', esIndex)
    response = requests.post(esIndex + '/_open').text
    logging.info(response)
    if isOk(response):
        return True
    else:
        return False

def updateSetting(esServer = "localhost:9200", indexName = "test", setting = {}):

    conn = ES(esServer)

    logging.info('Update setting for index %s ...', indexName)


def deleteIndex(esServer = "localhost:9200", indexName = "test"):

    logging.info('Delete index %s ...', indexName)
    conn = ES(esServer)
    try:
        conn.indices.delete_index(indexName)
        return True
    except:
        logging.info('Cannot delete index %s', indexName)
        return False


def getDocById(conn, indexName, indexType, docid):
    try:
        doc = conn.get(indexName, indexType, docid)
        return doc
    except exceptions.NotFoundException:
        return None


def getKeysAndDocsByIds(conn, indexName, indexType, docids):
    docs = conn.mget(docids, indexName, indexType)
    for doc in docs:
        yield doc.get_id(), doc if doc != {} else None


def getDocsByIds(conn, indexName, indexType, docids):
    for _, doc in getKeysAndDocsByIds(conn, indexName, indexType, docids):
        yield doc


def delete_batch(conn, indexName, indexType, docids):
    for docid in docids:
        conn.delete(indexName, indexType, docid, bulk=True)
    conn.force_bulk()


def upsert_batch(conn, indexName, indexType, docs):
    for docid, doc in docs.items():
        conn.index(doc, indexName, indexType, id=docid, bulk=True)
    conn.force_bulk()


def index_item(conn, indexName, indexType,docid, doc):
    #res = conn.index(indexName, indexType, id= docid, document=None,
    #            upsert=True, bulk=False,script=None)
    res = conn.index(doc, indexName, indexType, id=docid, parent=None, 
                    force_insert=False, op_type=None, bulk=False, version=None, querystring_args=None, ttl=None)
    return res
    

def main():
    print createIndex(esServer = 'http://localhost:9200', indexName = 'test', indexType = "doctype", mapping = {'properties' : {}}, setting = {}, clear = True)
    print closeIndex(esServer = 'http://localhost:9200', indexName = 'test')
    print updateSetting(esServer = 'http://localhost:9200', indexName = 'test', setting = {"index" : {"refresh_interval" : "5s"}})
    print openIndex(esServer = 'http://localhost:9200', indexName = 'test')
    print deleteIndex(esServer = 'http://localhost:9200', indexName = 'test')

if __name__ == '__main__':
    main()
