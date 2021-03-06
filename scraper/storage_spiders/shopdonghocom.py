# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='wrapper']/div[@class='info']/div[@class='headline']/h1",
    'price' : "//div[@class='wrapper']/div[@class='info']/div[@class='headline']/h2",
    'category' : "",
    'description' : "//div[@class='wrapper']/div[@class='info']/div[@class='headline']/p",
    'images' : "//div[@class='wrapper']/div[@class='img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'shopdongho.com'
allowed_domains = ['shopdongho.com']
start_urls = ['http://shopdongho.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/thuong-hieu/','/danh-muc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
