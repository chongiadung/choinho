# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='col-right-cm']/div[@class='c-product-view']/div[@class='info-product']/h1[@class='product-name']",
    'price' : "//div[@class='c-product-view']/div[@class='info-product']/h2[@class='product-price']/b",
    'category' : "//body/div[@id='container']/div[@class='c-link-daid']/a",
    'description' : "//div[@class='col-right-cm']/div[@class='module_larger']/div[@class='wd-content-proview']/div[@id='div-1']",
    'images' : "//div[@class='picture_fullsize']/div[@class='picture_larger']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dienmayhathanh.vn'
allowed_domains = ['dienmayhathanh.vn']
start_urls = ['http://dienmayhathanh.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
