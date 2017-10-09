# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='details-right-head']/h1",
    'price' : "//tr/td[@class='thongtin'][2]",
    'category' : "//li[@class='active-page']/a",
    'description' : "//div[@class='resp-tabs-container vertical-tabs']",
    'images' : "//img[@class='etalage_source_image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'kidsbike.vn'
allowed_domains = ['kidsbike.vn']
start_urls = ['http://kidsbike.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\d+-s\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html'], deny=['-\d+-s\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]