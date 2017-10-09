#!/usr/bin/env python
# encoding: utf-8

from common import config_name_datadog as cfg
from common import metric_datadog as metr
import service.monitor_crawler_service as mcs
# vars stats:
stats = {
    'nThreadsWorker' : 0,
    'nSpdsMiss' : 0,
    'nSpdsNotRun' : 0,
    'totalSpds' : 0,
    'pendingSpds' : 0,
    'runningSpds' : 0
}

def setStats():
    # Number threads in workers
    data_threads = mcs.get_thread_workers()
    stats['nThreadsWorker'] = data_threads.get('total_crawler_thread', 0)
    
    spds_running = mcs.get_list_spiders(data_threads)
    spds_stt_running = mcs.get_list_spiders(mcs.get_spds_stt_running())
    
    stats['nSpdsMiss'] = mcs.count_spiders(mcs.get_spiders_missing(spds_stt_running, spds_running))
    stats['nSpdsNotRun'] = mcs.count_spiders(mcs.get_spiders_not_running(spds_stt_running, spds_running))
    
    stats['totalSpds'] = mcs.count_spiders(mcs.get_total_spds())
    stats['pendingSpds'] = mcs.count_spiders(mcs.get_spds_stt_pending())
    stats['runningSpds'] = mcs.count_spiders(mcs.get_spds_stt_running())

def push_datadog():
    setStats()
    metr.gauge(cfg.WORKER, stats['nThreadsWorker'])
#     metr.gauge(cfg.WORKER_2, thread_w2)
#     metr.gauge(cfg.WORKER_3, thread_w3)
    metr.gauge(cfg.TOTAL_SPIDERS, stats['totalSpds'])
    metr.gauge(cfg.PEDING_SPIDERS, stats['pendingSpds'])
    metr.gauge(cfg.RUNNING_SPIDERS, stats['runningSpds'])
    metr.gauge(cfg.NOT_RUNNING_SPIDERS, stats['nSpdsNotRun'])
    metr.gauge(cfg.MISSING_SPIDERS, stats['nSpdsMiss'])

if __name__ == "__main__":
    push_datadog()
