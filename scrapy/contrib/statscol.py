"""
A Stats collector for persisting stats to Amazon SimpleDB.

Requires the boto library: http://code.google.com/p/boto/
"""

from datetime import datetime

from twisted.internet import threads

from scrapy.utils.simpledb import to_sdb_value
from scrapy.statscol import StatsCollector
from scrapy import log
from scrapy.conf import settings

class SimpledbStatsCollector(StatsCollector):

    def __init__(self):
        super(SimpledbStatsCollector, self).__init__()
        self._sdbdomain = settings['STATS_SDB_DOMAIN']
        self._access_key = settings['AWS_ACCESS_KEY_ID']
        self._secret_key = settings['AWS_SECRET_ACCESS_KEY']

        self._async = settings.getbool('STATS_SDB_ASYNC')
        import boto
        self.connect_sdb = boto.connect_sdb
        self.connect_sdb(aws_access_key_id=self._access_key, aws_secret_access_key=self._secret_key).create_domain(self._sdbdomain)

    def _persist_stats(self, stats, spider=None):
        if spider is None: # only store spider-specific stats
            return
        if not self._sdbdomain:
            return
        if self._async:
            dfd = threads.deferToThread(self._persist_to_sdb, spider, stats.copy())
            dfd.addErrback(log.err, 'Error uploading stats to SimpleDB', \
                spider=spider)
        else:
            self._persist_to_sdb(spider, stats)

    def _persist_to_sdb(self, spider, stats):
        ts = self._get_timestamp(spider).isoformat()
        sdb_item_id = "%s_%s" % (spider.name, ts)
        sdb_item = dict((k, self._to_sdb_value(v, k)) for k, v in stats.iteritems())
        sdb_item['spider'] = spider.name
        sdb_item['timestamp'] = self._to_sdb_value(ts)
        self.connect_sdb(aws_access_key_id=self._access_key, aws_secret_access_key=self._secret_key).put_attributes(self._sdbdomain, sdb_item_id, sdb_item)

    def _get_timestamp(self, spider):
        return datetime.utcnow()

    def _to_sdb_value(self, obj, key=None):
        try:
            return to_sdb_value(obj)
        except TypeError:
            raise TypeError("%s unsupported type %r used in key %r" % \
                (type(self).__name__, type(obj).__name__, key))
