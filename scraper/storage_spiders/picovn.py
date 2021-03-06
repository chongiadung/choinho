# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-single']/div[@class='page-noneback']/h1",
    'price' : "//div[@class='sidebar-box-content sidebar-padding-box product-single-info ']/span[@class='price'] | //div[@class='sidebar-box-content sidebar-padding-box product-single-info ']/div[@class='priceInfo']/span[@class='price']",
    'category' : "//div[@class='links-breadcrumbs']/div/a/span",
    'description' : "//div[@class='social-bar'][1]/p|//div[@class='content-descr']",
    'images' : "//link[@rel='image_src']/@href | //div[@class='jqzoom_pico']/a/@href | //div[@id='product-slider']/ul[@class='slides']/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : "//div[@id='part_promotion']/ul/li"
}
name = 'pico.vn'
allowed_domains = ['pico.vn']
start_urls = ['http://pico.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/\d+/[a-zA-Z0-9-_]+\.html$'], deny=['-nhom-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-nhom-\d+\.html($|\?&pageIndex=\d+$)'], deny=['min=','max=','/tin-tuc','/[a-zA-Z0-9-]+ban-tin+-\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
