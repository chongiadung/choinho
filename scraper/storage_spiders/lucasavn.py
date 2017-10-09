# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='intro']/div[@id='intro_wrap']/div[@class='s_wrap']/h1",
    'price' : "//div[@id='product_share']/div[@id='product_price_']/p/span",
    'category' : "//div[@id='breadcrumbs']/div/a/span",
    'description' : "//div[@class='s_tab_box']/div[@id='product_attributes'] | //div[@class='s_tab_box']",
    'images' : "//div[@id='product_images']/div[@id='product_image_preview_holder']//img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'lucasa.vn'
allowed_domains = ['lucasa.vn']
start_urls = ['http://www.lucasa.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-/]+($|\?page=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]