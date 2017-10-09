# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//td[@class='title']/h1",
    'price' : "//table[1]/tbody/tr[10]/td[@class='title']",
    'category' : "//div[@class='topic']/a",
    'description' : "//table[2]/tbody/tr[2]/td[@class='content']",
    'images' : "//td/div[@id='content']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'beon.vn'
allowed_domains = ['beon.vn']
start_urls = ['http://beon.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]