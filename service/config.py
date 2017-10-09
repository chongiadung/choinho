#!/usr/bin/env python2.7
# encoding: utf-8
import copy

CONFIG_SCRAPER = {
    'couchbase_server'      : 'localhost:8091',
    'crawl_dir'             : '/mofind/crawler',
    'log_dir'               : '/extra/logs/timcho/spiders/',
    'python'                : 'python',
    'crawled_products'      : 'timcho_item_v3',
    'help_api'              : 'http://localhost:6081',
    'datadog_used'          : True,
}

CONFIG_MONGO = {
    'mongo_server'          : 'localhost',
    'mongo_env'             : 'staging',
    'mongo_crawler_db'      : 'crawler',
    'mongo_port'            : 27017,
}

CONFIG_PIPELINES = {
    'es_server'             : 'localhost:9200',
    'es_port'               : '9200',
    'crawled_index'         : 'timcho_item_v3',
    'crawled_index_type'    : 'product',
    'kafka_broker'          : 'localhost:9092',
    'kafka_topic'           : 'crawled_products',
    'kafka_max_size'        : 1000,
    'kafka_max_time'        : 5,
    'redis'                 : 'localhost',
    'redis_auth'            : 'zzzzzzzzzz',
}

CONFIG_IMAGES_CACHED = {
    'store_uri'             : 's3://bucket/images/',
    'aws_access_key_id'     : '',
    'aws_secret_access_key' : '',
    'base_url'              : '',
}

CONFIG_COMMON = copy.deepcopy(CONFIG_SCRAPER)
CONFIG_COMMON.update(CONFIG_MONGO)
CONFIG_COMMON.update(CONFIG_PIPELINES)
CONFIG_COMMON.update(CONFIG_IMAGES_CACHED)


def get(key):
    return CONFIG_COMMON.get(key)

# print "Loaded configuration "
# pprint.pprint(CONFIG_COMMON, indent = 4)

# Backward compatible configs
COUCHBASE_SERVER            = get('couchbase_server')
CRAWL_DIR                   = get('crawl_dir')
LOG_DIR                     = get('log_dir')
PYTHON                      = get('python')
CRAWLED_PRODUCTS            = get('crawled_products')
HELP_API                    = get('help_api')
DATADOG_USED                = get('datadog_used')

MONGO_SERVER                = get('mongo_server')
MONGO_ENV                   = get('mongo_env')
MONGO_CRAWLER_DB            = get('mongo_crawler_db')
MONGO_PORT                  = get('mongo_port')

ES_SERVER                   = get('es_server')
ES_PORT                     = get('es_port')
CRAWLED_INDEX               = get('crawled_index')
CRAWLED_INDEX_TYPE          = get('crawled_index_type')
KAFKA_BROKER                = get('kafka_broker')
KAFKA_TOPIC                 = get('kafka_topic')
KAFKA_MAX_SIZE              = get('kafka_max_size')
KAFKA_MAX_TIME              = get('kafka_max_time')
REDIS                       = get('redis')
REDIS_AUTH                  = get('redis_auth')

STORE_URI                   = get('store_uri')
AWS_ACCESS_KEY_ID           = get('aws_access_key_id')
AWS_SECRET_ACCESS_KEY       = get('aws_secret_access_key')
BASE_URL                    = get('base_url')

CRAWLER_SERVICE_DIR         = LOG_DIR + '/crawler_service_dir'
NOPRICE_DIR                 = LOG_DIR + '/noprice'
OUTDATED_DIR                = LOG_DIR + '/outdated'
UPDATE_OUTDATED             = '/home/logs/update_outdated'
UPDATE_MISSING              = '/home/logs/update_missing'
UPDATE_COUNT                = '/home/logs/update_count'
OUTDATED_PROCESS_DIR        = LOG_DIR + '/outdated_process'
