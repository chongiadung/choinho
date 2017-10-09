"""
Script to re-crawl items from urls.

Created by Giang Nguyen Truong on 2015-09-28.

Copyright (c) 2015 Chongiadung All rights reserved.
"""

import requests, json, urlparse
from scraper.pipelines import SavingPipeline
from common.logger import logging
from scraper.common import util
from common.util import getFileNameFromSpiderName as module_name
from common.util import getClassNameFromDomain as class_name
import config
import Queue
import threading
from service import cache_images_service as cis

if config.DATADOG_USED:
    from scraper.common import cfg_name_datadog as cfn
    from scraper.common import datadog_util as metr

source_api = "http://localhost:6081/stats/crawled_products?sort=timestamp asc"
savingPipe = SavingPipeline()
DEFAULT_LIMIT = 10000
queue = Queue.Queue(maxsize=0)
NUM_THREADS = 30

def getSpiderNameFromUrl(url):
    uri = urlparse.urlparse(url)
    return uri.netloc.replace('www.', '')

def processUrl(spider_name, url):
    exec("from scraper.spiders.%s import %s as Spider" % (module_name(spider_name).replace('.py', ''), class_name(spider_name)))
    spider = Spider()
    item = spider.parse_item(None, url=url)
    # Cache images
    if item and 'images' in item and item['images']:
        images_cached = cis.cache_images(item['images'])
        if images_cached:
            item['images_cached'] = images_cached
    return item

def crawlProduct(url):
    spider_name = getSpiderNameFromUrl(url)
    product = processUrl(spider_name, url)
    if product is None or product['origin_url'] != url:
        savingPipe.set_item_expired(url)
    if product is not None:
        savingPipe.save_item(product)
    return product
    

def run(queue):
    while True:
        item = queue.get()
        product = processUrl(item['source'][0], item['url'][0])
        if product is not None:
            savingPipe.save_item(product)
        if product is None or util.getIdFromUrl(product['origin_url']) != item['id']:
            savingPipe.set_item_expired_by_id(item['id'])
        if config.DATADOG_USED == True:
            metr.incr(cfn.CRAWLER_OUTDATED_SPEED, tags=["source:%s" % item['source'][0]])
        queue.task_done()
        

def getUrls(source, sincedays, beforedays, missing, start=0, limit=1000):
    logging.info("Get data...")
    url_query = source_api
    if source is not None:
        url_query += "&source=" + source
    if sincedays is not None:
        url_query += "&sincedays=" + str(sincedays)
    if beforedays is not None:
        url_query += "&beforedays=" + str(beforedays)
    if missing is not None:
        url_query += "&missing=" + missing
    urls = []
    while True:
        url_query += '&start=' + str(start) + '&limit=' + str(limit)
        urls.extend(json.loads(requests.get(url_query).text)['hits'])
        start += limit
        if start >= DEFAULT_LIMIT:
            break
    logging.info("Done!")
    return urls
    

def run_threads(num_threads):
    logging.info("Total urls: %d" % queue.qsize())
    for i in range(num_threads):
        crawler = threading.Thread(target=run, args=(queue,))
        crawler.setDaemon(True)
        crawler.start()

def main(source, sincedays, beforedays, missing, start, limit):
    while True:
        urls = getUrls(source, sincedays, beforedays, missing, start, limit)
        if not urls:
            break
        for url in urls:
            queue.put(url)
        run_threads(NUM_THREADS)
        queue.join()

if __name__ == '__main__':
#     print crawlProduct('http://davibooks.vn/products/view/50455.Lam-Chu-Mon-Hoa-Trong-30-Ngay-Tap-1-Hoa-Huu-Co.html')
    main(None, None, 30, 'expired', 0, 1000)
