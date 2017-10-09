# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//ul/li[@class='info-highlights-f1']/div/a",
    'price' : "//li[@class='info-highlights-f3']/a[@class='price-discount']",
    'category' : "//div[@class='bk_main']/p/span/a",
    'description' : "//div[@class='dien_features_content1 dien_show']",
    'images' : "//div[@class='image_part']/div[@class='image_main_part']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dienmayquangphuong.com'
allowed_domains = ['dienmayquangphuong.com']
start_urls = ['http://dienmayquangphuong.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d','/nha-san-xuat/','/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]