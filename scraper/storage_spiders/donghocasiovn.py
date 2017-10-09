# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-shop']/div[@class='product-name']/h1",
    'price' : "//div[@class='price-box']/span/span | //div[@class='product-shop']/div[@class='price-box']/p[@class='special-price']/span",
    'category' : "//div[@class='breadcrumbs']/ul/li[@class='product']/strong",
    'description' : "//div[@class='description-content']//p | //div[@class='product-collateral']/div[@class='box-collateral box-description']",
    'images' : "//div[@class='product-img-box']/div[@class='more-views']/ul/li/a/@href|//p[@class='product-image']/div[@id='wrap']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'donghocasio.vn'
allowed_domains = ['donghocasio.vn']
start_urls = ['http://www.donghocasio.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]