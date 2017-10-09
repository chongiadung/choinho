# Auto generated by generator.py. Delete this line if you make modification.

from scraper.spiders.detail_scrapers import DetailScraper
from scraper.storage_spiders import adayroicom

class Adayroicom(DetailScraper):

    name = adayroicom.name
    allowed_domains = adayroicom.allowed_domains
    start_urls = adayroicom.start_urls
    tracking_url = adayroicom.tracking_url
    sitemap_urls = adayroicom.sitemap_urls
    sitemap_rules = adayroicom.sitemap_rules
    sitemap_follow = adayroicom.sitemap_follow
    rules = adayroicom.rules
    
    def __init__(self, files=None):
        DetailScraper.__init__(self, adayroicom.XPATH, files)
    