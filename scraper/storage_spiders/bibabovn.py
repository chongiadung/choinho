# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='title']",
    'price' : "//div[@class='row']/p/span[@class='price']",
    'category' : "//div[@class='col-md-12']/a[@class='a']",
    'description' : "//div[@class='col-md-12']/div[@class='block mb0 product_text row']",
    'images' : "//div/img[@class='single_img']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'bibabo.vn'
allowed_domains = ['bibabo.vn']
start_urls = ['http://bibabo.vn/ec/product/home']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/product/show/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/product/list/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
