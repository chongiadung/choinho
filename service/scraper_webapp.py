#!/usr/bin/env python
# encoding: utf-8
"""
scraper_webapp.py

Created by Toan Vinh Luu on 2013-01-09.
Copyright (c) 2013 CGD Inc. All rights reserved.
"""

import json
from common import util_crawler as uc
import web
import os
import config
from common import util_rest as ur
import crawled_products_service as cps
import scraper_service as ss
import monitor_crawler_service as mcs
from service import crawl_url_script as cus
import requests
import logging

#import xmltodict
urls = (
    '/help', 'help',
    # crawler api
    '/crawler/generate', 'generate',
    '/crawler/startcrawl', 'startcrawl',
    '/crawler/stopcrawl', 'stopcrawl',
    '/crawler/taillog', 'taillog',
    '/crawler/delete_source', 'delete_source',
    '/crawler/thread_count', 'thread_count',
    '/crawler/stopSpiders', 'stopSpiders',
    '/crawler/insert_spider', 'insert_spider',
    '/crawler/check_parse_item', 'checkParseItem',
    '/crawler/crawl_product', 'crawlProduct',
    '/crawler/debugCrawler', 'debugCrawler',
    '/crawler/debugCrawler/fixBug', 'fixBug',
    '/crawler/delete', 'delete',
    '/crawler/spider_history', 'spider_history',
    '/crawler/update_category_blacklist', 'update_category_blacklist',
    # Statistic api
    '/stats/crawled_products', 'crawled_products',
    '/stats/onlinefriday', 'onlinefriday',
    # san_gia api
    '/san_gia/sangia_products', 'sangia_products',
    # kpi crawler
    '/kpi/spiders_started', 'number_spiders_started',
    '/kpi/spiders_stopped', 'number_spiders_stopped',
    '/kpi/spiders_created', 'number_spiders_created',
#     '/kpi/spiders_delete', 'number_spiders_delete',
    '/kpi/items_crawled', 'number_items_crawled'
)

NUM_SECONDS_IN_A_DAY = 60 * 60 * 24

#docs for help
docs = {}

class delete:
    docs['del_file'] = [
        ('method', 'GET'),
        ('path', '/crawler/delete?spider_name=...&type_file=...'),
        ('description', 'delete spider python file')
    ]
    def GET(self):
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')
        params = web.input(spider_name=None, _type=None)

        spider_name         = params.spider_name
        _type           = params._type
        if spider_name is None or spider_name == "" or _type is None or _type == "":
            return "Spider_name or type_file is None!"
        else:
            return ss.delete(spider_name, _type)
            

