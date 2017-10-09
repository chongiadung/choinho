# Extension to do stuff after finish crawling
# Author Giang Nguyen 9/9/2015

from scrapy import signals
from common import mongo, util
from scrapy.exceptions import CloseSpider
from service import config
from common.logger import logging
import os
from pymongo.errors import NetworkTimeout
from time import sleep
import time
from kafka.client import KafkaClient
import json
from kafka.producer import SimpleProducer
from kafka.common import FailedPayloadsError

if config.DATADOG_USED == True:
    from common import metric_datadog as metr
    from common import config_name_datadog as cfg

KAFKA_LOG_STATS_TOPIC = 'spider_stats'

class ExtensionThatAccessStats(object):

    def __init__(self, stats):
        self.stats = stats
        self.collection_spider = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, "spiders")
        self.collection_stats = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, "stats")
        self.client = None
        self.kafka = None
    
    @classmethod
    def from_crawler(cls, crawler):
        ext = cls(crawler.stats)
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_idle, signal=signals.spider_idle)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext
    
    def spider_opened(self,spider):
        print "==============> Start crawling " + spider.name
        if config.DATADOG_USED == True:
            metr.event("SPIDER START!", "["+spider.name+"]Spider just started!", "info", util.get_name_server())
        try:
            util.updateTimeStart(spider.name)
        except (RuntimeError, TypeError, KeyError):
            pass

    def spider_idle(self, spider):
        stats = self.stats.get_stats()
        pages = stats.get('downloader/response_status_count/200', 0)
        items = stats.get('item_scraped_count', 0)
        percent_items = util.get_percent(items, pages)
        if int(pages) > 20000 and percent_items < 10:
            if config.DATADOG_USED == True:
                metr.event("SPIDER ERROR!", "["+spider.name+"]Spider error: Ratio items/pages is very low, please check rule.", "error", util.get_name_server())
                metr.incr(cfg.SPIDER_ERROR, 1)
            raise CloseSpider('Ratio items/pages is very low')

    def spider_closed(self, spider):
        self.stats_items(spider)
        self.close_all_connect()
    
    def stats_items(self, spider):
        stats = self.stats.get_stats()
        self.push_log(spider.name, stats)
        if config.DATADOG_USED == True:
            metr.event("SPIDER STOP!", "["+spider.name+"]Spider just stopped!", "info", util.get_name_server())
        try:
            scraped_items = stats.get('item_scraped_count', 0)
            self.remove_dir_crawl(spider.name)
            spider.log("Total items: %s" % scraped_items)
            if int(scraped_items) < 1:
                spider.log("===============>Spider Error %s: item_scraped_count is zero" % spider.name)
                if config.DATADOG_USED == True:
                    metr.event("SPIDER ERROR!", "["+spider.name+"]Spider error: Total items crawled equal zero", "error", util.get_name_server())
                    metr.incr(cfg.SPIDER_ERROR, 1)
                if util.setSpiderError(spider.name):
                    spider.log("Spider's status updated")
            else:
                if int(scraped_items) < 100 and config.DATADOG_USED == True:
                    metr.event("SPIDER WARNING!", "["+spider.name+"]Spider warning: Total items crawled less than 100", "warning", util.get_name_server())
                    metr.incr(cfg.SPIDER_WARNING, 1)
                spiders_mongo = self.collection_spider.find({'doc.spider':spider.name})
                spiders = []
                try:
                    for spd in spiders_mongo:
                        spiders.append(spd)
                except NetworkTimeout:
                    sleep(60)
                    for spd in spiders_mongo:
                        spiders.append(spd)
                if len(spiders) > 1:
                    if config.DATADOG_USED == True:
                        metr.event("SPIDER WARNING!", "["+spider.name+"]Spider warning: Duplicate spider in mongo", "warning", util.get_name_server())
                        metr.incr(cfg.SPIDER_WARNING, 1)
                    util.updateTimeStop(spider.name, spiders[0]['crawler_status']['items'])
                elif len(spiders) < 1 and config.DATADOG_USED == True:
                    metr.event("SPIDER WARNING!", "["+spider.name+"]Spider warning: None spider in mongo", "warning", util.get_name_server())
                    metr.incr(cfg.SPIDER_WARNING, 1)
                else:
                    scraped_items_old = spiders[0]['crawler_status'].get("items", 1)
                    percent_diff = util.get_percent(scraped_items, scraped_items_old)
                    if percent_diff < 80:
                        if config.DATADOG_USED == True:
                            metr.event("SPIDER WARNING!", "["+spider.name+"]Spider warning: Total items crawled decreased "+str(percent_diff)+"%", "warning", util.get_name_server())
                            metr.incr(cfg.SPIDER_WARNING, 1)
                        util.updateTimeStop(spider.name, scraped_items_old)
                    else:
                        util.updateTimeStop(spider.name, scraped_items)
        except KeyError as e:
            spider.log("===============>Spider Error {0}: KeyError {1}".format(spider.name, e))
            if config.DATADOG_USED == True:
                metr.event("SPIDER ERROR!", "["+spider.name+"]Spider error: Spider don't start", "error", util.get_name_server())
                metr.incr(cfg.SPIDER_ERROR, 1)
            util.setSpiderError(spider.name)
    
    def spider_error(self, failure, response, spider):
        spider.log("===============>Spider Error %s" % spider.name)
        if config.DATADOG_USED == True:
            metr.event("SPIDER ERROR!", "["+spider.name+"]Spider error: Spider dump", "error", util.get_name_server())
            metr.incr(cfg.SPIDER_ERROR, 1)
        if util.setSpiderError(spider.name):
            spider.log("Spider's status updated")
    
        #spider.log("spider stats %s" % self.stats.get_stats())
    
    def remove_dir_crawl(self, spider_name):
        commands = 'rm -rf ' + config.LOG_DIR + 'crawls/' + spider_name
        logging.info(" ".join(commands))
        os.system(commands)
    
    def push_log(self, spider_name, stats):
        self.connect_kafka()
        stats['start_time'] = time.mktime(stats['start_time'].timetuple())
        stats['finish_time'] = time.mktime(stats['finish_time'].timetuple())
        stats['spider'] = spider_name
        try:
            #logging.info(stats)
            self.kafka.send_messages(KAFKA_LOG_STATS_TOPIC, *[json.dumps(stats)])
        except FailedPayloadsError as e:
            logging.error(e)
	    logging.info(stats)
        del stats['spider']
        for key in stats.keys():
            if '.' in key:
                del stats[key]
        stat_spider_old = self.collection_stats.find_one({"spider": spider_name})
        if stat_spider_old:
            stat_spider_new = stat_spider_old
        else:
            stat_spider_new = {'spider': spider_name,
                               'stats': []}
        if len(stat_spider_new['stats']) < 7:
            stat_spider_new['stats'].append(stats)
        else:
            stat_spider_new['stats'].pop(0)
            stat_spider_new['stats'].append(stats)
        stat_spider_new['last_history'] = stats
        self.collection_stats.update({"spider": spider_name}, {"$set": stat_spider_new}, upsert=True, multi=False)
    
    def connect_kafka(self):
        self.client = KafkaClient(config.KAFKA_BROKER)
        self.kafka = SimpleProducer(self.client)
    
    def close_all_connect(self):
#         if self.collection_spider:
#             self.collection_spider.close()
        if self.kafka:
            self.kafka.stop()
            self.kafka.client.close()
        logging.info("Closed all connection.")
