
from bs4 import BeautifulSoup
import lxml.html
import time
import os
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scraper.items import Product
from scraper import settings
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy import signals, log
from scrapy.selector import HtmlXPathSelector
from scraper_model.pipelines import SavingPipeline
import hashlib
from scraper.common import util

def cleanText(data):
    if type(data) == list: 
        return map(cleanText, data)
    elif type(data) in [str, unicode] :
    	# return lxml.html.fromstring(data).text_content()
    	return ' '.join(BeautifulSoup(data).findAll(text=True))
    else:
   	    return data

class DetailScraperModel(CrawlSpider):
    name = None
    allowed_domains = []
    start_urls = []
    rules = []
    from_url_file = None
    savingPipe = None
    handle_httpstatus_list = [404,302,500,301]
    def __init__(self, xpath_dict = {}, files=None):
        CrawlSpider.__init__(self)
        self.xpath_dict = xpath_dict
        self.from_url_file = files
        self.savingPipe  = SavingPipeline()
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        if self.from_url_file:
            self.crawl_from_files()  

    def crawl_from_files(self):
        print "============================> Read file", self.from_url_file
        f = open(self.from_url_file,'r')
        self.start_urls = [url.strip() for url in f.readlines()]
        f.close()

    def parse(self, response):        
        if self.from_url_file:
            item = self.parse_item(response)
            if item:
                return item
        else:
            return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)  
            
        print '======================>EXTRACT', response.url
        item = Product()
        item['url']         = response.url 
        item['timestamp']   = time.time()
        item['source']      = self.name
        
        for prop, xpath in self.xpath_dict.items():            
            if xpath.strip():
                item[prop]  = cleanText(hxs.xpath(xpath).extract())
                if not hxs.xpath((xpath)).extract() or hxs.xpath(xpath).extract() == "":
                    del item[prop]               
                if prop == "property":                    
                    item["property"] = hxs.xpath(xpath +"/node()").extract()
        if item.isValid():
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
        #self.savingPipe.kafka.stop()
        #self.savingPipe.kafka.client.close()
        print "Done processing spider, close kafka"