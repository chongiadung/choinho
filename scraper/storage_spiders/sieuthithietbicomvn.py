# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='titmsg']/h1",
    'price' : "//body/div[2]/div/div[3]/div[2]/div[4]/div/div[2]/div[@class='giamoi']/strong/span[@class='price']",
    'category' : "",
    'description' : "//body/div[2]/div/div[3]/div[2]/div[4]/div/div[5]/p",
    'images' : "//body/div[2]/div/div[3]/div[2]/div[4]/div/div[2]/div[1]/a[@class='other']/img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'sieuthithietbi.com.vn'
allowed_domains = ['sieuthithietbi.com.vn']
start_urls = ['http://sieuthithietbi.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-\d+p\d+s\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['-\d+c\.html','-\d+p\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]