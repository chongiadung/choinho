# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='right']/h1",
    'price' : "//div[@class='price']/span[@id='price_container']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@id='content']/div[@class='tab-content']",
    'images' : "//div[@class='product-info']/div[@class='left']/div[@class='image']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'haily.vn'
allowed_domains = ['haily.vn']
start_urls = ['http://haily.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item_and_links'),
]
