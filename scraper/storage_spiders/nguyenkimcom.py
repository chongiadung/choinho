# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='block_product-title']",
    'price' : "//span[contains(@id, 'sec_discounted_price')]",
    'category' : "//div[@class='breadcrumbs clearfix']/a",
    'description' : "//div[@id='content_description']",
    'images' : "//div[@class='border-image-wrap cm-preview-wrapper']/a/img/@data-original",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'nguyenkim.com'
allowed_domains = ['nguyenkim.com']
start_urls = ['http://www.nguyenkim.com/']
tracking_url = 'http://click.accesstrade.vn/adv.php?rk=0000uy0000uw&url=,utm_source=accesstrade&utm_medium=affiliate&utm_campaign=nguyenkim&at_sessionid={clickid}'
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow = ['/[a-zA-Z0-9-.]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/$'], deny=['sort_by=','sort_order=','features_hash=','items_per_page=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]