# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='productDetail']/div[@class='description-products']/h3",
    'price' : "//div[@class='productDetail']/div[@class='description-products']/label[@class='price']",
    'category' : "//a[@class='CMSBreadCrumbsLink']",
    'description' : "//div[@class='container_tab']/div[@class='tab-content current']",
    'images' : "//img[@class='cloudzoom-gallery']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'theblues.vn'
allowed_domains = ['theblues.vn']
start_urls = ['http://www.theblues.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.aspx($|\?page=\d+$)']), 'parse_item_and_links'),
]