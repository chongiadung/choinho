# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='proView']/div[@id='viewRight']/form/h1",
    'price' : "//div[@id='viewRight']/form/h2/span",
    'category' : "//div[@id='conten']/div[@id='main_page']/div[@id='duongdan_link']/a",
    'description' : "//div[@id='homePro']/div[@id='pro_tabs']/div[@id='tab1']/div[@id='tabs_content']",
    'images' : "//div[@id='proView']/div[@id='viewLeft']/div[@id='imgMain']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthianninhantoan.com'
allowed_domains = ['sieuthianninhantoan.com']
start_urls = ['http://sieuthianninhantoan.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/view+-\d+-']), 'parse_item'),
    Rule(LinkExtractor(allow=['/cata+-\d+-']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
