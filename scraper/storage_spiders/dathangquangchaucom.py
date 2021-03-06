# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div/h2[@class='title']",
    'price' : "//div[@id='sidebar-primary']/ul/li/div[@class='textwidget']/div/h1/span",
    'category' : "//div[@class='breadcrumb breadcrumbs']/div[@class='rdfa-breadcrumb']/div/p/span/a",
    'description' : "//div[@id='content']/div/div[@class='entry clearfix']/div/a/img/@src",
    'images' : "//div[@id='main']/div[@id='content']/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dathangquangchau.com'
allowed_domains = ['dathangquangchau.com']
start_urls = ['http://dathangquangchau.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(deny=['/tin-tuc/','/gioi-thieu/','/lien-he/'], allow=['/[a-zA-Z0-9-]/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
