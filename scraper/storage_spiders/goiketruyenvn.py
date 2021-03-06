# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//p[@class='normal-price']/span[@class='price']",
    'category' : "",
    'description' : "//div[@class='product-collateral']/div[@class='product-tabs-content'][1]",
    'images' : "//li[@class='thumbnail-item']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'goiketruyen.vn'
allowed_domains = ['goiketruyen.vn']
start_urls = ['http://goiketruyen.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse_item_and_links'),
]
