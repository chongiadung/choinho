# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/h1",
    'price' : "//div[@class='right']/div[@class='price']/span[@class='price-new']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@id='tab-description']",
    'images' : "//div[@class='left']/div[@class='image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'ensagrow.com'
allowed_domains = ['ensagrow.com']
start_urls = ['http://ensagrow.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]