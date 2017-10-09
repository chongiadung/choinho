# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='item_container'][1]/h1[@class='title_item']/strong",
    'price' : "//div[@class='product_buy_container']/div/strong[@class='product_price']",
    'category' : "",
    'description' : "//div[@class='content_item_product']/div[@class='product_details'] | //div[@class='content_item_product']/div[@class='product_details']/p/a/img/@src",
    'images' : "//div[@class='content_image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'casauhuyhoang.com'
allowed_domains = ['casauhuyhoang.com']
start_urls = ['http://casauhuyhoang.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-/]+($|/\d+$)']), 'parse_item_and_links'),
]