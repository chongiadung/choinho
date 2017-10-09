# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import time
import json
from pyes import ES
from elasticsearch import Elasticsearch
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from scraper.common import es_util
from scraper.common import util
from scrapy import log
from service import config

class SavingPipeline(object):
    def __init__(self):
        self.kafka = None
        self.initES()

    def initES(self):
        self.conn = ES("http://" + config.ES_SERVER + ":" + config.ES_PORT)

    def process_item(self, item, spider=None):
        record = {}
        for k, v in item.items():
            record[k] = v
        new_url = util.get_raw_url(record['url'])
        recordid = util.getIdFromUrl(new_url)
        record['_id'] = recordid
        es_util.index_item(self.conn,config.CRAWLED_INDEX,config.CRAWLED_INDEX_TYPE, recordid, record)
        log.msg("Saved into ES: " + recordid)
        return record

    def set_item_expired(self, url):
        item = self.get_item(url)
        if item:
            item['timestamp'] = time.time()
            item['expired'] = 1
            log.msg("Saved outdated item " + item['_id'])
        return item

    def get_item(self, url):
        recordid = util.getIdFromUrl(url)
        return es_util.getDocById(self.conn, config.CRAWLED_INDEX, config.CRAWLED_INDEX_TYPE, recordid)
    
    def set_item_expired_by_id(self, recordid):
        item = self.get_item_by_id(recordid)
        if item:
            item['timestamp'] = time.time()
            item['expired'] = 1
            log.msg("Saved outdated item " + item['_id'])
        return item

    def get_item_by_id(self, recordid):
        return es_util.getDocById(self.conn, config.CRAWLED_INDEX, config.CRAWLED_INDEX_TYPE, recordid)
