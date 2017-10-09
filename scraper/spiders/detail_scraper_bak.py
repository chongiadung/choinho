#!/usr/bin/env python
# encoding: utf-8
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
"""
Created by Cuong Pham on 2012-01-27.
Copyright (c) 2012 Nemo Find Inc. All rights reserved.
Base class for all of our spiders.
"""

from bs4 import BeautifulSoup
import lxml.html
import time
import os
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scraper.items import Product
from scraper import settings
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy import signals, log
from scrapy.selector import HtmlXPathSelector
from scraper.pipelines import SavingPipeline
import hashlib
from scraper.common import util
import urlparse
from common import metric_datadog as metr
from common import config_name_datadog as cnd


BLACK_CHAR = ["»"]

def cleanText(data):
    if type(data) == list: 
        return map(cleanText, data)
    elif type(data) in [str, unicode] :
    	# return lxml.html.fromstring(data).text_content()
    	return ' '.join(BeautifulSoup(data).findAll(text=True))
    else:
   	    return data

class DetailScraper(CrawlSpider):
    name = None
    allowed_domains = []
    start_urls = []
    rules = []
    accesstrade_link = None
    from_url_file = None
    savingPipe = None
    handle_httpstatus_list = [404,302,500,301]
    debug_call_stop = 0
    def __init__(self, xpath_dict = {}, files=None):
        CrawlSpider.__init__(self)
        self.xpath_dict = xpath_dict
        self.from_url_file = files
        self.savingPipe  = SavingPipeline()
        if self.from_url_file:
            self.crawl_from_files()  

    def crawl_from_files(self):
        print "============================> Read file", self.from_url_file
        f = open(self.from_url_file,'r')
        self.start_urls = [url.strip() for url in f.readlines()]
        f.close()

    def setExpiredItemsBaseOnStatus(self,response):
        isExpired = False
        if response.status == 404:
            record = self.savingPipe.set_item_expired(response.url)
            print "==============================> Item expired because of 404:", response.url 
            isExpired = True
        if response.status == 500:
            record = self.savingPipe.set_item_expired(response.url)
            print "==============================> Item expired because of 500:", response.url 
            isExpired = True
        if response.status == 302:
            record = self.savingPipe.set_item_expired(response.url)
            print "==============================> Item expired because of 302:", response.url 
            isExpired = True
        if response.status == 301:
            record = self.savingPipe.set_item_expired(response.url)
            print "==============================> Item expired because of 301:", response.url 
            isExpired = True
        return isExpired

    def parse(self, response):
        #self.setExpiredItemsBaseOnStatus(response)
        if self.from_url_file:
            item = self.parse_item(response)
            if item:
                return item
        else:
            return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        expired = self.setExpiredItemsBaseOnStatus(response)
        if not expired:
            print '======================>EXTRACT', response.url
            item = Product()
            item['source']      = self.name
            item['origin_url'] = response.url
            if not self.accesstrade_link or self.accesstrade_link is None:
                item['url']         = response.url
            else:
                item['url'] = self.accesstrade_link + response.url
            item['timestamp']   = time.time()

            for prop, xpath in self.xpath_dict.items():
                if xpath.strip():
                    try:
                        item[prop]  = cleanText(hxs.select(xpath).extract())
                    except KeyError:
                        continue
	 	    if 'canonical' in item and item['url'] != item['canonical'][0]:
                        print '==================> Item expired!'
 			item['expired'] = 1
                    if not hxs.select((xpath)).extract() or hxs.select(xpath).extract() == "":
                        del item[prop]
                    if prop == "description":
                        item["description"] = hxs.select(xpath +"/node()").extract()
		    if prop == "properties":
                        item["properties"] = hxs.select(xpath +"/node()").extract()
            item = self.check_item(item)
            if item is not None and item.isValid():
                self.state['items_count'] = self.state.get('items_count', 0) + 1
            	return item

    def parse_item_and_links(self, response):
        item = self.parse_item(response)
        if item:
            yield item
        for rule in self.rules: 
            if not rule.link_extractor: 
                continue
            links = rule.link_extractor.extract_links(response)
            for link in links:
                if link.url.startswith("http"):
                    url = self.parse_links(link.url)
                    yield Request(url)
    
    def save_item(self,response):
        item        = self.parse_item(response) 
        item_id     = util.getIdFromUrl(item['url'])
        print '=== INSERTING===',item_id
        record = self.savingPipe.process_item(item,self.name) 
        if record:
            print '===INSERTED===',record
        else:
            print '===INSERT ERROR==='
        return item   

    def spider_closed(self,spider,reason):
        self.savingPipe.kafka.stop()
        self.savingPipe.kafka.client.close()
        print "Done processing spider, close kafka"
    
    def check_item(self, item):
        if item is not None:
            if 'canonical' in item and item['canonical'] is not None and len(item['canonical']) > 1:
                prop_canonical = item['canonical'][0]
                uri = urlparse.urlparse(item['origin_url'])
                if prop_canonical.startswith('/'):
                    prop_canonical = uri.scheme + "://" + uri.netloc + prop_canonical
                elif not prop_canonical.startswith('/') and not prop_canonical.startswith('http'):
                    prop_canonical = uri.scheme + "://" + uri.netloc + "/" + prop_canonical
                if prop_canonical != item['origin_url']:
                    print "=======> Item duplicate: " + item['url'] + ", we re-update it"
                    self.savingPipe.set_item_expired(item['url'])
                    item['url'] = prop_canonical
