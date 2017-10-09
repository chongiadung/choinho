#!/bin/sh
# Usage:
# ./run.sh [command]
if [ $# -lt 1 ]
then
  echo "Usage: `basename $0` [command] <-q=optional for quiet mode>"
  echo "Example: `basename $0` crawler_service_start"
  exit
fi

cmd=$1
isQuiet=0
if [ "$2" = "-q" ]
then
    isQuiet=1
fi

TIME=`date +"%Y%m%d_%H%M%S"`
export PYTHONPATH=.
export LOG_DIR=/extra/logs/timcho
mkdir -p $LOG_DIR

if [ $cmd = "crawler_service_start" ]; then
  mkdir -p $LOG_DIR
  LOG_FILE=$LOG_DIR/scraper_webapp.nohup.log
  cp $LOG_FILE $LOG_FILE.$TIME
  ps -ef | grep scraper_webapp | grep -v grep | awk '{print $2}' | xargs kill -9;
  nohup python service/scraper_webapp.py 6081 > $LOG_FILE &

  if [ $isQuiet -eq 0 ]
  then
    echo "Tailing the log..."
    sleep 5
    tail -f $LOG_FILE
  fi
  exit
fi

if [ $cmd = "master_service_start" ]; then
  mkdir -p $LOG_DIR
  LOG_FILE=$LOG_DIR/master_service.nohup.log
  cp $LOG_FILE $LOG_FILE.$TIME
  ps -ef | grep master_service.py | grep -v grep | awk '{print $2}' | xargs kill -9;
  nohup python service/master_service.py &> $LOG_FILE &
  echo "Tailing the log..."
  sleep 5
  tail -f $LOG_FILE
  exit
fi

echo "Unknown command: $cmd"
exit 1