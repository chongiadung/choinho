# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='row']/div[@class='seven columns productDetailInfo']/span[@class='detail']/strong",
    'price' : "//div[@class='row']/div[@class='seven columns productDetailInfo']/div/span[1]",
    'category' : "//div[@class='twelve columns']/ul[@class='breadcrumbs']/a",
    'description' : "//div[@class='tabProductType']/ul[@class='tabs-content']/li[@id='Prod2Tab']/div[@id='tab1']",
    'images' : "//div[@class='five columns productImages']/div[@id='image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dienmayphuthinh.vn'
allowed_domains = ['dienmayphuthinh.vn']
start_urls = ['http://dienmayphuthinh.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_pid+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_pcid+\d+\.html'], deny=['/filter_']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
