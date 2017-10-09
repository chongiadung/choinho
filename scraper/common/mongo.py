#!/usr/bin/env python
# encoding: utf-8
"""
mongo.py

Created by Toan Vinh Luu on 2014-02-17.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""

from pymongo import MongoClient

MONGO_SETTING = {
    'staging' : 'mongodb://localhost:2828',
    'production' : 'mongodb://localhost:2828',
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

