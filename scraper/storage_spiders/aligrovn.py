# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title']/h1",
    'price' : "//div[@class='Row Price']/div[@class='ProductPrice VariationProductPrice']",
    'category' : "//div[@class='Breadcrumb']/ul/li/a",
    'description' : "//div[@class='ProductTabs']/div[@class='Block Panel ProductDescription']",
    'images' : "//div[@class='ProductThumb']/div[@class='ProductThumbImage']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'aligro.vn'
allowed_domains = ['aligro.vn']
start_urls = ['http://aligro.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-b\d+\.html($|\?pn=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
