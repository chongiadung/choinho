# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td/h1/span[@id='content1_ctl00_lbtendieuhoa']",
    'price' : "//td/strong/font/span[@id='content1_ctl00_lbgiaban']",
    'category' : "//div[@class='special_group_bt']//tr/td/a",
    'description' : "//tbody/tr/td/span[@id='content1_ctl00_lbmotanho']",
    'images' : "//table[@class='table_t2']//td/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dienlanhhanoi.com.vn'
allowed_domains = ['dienlanhhanoi.com.vn']
start_urls = ['http://dienlanhhanoi.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]