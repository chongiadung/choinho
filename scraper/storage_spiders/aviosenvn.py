# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//span/table//tr/td/h2",
    'price' : "//table//tr/td/div/del | //table//tr/td/h3[@class='price-product']",
    'category' : "//span[@id='dnn_ctr388_news_view_lblContent']/table//tr/td/a",
    'description' : "//span[@id='dnn_ctr388_news_view_lblContent']/table//tr/td/div[@id='tab2']",
    'images' : "//span[@id='dnn_ctr388_news_view_lblContent']/table//tr/td/table//tr/td/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'aviosen.vn'
allowed_domains = ['aviosen.vn']
start_urls = ['http://aviosen.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/products/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]