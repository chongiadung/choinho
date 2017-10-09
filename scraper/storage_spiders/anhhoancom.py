# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='product-shop col-sm-7']/div/div[@class='price-box']/p[@class='special-price']/span[@class='price']",
    'category' : "",
    'description' : "//div[@class='product-tab tab-custom']/div[@class='tab-content']/div[@class='tab-pane active']",
    'images' : "//a[@class='cloud-zoom']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "//p[@class='availability in-stock']/span[@id='face-stock']",
    'guarantee' : "",
    'promotion' : ""
}
name = 'anhhoan.com'
allowed_domains = ['anhhoan.com']
start_urls = ['http://anhhoan.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/products/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]