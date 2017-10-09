import logging

from twisted.internet import task

from scrapy.exceptions import NotConfigured
from scrapy import signals
from common import util
from service import config

logger = logging.getLogger(__name__)
if config.DATADOG_USED == True:
    from common import metric_datadog as metr
    from common import config_name_datadog as cfg

class LogStats(object):
    """Log basic scraping stats periodically"""

    def __init__(self, stats, interval=60.0):
        self.stats = stats
        self.interval = interval
        self.multiplier = 60.0 / self.interval
        self.items_crawled = 0
        self.count_zero_sequent = 0

    @classmethod
    def from_crawler(cls, crawler):
        interval = crawler.settings.getfloat('LOGSTATS_INTERVAL')
        if not interval:
            raise NotConfigured
        o = cls(crawler.stats, interval)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

    def spider_opened(self, spider):
        self.pagesprev = 0
        self.itemsprev = 0

        self.task = task.LoopingCall(self.log, spider)
        self.task.start(self.interval)

    def log(self, spider):
        items = self.stats.get_value('item_scraped_count', 0)
        pages = self.stats.get_value('response_received_count', 0)
        irate = (items - self.itemsprev) * self.multiplier
        prate = (pages - self.pagesprev) * self.multiplier
        self.pagesprev, self.itemsprev = pages, items
        if config.DATADOG_USED == True:
            metr.gauge(cfg.TRACKING_MERCHANT + "pages_count", pages, tags=['source:%s' % spider.name])
            metr.gauge(cfg.TRACKING_MERCHANT + "pages_speed", prate, tags=['source:%s' % spider.name])
            metr.gauge(cfg.TRACKING_MERCHANT + "items_count", items, tags=['source:%s' % spider.name])
            metr.gauge(cfg.TRACKING_MERCHANT + "items_speed", irate, tags=['source:%s' % spider.name])
        msg = ("Crawled %(pages)d pages (at %(pagerate)d pages/min), "
               "scraped %(items)d items (at %(itemrate)d items/min)")
        log_args = {'pages': pages, 'pagerate': prate,
                    'items': items, 'itemrate': irate}
        logger.info(msg, log_args, extra={'spider': spider})
        if items - self.items_crawled == 0 and irate == 0:
            self.count_zero_sequent += 1
        else:
            self.count_zero_sequent = 0
        if self.count_zero_sequent >= 15:
            if config.DATADOG_USED == True:
                metr.event("SPIDER DON'T PARSE ITEMS IN LONG TIME!", "["+spider.name+"]Spider error: Don't parse items in long time, please check rule.", "warning", util.get_name_server())
                metr.incr(cfg.SPIDER_WARNING, 1)
            import requests
            requests.get("http://localhost:6082/crawler/stopcrawl?spider="+spider.name)
        self.items_crawled = items

    def spider_closed(self, spider, reason):
        if self.task.running:
            self.task.stop()
