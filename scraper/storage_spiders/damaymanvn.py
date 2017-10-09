# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='jv-detail-padding']/h3[1]",
    'price' : "//div[@class='jv-detail-padding']/span[@class='productPrice']",
    'category' : "",
    'description' : "//div[@class='jv-detail-padding']/p",
    'images' : "//div[@class='jv-detail-imgfull']/a/@href",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'damayman.vn'
allowed_domains = ['damayman.vn']
start_urls = ['http://damayman.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z]+\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.html'], deny=['table']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]