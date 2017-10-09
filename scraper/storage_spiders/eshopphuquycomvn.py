# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='ProductDetails_Title']/h1",
    'price' : "//div[@class='field field-name-commerce-price field-type-commerce-price field-label-hidden']/div[@class='field-items']/div[@class='field-item even']",
    'category' : "",
    'description' : "//div[@class='ProductDetails_Others']/div[@class='table_product_info']",
    'images' : "//span[@class='thumb selected']/img/@data-zoomsrc",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'eshop.phuquy.com.vn'
allowed_domains = ['eshop.phuquy.com.vn']
start_urls = ['http://eshop.phuquy.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/product/[a-zA-Z0-9-/]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]