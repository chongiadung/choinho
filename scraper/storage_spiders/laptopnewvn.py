# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//body/div[@id='container']/div[@id='content']/h1",
    'price' : "//div[@id='content']/div[@class='product-info']/div[@class='right']/div[@class='price']/text()",
    'category' : "//div[@id='container']/div[@id='content']/div[@class='breadcrumb']/a",
    'description' : "//body/div[@id='container']/div[@id='content']/div[@id='tab-attribute']",
    'images' : "//div[@class='left']/div[@class='image']/a[@class='colorbox cboxElement']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'laptopnew.vn'
allowed_domains = ['laptopnew.vn']
start_urls = ['http://laptopnew.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]