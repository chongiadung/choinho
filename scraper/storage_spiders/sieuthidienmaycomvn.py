# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='titmsg']/h1",
    'price' : "/html/body/div[1]/div/div/div[3]/div[2]/div[3]/div[1]/div[2]/div[2]/div[@class='giamoi']/strong/span[@class='price']",
    'category' : "",
    'description' : "/html/body/div[1]/div/div/div[3]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]",
    'images' : "/html/body/div[1]/div/div/div[3]/div[2]/div[3]/div[1]/div[2]/div[1]/a[@class='other']/img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'sieuthidienmay.com.vn'
allowed_domains = ['sieuthidienmay.com.vn']
start_urls = ['http://www.sieuthidienmay.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[\w\d-]+-3show1\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w\d-]+-3pro1(-\d+)*\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
