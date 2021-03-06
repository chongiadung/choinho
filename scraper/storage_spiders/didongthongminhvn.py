# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail-sp']/div[@class='infor-detail']/h1",
    'price' : "//div[@class='infor-detail']/p[@class='price-detail']/span",
    'category' : "",
    'description' : "//div[@id='prodetails_tab3']/div/div[@id='Wrapper_attributes']",
    'images' : "//div[@class='detail-sp']/div[@class='chitietdienthoai-dt']/img/@src | //div[@class='detail-sp']/div/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'didongthongminh.vn'
allowed_domains = ['didongthongminh.vn']
start_urls = ['http://didongthongminh.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+-[a-zA-Z0-9-]+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+-[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
