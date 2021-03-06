# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='productName']",
    'price' : "//div[@class='detail-right']/p[@class='price']",
    'category' : "//div[@id='breadcrumb']/span/a",
    'description' : "//div[@class='detail-right']/div[@class='content-format']",
    'images' : "//div[@id='gallery']/div[@class='bgButton']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vscential.com'
allowed_domains = ['vscential.com']
start_urls = ['http://www.vscential.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
