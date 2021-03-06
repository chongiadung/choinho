# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/b",
    'price' : "//table//tr[3]/td[2]/font/b",
    'category' : "//table//tr[1]/td[@class='spbar_title']",
    'description' : "//table//tr/td[3]/table//tr[3]/td/table//tr/td[3]/table//tr[7]/td",
    'images' : "//table//tr/td[3]/table//tr[3]/td/table//tr/td[1]/table//tr[2]/td/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'huythuanmobile.com'
allowed_domains = ['huythuanmobile.com']
start_urls = ['http://www.huythuanmobile.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/viewp/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/viewc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
