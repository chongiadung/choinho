# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-main-info']/div[@class='clearfix tpn-infoProduct']/div[@class='tpn-title-product']/h1[@class='mainbox-title tpn-bold']",
    'price' : "//div[@class='float-left product-prices']/p[@class='actual-price']",
    'category' : "//div[@class='span16 breadcrumbs-grid']/div[@id='breadcrumbs_9']/div[@class='breadcrumbs clearfix']/a[@class='vnfour_a_none']",
    'description' : "//div[@class='span11 main-content-grid']/div[@class='product-main-info']/div[@class='tpn-tabs-productsObj']/div[@id='tabs_content']",
    'images' : "//div[@class='border-image-wrap cm-preview-wrapper']/a/@href",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'thucphamnhanh.com'
allowed_domains = ['thucphamnhanh.com']
start_urls = ['http://thucphamnhanh.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[^(\.html)]+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
