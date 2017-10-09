# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//span[@class='productPrice']",
    'category' : "//div[@class='breadcrumbs pathway']/a",
    'description' : "//div[@id='vmMainPage']/div[4]/table//tr/td",
    'images' : "//div[@id='vmMainPage']//td/a/img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'winwintoys.com'
allowed_domains = ['winwintoys.com']
start_urls = ['http://www.winwintoys.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/detail/[a-zA-Z0-9-]+\.html\?sef=hp$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]