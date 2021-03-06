# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='info_pt']/h2",
    'price' : "//li[@class='products_price']/b",
    'category' : "//div[@class='menudd']/ul/li/a/span",
    'description' : "//div[@class='info_pt']/ul/li[6]|//div[@class='boxphai'][1]/table[1]//tr/td/div[2]",
    'images' : "//img[@id='multizoom1']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'anninh247.vn'
allowed_domains = ['anninh247.vn']
start_urls = ['http://anninh247.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-pp\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['-cp\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
