# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product-title']",
    'price' : "//li[@class='purchase']/p[@class='product-price']/span[@class='price']",
    'category' : "//div[@class='breadcrumb clearfix']/span/a",
    'description' : "//div[@class='product-content entry-content clearfix']/div[1]/div",
    'images' : "//div[@class='jqzoom']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'sonthuypc.com'
allowed_domains = ['sonthuypc.com']
start_urls = ['http://sonthuypc.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/products/'], deny=['/all/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/[a-zA-Z0-9-/]+($|\?page=\d+$)'], deny=['/products/','/all']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
