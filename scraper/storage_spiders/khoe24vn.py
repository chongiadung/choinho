# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[2]/h1/a",
    'price' : "//h3[@class='views-field views-field-display-price']/span[@class='field-content']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@class='views-field views-field-body']/div[@class='field-content']",
    'images' : "//div[@class='field-item even']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'khoe24.vn'
allowed_domains = ['khoe24.vn']
start_urls = ['http://khoe24.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/thuoc/']), 'parse_item'),
    Rule(LinkExtractor(deny = ['/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]