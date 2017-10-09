# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='contpadb clearfix']/h1",
    'price' : "//span[@class='price_valuedt']",
    'category' : "",
    'description' : "//div[@id='diem-noi-bat']",
    'images' : "//div[@class='mid']/ul/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nhanhmua.vn'
allowed_domains = ['nhanhmua.vn']
start_urls = ['http://nhanhmua.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/deal/']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/danh-sach-deal/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]