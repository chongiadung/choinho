# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='tit nocap']",
    'price' : "//form[@id='frmproduct']/p[@class='price']",
    'category' : "//ul[@class='pageNav']/li/a",
    'description' : "",
    'images' : "//div[@class='imgLarge']/img[@class='cloudzoom']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioianhsang.vn'
allowed_domains = ['thegioianhsang.vn']
start_urls = ['http://thegioianhsang.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-p\d+-c\d+-spro$']), 'parse_item'),
    Rule(LinkExtractor(allow=['-c\d+-spdt']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
