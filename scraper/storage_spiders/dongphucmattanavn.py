# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='page-header']/h1",
    'price' : "//span[@class='sale-price']",
    'category' : "//div[@id='breadcrumbs']/div[@class='container']/span/span/span//a",
    'description' : "//div[@class='summary entry-summary']/div[@class='woocommerce-tabs wc-tabs-wrapper']/div[@class='panel entry-content wc-tab']",
    'images' : "//div[@class='images']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'dongphucmattana.vn'
allowed_domains = ['dongphucmattana.vn']
start_urls = ['http://dongphucmattana.vn/danh-muc/san-pham-thiet-ke/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham/'], deny=['dong-phuc']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/'], deny=['/san-pham-dong-phuc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]