# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-detail-top']/div[@class='Right']/div[1]/h4",
    'price' : "//div[@class='product-detail-top']/div[@class='Right']/div[2]",
    'category' : "",
    'description' : "//div[@class='Product_detail']/div[@class='content1']",
    'images' : "//div[@class='stage']/div[@class='carousel carousel-stage']/ul/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'xedapdienchinhhang.vn'
allowed_domains = ['xedapdienchinhhang.vn']
start_urls = ['http://xedapdienchinhhang.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet-']), 'parse_item'),
    Rule(LinkExtractor(allow=['/lsan-pham-']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
