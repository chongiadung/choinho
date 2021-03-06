# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='box-infoprod']/div[@class='clearfix name-prod']/h1",
    'price' : "//div[@class='box-infoprod']/div[@class='clearfix price-sell']/strong",
    'category' : "//div[@class='container']/section[@class='linkway']/article/a",
    'description' : "//article[@class='page-full']/div[@class='product-detail']/p",
    'images' : "//div[@class='img-view']/div[@id='wrap']/a/@href | //div[@class='info-product']/div[@class='img-view']//img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioirem.com'
allowed_domains = ['thegioirem.com']
start_urls = ['http://thegioirem.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
