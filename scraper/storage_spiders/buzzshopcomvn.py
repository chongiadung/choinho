# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='nav_menuDT']/div[@class='title']",
    'price' : "//div[@class='left detail_right']/div[@class='lable_detail mt13'][1]",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='img mt13']/a/img/@src | //div[@class='list_img mt5']/ul/li/a/img/@src | //div[@class='list_img mt5']/ul/li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'buzzshop.com.vn'
allowed_domains = ['buzzshop.com.vn']
start_urls = ['http://www.buzzshop.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product_detail.php']), 'parse_item'),
    Rule(LinkExtractor(allow=['/products.php']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
