#!/usr/bin/env python
# encoding: utf-8
"""
util_config.py
read write simple config containg key-value separated by "="
Created by Toan Luu on 2011-11-11.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os

params = {}
filename = 'config.txt'

def read(fn):
    global params
    global filename
    
    if fn is not None: filename = fn
    
    f = open(filename)
    for l in f:
        tokens = l.split('=')
        if len(tokens) == 2:
            params[tokens[0].strip()] = tokens[1].strip()
    f.close()
    
def write(key, value):
    global params
    params[key] = value
    f = open(filename, 'w')
    for key, value in params.items():
        f.write(key + ' = ' + str(value) + '\n')
    f.close()

def get(key):
    try:
        return params[key]
    except:
        print 'Error when reading key', k
        return None
    
def main():
    pass
    


if __name__ == '__main__':
	main()

