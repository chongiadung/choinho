# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@class='clearfix block__price']/span[@itemprop='price']",
    'category' : "//ol[@class='breadcrumb']/li[@itemprop='itemListElement']/a",
    'description' : "",
    'images' : "//ul[@id='thumblist']/li[@class='thumb_item ']/a/@data-image",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'cindydrella.com'
allowed_domains = ['cindydrella.com']
start_urls = ['http://cindydrella.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/products/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/all($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]