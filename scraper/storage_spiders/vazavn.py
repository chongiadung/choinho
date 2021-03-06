# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='title']/h1/span[@id='lbProductName']",
    'price' : "//div/p[@class='giaban']/span[@id='lbPriceSale']",
    'category' : "//div[@class='breadcrumbs']/a/span",
    'description' : "//div[@id='product-detail']",
    'images' : "//div[@id='deals-wrapper']/div/a/@data-zoom-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vaza.vn'
allowed_domains = ['vaza.vn']
start_urls = ['http://vaza.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-z0-9]+-z+\d+\.php']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-z0-9]+\.php']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
