# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='content_proudct']/h1[@class='title_product']",
    'price' : "//div[@class='content_proudct']/table//tr[1]/td[@class='price3']",
    'category' : "//ul[@class='breakrum']/li/a",
    'description' : "//div[@class='element_content_tab1 element_content_tab current_element_content_tab']/div/span",
    'images' : "//div[@class='slide_product']/ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'ahaha.vn'
allowed_domains = ['ahaha.vn']
start_urls = ['http://ahaha.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/','/thuong-hieu/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]