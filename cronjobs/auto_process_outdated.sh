#!/bin/sh
cd /mofind/crawler/
TIME=`date +"%Y%m%d_%H%M%S"`
export PYTHONPATH=.
export LOG_DIR=/extra/logs/timcho
mkdir -p $LOG_DIR
LOG_FILE=$LOG_DIR/crawler_outdated.nohup.log
cp $LOG_FILE $LOG_FILE.$TIME
ps -ef | grep service/crawl_url_script.py | grep -v grep | awk '{print $2}' | xargs kill -9;
nohup /usr/bin/python2.7 service/crawl_url_script.py &> $LOG_FILE &
#tail -f $LOG_FILE
