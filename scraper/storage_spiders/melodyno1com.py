# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//p[@class='price']/ins/span[@class='woocommerce-Price-amount amount']",
    'category' : "//nav[@itemprop='breadcrumb']/a",
    'description' : "//div[@class='woocommerce-tabs wc-tabs-wrapper']/div[@class='panel entry-content wc-tab']",
    'images' : "//div[@class='images']/a[@itemprop='image']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'melodyno1.com'
allowed_domains = ['melodyno1.com']
start_urls = ['http://melodyno1.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/shop/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/sanpham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]