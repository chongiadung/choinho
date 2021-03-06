# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='title_detailproduct']",
    'price' : "//div[@class='price']/p/span[@id='our_price_display']",
    'category' : "//ul[@class='breadcrumb']/li/a",
    'description' : "//div[@class='rte']/p",
    'images' : "//ul[@id='thumbs_list_frame']/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthihoalan.com'
allowed_domains = ['sieuthihoalan.com']
start_urls = ['http://sieuthihoalan.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+-[\w\d-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+-[\w\d-]+($|\?p=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
