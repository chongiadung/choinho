# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/h1[@class='mainbox-title']",
    'price' : "//div[@class='product-info']/div[@class='clear']/p/span/span/span | //div[@class='product-info']/div[@class='prices-container clear']/div[@class='float-left product-prices']/p/span/span/span",
    'category' : "//div[@class='breadcrumbs']/a",
    'description' : "//div[@class='product-main-info']/div[@id='tabs_content']",
    'images' : "//div[@class='product-main-info']/form/div/div/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'muahangtructuyen.com.vn'
allowed_domains = ['muahangtructuyen.com.vn']
start_urls = ['http://muahangtructuyen.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]