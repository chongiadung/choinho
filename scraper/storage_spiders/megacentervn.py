# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@itemprop='price']/div[@class='draw-price price-thumb-full']",
    'category' : "//div[@class='forecastle']/a",
    'description' : "//div[@class='prods_info decks big']/div[2]/table",
    'images' : "//ul[@id='pikame']/li[1]/a/img[1]/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : "//ul[@class='l pdtr-ul-info'][1]/li[3]/span",
    'in_stock' : "//ul[@class='l pdtr-ul-info'][1]/li[@class='last']",
    'guarantee' : "",
    'promotion' : ""
}
name = 'megacenter.vn'
allowed_domains = ['megacenter.vn']
start_urls = ['http://megacenter.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/san-pham-']), 'parse_item'),
    Rule(LinkExtractor(allow=['/loai-hang','/nganh-hang']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]