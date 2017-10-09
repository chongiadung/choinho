# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//header[@class='entry-header']/h1[@class='entry-title']/a",
    'price' : "//div[@class='product-detail-item']/p[@class='price-item']",
    'category' : "//header[@class='entry-header']/div[@class='entry-meta']/span/a/span",
    'description' : "//div[@class='entry-content']/p | //div[@class='entry-content']/div/a/img/@src",
    'images' : "//div[@id='product-detail-image']/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'quanaosi.vn'
allowed_domains = ['quanaosi.vn']
start_urls = ['http://quanaosi.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c/'], deny=['/lien-he','/kinh-nghiem-quan-ao+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]