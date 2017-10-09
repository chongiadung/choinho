# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='main']/div[@class='midlemain']/div[@class='chitietsp']/div[@class='tieudesp']",
    'price' : "//div[@class='content']/div[@class='thongso']/div[@class='chitiet']/p[@class='gia']",
    'category' : "",
    'description' : "//div[@class='thongso2']/div/div/div",
    'images' : "//div[@class='content']/div[@class='img anhchitiet']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dogiadung24h.vn'
allowed_domains = ['dogiadung24h.vn']
start_urls = ['http://dogiadung24h.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/sanpham-']), 'parse_item'),
    Rule(LinkExtractor(allow=['/dmsp-']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]