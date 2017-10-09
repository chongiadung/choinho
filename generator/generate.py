# encoding: utf-8
"""
Copyright (c) 2013 CGD Inc. All rights reserved.
Author: Cuong Pham
"""
from django import template
import os
import pprint
from urlparse import urlparse

from common.cmdline import flags
from common.logger import logging
from service import config
from common.util import getFileNameFromSpiderName, getClassNameFromDomain
from common import mongo

flags.defaultString("spider_name", "")
flags.defaultString("spider_col", "spiders")
flags.defaultString("output_spider_py", "")
flags.defaultString("output_dir", "")
flags.defaultString("spider_template", "spider_template.django.py")
flags.defaultString("output_storage_py", "")
flags.defaultString("storage_spider_template", "storage_spider_template.django.py")

SPIDER_TYPE = {'sitemap' : {'detail_module' : 'detail_site_map',
                            'detail_class'  : 'DetailSiteMap'
                            },
               'crawl' : {'detail_module' : 'detail_scrapers',
                            'detail_class'  : 'DetailScraper'
                            }
               }

def getDomain(url):
    hostname = urlparse(url).hostname
    if hostname.startswith('www.'):
        return hostname[4:]
    else:
        return hostname


def getSpider(spider_name):
    print "Mongo server %s" % config.get("mongo_server")
    assert config.get("mongo_server")
    print "Db %s" % config.get("mongo_crawler_db") 
    print "  spider name : %s" % spider_name

    collection      = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, flags.get("spider_col"))
    data            = collection.find_one({"doc.spider":spider_name})
    return data['doc']


def ShouldOverwrite(spiderGeneratedPy, existingPy):
    existingCode = open(existingPy).readlines()    
    return spiderGeneratedPy.split("\n",1)[0].strip() == existingCode[0].strip()

def main(_):
    print "Generate template for spider %s" % config.get("spider_name")
    assert flags.get("output_spider_py") or flags.get("output_dir")
#     assert flags.get("output_storage_py")
    output_spider_py   = flags.get("output_spider_py")
    output_storage_py = flags.get("output_storage_py")
    spider_name = flags.get("spider_name")
#     spider_id   = getMd5(spider_name)
    db          = getSpider(spider_name)
    tpl_spider         = template.Template(open(flags.get("spider_template")).read())
    tpl_storage_spider         = template.Template(open(flags.get("storage_spider_template")).read())
    if not output_spider_py:
        # get output_spider_py from output_dir/spider_name.py instead.
        output_spider_py = os.path.join(flags.get("output_dir"), getFileNameFromSpiderName(spider_name))
    over_write = flags.get("over_write", 'false')
    name_module = getFileNameFromSpiderName(spider_name).replace('.py', '')    
    if True:
        # spec = simplejson.load(open("specs.json"))
        spec = dict(db)
        print "Spider spec :"
        spec["name_module"] = name_module
        # copy the xpath fields into "xpath"
        if "xpath" not in spec:
            spec["xpath"] = {}
            for field in ('name', 'price', 'category', 'description', 'images', 'canonical', 'base_url', 'brand', 'in_stock', 'guarantee', 'promotion'):
                if field in spec:
                    spec["xpath"][field] = spec[field]
        
        spec['hashtag_all_rule'] = "#"
        spec['hashtag_no_rule'] = ""
        if 'allowed_domain' not in spec:
            spec["allowed_domain"] = getDomain(spec["start_url"])
        if 'spider_class' not in spec:
            spec['spider_class'] = getClassNameFromDomain(spec['allowed_domain'])
        if 'item_url_pattern' not in spec:
            spec['item_url_pattern'] = ''
        if 'follow_link_pattern' not in spec:
            spec['follow_link_pattern'] = ''
        if 'all_links_pattern' not in spec:
            spec['all_links_pattern'] = ''
        if 'all_links_pattern' in spec and spec['all_links_pattern'] != '':
            spec['hashtag_no_rule'] = '#'
            spec['hashtag_all_rule'] = ''
        if 'type' not in spec or spec['type'] == "":
            spec['type'] = 'crawl'
        spec['detail_module'] = SPIDER_TYPE[spec['type']]['detail_module']
        spec['detail_class'] = SPIDER_TYPE[spec['type']]['detail_class']
            
        pprint.pprint(spec, indent = 4)
        output_spider = tpl_spider.render(template.Context({'spider' : spec}))
        output_storage = tpl_storage_spider.render(template.Context({'spider': spec}))
        
        open(output_storage_py, "w").write(output_storage)
        msg = "Scraper written to %s" % output_storage_py
        if over_write == 'true' and os.path.exists(output_spider_py) or not os.path.exists(output_spider_py):
            open(output_spider_py, "w").write(output_spider)
            msg += " and %s" % output_spider_py
        else:
            logging.warning("Spider file exists: %s", output_spider_py)
        logging.info(msg)


