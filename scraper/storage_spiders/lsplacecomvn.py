# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product-name']",
    'price' : "//div[@class='prices']/span[@class='product-price']",
    'category' : "//div[@class='breadcrumb']/ul/li/a",
    'description' : "",
    'images' : "//div[@class='product-essential']/div[@class='picture']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "//div[@class='manufacturers']/a",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'lsplace.com.vn'
allowed_domains = ['lsplace.com.vn']
start_urls = ['http://lsplace.com.vn/vi/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/vi/p/\d+/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/vi/c/\d+/[a-zA-Z0-9-]+($|\?pagenumber=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]