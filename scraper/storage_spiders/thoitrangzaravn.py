# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='ProductMain']/div[@class='product-title']/h1",
    'price' : "//div[@class='Value']/em[@class='ProductPrice VariationProductPrice'] | //div[@class='ProductPrice VariationProductPrice']",
    'category' : "//div[@id='Breadcrumb']/ul/li/a",
    'description' : "//div[@class='ProductDescriptionContainer']",
    'images' : "//div[@class='ProductThumb']/div[@class='ProductThumbImage']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thoitrangzara.vn'
allowed_domains = ['thoitrangzara.vn']
start_urls = ['http://thoitrangzara.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-b+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
