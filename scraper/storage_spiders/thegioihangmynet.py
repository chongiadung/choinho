# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tabDetailProduct']/div[@class='colR']/div[@class='infoDetail']/div[@class='row capitalize large bold']",
    'price' : "//div[@class='colR']/div[@class='infoDetail']/div[@class='row']/span[@class='price']",
    'category' : "//div[@id='tabBody']/div[@class='tabMain']/h4[@class='titleBarMainPro']/a",
    'description' : "//div[@class='tabMain']/div[@class='padT5']/div[@class='tabDetailProduct']",
    'images' : "//div[@class='padT10']/div[@id='gallery']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioihangmy.net'
allowed_domains = ['thegioihangmy.net']
start_urls = ['http://thegioihangmy.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product+/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category+/\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]