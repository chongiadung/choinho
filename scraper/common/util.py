#!/usr/bin/env python
# encoding: utf-8
"""
Copyright (c) 2013 CGD Inc. All rights reserved.
Author: Toan Luu
"""

import time
import random
from bs4 import BeautifulSoup
from datetime import datetime
import urllib2, requests
import operator
import hashlib
import json
import subprocess
import urlparse
import urllib
from math import sin,cos,atan2,pi,sqrt
import mongo
from common.logger import logging
import socket
from requests.exceptions import InvalidURL
from service import config

SERVER = {'ip-172-31-16-75':'crawl1',
          'ip-172-31-18-167':'crawl2',
          'ip-172-31-16-225':'crawl3'}

collection = mongo.connectCol(config.MONGO_ENV, config.MONGO_CRAWLER_DB, "spiders")

def get_name_server():
    return SERVER.get(socket.gethostname(), socket.gethostname())

class Milestone():
    """ Usage: 
            ms = Milestone()
            for ... a long loop
                ms.check(COUNT_UNTIL_REPORT_PROGRESS)
    """
        

    def __init__(self):
        self.cnt = 0

    def check(self, value):
        self.cnt = self.cnt + 1
        if self.cnt % value == 0:
            logging.info('Processed %s', self.cnt)
    
    def reset(self):
        self.cnt = 0
    
    def value(self):
        return self.cnt

def get_status_code(url):
    try:
        r = requests.get(url, allow_redirects=False, timeout = 20)
        return r.status_code
        #prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        logging.error("failed to connect")
        return None
    except InvalidURL:
        logging.error("Url %s has an invalid label" % url)
        return None
    except Exception as e:
        logging.error(e)
        return None

def cleanText(data):
    if type(data) == list: 
        return map(cleanText, data)
    elif type(data) in [str, unicode] :
        try:
        # return lxml.html.fromstring(data).text_content()
            return ' '.join(BeautifulSoup(data).findAll(text=True))
        except UnicodeEncodeError:
            return ' '.join(BeautifulSoup(data.encode('utf-8')).findAll(text=True))
    else:
        return data

def setSpiderError(spider_name):
    now = time.time()
    return collection.update( {"doc.spider": spider_name} , {"$set":{'crawler_status.status': 0 , 'doc.status' : 0, 'crawler_status.last_stop_time' : now, 'crawler_status.server_running' : None}},upsert=False, multi=False)        
  
def updateTimeStop(spider_name,items,crawled_pages):
    now = time.time()
    return collection.update( {"doc.spider": spider_name} , {"$set":{'crawler_status.last_stop_time' : now, 'crawler_status.status' : 0 ,'crawler_status.items' : items,'crawler_status.server_running' : None}},upsert=False, multi=False)

def updateTimeStart(spider_name):
    now = time.time()
    return collection.update( {"doc.spider": spider_name} , {"$set":{'crawler_status.last_start_time' : now, 'crawler_status.status' : 1, 'crawler_status.server_running' : SERVER.get(socket.gethostname(), socket.gethostname())}},upsert=False, multi=False)

def nbsp(text):
    if text is None: return None
    return text.replace('&nbsp;','')

def rsleep():
    time.sleep(1 + random.random())

def sleep(second):
    time.sleep(second)

def timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def timestampnumber():
    return datetime.now().strftime('%Y%m%d%H%M%S')

def getHtmlFromUrl(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        infile = opener.open(url)
        html = infile.read()
        return html
    except:
        return None
    
#this will return list of pair
def sortedValues(aMap):
    return sorted(aMap.iteritems(), key=operator.itemgetter(1))
  
def extract(text, beginTag, endTag):
    begin = text.find(beginTag)
    if begin > -1:
        end = text.find(endTag, begin)
        if end > -1:
            return text[begin + len(beginTag): end]
    
    return None

def getMd5(text):
    # handle the 'ordinal not in range(128)' problem
    if type(text) == unicode:
        return hashlib.md5(text.encode('utf8')).hexdigest()   
    else:
        return hashlib.md5(text).hexdigest()   

def getMd5Long(text):
    return int(getMd5(text), 16)


def printJson(tree):
    s = json.dumps(tree, sort_keys=True, indent=4 * ' ')
    print '\n'.join([l.rstrip().encode('utf-8') for l in  s.splitlines()])

def isEmpty(s):
    return (s is None) or (len(s.strip()) == 0)

def distance(lat1, lon1, lat2, lon2):
    earthradius = 6371.0    
    #Haversine formula 

    # convert to radians
    lon1 = lon1 * pi / 180.0
    lon2 = lon2 * pi / 180.0
    lat1 = lat1 * pi / 180.0
    lat2 = lat2 * pi / 180.0

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2.0))**2
    c = 2.0 * atan2(sqrt(a), sqrt(1.0-a))
    km = earthradius * c

    return km
    
