# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='mytextarea']/span",
    'price' : "//span/div[@class='price']",
    'category' : "//div[@id='accordion']/ul/li",
    'description' : "//div[@class='table_center']/div[2]/table/tbody/tr/td|//div[@class='table_center']/div[3]/table/tbody/tr/td",
    'images' : "//img[@id='ctl00_MainPlaceHolder_ctl00_imgLaptop']/@src|//ul/li/a[@class='highslide']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thienthientan.vn'
allowed_domains = ['thienthientan.vn']
start_urls = ['http://www.thienthientan.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
