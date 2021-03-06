# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//form[@id='product_addtocart_form']/div[@class='product-shop']/div[@class='product-name']/h1",
    'price' : "//div[@class='product-shop']/div[@class='price-box']/span/span[@class='price']",
    'category' : "//div[@class='middle col-2-right-layout']/ul[@class='breadcrumbs']/li/a",
    'description' : "//div[@class='product-view']/div[@class='product-collateral']/div[@class='collateral-box']/div[@class='padder']",
    'images' : "//form[@id='product_addtocart_form']/div[@class='product-img-box']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'shopnguoilon.vn'
allowed_domains = ['shopnguoilon.vn']
start_urls = ['http://www.shopnguoilon.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
