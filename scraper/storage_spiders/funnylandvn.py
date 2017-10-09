# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title'][1]/h1",
    'price' : "//div[@class='row detail']/div[@class='col-lg-6 col-md-7 col-sm-8 col-xs-12']/div[@class='product-price']/span",
    'category' : "",
    'description' : "",
    'images' : "//img[@class=' product-image-feature']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "//p[@class='title-value']/span[@class='label label-success']",
    'guarantee' : "",
    'promotion' : ""
}
name = 'funnyland.vn'
allowed_domains = ['funnyland.vn']
start_urls = ['http://www.funnyland.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/products/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]