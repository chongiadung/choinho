# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product_title']",
    'price' : "//p[@class='price']/span[@class='amount']",
    'category' : "//div[@class='breadcrumbs']/div[@class='container']/ul/li/a",
    'description' : "//div[@class='woocommerce-tabs']/div[@class='resp-tabs-container']",
    'images' : "//a[@itemprop='image']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'talaha.vn'
allowed_domains = ['talaha.vn']
start_urls = ['http://talaha.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/$'], deny=['/danh-muc/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]