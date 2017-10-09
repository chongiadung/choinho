import common.metric_datadog as metric
import requests, json
from common import config_name_datadog as cfg

HOST = 'http://localhost:6081/stats'

def fresh_items():
    data = requests.get(HOST + '/crawled_products?sincedays=20&missing=expired').json()
    if data['total_items']:
        metric.gauge('fresh_items', data['total_items'])
        
def compare_items_crawled():
    data_total = requests.get(HOST + '/crawled_products?missing=expired').json()
    if data_total['total_items']:
        metric.gauge('total_items_crawled', data_total['total_items'])
        
    data_20day = requests.get(HOST + '/crawled_products?sincedays=20&limit=0&missing=expired').json()
    if data_20day['total_items']:
        metric.gauge('total_items_crawled_20day', data_20day['total_items'])
        
def top_spiders():
    top_spiders = 0
    data_top = requests.get(HOST + '/crawled_products?sincedays=20&limit=0&missing=expired,feed&facetsize=1000').json()
    if data_top['sources']:
        for source in data_top['sources']:
            if int(source['count']) > 100:
                top_spiders += 1
        metric.gauge('top_spiders', top_spiders)
    data_total = requests.get(HOST + '/crawled_products?missing=expired,feed&limit=0&facetsize=5000').json()
    if data_total['sources']:
        metric.gauge('total_spiders', len(data_total['sources']))
        
        
def items_crawled_perday():
    data = requests.get(HOST + '/crawled_products?sincedays=1&missing=expired,feed').json()
    if data['total_items']:
        metric.gauge('items_crawled_perday', data['total_items'])
        

def monitor_items_usa():
    data = json.loads(requests.get('http://localhost:9200/timcho_item_v3/_search?q=price.currency.name:%22USD%22&fields=').text)
    if 'hits' in data and 'total' in data['hits']:
        metric.gauge(cfg.ITEMS_USA, data['hits']['total'])
    else:
        metric.gauge(cfg.ITEMS_USA, 0)

def main():
    fresh_items()
    compare_items_crawled()
    top_spiders()
    items_crawled_perday()
    monitor_items_usa()
    

if __name__ == "__main__":
    main()
