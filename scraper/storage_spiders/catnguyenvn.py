# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='container']/div[@id='content']/h1",
    'price' : "//div[@class='right']/div[@class='price']/text()",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@id='content']/div[@id='tab-description']",
    'images' : "//div[@class='left']/div[@class='image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'catnguyen.vn'
allowed_domains = ['catnguyen.vn']
start_urls = ['http://catnguyen.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[A-Z]+\d+$']), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]