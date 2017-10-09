# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='product-wapper']/div[@class='product-info']/div[@class='right']/h1",
    'price' : "//div[@id='product-wapper']/div[@class='product-info']/div[@class='right']/div[@class='price']/text()",
    'category' : "//div[@id='container']/div[@id='content']/div[@class='breadcrumb']/a",
    'description' : "//body/div[@id='container']/div[@id='content']/div[@id='tab-description']",
    'images' : "//div[@class='left']/div[@class='image']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'milanplaza.com.vn'
allowed_domains = ['milanplaza.com.vn']
start_urls = ['http://milanplaza.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+'], deny=['\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]