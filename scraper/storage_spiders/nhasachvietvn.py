# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='main']/div[@id='detail_book']/div[@class='right_detail']/h2[@class='page-title'] | //div[@class='main']/div[@id='detail_book']/div[@class='right_detail']/h1[@class='page-title']",
    'price' : "//div[@class='right_detail']/div[@class='l_info_book']/p/span[@class='price_buy']",
    'category' : "",
    'description' : "//div[@class='inner']/div[@class='main']/div[@id='detail_book']/div[@class='details']",
    'images' : "//div[@class='inner']/div[@class='main']/div[@id='detail_book']/div[@class='left_detail']//a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'nhasachviet.vn'
allowed_domains = ['nhasachviet.vn']
start_urls = ['http://nhasachviet.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/sach/','/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-sach/','/nhom-san-pham/'], deny=[' ',' ','raovat247']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
