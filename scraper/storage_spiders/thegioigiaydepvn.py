# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/h1[@class='mainbox-title']",
    'price' : "//p/span[contains(@id,'price_update')]/span[contains(@id,'line_discounted_price')]/span[contains(@id,'sec_discounted_price')]",
    'category' : "//div[@class='breadcrumbs']/a",
    'description' : "//div[@id='tabs_content']",
    'images' : "//div[contains(@class,'image-border float-left center cm-reload')]/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioigiaydep.vn'
allowed_domains = ['thegioigiaydep.vn']
start_urls = ['http://www.thegioigiaydep.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-[a-z]+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.html'], deny=['layout=','sort_by=','sort_order=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]