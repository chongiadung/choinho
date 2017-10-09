# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "{{ spider.xpath.name|safe }}",
    'price' : "{{ spider.xpath.price|safe }}",
    'category' : "{{ spider.xpath.category|safe}}",
    'description' : "{{ spider.xpath.description|safe}}",
    'images' : "{{ spider.xpath.images|safe}}",
    'canonical' : "{{spider.xpath.canonical|safe}}",
    'base_url' : "{{spider.xpath.base_url|safe}}",
    'brand' : "{{spider.xpath.brand|safe}}",
    'in_stock' : "{{spider.xpath.in_stock|safe}}",
    'guarantee' : "{{spider.xpath.guarantee|safe}}",
    'promotion' : "{{spider.xpath.promotion|safe}}"
}
name = '{{ spider.spider }}'
allowed_domains = ['{{ spider.allowed_domain }}']
start_urls = ['{{ spider.start_url|safe }}']
tracking_url = '{{ spider.tracking_url|safe }}'
sitemap_urls = ['{{ spider.sitemap_urls|safe }}']
sitemap_rules = [('{{ spider.sitemap_rules|safe }}', 'parse_item')]
sitemap_follow = ['{{ spider.sitemap_follow|safe }}']
rules = [
    {{ spider.hashtag_no_rule|safe }}Rule(LinkExtractor({{ spider.item_url_pattern|safe }}), 'parse_item'),
    {{ spider.hashtag_no_rule|safe }}Rule(LinkExtractor({{ spider.follow_link_pattern|safe }}), 'parse'),
    {{ spider.hashtag_all_rule|safe }}Rule(LinkExtractor({{ spider.all_links_pattern|safe }}), 'parse_item_and_links'),
]