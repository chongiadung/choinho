# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='left']/div[@class='image']/a/img[@id='image']/@title",
    'price' : "//div[@class='right']/div[@class='product-options']/div[@class='price']/span[@class='product-price']",
    'category' : "//div[@class='breadcrumb']/span/a/span",
    'description' : "//div[@class='extended-container']/div[@id='container']/div[@id='content']/div[@id='tab-description']",
    'images' : "//div[@class='left']/div[@class='image']/a/img[@id='image']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dochoididong.com'
allowed_domains = ['dochoididong.com']
start_urls = ['http://www.dochoididong.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
