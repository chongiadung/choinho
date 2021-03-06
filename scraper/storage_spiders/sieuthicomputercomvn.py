# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//table//tr/td/h2",
    'price' : "//div[@class='center-wrap-content02']//strong[@class='pro-price']",
    'category' : "",
    'description' : "//div[@class='center-wrap-content02']//div[@class='thongso-sp-conten']//strong/span",
    'images' : "//div[@class='center-wrap-content02']//img[@class='image-subject']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthicomputer.com.vn'
allowed_domains = ['sieuthicomputer.com.vn']
start_urls = ['http://www.sieuthicomputer.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product_detail.php.*']), 'parse_item'),
    Rule(LinkExtractor(allow=['/products.php.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
