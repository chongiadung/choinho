# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='summary']/h1",
    'price' : "//p[@class='price']/span[@class='amount']",
    'category' : "",
    'description' : "//div[@id='tab-description']/p",
    'images' : "//div[@class='images']/a/img/@src | //div[@class='thumbnails']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bansitrangsuc.lynnlen.com'
allowed_domains = ['bansitrangsuc.lynnlen.com']
start_urls = ['http://bansitrangsuc.lynnlen.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
