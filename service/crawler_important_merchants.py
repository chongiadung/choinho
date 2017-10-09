#!/usr/bin/env python
# encoding: utf-8
from service.crawl_url_script import startService
import sys
def main():
    if len(sys.argv) > 1:
        startService(sys.argv[1], None, 2, 'expired', None, 1000)

if __name__ == "__main__":
    main()