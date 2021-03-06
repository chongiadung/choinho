# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='goodsInfo_text']/form/div[@class='clearfix']/p",
    'price' : "//div[@id='goodsInfo_text']/form[@id='ECS_FORMBUY']/span[@id='ECS_SHOPPRICE']",
    'category' : "//div[@class='block vote']/a",
    'description' : "//div[@id='right']/div[@id='com_v']",
    'images' : "//div[@id='goodsInfo_img']/div[@class='goodsImg']/a/img/@src | //div[@id='gallery']/div/div[@id='demo']/div/ul/li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vietsao.com.vn'
allowed_domains = ['vietsao.com.vn']
start_urls = ['http://vietsao.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/goods+-\d+-[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category+-\d+-[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
