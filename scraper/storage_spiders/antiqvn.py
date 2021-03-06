# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='filter']/div[@id='productDetail']/div[@id='productInfo']/h1",
    'price' : "//div[@id='productDetail']/div[@id='productInfo']/div[@class='price']/p",
    'category' : "//div[@class='breadcrumb_view']/ul[@class='breadcrumbs']/li/a",
    'description' : "",
    'images' : "//ul[@id='listImgZoom']/li/@data-src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'antiq.vn'
allowed_domains = ['antiq.vn']
start_urls = ['http://antiq.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+/'], deny=['\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
