#!/usr/bin/env python
# encoding: utf-8
"""
Created by Cuong Pham on 2012-01-27.
Copyright (c) 2012 Nemo Find Inc. All rights reserved.

Base class for all of our spiders.
"""
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

import urlparse, requests
import time
import urllib
from common.logger import logging
from bs4 import BeautifulSoup
from scraper.items import Product
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy import Selector
from service import category_blacklist, test_data

BLACK_PRODUCT_NAME = ['A PHP Error was encountered']
BLACK_PRODUCT_URL = ['http://www.sieuthimayvietnam.vn/sanpham/May-cay-lua-8-hang-tay-cay-Robot-2Z8238BGED/48268.html', 'http://www.vtconline.vn/may-cay-lua-8-hang-tay-cay-robot-2z8238bged-p37371.html']
BLACK_PRODUCT_NAME_CONTENT = [u'HAMCO', u'2Z-8238BG-E-D']
HDR = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}

BLACK_CATEGORY = category_blacklist.BLACKLIST

def cleanText(data):
    if type(data) == list: 
        return map(cleanText, data)
    elif type(data) in [str, unicode] :
        return ' '.join(BeautifulSoup(data, "lxml").findAll(text=True))
    else:
        return data


class DetailScraper(CrawlSpider):
    name = None
    allowed_domains = []
    start_urls = []
    rules = []
    tracking_url = ""
    from_url_file = None
    savingPipe = None
    handle_httpstatus_list = [404,302,500,301]
    debug_call_stop = 0
    def __init__(self, xpath_dict = {}, files=None):
        CrawlSpider.__init__(self)
        self.xpath_dict = xpath_dict
        self.from_url_file = files
        if self.from_url_file:
            self.crawl_from_files()  

    def crawl_from_files(self):
        logging.info("============================> Read file %s", self.from_url_file)
        f = open(self.from_url_file,'r')
        self.start_urls = [url.strip() for url in f.readlines()]
        f.close()
    
    def request(self, url, callback):
        request = Request(url=url, callback=callback)
        return request
    
    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield self.request(url, self.parse)
    
    def setExpiredItemsBaseOnStatus(self, url, status):
        isExpired = False
        if status == 404:
            logging.error("==============================> Item expired because of 404: %s", url )
            isExpired = True
        if status == 500:
            logging.error("==============================> Item expired because of 500: %s", url)
            isExpired = True
        if status == 302:
            logging.error("==============================> Item expired because of 302: %s", url) 
            isExpired = True
        if status == 301:
            logging.error("==============================> Item expired because of 301: %s", url)
            isExpired = True
        return isExpired
    
    def parse(self, response):
        if self.from_url_file:
            item = self.parse_item(response)
            if item:
                return item
        else:
            return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)

    def parse_item(self, response, url=None):
        origin_url = None
        if url is None:
            if self.from_url_file == None:
                self.parse(response)
            hxs = Selector(response)
            expired = self.setExpiredItemsBaseOnStatus(response.url, response.status)
            origin_url = response.url
            url = self.add_tracking_code(response.url)
        else:
            origin_url = self.remove_tracking_code(url)
            req = self.get_requests(origin_url)
            if req:
                expired = self.setExpiredItemsBaseOnStatus(origin_url, req.status_code)
                if not expired:
                    hxs = Selector(text=req.content)
                else:
                    return None
            else:
                return None
        if not expired:
            logging.info('======================>EXTRACT %s', origin_url)
            item = Product()
            item['source']      = self.name
            item['origin_url'] = origin_url
            item['url'] = self.add_tracking_code(origin_url)
            item['timestamp']   = time.time()

            for prop, xpath in self.xpath_dict.items():
                if xpath.strip():
                    try:
                        item[prop]  = cleanText(hxs.xpath(xpath).extract())
                    except KeyError:
                        continue
                    if not hxs.xpath((xpath)).extract() or hxs.xpath(xpath).extract() == "":
                        del item[prop]
                    if prop == "description":
                        item["description"] = hxs.xpath(xpath +"/node()[not(self::script)]").extract()
                    if prop == "property":
                        item['property'] = hxs.xpath(xpath + "/node()[not(self::script)]").extract()
            item = test_data.process_data(item)
            item = self.check_item(item)
            if item is not None and self.isValid(item):
                return item
            else:
                return None
        elif url is not None:
            return None
        
    def isValid(self, item):
        return item['url'] and item['name']
    
    def parse_item_and_links(self, response):
        item = self.parse_item(response)
        if item:
            logging.info("Link item: %s", response.url)
            yield item
        else:
            logging.info("Not link item: %s", response.url)
        for rule in self.rules: 
            if not rule.link_extractor: 
                continue
            links = rule.link_extractor.extract_links(response)
            for link in links:
                if link.url.startswith("http"):
                    yield self.request(link.url, callback=self.parse_item_and_links)
    
    def check_item(self, item):
        if item is not None:
            if 'canonical' in item and item['canonical'] is not None and len(item['canonical']) > 0:
                prop_canonical = item['canonical'][0]
                if prop_canonical != item['origin_url']:
                    logging.warning("=======> Item duplicate: " + item['url'] + ", we re-update it")
                    item['origin_url'] = prop_canonical
                    item['url'] = self.add_tracking_code(prop_canonical)
            if 'name' in item and item['name'] is not None and len(item['name']) > 0:
                for name in item['name']:
                    if name in BLACK_PRODUCT_NAME:
                        logging.warning("=======> Item expired because name in black product name: " + name + " at " + item['url'])
                        return None
                    for black_name_content in BLACK_PRODUCT_NAME_CONTENT:
                        if black_name_content.lower() in name.lower():
                            logging.warning("=======> Item expired because name contain black product name content: " + name + " at " + item['url'])
                            return None
            else:
                logging.warning("=======> Item expired because invalid name: " + item['url'])
                return None
            for black_url in BLACK_PRODUCT_URL:
                if item['origin_url'] == black_url:
                    logging.warning("=======> Item expired because name in black product link: " + item['url'])
                    return None
            if (not 'images' in item and not 'price' in item):
                logging.warning("=======> Item expired because invalid images and price: " + item['url'])
                return None
        return item
    
    def add_tracking_code(self, url):
        if self.tracking_url == '':
            return url
        tokens = self.tracking_url.split(",")
        if len(tokens) >= 2:
            if "?" in url:
                url = url + "&"
            else:
                url = url + "?"
        query_url = urllib.quote_plus(url + ("&").join(tokens[1:]))
        url = tokens[0] + query_url
        return url
    
    def remove_tracking_code(self, url):
        if self.tracking_url == '':
            return url
        if "ho.lazada.vn" in url:
            return urlparse.parse_qs(urlparse.urlparse(url).query)['url'][0].split("?")[0]
        if self.tracking_url != "":
            tokens = self.tracking_url.split(",")
            url = url.replace(tokens[0], '')
            url = urllib.unquote_plus(url)
            if len(tokens) > 1:
                for token in tokens[1:]:
                    if token in url:
                        url = url.replace(token, '')
        if url.endswith('&') or url.endswith('?'):
            url = url[:-1]
        return url

    def get_requests(self, url):
        try:
            req = requests.get(url, headers=HDR, allow_redirects=False, timeout=60)
            return req
        except Exception as e:
            logging.exception(e)
            logging.info("Get content from %s null", url)
            return None
    
