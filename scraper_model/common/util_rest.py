#!/usr/bin/env python
# encoding: utf-8
"""
util_rest.py

RESTful utilities

Created by Toan Vinh Luu on 2013-03-29.
Copyright (c) 2013 __local.ch AG__. All rights reserved.
"""
import json

def formatDocs(title, docs):
    response = title + '\n'
    response = response + ('=' * len(title))  + '\n'
    for name in sorted(docs.keys()):
        details = docs[name]
        response = response + name + '\n'
        for detail in details:
            response = response + '\t' + detail[0] + ': ' + detail[1] + '\n'
    response = response + 'help: /help\n'
    
    return response

def msg(code, message):
    return {'code' : code, 'message' : message}

def msg_notfound(message =  'Not found'):
    return msg(404, message)

def msg_success(message = 'Success'):
    return msg(200, message)

def msg_data(message = 'Success', data = {}):
    msgdata = msg(200, message)
    msgdata['data'] = data
    return msgdata
        
def msg_fail(message = 'Fail'):
    return msg(400, message)

