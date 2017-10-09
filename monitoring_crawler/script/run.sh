#!/bin/bash
cd /mofind/crawler
export PYTHONPATH=.
/usr/bin/python2.7 monitoring_crawler/monitor_crawler_dtdog.py &> /extra/logs/timcho/monitor_crawler_dtdog.log &
