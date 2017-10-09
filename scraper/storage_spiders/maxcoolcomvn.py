# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title']/h1",
    'price' : "//div[@class='Row Price']/div[@class='ProductPrice VariationProductPrice']",
    'category' : "//div[@class='Breadcrumb']/ul/li/a",
    'description' : "//div[@class='ProductDescriptionContainer']",
    'images' : "//div[@class='ProductThumb']/div[@class='ProductThumbImage']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'maxcool.com.vn'
allowed_domains = ['maxcool.com.vn']
start_urls = ['http://maxcool.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[\w\d-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w\d-]+-b\d+\.html($|\?pn=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]