#!/usr/bin/env python
# encoding: utf-8
"""
host_stats.py

Get status of cpu, memory, disk of a host.
Read http://code.google.com/p/psutil/ for detail

Created by Toan Vinh Luu on 2013-06-01.
Copyright (c) 2013 __local.ch AG__. All rights reserved.
"""

import sys
import os
import psutil
import json
import locale
# locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

def f(num):
    return locale.format("%d", num, grouping=True)
    return "%d" % num
    
def getHostStatus():
    status = {}
    
    status['cpu'] = {}
    for i in range(1,4):
        status['cpu']['t' + str(i)] = psutil.cpu_percent(interval=1)
    
    vmem = psutil.virtual_memory()
    status['memory'] = {}
    status['memory']['total'] = f(vmem.total)
    status['memory']['available'] = f(vmem.available)
    status['memory']['percent'] = vmem.percent
    status['memory']['used'] = f(vmem.used)
    status['memory']['free'] = f(vmem.free)
    status['memory']['active'] = f(vmem.active)
    status['memory']['inactive'] = f(vmem.inactive)

    usage = psutil.disk_usage('/')
    status['disk'] = {}
    status['disk']['total'] = f(usage.total)
    status['disk']['used'] = f(usage.used)
    status['disk']['free'] = f(usage.free)
    status['disk']['percent'] = usage.percent
    
    return status

def getJsonHostStatus():
    return json.dumps(getHostStatus(), indent=4)
     
def main():
    print getJsonHostStatus()
    

if __name__ == '__main__':
	main()

