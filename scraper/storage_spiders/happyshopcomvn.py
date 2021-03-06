# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='set-size-grid']/h2",
    'price' : "//div[@class='right']/div[@class='price']/p",
    'category' : "//div[@class='set-size-grid']/a",
    'description' : "//div[@class='whole-tabs']/div[@class='tab-description']",
    'images' : "//div[@class='left']/div[@class='zoom-image']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'happyshop.com.vn'
allowed_domains = ['happyshop.com.vn']
start_urls = ['http://happyshop.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[\w-]+$'], deny=['index\.php']), 'parse_item_and_links'),
]