class stopSpiders:
    docs['stopSpiders'] = [
        ('method', 'GET'),
        ('path', '/crawler/stopSpiders'),
        ('description', 'stop all running spiders')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        return ss.stopAllSpider()

class help:
    def GET(self):
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')
        return ur.formatDocs('Scraper API:', docs)

class generate:
    docs['generate'] = [
        ('method', 'GET'),
        ('path', '/crawler/generate?spider=...&overWrite=true/false'),
        ('description', 'generate spider')
    ]
    def GET(self):
        params = web.input(spider = None, over_write = 'false')
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        spider = params.spider
        over_write = params.over_write
        if spider == None: return 'Missing spider name: spider=...'

        response = ss.generateSpider(spider, over_write)
        return response

class checkParseItem:
    docs['checkParseItem'] = [
        ('method', 'GET'),
        ('path', '/crawler/check_parse_item?url=...'),
        ('description', 'Use xpath to parse item from url')
    ]
    def GET(self):
        params = web.input(spider = None)
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        url = params.url
        if url is None: return 'Missing Url: url=...'

        response = ss.check_parse_item(url)
        return json.dumps(response)

class delete_source:
    docs['delete_source'] = [
        ('method', 'GET'),
        ('path', '/crawler/delete_source?source=...'),
        ('description', 'delete items from source')
    ]
    def GET(self):
        params = web.input(spider = None)
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        source = params.source
        if source == None: return 'Missing source name: source=...'

        response = uc.delete(source)
        return response


class startcrawl:
    docs['startcrawl'] = [
        ('method', 'GET'),
        ('path', '/crawler/startcrawl?spider=...'),
        ('description', 'start spider')
    ]

    def GET(self):
        params = web.input(spider = None)
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        spider = params.spider
        if spider == None or spider == "": return 'Missing spider name: spider=...'

        response = ss.startCrawl(spider)
        raise web.seeother(response)

class stopcrawl:
    docs['stopcrawl'] = [
        ('method', 'GET'),
        ('path', '/crawler/stopcrawl?spider=...'),
        ('description', 'stop spider')
    ]
    def GET(self):
        params = web.input(spider = None)
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        spider = params.spider
        if spider == None: return 'Missing spider name: spider=...'

        response = ss.stopCrawl(spider)
        raise web.seeother(response)


class taillog:
    docs['taillog'] = [
        ('method', 'GET'),
        ('path', '/crawler/taillog?spider=...&number=...'),
        ('description', 'view log of a spider given last number of log lines')
    ]
    def GET(self):
        params = web.input(spider = None, number = 100,files=None)
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        spider      = params.spider
        numberLine  = params.number
        files       = params.files
        if spider == None: return 'Missing spider name: spider=...'

        response = ss.tailLog(spider, numberLine, files)
        return response


class crawlProduct:
    docs['crawl_product'] = [
        ('method', 'GET'),
        ('path', '/crawler/crawl_product?url=...'),
        ('description', 'crawl an item from given url')
    ]
    def GET(self):
        params = web.input(url = None)
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')
        
        import urllib
        
        url = urllib.unquote_plus(params.url)
        if url == None: return 'Missing url: url =...'
        print "Crawling ..." + url
        response = cus.crawlProduct(url)
        return json.dumps(response.__dict__)


class thread_count:
    docs['thread_count'] = [
        ('method', 'GET'),
        ('path', '/crawler/thread_count'),
        ('description', 'Count the number of crawling service currently started')
    ]
    def GET(self):
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        response = json.dumps(ss.threadCount())
        return response

class crawled_products:
    docs['crawled_products'] = [
        ('method', 'GET'),
        ('description', 'Get list of crawled items by some criterias'),
        ('path', '/stats/crawled_products?start=...&limit=...&source=...&sincedays=...&beforeday=...&facetsize=...&missing=...&expired=true/false'),
        ('param missing', 'list of field name seperated by ,. example: missing=price,category')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')
        params      = web.input(start = 0, limit = 10, sincedays = None, beforedays = None, source = None, facetsize = 100, missing = None, exists = None, expired = None, sort=None)
        start       = int(params.start)
        limit       = int(params.limit)

        sincedays   = params.sincedays
        beforedays  = params.beforedays

        facetsize   = int(params.facetsize)
        missing     = params.missing
        exists      = params.exists
        source      = params.source
        expired     = params.expired
        sort        = params.sort

        response    = cps.getItems(start, limit, sincedays, beforedays, source, facetsize, missing, exists, expired,sort)

        return json.dumps(response)

    
class debugCrawler:
    docs['debugCrawler'] = [
        ('method', 'GET'),
        ('path', '/crawler/debugCrawler'),
        ('description', 'return list spiders not running, missing, duplicate')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')
        return json.dumps(mcs.get_debugCrawler())


class fixBug:
    docs['fixBug'] = [
        ('method', 'GET'),
        ('path', '/crawler/debugCrawler/fixBug'),
        ('description', 'return list spiders not running, missing, duplicate')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')
        return json.dumps(mcs.fixBugSpiderNotRun(None))


class insert_spider:
    docs['insert_spider'] = [
        ('method', 'GET'),
        ('path', '/crawler/insert_spider'),
        ('description', 'Insert new spider to mongodb')
    ]
    def POST(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin','*')

        document    = web.data()
        return ss.insertSpider(json.loads(document))


class spider_history:
    docs['spider_history'] = [
        ('method', 'GET'),
        ('path', '/crawler/spider_history?spider_name=...'),
        ('description', 'return history crawler of spider')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin', '*')
        parms = web.input(spider_name=None)
        spider_name = parms.spider_name
        if spider_name:
            return ss.get_spider_history(spider_name)
        return "Missing spider name!"


class number_spiders_started:
    docs['number spiders started'] = [
        ('method', 'GET'),
        ('path', '/kpi/spiders_started?days=...'),
        ('description', 'return number spider started in a day')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin', '*')
        parms = web.input(days=None)
        days = parms.days
        if days:
            return json.dumps(ss.get_number_spiders_started(int(days)))
        return "Missing day parameter!"


class number_spiders_stopped:
    docs['number spiders stopped'] = [
        ('method', 'GET'),
        ('path', '/kpi/spiders_stopped?days=...'),
        ('description', 'return number spider stopped in a day')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin', '*')
        parms = web.input(days=None)
        days = parms.days
        if days:
            return json.dumps(ss.get_number_spiders_stopped(int(days)))
        return "Missing day parameter!"


class number_spiders_created:
    docs['number spiders created'] = [
        ('method', 'GET'),
        ('path', '/kpi/spiders_created?days=...'),
        ('description', 'return number spiders created in a day')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin', '*')
        parms = web.input(days=None)
        days = parms.days
        if days:
            return json.dumps(ss.get_number_spider_created(int(days)))
        return "Missing day parameter!"


class number_items_crawled:
    docs['number items crawled'] = [
        ('method', 'GET'),
        ('path', '/kpi/items_crawled?days=...'),
        ('description', 'return number items crawled in a day')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin', '*')
        parms = web.input(days=None)
        days = parms.days
        if days:
            res = json.loads(requests.get('http://localhost:6081/stats/crawled_products?missing=expired&sincedays=' + days).text)
            return res['total_items']
        return "Missing day parameter!"


class update_category_blacklist:
    docs['update category blacklist'] = [
        ('method', 'GET'),
        ('path', '/crawler/update_category_blacklist'),
        ('description', 'update category blacklist from mongodb')
    ]
    def GET(self):
        web.header('Content-Type', 'application/json; charset=UTF-8')
        web.header('Access-Control-Allow-Origin', '*')
        ss.update_category_blacklist()
        return 'Success!'


def main():
    os.chdir(config.CRAWL_DIR)
    app = web.application(urls, globals())
    app.run()
    logging.info('Start Done!')

if __name__ == '__main__':
    main()
