# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//td[@class='title16']/strong",
    'price' : "//td[@class='brd_bott'][2]/span[@class='fontred']",
    'category' : "//a[contains(@class,'linkcat')]",
    'description' : "//td[@class='paddmain']/table[2]//tr/td/div[2]",
    'images' : "//div[@align='center']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioikts.com'
allowed_domains = ['thegioikts.com']
start_urls = ['http://www.thegioikts.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['prodetail.*.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['\.html'], deny=['newsdetail']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
