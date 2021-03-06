# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h2[@class='titledeal']/a/strong",
    'price' : "//p[@class='margin-negative']",
    'category' : "",
    'description' : "//div[@id='dGioiThieu']",
    'images' : "//div[@class='ws_images']/ul/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nhomsieure.vn'
allowed_domains = ['nhomsieure.vn']
start_urls = ['http://nhomsieure.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/[a-z-]+/[a-z0-9-]+.html$'], deny = ['/thanh-vien/', 'category']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/[a-z-]/$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
