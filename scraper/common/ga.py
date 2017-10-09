#!/usr/bin/env python
# encoding: utf-8
"""
ga.py

Created by Toan Vinh Luu on 2014-06-23.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""

import sys
import os
import gdata.analytics.client
import urllib
import requests, json

class GA(object):
    
    SOURCE_APP_NAME = 'hello'
    USERNAME = 'abc@hello.com'
    PASSWORD = ''
    TABLE_ID = ''
    
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    SCOPE = ''  # Default scope for analytics
    REDIRECT_URI = ''
    USER_AGENT = 'Analytic Script'
    ACCESS_TOKEN = ''
    
    SAVED_GLOB = ''
    
    def generateNewToken(self):
        token = gdata.gauth.OAuth2Token(
            client_id = self.CLIENT_ID,
            client_secret = self.CLIENT_SECRET,
            scope = self.SCOPE,
            user_agent = self.USER_AGENT
         )
        # Generate authorize url here:
        print token.generate_authorize_url(redirect_uri = self.REDIRECT_URI)
        print 'Copy url to browser and accept it! Copy generated token to ACCESS_TOKEN'
        # token.redirect_uri = self.REDIRECT_URI
        token.get_access_token(self.ACCESS_TOKEN)
        saved_blob_string = gdata.gauth.token_to_blob(token)
        print 'Save glob:'
        print saved_blob_string
        sys.exit(0)

    
    #Acces to Google analytics
    def __init__(self):
        self.my_client = gdata.analytics.client.AnalyticsClient(source = self.SOURCE_APP_NAME)
        token = gdata.gauth.token_from_blob(self.SAVED_GLOB)
        token.authorize(self.my_client)

    def getTopSearch(self, startDate, endDate, top):

        data_query = gdata.analytics.client.DataFeedQuery({
            'ids': self.TABLE_ID,
            'start-date': startDate,
            'end-date': endDate,
            'dimensions': 'ga:eventAction,ga:eventLabel',
            'metrics': 'ga:totalEvents',
            'filters': 'ga:eventAction==has_result',
            'sort': '-ga:totalEvents',
            'max-results': top})

        self.feed = self.my_client.GetDataFeed(data_query)

        topsearch = {}
        for entry in self.feed.entry:
            # key = urllib.unquote(entry.dimension[1].value)
            key = entry.dimension[1].value
            value = int(entry.metric[0].value)
            # print key, value
            yield key, value

    def getEventStats(self, startDate, endDate, category, action, label):

        data_query = gdata.analytics.client.DataFeedQuery({
            'ids': self.TABLE_ID,
            'start-date': startDate,
            'end-date': endDate,
            'dimensions': 'ga:eventAction,ga:eventLabel',
            'metrics': 'ga:totalEvents',
            'filters': 'ga:eventCategory==' + category + ';ga:eventAction==' + action + ';ga:eventLabel=@' + label,
            'sort': '-ga:totalEvents',
            'max-results': 100})

        self.feed = self.my_client.GetDataFeed(data_query)
        totalEvents =  self.feed.aggregates.metric[0].value
        
        results = []
        for entry in self.feed.entry:
            # print entry
            # key = urllib.unquote(entry.dimension[1].value)
            key = entry.dimension[1].value
            value = int(entry.metric[0].value)
            # print key, value
            results.append((key, value))
        return totalEvents, results

    def getActionStats(self, startDate, endDate, category, action):

        data_query = gdata.analytics.client.DataFeedQuery({
            'ids': self.TABLE_ID,
            'start-date': startDate,
            'end-date': endDate,
            'dimensions': 'ga:eventAction,ga:eventLabel',
            'metrics': 'ga:totalEvents',
            'filters': 'ga:eventCategory==' + category + ';ga:eventAction==' + action,
            'sort': '-ga:totalEvents',
            'max-results': 10000})

        self.feed = self.my_client.GetDataFeed(data_query)
        totalEvents =  self.feed.aggregates.metric[0].value

        results = []
        for entry in self.feed.entry:
            # print entry
            # key = urllib.unquote(entry.dimension[1].value)
            key = entry.dimension[1].value
            value = int(entry.metric[0].value)
            # print key, value
            results.append((key, value))
        return totalEvents, results

def getCategory(value):
    i = value.find(':')
    if i < 1: return None
    cat = value[0:value.find(':')]
    if cat .find('-') < 0: return None
    return cat

def getCustomerStats(date1, date2, customer):
    ga = GA()
    # for k, v in ga.getTopSearch('2014-06-01', '2014-06-22', 1000):
    #     print k, v
    output = ''
    output += 'Customer: %s\n' % customer
    output += 'From: %s, To: %s\n' % (date1, date2)
    for category in ['search_page', 'detail_page']:
        for action in  ['banner_display', 'banner_click']:
            output += '==========>Statistic in %s, action: %s\n' % (category, action)
            total, bannerDisplay = ga.getEventStats(date1, date2, category, action, customer)
            output += 'Number of events:\t%s\n' % total
            output += 'Detail per category:\n'
            for e in bannerDisplay:
                cat = getCategory(e[0])
                if cat is not None:
                    output += '%s\t%s\n' % (cat, e[1])
    return output

def readCategory():
    cats = {}
    r = requests.get('http://localhost:5984/cgd_category/_all_docs?include_docs=true')
    data = json.loads(r.text)
    for cat in data['rows']:
        catId = cat['id']
        name = cat['doc']['category_names'][0]['name']
        parent = []
        for p in  cat['doc']['category_names'][1:]:
            parent.insert(0, p['id'])
        cats[catId] = {'name': name, 'parent': parent, 'freq' : 0}
    return cats
            
def exportEvent(date1, date2, category, action):
    ga = GA()
    total, values = ga.getActionStats(date1, date2, category, action)
    s = 0
    cnt = 0
    for value in values:
        cnt += 1
        print '%s\t%s\t%s' % (cnt, value[0], value[1])
        s += value[1]
        
    print total, s

def analyzeDetailView(fromDate, toDate):
    ga = GA()
    cats = readCategory()
    total, values = ga.getActionStats(fromDate, toDate , 'detail_page', 'detail_cat')
    for value in values:
        catId = value[0].split(':')[0].strip()
        if len(catId.strip()) > 3:
            freq = value[1]
            cat = cats[catId]
            cat['freq'] += freq
            for p in cat['parent']:
                catParent = cats[p]
                catParent['freq'] += freq
    errors = []
    for catId, catValue in cats.items():
        if catValue['freq'] > 0:
            output = ''
            sortedKey = ''; 
            for p in catValue['parent']:
                if p in cats:
                    catParent = cats[p]
                    sortedKey += str(catParent['freq']).zfill(6) + '_' + p + '_'
                    output += '_%s\t%s\t%s\t' % (p, catParent['name'], 0)
                else:
                    errors.append('ERROR: Cannot find category for ' + p + ' as parent of category ' + catId)
            sortedKey += str(catValue['freq']).zfill(6) + '_' + catId
            output += '_%s\t%s\t%s\t' % (catId, catValue['name'], catValue['freq'])
            print sortedKey + '\t' + output

    for e in errors:
        print e
               
def main():
    # print getCustomerStats('2015-05-01', '2015-06-01', 'lingo')
    # print exportEvent('2015-02-01', '2015-03-01', 'detail_page', 'detail_cat')
    # cats = readCategory()
    # for k,v in cats.items():
    #     print k, v
    analyzeDetailView('2015-05-01', '2015-06-01')

if __name__ == '__main__':
    main()

