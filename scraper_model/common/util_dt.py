#!/usr/bin/env python
# encoding: utf-8
"""
util_dt.py

Utility for processing datetime

Created by Toan Vinh Luu on 2014-01-21.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""

from datetime import datetime
import time
import calendar

def sleep(second):
    time.sleep(second)
    
def rsleep():
    time.sleep(1 + random.random())

def timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
def getTimestampFromEpoch(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch))

def getEpochFromTime(timestamp):
    return  calendar.timegm(time.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))

def getEpochSinceDays(days):
    return time.time() - days * 24 * 60 * 60 
    
def main():
    epoch = 1378771200
    print getTimestampFromEpoch(epoch), epoch
    print getEpochFromTime('2013-09-10 00:00:00')
    epoch = getEpochSinceDays(10)
    print epoch
    print getTimestampFromEpoch(epoch)
    print getEpochSinceDays(60)
    
if __name__ == '__main__':
    main()