# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/div[@class='wrapper']/div[@id='km_navigationemain']/div[@id='km_main']/div[@id='boxcontain']/div[@class='main-catalogcontent']/div[@id='chitiet']/div[@class='rowsp']/div[@class='dtitle']/h1",
    'price' : "/html/body/div[@class='wrapper']/div[@id='km_navigationemain']/div[@id='km_main']/div[@id='boxcontain']/div[@class='main-catalogcontent']/div[@id='chitiet']/div[@class='rowsp']/div[@class='dgia']/strong",
    'category' : "/html/body/div[@class='wrapper']/div[@id='km_navigationemain']/div[@id='km_main']/div[@id='boxcontain']/div[@class='main-catalogtitle']",
    'description' : "//div[@class='rowsp']/div[@class='dcontent']/span",
    'images' : "/html/body/div[@class='wrapper']/div[@id='km_navigationemain']/div[@id='km_main']/div[@id='boxcontain']/div[@class='main-catalogcontent']/div[@id='chitiet']/div[@class='rowsp']/div[@class='imgdetail']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dungcuykhoakimminh.com'
allowed_domains = ['dungcuykhoakimminh.com']
start_urls = ['http://dungcuykhoakimminh.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham+-\d+/[a-zA-Z0-9]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
