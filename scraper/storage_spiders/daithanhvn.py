# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='all']/div[@class='views_spcungtop views_sp03']/div[@class='chitiet_right fr']/h1[@class='fn']",
    'price' : "//div[@class='views_spcungtop views_sp03']/div[@class='chitiet_right fr']/div[@class='giaKM']/span",
    'category' : "//div[@class='wrap-path pc-path']/ul[@class='ls path']/li/a",
    'description' : "//div[@class='all']/div[@class='views_spcungtop views_sp03']/div[@class='thogntin_sanpham all']/div[@id='div-1']",
    'images' : "//ul[@class='list_other fl']/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'daithanh.vn'
allowed_domains = ['daithanh.vn']
start_urls = ['http://daithanh.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-c+\d+\.html'], deny=['\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]