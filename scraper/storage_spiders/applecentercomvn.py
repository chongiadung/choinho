# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='productName']/h1",
    'price' : "//div[@class='product_right']/b[@class='giacuahang price'] | //div/b[@class='giacuahang price']",
    'category' : "//div[@class='navigation']/span/a",
    'description' : "//div[@class='it_row_center_detail']/div",
    'images' : "//div[@class='it_row_center_detail']/div/p/img/@src | //div[@class='oneByOne1']//img/@src | //div[@class='it_row_center_detail']/div/img/@src | //div[@class='it_row_center_detail']/div/div/img/@src | //div[@class='oneByOne_item']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'applecenter.com.vn'
allowed_domains = ['applecenter.com.vn']
start_urls = ['http://applecenter.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]