# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='sp-infogroup']/div[@class='sp-longname lbl3 lblucase']",
    'price' : "//div[@class='label1'][3]/div[@class='label3'] | //div[@class='sp-infogroup']//td[@class='lbl3 giaban']",
    'category' : "//div[@class='mybox-title-tag bgcolor-white']/text()",
    'description' : "",
    'images' : "//div[@class='sp-imggroup']/img[@class='sp-pic-whow']/@src | //div[@class='sp-pic-all']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'aokhoacnam.com'
allowed_domains = ['aokhoacnam.com']
start_urls = ['http://aokhoacnam.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/catalog/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
