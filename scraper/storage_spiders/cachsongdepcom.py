# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div/div[@class='row']/div[@class='summary entry-summary']/h1[@class='product_title entry-title']",
    'price' : "//div[@class='border group']/div/p[@class='price']/span[@class='amount'] | //p[@class='price']/ins/span[@class='amount']",
    'category' : "//div[@class='row']/div[@id='page-meta']/nav[@class='woocommerce-breadcrumb']/a",
    'description' : "//div[@class='row']/div[@class='product-extra span9']/div[@class='woocommerce-tabs']/div[@id='tab-description']",
    'images' : "//div[@class='row']/div[@class='images']//a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'cachsongdep.com'
allowed_domains = ['cachsongdep.com']
start_urls = ['http://cachsongdep.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
