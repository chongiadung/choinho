# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@class='content-show']/h3",
    'price' : "//form[@id='siteForm']/table//tr/td/span",
    'category' : "//div[@class='brescum']/p/a",
    'description' : "//div[@class='view-more']/div[@class='content-more']",
    'images' : "//div[@class='picture-view']/div[@id='showimg']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'buyspot.vn'
allowed_domains = ['buyspot.vn']
start_urls = ['http://buyspot.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/pr+\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/t+\d+c+\d+[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
