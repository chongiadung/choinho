# encoding: utf-8
"""
command.util_crawler

Created by Tien M. Le on 2015-05-30.
Copyright (c) 2015 __ChonGiaDung.com CGD__. All rights reserved.
"""
import json
import requests
from common.logger import logging
import time

ES_SERVER = "http://localhost/elastic/crawled_products/product/_search"
COMMAND_API = "http://localhost:10001/proc/command?command="

class CommandType():
    REPROCESS = "reprocess"
    DELETE = "delete"
    SET_EXPIRED = "set_expired"
    SET_NONEXPIRED = "set_nonexpired"

def getAllDocIdsBySource(es_server, source, limit=10000):
    base_url = es_server + "?q=source:%s&_source=false" % source
    start = 0
    limit = limit
    docids = []
    cnt = 0
    while True:
        url = base_url + "&from=%d&size=%d" % (start, limit)
        data = json.loads(requests.get(url).text)
        if 'hits' in data:
            for doc in data['hits']['hits']:
                docids.append(doc['_id'])
                cnt += 1
            logging.info("Get %d docids", cnt)
            if len(data['hits']['hits']) < limit:
                break
        else:
            break
        start += limit
    return docids

def send_command(command_api, command, data):
    assert type(data) == list, "Bad data %s" % type(data)
    return requests.put(command_api + command, data=json.dumps(data))

def process_source_docs(source, command_type, batch_size=1000):
    docids = getAllDocIdsBySource(ES_SERVER, source)
    batch = []
    cnt = 0
    for docid in docids:
        batch.append(docid)
        cnt += 1
        if batch_size <= len(batch):
            response = send_command(COMMAND_API, command_type, batch)
            if response.status_code != 200:
                raise Exception("Error when execute command %s", command_type)
            logging.info("Sent to %s %d docs", command_type, cnt)
            batch = []
            time.sleep(5)
    if len(batch) > 0:
        send_command(COMMAND_API, command_type, batch)
        logging.info("Sent to %s %d docs", command_type, cnt)
    logging.info("Done %s %d docs from source %s", command_type, cnt, source)

def delete(source):
    process_source_docs(source, CommandType.DELETE)

def set_expired(source):
    process_source_docs(source, CommandType.SET_EXPIRED)

def set_nonexpired(source):
    process_source_docs(source, CommandType.SET_NONEXPIRED)
