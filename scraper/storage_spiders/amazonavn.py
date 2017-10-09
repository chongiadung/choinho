# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='h1Title']",
    'price' : "//div[@class='row_infoP']/span[@class='dt_price']",
    'category' : "//div[@class='path flt']/a/span",
    'description' : "//div[@id='tabs_detail_content']/div[@class='section'][1]",
    'images' : "//img[@id='mainImage']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'amazona.vn'
allowed_domains = ['amazona.vn']
start_urls = ['http://amazona.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/[a-zA-Z0-9-]+\.html($|\?page=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]