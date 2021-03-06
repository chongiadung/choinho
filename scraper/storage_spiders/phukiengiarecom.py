# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='ty-product-block-title']",
    'price' : "//div[@class='ty-product-prices']//span[@class='ty-price']/span[@class='ty-price-num']",
    'category' : "//div[@class='ty-breadcrumbs clearfix']/div/a",
    'description' : "",
    'images' : "//div[@class='ty-product-img cm-preview-wrapper']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'phukiengiare.com'
allowed_domains = ['phukiengiare.com']
start_urls = ['http://phukiengiare.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(deny=['/phu-kien-theo-cac-dong-may/','/sac-pin-du-phong\.','/do-choi-cong-nghe\.','/tai-nghe\.','/bao-da/','/op-lung/','/theo-cac-thuong-hieu/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/phu-kien-theo-cac-dong-may/','/sac-pin-du-phong\.','/do-choi-cong-nghe\.','/tai-nghe\.','/bao-da/','/op-lung/','/theo-cac-thuong-hieu/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
