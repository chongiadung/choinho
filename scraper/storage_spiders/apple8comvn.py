# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product_info']/h1",
    'price' : "//div[@class='price']/span[@class='new_price']",
    'category' : "//div[@class='location_bar']/a",
    'description' : "//div[@id='container-10']/div[@id='tab_01']",
    'images' : "//div[@id='gal1']/a/@data-zoom-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'apple8.com.vn'
allowed_domains = ['apple8.com.vn']
start_urls = ['http://apple8.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
