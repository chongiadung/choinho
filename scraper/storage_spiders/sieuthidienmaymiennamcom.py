# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//head/title[1]",
    'price' : "//div[@class='content']/span[@class='font_red_b']",
    'category' : "",
    'description' : "//div[@class='content_info_1']/div[@class='textx'][2]",
    'images' : "//div[@class='img_product_detail']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthidienmaymiennam.com'
allowed_domains = ['sieuthidienmaymiennam.com']
start_urls = ['http://sieuthidienmaymiennam.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-ct+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-dm+-\d+(-\d+)*\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
