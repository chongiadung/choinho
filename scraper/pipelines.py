# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import time
import json
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from scraper.common import es_util
from scraper.common import util
from scraper.common.logger import logging
from scraper.common import cfg_name_datadog as cfn
from service import config
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
import hashlib
import redis

if config.DATADOG_USED == True:
    from scraper.common import datadog_util as metr

THUMBS_TYPE = ['big', 'normal', 'small']

class SavingPipeline(ImagesPipeline):
    def __init__(self, store_uri=config.STORE_URI, connect=True):
        ImagesPipeline.__init__(self, store_uri)
        self.kafka = None
        if connect:
            self.initES()
            self.initKafka()
            self.initRedis()

    def initES(self):
        self.conn = es_util.ESClient(hosts="http://" + config.ES_SERVER + ":" + config.ES_PORT)

    def initKafka(self):
        client = KafkaClient(config.KAFKA_BROKER)
        self.kafka = SimpleProducer(client)
        
    def initRedis(self):
        self._r = redis.StrictRedis(host=config.REDIS, password=config.REDIS_AUTH)
    
    def get_media_requests(self, item, info):
        if 'images' in item and item['images']:
            item['images'] = list(set(item['images']))
            for image_url in item['images']:
                yield Request(image_url)
        
    def item_completed(self, results, item, info):
        images_cached = {}
        images_cached['base_url'] = config.BASE_URL
        images_cached['images'] = []
        for ok, x in results:
            if ok:
                image_id = hashlib.sha1(x['url']).hexdigest()
                self._r.set(name=image_id, value=x['url'])
                images_cached['images'].append({
                                    'image_id': image_id,
                                    'thumbs_type': THUMBS_TYPE})
        if images_cached:
            item['images_cached'] = images_cached
        record = self.save_item(item)
        return record
    
    def save_item(self, item):
        record = {}
        for k, v in item.items():
            record[k] = v
        recordid = util.getIdFromUrl(record['origin_url'])
        record['id'] = recordid
        self.kafka.send_messages(config.KAFKA_TOPIC, json.dumps(record))
        if config.DATADOG_USED == True:
            metr.incr(cfn.CRAWLER_SPEED, 1, tags=["source:%s" % item['source']])
        logging.info("Saved into Kafka Queue: %s", recordid)
        return record
    
    def set_item_expired(self, url):
        item = self.get_item(url)
        if item:
            item['timestamp'] = time.time()
            item['expired'] = 1
            logging.info("Saved outdated item %s", item['id'])
            self.kafka.send_messages(config.KAFKA_TOPIC, json.dumps(item))
            if config.DATADOG_USED == True:
                metr.incr(cfn.CRAWLER_SPEED, 1, tags=["source:%s" % item['source']])
        return item
    
    def get_item(self, url):
        recordid = util.getIdFromUrl(url)
        return self.conn.getDocById(config.CRAWLED_INDEX, config.CRAWLED_INDEX_TYPE, recordid)
    
    def set_item_expired_by_id(self, recordid):
        item = self.get_item_by_id(recordid)
        if item:
            item['timestamp'] = time.time()
            item['expired'] = 1
            if "_id" in item:
                item['id'] = item['_id']
                del item['_id']
            logging.info("Saved outdated item %s", item['id'])
            self.kafka.send_messages(config.KAFKA_TOPIC, json.dumps(item))
            if config.DATADOG_USED == True:
                metr.incr(cfn.CRAWLER_SPEED, 1, tags=["source:%s" % item['source']])
        return item

    def get_item_by_id(self, recordid):
        return self.conn.getDocById(config.CRAWLED_INDEX, config.CRAWLED_INDEX_TYPE, recordid)
