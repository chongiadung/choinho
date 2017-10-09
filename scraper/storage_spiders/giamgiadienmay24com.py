# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail']/div[@class='detail-header']/h1",
    'price' : "//div/span[@class='price']",
    'category' : "//ul[@class='breadcrumb space-bottom']/li/a",
    'description' : "//div[@class='article space-top'][1]/div[@class='article-content left']",
    'images' : "//div[@id='detail_image']/ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'giamgiadienmay24.com'
allowed_domains = ['giamgiadienmay24.com']
start_urls = ['http://www.giamgiadienmay24.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]