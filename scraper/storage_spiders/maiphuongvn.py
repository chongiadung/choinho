# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='prod-cate']/article[@class='cont-prod']/h1[@class='t-prod-d']/span[@class='name-tpd']",
    'price' : "//div[@class='side-prod']/div[@class='wrap-sp bg-shadow']/div[@class='b-s-1 bg-shadow']/h2[@class='price-prod']",
    'category' : "//div[@class='breadcum']/ul/li/a",
    'description' : "//div[@class='prod-cate']/article[@class='cont-prod']/div[@class='info-cpd']/div[@class='i2-cpd clearfix']",
    'images' : "//meta[@property='og:image']/@content",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'maiphuong.vn'
allowed_domains = ['maiphuong.vn']
start_urls = ['http://maiphuong.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