def ToDebugString(object):
    """ return an utf8 string of the object. Need the conversion because sometime 
        'print object' can not print unicode string."""
    return unicode(object).encode('utf8')


def getFileNameFromSpiderName(spider_name):
    assert spider_name
    tokens = spider_name.split('.')
    if tokens[0] == 'www': 
        spider_name = tokens[1] + '.py'
    else: 
        spider_name = tokens[0] + '.py'
    if spider_name[0].isdigit():
        spider_name = "www" + spider_name
    return spider_name

def getDomainFromHost(hostname):
    for tld in TLD:
        if hostname.endswith(tld):
            pos = len(hostname) - len(tld)
            domain = hostname[0:pos].split(".")[-1] + tld
            return domain
    return hostname

def convertXPathResultToText(value):
    if type(value) == list:
        return "\n".join(value)
    else:
        return value

def capitalizeEachWord(phrase):
    if not isinstance(phrase, unicode):
        phrase = unicode(phrase)
    return " ".join(map(unicode.capitalize, phrase.split()))

TLD = [".com", ".com.vn", ".vn"]
def getDomainFromHostname(hostname):
    for tld in TLD:
        if hostname.endswith(tld):
            pos = len(hostname) - len(tld) - 1
            domain = hostname[0:pos].split(".")[-1] + tld
            return domain
    return hostname

def getItemUrlFromHasOfferUrl(has_offer_url):
    """
    http://ho.lazada.vn/SH3gPd?url=http%3A%2F%2Fwww.lazada.vn%2Festar-ce390a-muc-in-laser-90a-den-238124.html%3Foffer_id%3D%7Boffer_id%7D%26affiliate_id%3D%7Baffiliate_id%7D%26offer_name%3D%7Boffer_name%7D_%7Boffer_file_id%7D%26affiliate_name%3D%7Baffiliate_name%7D%26transaction_id%3D%7Btransaction_id%7D
    """
    if 'ho.lazada.vn':
        parsedUrl = urlparse.urlparse(has_offer_url)
        url = urlparse.parse_qs(parsedUrl.query)['url'][0].split("?")[0]
        return url
    return has_offer_url

def getSpecialItemsUrl(special_url,end_str=None):
    """
    http://click.accesstrade.vn/adv.php?rk=00003j0000uw&url=http%3A%2F%2Fwww.penda.vn%2Fp10047365%2Fvi-dai-noname-vd68%2F%3Fnse%3D1435566941%26utm_source%3Dctv1228eb%26utm_medium%3Dctv%26utm_campaign%3D06-29-2015
    """
    parsedUrl = urlparse.urlparse(special_url)
    url = None
    try:        
        if parsedUrl.query:
            url = urlparse.parse_qs(parsedUrl.query)['url'][0].split(end_str)[0]        
    except KeyError, e:
        print "Got key error " + str(parsedUrl) + " =====> " +str(e)
        return
    return url
            
def getIdFromUrl(url):
    #try:
    error_case = [{'error': 'http//',
                   'replace': 'http://'},
                  {'error': 'https//',
                   'replace': 'https://'}]
    for case in error_case:
        if case['error'] in url:
            url = url.replace(case['error'], case['replace'])
            break
    parsedUrl = urlparse.urlparse(url)
    domain = getDomainFromHostname(parsedUrl.hostname)
    # replace the hostname with domain only once.
    return getMd5(url.replace(parsedUrl.hostname, domain, 1))

"""
Excecute list of commands, e.g:
bashexec([['ls', '-lh'],['grep', '.py']])
"""
def bashexec(listCommands):
    p1 = subprocess.Popen(listCommands[0], stdout=subprocess.PIPE)
    for i in range(1, len(listCommands)):
        command = listCommands[i]
        p2 = subprocess.Popen(command, stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        p1 = p2

    output = p1.communicate()[0]
    return output.strip()

def pretty(data):
    return json.dumps(data, indent = 4, separators = (',', ': '))

def time_run(time_stop, time_start):
    return time_stop - time_start

def get_percent(x, y):
    return round(float(x)/float(y)*100,3)

def get_raw_url(url):
    if "ho.lazada.vn" in url:
        return urlparse.parse_qs(urlparse.urlparse(url).query)['url'][0].split("?")[0]
    else:
        return url

