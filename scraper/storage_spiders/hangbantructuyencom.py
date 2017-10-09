# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='vnz_col1']/div/span/span[@class='price']",
    'category' : "//li[@class='category36']/a",
    'description' : "//div[@class='short-description']/div[@class='std']/address/span",
    'images' : "//p[@class='product-image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hangbantructuyen.com'
allowed_domains = ['hangbantructuyen.com']
start_urls = ['http://hangbantructuyen.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]