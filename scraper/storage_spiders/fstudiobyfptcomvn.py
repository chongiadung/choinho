# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='productName']/a",
    'price' : "//div[@class='prices']/label/b[@class='redPrice']",
    'category' : "//div[@class='breadcrumb']/ul/li/div/a",
    'description' : "//ul[@class='discoption']",
    'images' : "//div[@class='lof-main-outer']/ul[@class='lof-main-wapper']/li/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'fstudiobyfpt.com.vn'
allowed_domains = ['fstudiobyfpt.com.vn']
start_urls = ['http://fstudiobyfpt.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+']), 'parse_item_and_links'),
]