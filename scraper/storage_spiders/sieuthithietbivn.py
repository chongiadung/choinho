# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product_title entry-title']",
    'price' : "//p[@class='price']/span[@class='amount']",
    'category' : "//nav[@class='woocommerce-breadcrumb']/a",
    'description' : "//div[@class='woocommerce-tabs']/div[@class='panel entry-content']",
    'images' : "//div[@class='images']/a[@class='woocommerce-main-image zoom']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthithietbi.vn'
allowed_domains = ['sieuthithietbi.vn']
start_urls = ['http://www.sieuthithietbi.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+/$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/[a-zA-Z0-9-]+/($|page/\d+/$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
