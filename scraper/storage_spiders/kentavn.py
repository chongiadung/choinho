# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='partial-product_info']/h1[@class='product-name']",
    'price' : "//span[@class='price-retail']/font",
    'category' : "//div[@class='partial-product_detail']/div/b/a",
    'description' : "//div[@class='partial-product_info']/div[1]/div",
    'images' : "//div[@id='detail']/div/img[@class='variant-image-img']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'kenta.vn'
allowed_domains = ['kenta.vn']
start_urls = ['http://kenta.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet+/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/','/phu-kien/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
