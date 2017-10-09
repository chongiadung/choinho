#!/usr/bin/env python
# encoding: utf-8
"""
util_check.py

Created by Toan Vinh Luu on 2014-08-02.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""

import sys
import os
import requests
import json
from common.logger import logging

class msgcolor:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
def xtract(jsonContent, xpath):
    value = jsonContent
    tokens =  xpath.split('.')
    for path in tokens:
        if type(value) is list: value = value[0]
        if path in value: value = value[path]
        else:
            logging.error('Cannot find %s', xpath)
            return None
    return value

def xtractFromUrl(url, xpath):
    try:
        response = requests.get(url)
        jsonContent = json.loads(response.text)
        return xtract(jsonContent, xpath)
    except:
        logging.error('Cannot load json from %s', url)
        return None

            
def checkContentContain(url, expectContent):
    logging.info("checkContentContain %s  with %s" % (expectContent, url))
    try:
        response = requests.get(url)
        content = response.text.lower()
        return  content.find(expectContent.lower()) >= 0 
    except:
        logging.error('Cannot load content from %s', url)
        return False
    
def checkJsonGreater(url, xpath, expectValue):
    logging.info("checkJsonGreater %s with %s" % (expectValue, url))
    value = xtractFromUrl(url, xpath)
    if value is None: return False
    try:
        return int(value) > expectValue
    except:
        logging.warn('%s is not int', value) 
        return False

def checkJsonExist(url, xpath):
    logging.info("checkJsonExist %s with %s" % (xpath, url))
    value = xtractFromUrl(url, xpath)
    return value is not None

def checkJsonContain(url, xpath, expectValue):
    logging.info("checkJsonContain %s with %s" % (expectValue, url))
    value = xtractFromUrl(url, xpath)
    if value is None: return False
    return value.find(expectValue) >= 0
            
        
def printColor(typemsg, text):
    print typemsg + str(text) + msgcolor.ENDC
    
def printOK():
    printColor(msgcolor.OK, 'OK')

def printFail():
    printColor(msgcolor.FAIL, 'FAIL')
