# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='mo-ta']/p[1]",
    'price' : "//span[@class='item_price']",
    'category' : "//div[@class='tieu-de']/h1/a",
    'description' : "//div[@id='my-cls-ajax']/table//tr[2]/td[3]",
    'images' : "//div[@id='picture']/img[@id='large_image']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'kkfashion.vn'
allowed_domains = ['kkfashion.vn']
start_urls = ['http://kkfashion.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/shop-online+/[a-zA-Z0-9_-]+\.html',''], deny = ['Huong_Dan']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/[a-zA-Z0-9-_]+\.html'], deny = ['Huong_Dan']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]