# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='divName']",
    'price' : "//div[@class='price_info']",
    'category' : "//div[@class='navation']/div[@class='home']/span/a",
    'description' : "//div[@class='desc']/table[@class='product_technical_table']",
    'images' : "//div[@id='divImage']/a/@href | //div[@class='imgPro']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthionline.com'
allowed_domains = ['sieuthionline.com']
start_urls = ['http://www.sieuthionline.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/detail/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/product+/[a-zA-Z0-9-]+-\d+\.html($|/\?p=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]