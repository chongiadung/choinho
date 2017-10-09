# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pro-cover']/div[@class='title']/h2/a",
    'price' : "//span[@class='p-cost']",
    'category' : "//div[@id='casing']/ul[@class='breadcrumbs clearfix']/li",
    'description' : "//div[@class='pro-cover']/div[@class='entry'] | //a/img[@class='aligncenter size-full wp-image-4564']/@src",
    'images' : "//div[@class='pro-snap']/a/img[@class='boximg']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'aobongda.edu.vn'
allowed_domains = ['aobongda.edu.vn']
start_urls = ['http://aobongda.edu.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/item+/[a-zA-Z0-9-_]+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/product+/[a-zA-Z0-9-_]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]