# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//table[@class='cont_heading_table']//tr/td[@class='cont_heading_td']/div/a[2]",
    'price' : "//div[@class='product-info']/div/div[@class='price']",
    'category' : "//table[@class='cont_heading_table']//tr/td/div/a",
    'description' : "",
    'images' : "//div[@class='image']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'banbuonbanlethoitrangxuatkhau.com'
allowed_domains = ['banbuonbanlethoitrangxuatkhau.com']
start_urls = ['http://banbuonbanlethoitrangxuatkhau.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product&']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category&']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]