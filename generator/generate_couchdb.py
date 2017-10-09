#!/usr/bin/env python
# encoding: utf-8
"""
Copyright (c) 2013 CGD Inc. All rights reserved.
Author: Cuong Pham
"""
from common.util import getMd5
from django import template
import os
import pprint
import simplejson
from urlparse import urlparse

from common.cmdline import flags
from common import couch_util
from common.util import getFileNameFromSpiderName

flags.defaultString("couch_server", "")
flags.defaultString("spider_name", "")
flags.defaultString("spider_db", "spiders")
flags.defaultString("output_py", "")
flags.defaultString("output_dir", "")
flags.defaultString("spider_template", "spider_template.django.py")

def getDomain(url):
    hostname = urlparse(url).hostname
    if hostname.startswith('www.'):
        return hostname[4:]
    else:
        return hostname

def getClassNameFromDomain(domain):
    domain = domain.replace(".","")
    if domain[0].isdigit():
        domain = "www" + domain
    return domain[0].upper() + domain[1:].lower()

def main(_):
    print "Generate template for spider %s" % flags.get("spider_name")
    print "Couch server %s" % flags.get("couch_server")
    assert flags.get("couch_server")
    assert flags.get("spider_name")
    assert flags.get("output_py") or flags.get("output_dir")
       
    print "Db %s" % flags.get("spider_db")
    spider_name = flags.get("spider_name")
    spider_id = getMd5(spider_name)
    print "  spider id : %s" % spider_id
    db = couch_util.getDb(couch_util.getCouch(flags.get("couch_server")), flags.get('spider_db'), False)
    tpl = template.Template(open(flags.get("spider_template")).read())
    output_py = flags.get("output_py")
    if not output_py:
        # get output_py from output_dir/spider_name.py instead.
        output_py = os.path.join(flags.get("output_dir"), getFileNameFromSpiderName(spider_name))
        
    if True:
        # spec = simplejson.load(open("specs.json"))
        spec = dict(db[spider_id])
        print "Spider spec :"
        # copy the xpath fields into "xpath"
        if "xpath" not in spec:
            spec["xpath"] = {}
            for field in ('name', 'price', 'category', 'description', 'images'):
                spec["xpath"][field] = spec[field]
        if 'allowed_domain' not in spec:
            spec["allowed_domain"] = getDomain(spec["start_url"])
        if 'spider_class' not in spec:
            spec['spider_class'] = getClassNameFromDomain(spec['allowed_domain'])
        if 'item_url_pattern' not in spec:
            spec['item_url_pattern'] = ''
        if 'follow_link_pattern' not in spec:
            spec['follow_link_pattern'] = ''
        pprint.pprint(spec, indent = 4)
        output = tpl.render(template.Context({'spider' : spec}))
        open(output_py, "w").write(output)
        print "Scraper written to %s" % output_py


