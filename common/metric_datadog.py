"""
    Script push data to datadog dashboards
    Install lib datadog: pip install datadog

    Usage: if you want to increment a metric or elsesome on datadog metric_datadog.incr(key, value)

    NOTE: Must install datadog agent on the server which used this

    DD_API_KEY='' bash -c "$(curl -L https://raw.githubusercontent.com/DataDog/dd-agent/master/packaging/datadog-agent/source/install_agent.sh)"

"""

from datadog import initialize
from datadog import statsd
import time
#from common.logger import logging


options = {
    'api_key': ''
}
initialize(**options)

def event(title, text, alert_type, worker):
    statsd.event(title=title, text=text, alert_type=alert_type, hostname=worker)

def pushMetric_incr(key, value):
#    logging.warning("This method is deprecated, use `incr` if you want to increment a metric.")
    statsd.increment(key, value)


def incr(key, value=1, tags=None):
    statsd.increment(metric=key, value=value, tags=tags)


def decr(key, value=1, tags=None):
    statsd.decrement(metric=key, value=value, tags=tags)


def set(key, value, tags=None):
    statsd.set(metric=key, value=value, tags=tags)

def gauge(key, value, tags=None):
    statsd.gauge(metric=key, value=value, tags=tags)
    
    
from datadog import api
# api.Metric.send(metric="home.page.ping", points=1)

# Push a single metric
def pushMetric(key, value):
    api.Metric.send(metric=key, points=value)

# Push multiple metrics
# Contructor data: [{'key':'name_key1', 'value':value1},{'key':'name_key2', 'value':value2},...]
def pushMetrics(data):
    metrics_data = []
    for metric in data:
        metrics_data.append({'metric':metric['key'], 'points':metric['value']})
    api.Metric.send(metrics_data)

# def main():
#     # data = [{'key':'my.series', 'value':1},{'key':'my1.series', 'value':10}]
#     pushMetric('tracking.merchant.deca.vn', 1)

# if __name__ == "__main__":
#     main()
