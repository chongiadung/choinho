# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h2[@id='hTitleDeal']/span/p",
    'price' : "//p[@class='pGiaTienID']/strong",
    'category' : "",
    'description' : "//div[@class='div_LBodyHL']",
    'images' : "//div[@class='lof-main-outer']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'windeal.vn'
allowed_domains = ['windeal.vn']
start_urls = ['http://windeal.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/xem-san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow = ['\?type']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
