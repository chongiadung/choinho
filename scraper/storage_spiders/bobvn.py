# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='titigioith']/div[@class='title']/h1",
    'price' : "//div[@class='giacafullnao']/div[@class='giaca']/div/p/b",
    'category' : "//div[@class='rdfa-breadcrumb']/div/p/span/a",
    'description' : "//div[@class='tabsanpham']/div[2]",
    'images' : "//div[@class='hinhanh']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bob.vn'
allowed_domains = ['bob.vn']
start_urls = ['http://bob.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+/+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]