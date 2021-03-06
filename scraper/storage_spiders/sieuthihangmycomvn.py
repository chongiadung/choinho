# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='col5 tx-Content']/h1[@class='title']",
    'price' : "//div[@id='controls']/p[@class='s-price txtRed']/span[@id='itmPrice'] | //p[@class='s-price txtRed']/span[1]",
    'category' : "//div[@class='i-groupMain bx-breakCum i-radius']/div[@class='ind-groupMain']/h6/a",
    'description' : "//div[@id='tabContent']/div[@id='tab1']",
    'images' : "//ul[@id='itmThumb']/li/span/img/@src | //div[@id='wrap']/a/@href | //meta[@property='og:image']/@content",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthihangmy.com.vn'
allowed_domains = ['sieuthihangmy.com.vn']
start_urls = ['http://sieuthihangmy.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham+/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/','/p/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
