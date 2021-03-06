# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title defaultTitle']/h1",
    'price' : "//em[@class='ProductPrice VariationProductPrice']",
    'category' : "//div[@id='Breadcrumb']/ul/li/a",
    'description' : "//div[@class='ProductDescriptionContainer']",
    'images' : "//div[@class='ProductTinyImageList listImages']/ul/li//a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieunhanvietnam.net'
allowed_domains = ['sieunhanvietnam.net']
start_urls = ['http://sieunhanvietnam.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
