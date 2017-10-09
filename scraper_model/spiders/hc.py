# -*- coding: utf-8 -*-
from scrapy.contrib.spiders.init import InitSpider
from scraper_model.spiders.detail_scraper_model import DetailScraperModel
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from scrapy.http import Request,FormRequest
from xml.etree import ElementTree as ET
import re

XPATH = {    
    'description' : "//div[@class='product-tabs-content']/div[@class='std']",
    'price' : "//div[@class='price-box productview_pricebox']/p[@class='special-price']/span[@class='price productview_specialprice']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'property' : "//div[@class='product-tabs-content']/table[@class='data-table']/tbody",
    'images' : "//div[@class='product-essential']//a/img/@src",
    'name' : "//div[@class='product-name']/h1",
    'norm_name' : ""
}

class Hccomvn(DetailScraperModel):
    """ sample url: http://hc.com.vn/ti-vi-samsung-smart-ua40j5500akxxv.html
    """
    name = 'hc.com.vn'
    allowed_domains = ['hc.com.vn']
    start_urls = ['http://hc.com.vn/']
    rules = [
        Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
        Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?p=\d+$)'], deny=['/khuyen-mai/','/do-choi']), 'parse'),
    ]    

    def getPropertiesFromPropertyTable(self,table,blackList):
        table_data = []
        prop = {}
        for row in BeautifulSoup(table)("tr"):  
            for cell1,cell2 in zip(row("th"), row("td")): 
                if cell1.text not in blackList:           
                    prop['name'] = cell1.text
                    prop['value'] = cell2.text                
                table_data.append(prop)
                prop = {}
        return table_data

    def norm_name(self,text, maxlen = 12):
        tokens = self.tokenized(text.lower())
        if len(tokens) > maxlen: tokens = tokens[0:maxlen]
        return ' '.join(tokens)

    def tokenized(self,text):
        pattern = re.compile(r"\W+", re.UNICODE)
        tokens = []
        for token in pattern.split(text):
            if token is not None and len(token) > 0: tokens.append(token)
        return tokens

    def simpleTokenized(self,text):
        pattern = re.compile("[ \-\t\n,]")
        tokens = []
        for token in pattern.split(text.lower()):
            if token is not None and len(token) > 0: tokens.append(token)
        return tokens

    def parse_item(self,response):
        item = DetailScraperModel.parse_item(self,response)
        table_data = []
        list_img = []
        blackList = [u'Tên sản phẩm', u'Mã số sản phẩm']
        if item:
            item['norm_name'] = self.norm_name(item['name'][0])
            item['property'] = ' '.join(item['property'])
            table_data = self.getPropertiesFromPropertyTable(item['property'],blackList)  
            item['property'] = table_data
            if 'value' in item['property'][2]:
                item['brand'] = item['property'][2]['value']
            del item['property'][2]
            item['property'] = filter(None, item['property'])
            return item


    def __init__(self,files=None):
        DetailScraperModel.__init__(self, XPATH,files)