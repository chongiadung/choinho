# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='prod_title']/a[@id='title_product_detail']",
    'price' : "//span[@class='price_item_detail']",
    'category' : "//ul[@id='becrum_ct']/li/a",
    'description' : "//div[@class='div_detailtab1 detail_wap_ct_tab']",
    'images' : "//div[@class='prod_image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'kata.vn'
allowed_domains = ['kata.vn']
start_urls = ['http://kata.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/shop/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/shop/[a-zA-Z-/0-9]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
