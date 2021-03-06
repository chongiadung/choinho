# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='single_meta_produc']/h1",
    'price' : "//div[@class='single_meta_produc']/div[@class='prile_giaca']/p",
    'category' : "//nav[@class='woocommerce-breadcrumb']/a",
    'description' : "//div[@id='chitietsanpham']",
    'images' : "//div[@class='single_img_produc']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'congtyherbalife.com'
allowed_domains = ['congtyherbalife.com']
start_urls = ['http://congtyherbalife.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['kiem-soat-can-nang','ho-tro-tim-mach','ho-tro-xuong-khop','ho-tro-tieu-hoa','dinh-duong-cho-be-yeu','cac-san-pham-khac']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
