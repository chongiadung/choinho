# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//p[@class='product_detail_name']",
    'price' : "//p[@class='product_detail_price']",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='product_detail_left_thumbnail']/a/@data-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'bitis.com.vn'
allowed_domains = ['bitis.com.vn']
start_urls = ['http://bitis.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[A-Z]+\d+[A-Z]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w-]+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]