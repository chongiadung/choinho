# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='product-type-data']/div[@class='price-box']/span/span[@class='price']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a/span",
    'description' : "//div[@class='tabs-panels']/div[@class='panel'][1]/div[@class='std']",
    'images' : "//a[@id='zoom1']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'xunhasaba.com.vn'
allowed_domains = ['xunhasaba.com.vn']
start_urls = ['http://xunhasaba.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html($|\?p=\d+$)']), 'parse_item_and_links'),
]
