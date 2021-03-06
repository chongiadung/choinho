# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='info_product']/div[@class='pikachoose']/ul/center/b",
    'price' : "//div[@class='detail_product']/table//tr/td/span[@class='price_detail']/span[@id='price']",
    'category' : "//div[@class='nav']/ul[@class='left']/li/a",
    'description' : "//div[@id='tabs-1']/table//tr/td",
    'images' : "//meta[@property='og:image']/@content",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dvs.vn'
allowed_domains = ['dvs.vn']
start_urls = ['http://dvs.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/'], deny=['mid=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
