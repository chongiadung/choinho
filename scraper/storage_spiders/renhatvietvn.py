# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='row']/h1",
    'price' : "//span[@class='cost-sale']",
    'category' : "//div[@class='br ']/a",
    'description' : "//div[@id='pd-tab1']",
    'images' : "//div[@id='pd_img_box']/a/@href",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'renhatviet.vn'
allowed_domains = ['renhatviet.vn']
start_urls = ['http://renhatviet.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c\d+/[a-zA-Z0-9-]+($|/page-\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
