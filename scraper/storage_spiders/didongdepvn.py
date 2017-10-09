# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='boxheadbgleft']/div[@class='boxheadbgright']",
    'price' : "//div[@class='inforDetail']/ul/li/p[@class='price']",
    'category' : "",
    'description' : "//div[@class='productDetailInforTab']/div[@class='panes']/div/table[@class='mceItemTable']//tr/td",
    'images' : "//div[@id='body']/div[@id='vlightbox1']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'didongdep.vn'
allowed_domains = ['didongdep.vn']
start_urls = ['http://didongdep.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/detail.php+\?+pid=+\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/product.php+\?+cid=+\d+\&+name=+[a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]