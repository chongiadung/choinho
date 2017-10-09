# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='content-content']/div/div[1]",
    'price' : "//tr/td/span",
    'category' : "//div[@class='content']/div[@class='centerColmn']/div[@class='breadcum']/a",
    'description' : "//div[@class='content-content']/div/div/p",
    'images' : "//tr/td/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'shopbanhangxachtay.com'
allowed_domains = ['shopbanhangxachtay.com']
start_urls = ['http://shopbanhangxachtay.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham-']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]