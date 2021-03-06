# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='container_content_center_left']/div[@class='detail_product']/div[@class='info']/h1[@class='name']",
    'price' : "//div[@class='detail_product']/div[@class='info']/div[@class='price']/div",
    'category' : "//div[@id='container_header']/div[@class='header']/div[@class='navigate']/a",
    'description' : "//div[@class='container_content_center_left']/div[@class='detail_product']/div[@class='picture']/p",
    'images' : "//td/a[@class='colorbox cboxElement']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'lambanhngon.com'
allowed_domains = ['lambanhngon.com']
start_urls = ['http://www.lambanhngon.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
