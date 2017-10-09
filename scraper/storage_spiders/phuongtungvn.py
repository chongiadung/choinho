# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='ty-product-block-title']",
    'price' : "//div[@class='ty-product-block__price-actual']/span/span/span",
    'category' : "//div[@class='span16 ']/div[@id='breadcrumbs_9']/div[@class='ty-breadcrumbs clearfix']/a[@class='ty-breadcrumbs__a']",
    'description' : "//div[@class='span16 main-content-grid']/div[@class='ty-product-block product-main-info']/div[@class='noxdug']/div[@id='tabs_content']",
    'images' : "//div/div[@class='ty-product-img cm-preview-wrapper']/a/img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'phuongtung.vn'
allowed_domains = ['phuongtung.vn']
start_urls = ['http://phuongtung.vn/store/index_html/index.php']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/'], deny=['sort_by=','sort_order=','subcats=','features_hash=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]