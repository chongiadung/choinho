# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product_title entry-title']",
    'price' : "//p[@class='price']//span[@class='amount']",
    'category' : "",
    'description' : "//div[@class='woocommerce-tabs']/div[@class='panel entry-content']",
    'images' : "//div[@class='product_thumbnails']/div/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'giaydep24.com'
allowed_domains = ['giaydep24.com']
start_urls = ['http://giaydep24.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/shop/[a-zA-Z0-9-]+/$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/[a-zA-Z0-9-]+/$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]