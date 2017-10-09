# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pdp_col_content']/h2[@class='HelveticaNeueRoman']",
    'price' : "//div[@class='common-price  HelveticaNeueRoman product_price_8472']/span",
    'category' : "//div[@class='breadcrumb_item']/span/a",
    'description' : "//div[@class='prod_details_box_content']/p",
    'images' : "//div[@id='alt-images']/div/input/@value",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'likewatch.com'
allowed_domains = ['likewatch.com']
start_urls = ['http://likewatch.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/shop[a-zA-Z0-9-/]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]