# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title defaultTitle']/h1",
    'price' : "//div[@class='Value']/em",
    'category' : "//div[@id='Breadcrumb']/ul/li/a",
    'description' : "//div[@class='ProductDescriptionContainer']",
    'images' : "//div[@class='ProductThumbImage']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'evashoes.com.vn'
allowed_domains = ['evashoes.com.vn']
start_urls = ['http://evashoes.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+[\d]+-[\d-]+.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
