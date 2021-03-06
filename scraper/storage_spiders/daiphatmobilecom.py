# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='info_detail_product']/h5[1]/b",
    'price' : "//div[@id='info_detail_product']/h5[3]/b",
    'category' : "",
    'description' : "//div[@id='content_box_center_main']/div[@id='detail_about2']",
    'images' : "//div[@class='img_detail_product']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'daiphatmobile.com'
allowed_domains = ['daiphatmobile.com']
start_urls = ['http://daiphatmobile.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['chi-tiet-san-pham']), 'parse_item'),
    Rule(LinkExtractor(allow=['nhom-san-pham']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
