# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/div[@class='ma-wrapper']/div[@class='ma-page']/div[@class='ma-main-container col1-layout']/div[@class='main']/div[@class='col-main']/div[@class='product-view']/div[@class='product-essential css3']/form[@id='product_addtocart_form']/div[@class='product-shop']/div[@class='product-name']/h1",
    'price' : "//div[@class='price-box']/span/span[@class='price']",
    'category' : "/html/body/div[@class='ma-wrapper']/div[@class='ma-page']/div[@class='ma-main-container col1-layout']/div[@class='main']/div[@class='breadcrumbs']/ul/li[@class='category21']/a",
    'description' : "/html/body/div[@class='ma-wrapper']/div[@class='ma-page']/div[@class='ma-main-container col1-layout']/div[@class='main']/div[@class='col-main']/div[@class='product-view']/div[@class='product-collateral']/div[@id='product_tabs_description_contents']",
    'images' : "/html/body/div[@class='ma-wrapper']/div[@class='ma-page']/div[@class='ma-main-container col1-layout']/div[@class='main']/div[@class='col-main']/div[@class='product-view']/div[@class='product-essential css3']/form[@id='product_addtocart_form']/div[@class='product-img-box']/div[@class='more-views ma-more-img']/ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'mypham-nhatban.com'
allowed_domains = ['mypham-nhatban.com']
start_urls = ['http://mypham-nhatban.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]