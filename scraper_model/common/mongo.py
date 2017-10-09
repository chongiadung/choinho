#!/usr/bin/env python
# encoding: utf-8
"""
mongo.py

Created by Toan Vinh Luu on 2014-02-17.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""

import sys
import os
from pymongo import MongoClient
from service import config

MONGO_SETTING = {
    'staging' : 'mongodb://'+config.MONGO_SERVER+':27017',
    'index' : 'mongodb://localhost:27017',
    'production' : 'mongodb://localhost:27017'
}

"""
Connnect to a database
"""
def connectDb(env, dbname):
    
    if env not in MONGO_SETTING:
        print 'Cannot find setting', env
        return None
    connectionStr = MONGO_SETTING[env]
    database = MongoClient(connectionStr)
    return database[dbname]

"""
Connect to a collection
"""
def connectCol(env, dbname, colname):
    db = connectDb(env, dbname)
    print 'Connect to %s, db %s, collection %s' % (MONGO_SETTING[env], dbname, colname)
    return db[colname]
  
def main():
    db = connectDb('staging', 'evaluation')
    searchCol  =  db['search']
    for doc in searchCol.find({}):
        print doc

if __name__ == '__main__':
	main()

