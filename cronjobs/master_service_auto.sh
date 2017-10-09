#!/bin/sh

cd /mofind/crawler/

export PYTHONPATH=.
export LOG_DIR=/extra/logs/timcho
mkdir -p $LOG_DIR
LOG_FILE=$LOG_DIR/master_service.nohup.log
ps -ef | grep master_service.py | grep -v grep | awk '{print $2}' | xargs kill -9;
nohup /usr/bin/python2.7 service/master_service.py &> $LOG_FILE &
#echo "TEST RUN" >> $LOG_FILE &
