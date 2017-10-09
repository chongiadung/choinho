# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='product-shop']/div//span[@class='price']",
    'category' : "//a[@class='has-link']|//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='std']",
    'images' : "//div[@class='more-views']/ul/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : "//div[@class='product-view-promo']/ul/li/text()"
}
name = 'hc.com.vn'
allowed_domains = ['hc.com.vn']
start_urls = ['https://hc.com.vn/']
tracking_url = 'http://go.masoffer.net/v1/6IXrYbHh32J9Sawqlp2CvNjjZiABFjMFkHxyzKldpDY/?url=,utm_source=masoffer'
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['hc\.com\.vn/[a-zA-Z0-9-]+($|\?p=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]