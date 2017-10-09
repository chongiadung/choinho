# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='container']/div[@id='content']/div[@class='product-info']/h1",
    'price' : "//div[@id='content']/div[@class='product-info']/div[@class='right']/div[@class='price']",
    'category' : "//div[@id='container']/div[@id='content']/div[@class='breadcrumb']/a",
    'description' : "//div[@id='content']/div[@class='product-info']/div[@class='product-description']/p",
    'images' : "//div[@class='left']/div[@class='image']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'thitruongmaytinh.vn'
allowed_domains = ['thitruongmaytinh.vn']
start_urls = ['http://www.thitruongmaytinh.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]