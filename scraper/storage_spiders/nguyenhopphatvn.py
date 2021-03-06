# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='Column-Right-Product']/div[@class='ProductNameLink']/h1/a",
    'price' : "//div[@class='row']/div[@id='Product-Right']/div[@class='ProductPriceNew clearfix']/span",
    'category' : "//ul[@class='col-xs-12']/li[@class='crust list-unstyled pull-left']/a[@class='crumb']/span",
    'description' : "//div[@class='quickSpecs']/article[@id='Context']/div[@class='Context']/ul[@class='ListStyle1']",
    'images' : "//img[@id='thumb']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nguyenhopphat.vn'
allowed_domains = ['nguyenhopphat.vn']
start_urls = ['http://nguyenhopphat.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['[a-zA-Z-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
