# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='right']/div[@class='description']/h2",
    'price' : "//div[@class='right']/div[@class='price']/span[@class='price-first']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@id='content']/div[@id='tab-description']",
    'images' : "//div[@class='bosszoomtoolbox']/div[@class='image']//a/@href | //ul[@class='skin-opencart']/li/div[@class='boss-image-add']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'azola.vn'
allowed_domains = ['azola.vn']
start_urls = ['http://azola.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
