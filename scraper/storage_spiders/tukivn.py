# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='widget-header']/h1[@itemprop='name']",
    'price' : "//div[@id='left-content']/div[@itemprop='offers']/p[@itemprop='price']",
    'category' : "//div[@class='row row20'][3]/ol[@class='breadcrumb']/li/a",
    'description' : "//div[@class='tab-content']/div/div[@class='article-style']",
    'images' : "//div[@id='left-content']/div[@id='image-block']/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "//div[@id='right-content']/div[@id='warranty-block']/ul/li",
    'promotion' : ""
}
name = 'tuki.vn'
allowed_domains = ['tuki.vn']
start_urls = ['http://tuki.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$'], deny=['/bo-suu-tap/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
