# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//span[@id='btAsinTitle']",
    'price' : "//b[@class='priceLarge']",
    'category' : "//div[@id='nav-bar-inner']/ul[@id='nav-subnav']/li[@class='nav-subnav-item']/a",
    'description' : "//div[@id='ctl00_ContentPlaceHolder_divsinglecolumnminwidth']/table[4]/tbody/tr/td[@class='bucket']",
    'images' : "//img[@id='main-image']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nhasachtritue.com'
allowed_domains = ['nhasachtritue.com']
start_urls = ['http://www.nhasachtritue.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/sach+/[a-zA-Z0-9-_]+\.htm']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/chuyen-muc+/[a-zA-Z0-9-]+\.htm']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]