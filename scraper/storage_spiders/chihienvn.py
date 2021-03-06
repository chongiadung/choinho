# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='box-content']/div[@class='box-header']/h1",
    'price' : "//div[@class='product-detail-table']/div[@class='product-field']/table//tr[7]/td[2]",
    'category' : "//div[@id='breadcrumbs']/a",
    'description' : "//div[@id='content_description']/p",
    'images' : "//div[@class='product-detail-thumb']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'chihien.vn'
allowed_domains = ['chihien.vn']
start_urls = ['http://chihien.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+-sp+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danhmuc.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
