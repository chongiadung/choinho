# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/div/div/a/@title",
    'price' : "//div[@id='right_column']/div[@class='product-info']/div[@class='right']/div[@class='price']",
    'category' : "//div[@id='center_column']/div[@id='right_column']/div[@class='breadcrumb']/a",
    'description' : "//div[@id='columns']/div[@id='center_column']/div[@id='right_column']/div[@id='tab-description']",
    'images' : "//div[@class='left']/div[@class='image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nhathuoc.vn'
allowed_domains = ['nhathuoc.vn']
start_urls = ['http://nhathuoc.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
