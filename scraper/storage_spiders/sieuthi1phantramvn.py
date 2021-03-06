# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pn_detail_name']/h1",
    'price' : "//div[@class='pn_detail_price']/p/strong[@class='pn_gb']",
    'category' : "//div[@class='breadcrumbs breadcrumb_url']/div/a/span",
    'description' : "//div[@class='dita_detail']",
    'images' : "//div[@class='pn_detail_img']/div/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthi1phantram.vn'
allowed_domains = ['sieuthi1phantram.vn']
start_urls = ['http://sieuthi1phantram.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/views/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/'],deny=['\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
