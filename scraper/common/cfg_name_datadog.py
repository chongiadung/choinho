'''
Metric id tracking
'''
TRACKING = "tracking."
TRACKING_MERCHANT = TRACKING + "merchant."


'''
Metric id crawler
'''
CRAWLER = 'crawler.'
CRAWLER_SPEED = CRAWLER + 'speed'
CRAWLER_OUTDATED_SPEED = CRAWLER + 'outdated.speed'
CRAWLER_DATA_FEED_SPEED = CRAWLER + 'datafeed.speed'
'''
Metric id crawler monitoring
'''
CRAWLER_MONITORING = CRAWLER + 'monitoring.'

WORKER_1 = CRAWLER_MONITORING + 'worker.1'
WORKER_2 = CRAWLER_MONITORING + 'worker.2'
WORKER_3 = CRAWLER_MONITORING + 'worker.3'

TOTAL_SPIDERS = CRAWLER_MONITORING + 'total.spiders'
PEDING_SPIDERS = CRAWLER_MONITORING + 'pending.spiders'
RUNNING_SPIDERS = CRAWLER_MONITORING + 'running.spiders'

NOT_RUNNING_SPIDERS = CRAWLER_MONITORING + 'not.run.spiders'
MISSING_SPIDERS = CRAWLER_MONITORING + 'missing.spiders'
DUPLICATE_SPIDERS = CRAWLER_MONITORING + 'dup.spiders'

SPIDER_ERROR = CRAWLER_MONITORING + 'error'
SPIDER_WARNING = CRAWLER_MONITORING + 'warning'

