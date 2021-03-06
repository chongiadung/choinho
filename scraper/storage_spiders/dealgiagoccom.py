# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@id='deal-intro']/h1/a",
    'price' : "//div[@class='deal-buy']/p[@class='deal-price']/strong | //div[@class='main']/table[@class='deal-discount']//tr[1]/td/b",
    'category' : "",
    'description' : "//div[@class='box-content cf']/div[@id='team_main_side'] | //div[@id='team_main_side']/div[@class='blk detail']/p/b/img/@src",
    'images' : "//div[@class='side']/div[@id='team_images']/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dealgiagoc.com'
allowed_domains = ['dealgiagoc.com']
start_urls = ['http://dealgiagoc.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/deal/+[a-zA-Z0-9-]+/\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/team/category.php+\?+type=+[a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
