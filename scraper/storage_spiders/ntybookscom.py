# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/th[@class='align-left']/div/h2[@class='page-title entry-title']",
    'price' : "//td[@class='align-left']/a/ins/span[@class='amount']",
    'category' : "//div[@id='breadcrumb']/span/a",
    'description' : "",
    'images' : "//div/a[@itemprop='image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'ntybooks.com'
allowed_domains = ['ntybooks.com']
start_urls = ['http://www.ntybooks.com/z/nty']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/z/nty/[a-zA-Z0-9-/]+($|/[1-2][0-9])?']), 'parse_item_and_links'),
]
