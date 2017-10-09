#!/usr/bin/env python
# encoding: utf-8
""" Usage:
       from common.logger import logging
       logging.info('...')
    From command line:
       ./program.py --debug_level debug --log_file stdout
"""

import logging as default_logging
import sys

logging = default_logging
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)
urllib3_log = logging.getLogger("urllib3")
urllib3_log.setLevel(logging.WARNING)

from cmdline import flags

DEBUG_LEVELS = {
    'info' : logging.INFO,
    'debug' : logging.DEBUG,
    'warning' : logging.WARNING,
    'error' : logging.ERROR,
}

debug_level = flags.get("debug_level", 'info')
if debug_level in DEBUG_LEVELS:
    debug_level = DEBUG_LEVELS[debug_level]
else:
    debug_level = logging.ERROR

LOG_FORMAT = '%(asctime)s (%(levelname)s) : [%(name)s],%(filename)s:%(lineno)d %(message)s'

log_file = flags.get("log_file")

if log_file:
    sys.stderr.write("Logging to file %s\n" % log_file)
    logging.basicConfig(filename=log_file, level=debug_level, format=LOG_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
else:
    logging.basicConfig(level=debug_level, format=LOG_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
