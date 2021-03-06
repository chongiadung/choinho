# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='single-sec']/div[@class='container1']/div[@class='single-right']/h1",
    'price' : "//div[@class='cost']/div[@class='prdt-cost']/ul/li[@class='active']",
    'category' : "//ol[@class='breadcrumb']/li/div[@class='sitemap']/a",
    'description' : "//div[@class='col-md-9 det']/div[@class='single-sec']/div[@class='container1']/div[@class='sofaset-info']",
    'images' : "//ul[@id='etalage']/li/div/img/@src | //meta[@itemprop='image']/@content",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'noithatvietnam.net'
allowed_domains = ['noithatvietnam.net']
start_urls = ['http://noithatvietnam.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.aspx']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-c+\d+\.aspx']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
