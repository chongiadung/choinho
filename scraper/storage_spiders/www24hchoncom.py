# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='block-info-product-detail']/h2",
    'price' : "//div[@class='pric_bar']/span[@class='product-detail-price']",
    'category' : "//div[@class='block-breadrum']/a",
    'description' : "//div[@class='block-promotions-content']/p",
    'images' : "//a[@id='Zoomer']/@href",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = '24hchon.com'
allowed_domains = ['24hchon.com']
start_urls = ['http://24hchon.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/san-pham/.+\.html']), 'parse_item_and_links'),
]
