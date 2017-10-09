# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='title_sp_detail width_common']",
    'price' : "//div[@class='block_item_detial']/div[@class='w70 price_at color_price_at']",
    'category' : "//div[@id='breakcumb']//div[@class='cate_sales_name']/a",
    'description' : "",
    'images' : "//div[@class='center_thumb']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'onlinefriday.vn'
allowed_domains = ['onlinefriday.vn']
start_urls = ['http://onlinefriday.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/nganh-hang/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]