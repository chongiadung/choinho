# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='name-deal-detail']",
    'price' : "//div[@class='price-prd']/h3",
    'category' : "//div[@id='ctl00_Breadcrumbs_pnlWrapper']/a",
    'description' : "//div[@class='tab-contents']",
    'images' : "//li/a[@class='imagesmall']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthi24.com'
allowed_domains = ['sieuthi24.com']
start_urls = ['http://www.sieuthi24.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