#                     return None
            if 'name' in item and item['name'] is not None and len(item['name']) > 0:
                item_name = item['name'][0]
                for char in BLACK_CHAR:
                    item_name = item_name.replace(char, "")
                item_name = item_name.strip()
                if len(item_name) <= 1:
                    print "=======> Item expired because invalid name: " + item['url']
                    self.savingPipe.set_item_expired(item['url'])
                    return None
                item['name'][0] = item_name
            else:
                print "=======> Item expired because invalid name: " + item['url']
                self.savingPipe.set_item_expired(item['url'])
                return None
            if (not 'images' in item and not 'price' in item):
                return None
        return item

"""    def spider_opened(self,spider): 
        log.msg('Opened Spider ' + str(spider.name) + ' ' +  self.getMd5( str(spider.name)) + ' ' + str(self.timestamp() ) ,spider = spider)
        log.msg('Started Spider!......................... ',spider = spider)
        self.collection     = self.db['spiders']
        res  = self.collection.update( {"doc._id":self.getMd5(str(spider.name))} , {"$set":{"doc.status":"CRAWL_STARTING","doc.server_id":settings.CRAWL_SERVER_ID,"doc.last_update":self.timestamp() } }, upsert=False, multi=False,safe=True)
        if res:
            log.msg('Update status spider CRAWL_STARTING success ',spider = spider)
        else:
            log.msg('Update status spider CRAWL_STARTING fail ',spider = spider)
        return
    def spider_closed(self,spider,reason):
        #print "Spider", spider, stats.get_stats(spider)
        log.msg('Closed Spider ' + self.getMd5( str(spider.name)) + ' ' + str(self.timestamp()),spider = spider)
        log.msg('Finish Spider! Update status to mongodb ',spider = spider)
        self.collection     = self.db['spiders']
        res = self.collection.update({"doc._id": self.getMd5( str(spider.name)) } , {"$set":{"doc.status":"CRAWL_STOPPED","doc.last_update":self.timestamp() } }, upsert=False, multi=False,safe=True)
        if res:
            log.msg('Update status spider CRAWL_STOPPED success ',spider = spider)
        else:
            log.msg('Update status spider CRAWL_STOPPED fail ',spider = spider)
        return   
    def spider_error(self, failure, response, spider):
        log.msg('Spider error! ' + str(response) + str(failure),spider = spider)
        self.collection     = self.db['spiders']
        res  = self.collection.update({"doc._id":self.getMd5(str(spider.name))} , {"$set":{"doc.status":"CRAWL_ERROR","doc.note:":str(failure),"doc.last_update":self.timestamp() } }, upsert=False, multi=False,safe=True)
        if res:
            log.msg("Update status spider error success ",spider = spider)
        else:
            log.msg("Update status spider error fail ",spider = spider)
        return
    def timestamp(self):
        return int(time.time())
    def getMd5(self,text):
        # handle the 'ordinal not in range(128)' problem
        if type(text) == unicode:
            return hashlib.md5(text.encode('utf8')).hexdigest()   
        else:
            return hashlib.md5(text).hexdigest()    
"""
