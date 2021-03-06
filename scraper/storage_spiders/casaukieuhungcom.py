# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='content']/p[1]/font",
    'price' : "//div[@class='contentProduct']/div[@class='content']/p[5]/font",
    'category' : "//div[@class='brearcum']/ul/li/a",
    'description' : "//div[@class='contentProduct']/div[@class='content']/p[6]",
    'images' : "//a[@class='thumbnail']/@data-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "//div[@class='content']/p[4]/span[@class='kichco1']",
    'guarantee' : "",
    'promotion' : ""
}
name = 'casaukieuhung.com'
allowed_domains = ['casaukieuhung.com']
start_urls = ['https://casaukieuhung.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['casaukieuhung\.com/[a-zA-Z0-9-]+($|/trang/\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
