# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//section[@class='main']/section[@class='col-main']/div[@class='detail']/h2",
    'price' : "//div[@class='detail']/div[@class='pinfo']/p[@class='dt-row']/span[@style='color:red']",
    'category' : "//section[@class='main']/section[@class='col-main']/div[@class='discrumble']/a",
    'description' : "//section[@class='main']/section[@class='col-main']/div[@class='detail']/div[@class='pdetail']",
    'images' : "//div[@class='detail']/div[@class='image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'noithatthegioi.net'
allowed_domains = ['noithatthegioi.net']
start_urls = ['http://noithatthegioi.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
