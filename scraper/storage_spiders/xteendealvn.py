# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='deal-intro']/h1",
    'price' : "//p[@class='deal-price']/strong",
    'category' : "",
    'description' : "//div[@id='team_main_side']",
    'images' : "//div[@class='mid']/ul/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'xteendeal.vn'
allowed_domains = ['xteendeal.vn']
start_urls = ['http://xteendeal.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/[a-z-]+/[a-z0-9-]+\d+.html']), 'parse_item'),
    Rule(LinkExtractor(allow = ['.vn/[a-z-]+\d+.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]