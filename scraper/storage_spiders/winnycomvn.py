# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='topicContent']/h1",
    'price' : "//table[2]//tr/td[2]/form/div[2]/table//tr/td[@class='title']",
    'category' : "//div/a[@class='contentFun']",
    'description' : "//div[@id='tab1']/div[@class='content']",
    'images' : "//div[@class='clearfix']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'winny.com.vn'
allowed_domains = ['winny.com.vn']
start_urls = ['http://winny.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[\w-]+\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w-]+/($|&pageID=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]