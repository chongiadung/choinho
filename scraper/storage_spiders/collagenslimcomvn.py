# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/h1",
    'price' : "//div[@class='float-left product-prices']/span/span/strike/span",
    'category' : "//div[@class='breadcrumbs clearfix']/a",
    'description' : "//div[@class='product-main-info']/div/div[@id='content_description']",
    'images' : "//div[@class='product-main-info']/div/form/div/div[@class='cm-image-wrap']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'collagenslim.com.vn'
allowed_domains = ['collagenslim.com.vn']
start_urls = ['http://collagenslim.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
