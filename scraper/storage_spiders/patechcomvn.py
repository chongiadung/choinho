# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='vmMainPage']//div/div/h1",
    'price' : "//span/span[@class='productPrice']",
    'category' : "",
    'description' : "//div[@id='vmMainPage']/table//td/p | //div[@id='vmMainPage']/table//td/ul/li",
    'images' : "//div[@class='anhsp']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'patech.com.vn'
allowed_domains = ['patech.com.vn']
start_urls = ['http://patech.com.vn/san-pham.html']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/component/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/','/patech-[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]