# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product_name']",
    'price' : "//div[@class='pac_chinhsach_1']/div[@class='product_price']/div",
    'category' : "//div[@class='page_nav productNav']/span/span/a",
    'description' : "//div[@class='product_summary']",
    'images' : "//div[@class='slide_image']//img[@itemprop='image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'phucanh.vn'
allowed_domains = ['phucanh.vn']
start_urls = ['http://phucanh.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\d+.*\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.html($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
