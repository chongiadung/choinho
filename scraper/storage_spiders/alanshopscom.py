# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//p[@class='special-price']/span[@class='price']",
    'category' : "//div[@class='breadcrumbs']/ol/li/a",
    'description' : "//div[@class='std']",
    'images' : "//img[@id='image-main']/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'alanshops.com'
allowed_domains = ['alanshops.com']
start_urls = ['http://alanshops.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/index.php/[a-zA-Z0-9-/]+\.html($|\?p=\d+$)']), 'parse_item_and_links'),
]