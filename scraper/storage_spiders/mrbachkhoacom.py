# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div/div[@id='pb-right-column']/h1[@class='name clearfix']/a",
    'price' : "//div[@class='product_attributes']/div[@class='price']/p[@class='our_price_display']/span[@id='our_price_display']",
    'category' : "//div[@class='page_wrapper_2 clearfix']/div[@id='columns']/div[@class='breadcrumb clearfix']/a",
    'description' : "//div[@id='primary_block']/div/div[@id='pb-right-column']/div[@id='idTab1']",
    'images' : "//div[@class='owl-wrapper']/div[@class='owl-item']/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'mrbachkhoa.com'
allowed_domains = ['mrbachkhoa.com']
start_urls = ['http://mrbachkhoa.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
