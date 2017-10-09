# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='cf']/h1",
    'price' : "//p[@class='deal-price']/strong",
    'category' : "",
    'description' : "//div[@class='side']/div[2]/table",
    'images' : "//div[@class='deal-buy-cover-img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = '24hdeal.vn'
allowed_domains = ['24hdeal.vn']
start_urls = ['http://www.24hdeal.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+_\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['\?gid=\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]