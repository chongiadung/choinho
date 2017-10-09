# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail-product-content-name']",
    'price' : "//div[@class='detail-product-content-box']/div[@class='price']",
    'category' : "//div[@class='module-title']/a",
    'description' : "//div[@class='motasp']",
    'images' : "//div[@class='detail-product-img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'shopbubu.com'
allowed_domains = ['shopbubu.com']
start_urls = ['http://shopbubu.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]