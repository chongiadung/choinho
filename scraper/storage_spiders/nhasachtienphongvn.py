# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='brief_book']/h1",
    'price' : "//div[@id='brief_book']/p[1]/span",
    'category' : "",
    'description' : "",
    'images' : "//div[@id='detail_book_page']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nhasachtienphong.vn'
allowed_domains = ['nhasachtienphong.vn']
start_urls = ['http://www.nhasachtienphong.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/index.php/Site/Book/\d+\?name=[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/index.php/[s|S]ite/ListProHome/\d+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]