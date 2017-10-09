# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='clear']/div[@class='product-info']/h1[@class='mainbox-title']",
    'price' : "//span[@class='product_detail_icon']/span[@class=' product_detail_padding']/span/span/span",
    'category' : "//div[@class='central-content']/div[@class='breadcrumbs']/a",
    'description' : "//div[@id='tabs_content']/div[@id='content_block_description']//span",
    'images' : "//a[contains(@id,'detailed_href1')]/@href",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'dienmaythienhoa.vn'
allowed_domains = ['dienmaythienhoa.vn']
start_urls = ['http://www.dienmaythienhoa.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z-0-9]+\d+.*\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.html($|#\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]