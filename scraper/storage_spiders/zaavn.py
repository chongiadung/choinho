# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@class='detail-right']/p/span[@class='name-product-detail']",
    'price' : "//div[@id='content']/div[@class='detail-right']/p/span[@class='price-detail']",
    'category' : "",
    'description' : "//div[@class='description']/div[@id='container']/div[@class='content news']/div[@class='content news']",
    'images' : "//div[@class='clearfix']/a[@class='jqzoom']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'zaa.vn'
allowed_domains = ['zaa.vn']
start_urls = ['http://zaa.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
