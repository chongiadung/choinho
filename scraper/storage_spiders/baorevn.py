# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='basic']/h2",
    'price' : "//div[@class='giadeal']",
    'category' : "",
    'description' : "//div[@class='detail']",
    'images' : "//div[@class='i_deal']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'baore.vn'
allowed_domains = ['baore.vn']
start_urls = ['http://baore.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/[a-zA-Z-]+/deal-\d+-[a-zA-Z0-9-]+.html']), 'parse_item'),
    Rule(LinkExtractor(allow = ['main.php']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]