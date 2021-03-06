# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product_title entry-title']",
    'price' : "//p[@class='price']/span[@class='amount']",
    'category' : "//nav[@id='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='tabs-container']/div[@class='panel tab-content entry-content']/p",
    'images' : "//a[@itemprop='image']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'dual.vn'
allowed_domains = ['dual.vn']
start_urls = ['http://dual.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/gian-hang/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
