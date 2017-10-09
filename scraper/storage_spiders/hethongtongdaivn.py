# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//ul[@class='list-unstyled']/li/h2",
    'category' : "//ul[@class='breadcrumb']/li/a",
    'description' : "//div[@class='tab-content']/div[@class='tab-pane active']",
    'images' : "//ul[@class='thumbnails']/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'hethongtongdai.vn'
allowed_domains = ['hethongtongdai.vn']
start_urls = ['http://hethongtongdai.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/shop/[a-zA-Z0-9-/]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/shop/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]