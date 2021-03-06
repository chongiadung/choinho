# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='name']/h1",
    'price' : "//h2[@id='detail_info']/label[@class='through'] |  //h2[@id='detail_info']/span",
    'category' : "",
    'description' : "//div[@id='dpdm-thongso']",
    'images' : "//a[@id='id_sanpham']/img[@id='id_show']/@src | //div[@class='detail_img_s']/div[@id]/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'amaytinhbang.com.vn'
allowed_domains = ['amaytinhbang.com.vn']
start_urls = ['http://amaytinhbang.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+\.html'], deny=['dien-thoai-smart-phone\.','may-tinh-bang-windows\.','may-tinh-bang\.','may-lau-don-thong-minh\.','may-tinh-bang-3g\.','phu-kien-may-tinh-bang\.','phu-kien-smartphone\.']), 'parse_item'),
    Rule(LinkExtractor(allow=['dien-thoai-smart-phone\.','may-tinh-bang-windows\.','may-tinh-bang\.','may-lau-don-thong-minh\.','may-tinh-bang-3g\.','phu-kien-may-tinh-bang\.','phu-kien-smartphone\.'], deny=['index', '/gioi-thieu/', '/lien-he', '/tin-tuc.html', '/ho-tro/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
