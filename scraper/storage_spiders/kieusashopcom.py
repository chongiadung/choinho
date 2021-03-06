# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='hidden-phone']",
    'price' : "//div[@itemprop='price']",
    'category' : "//div[@class='breadcrumb-detail clearfix']/a",
    'description' : "//div[@class='description text-left']",
    'images' : "//div[@id='gallery_main']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'kieusashop.com'
allowed_domains = ['kieusashop.com']
start_urls = ['http://kieusashop.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/collections/']), 'parse_item_and_links'),
]
