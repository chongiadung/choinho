#!/usr/bin/env python
# encoding: utf-8
"""
common.couchbase_util
Utilities for using CouchBase

Created by Tien M. Le on May 10, 2015.
Copyright (c) 2014 __ChonGiaDung.com CGD__. All rights reserved.
"""
import json
from common.logger import logging
from couchbase.bucket import Bucket
from couchbase.exceptions import NotFoundError, HTTPError, KeyExistsError, TemporaryFailError
from common import couch_util
from couchbase.items import Item

LOGGER = logging.getLogger("common.couchbase_util")

def getDb(server, bucket_name):
    return Bucket(server + bucket_name)

def createDb(name, 
             user="", passwd="", 
             ram=100,
             replica=0,
             server="http://localhost:8091/pools/default/buckets"):
    """ Create a new bucket by using system curl command
    """
    # curl -X POST -u username:password -d name=newbucket -d ramQuotaMB=100 -d authType=none 
    # -d replicaNumber=1 -d proxyPort=11216 http://localhost:8091/pools/default/buckets
    command = "curl -X POST -u %s:%s -d name=%s -d ramQuotaMB=%s -d authType=sasl " \
                    "-d replicaNumber=%s %s" \
                    % (user, passwd, name, ram, replica, server)
    import commands
    _, output = commands.getstatusoutput(command)
    lines = output.split("\n")
    if len(lines) < 4:
        logging.info("Create new bucket: %s" % name)
        return True
    response = json.loads(lines[3])
    if 'errors' in response:
        logging.error(response)
        return False
    else:
        logging.info("Create new bucket: %s" % name)
        return True
    
def getDoc(db, docid):
    try:
        doc = db.get(docid)
        return doc.value
    except NotFoundError:
        logging.error("Not found %s" % docid)
        return None
    
def getDocsByIds(db, docids):
    rows = db.get_multi(docids)
    for row in rows:
        yield row.value

def createOrUpdate(db, docid, doc):
    try:
        return db.upsert(docid, doc)
    except KeyExistsError:
        logging.warning("Locking currently %s", docid)
        return False

def createOrUpdateBatch(db, doc_batch):
    keys = {}
    for doc in doc_batch:
        keys[doc['_id']] = doc
    return db.upsert_multi(keys)

def delete(db, docid):
    try:
        db.remove(docid)
    except NotFoundError:
        logging.warning("Not found key %s to delete" % docid)

def deleteDocsByIds(db, docids):
    oks = db.remove_multi(docids, quiet=True)
    key_not_found = 0
    for docid in docids:
        if oks[docid].rc == 0xD:
            key_not_found += 1
            logging.warning("Not found key %s to delete" % docid)
    logging.info("Deleted %d docs" % (len(docids) - key_not_found))
    
def deleteAllDocs(db):
    bulk = 10000
    docids = []
    for key in get_ids_pager(db):
        docids.append(key)
        if len(docids) >= bulk:
            deleteDocsByIds(db, docids)
            docids = []
    if len(docids) > 0:
        deleteDocsByIds(db, docids)
     
def get_pager(db, design="doc", view_name="_all_docs", startkey=None, startkey_docid=None, endkey=None, endkey_docid=None, bulk=10000, include_docs=True):
    """ Iterate over docs of db by bulk
    """
    options = {'limit': bulk}
    if startkey:
        options['startkey'] = startkey
        if startkey_docid:
            options['startkey_docid'] = startkey_docid
    if endkey:
        options['endkey'] = endkey
        if endkey_docid:
            options['endkey_docid'] = endkey_docid
    options['include_docs'] = include_docs
    options['full_set'] = True
    done = False
    try:
        while not done:
            rows = db.query(design, view_name, **options)
            cnt = 0
            for row in rows:
                cnt += 1
                options['startkey'] = row.key
                options['startkey_docid'] = row.docid
                options['skip'] = 1
                yield row.doc.value
            if cnt < bulk:
                done = True
    except HTTPError:
        logging.error("_all_docs design has not exists. Please use function design_doc to create.")
        raise HTTPError
    
def get_ids_pager(db, design="doc", view_name="_all_docs", startkey=None, startkey_docid=None, endkey=None, endkey_docid=None, bulk=10000, include_docs=False):
    """ Iterate over docs of db by bulk
    """
    options = {'limit': bulk}
    if startkey:
        options['startkey'] = startkey
        if startkey_docid:
            options['startkey_docid'] = startkey_docid
    if endkey:
        options['endkey'] = endkey
        if endkey_docid:
            options['endkey_docid'] = endkey_docid
    options['include_docs'] = include_docs
    options['full_set'] = True
    done = False
    try:
        while not done:
            rows = db.query(design, view_name, **options)
            cnt = 0
            for row in rows:
                cnt += 1
                options['startkey'] = row.key
                options['startkey_docid'] = row.docid
                options['skip'] = 1
                yield row.docid
            if cnt < bulk:
                done = True
    except HTTPError:
        logging.error("_all_docs design has not exists. Please use function design_doc to create.")
        raise HTTPError

def design_doc(db, design="doc", name="_all_docs"):
    doc_by_all_docs = {
        'map': '''
        function(doc, meta) {
            emit(null, null);
        }
    '''
    }
    
    doc_design = {
        'views': {
            '_all_docs' : doc_by_all_docs
        }
    }
    bucket_manager = db.bucket_manager()
    try:
        doc_design = bucket_manager.design_get("doc", use_devmode=False)
        if '_all_docs' not in doc_design.value['views']:
            doc_design.value['views']['_all_docs'] = doc_by_all_docs
            bucket_manager.design_create("doc", doc_design.value, use_devmode=False, syncwait=5)
    except HTTPError:
        bucket_manager.design_create("doc", doc_design, use_devmode=False, syncwait=5)

def copy_couchdb_to_couchbase(fromDb, toDb, batch_size=10000):
    batch = {}
    cnt = 0
    for doc in couch_util.get_pager(fromDb):
        del doc['_rev']
        batch[doc['_id']] = doc
        if len(batch) > batch_size:
            try:
                toDb.upsert_multi(batch)
                cnt += len(batch)
            except TemporaryFailError:
                logging.warning("Connection timeout. Try to break and update batch")
                for key, value in batch.items():
                    toDb.upsert(key, value)
                    cnt += 1
            batch = {}
            logging.info("Copied %s docs" % cnt)
    if len(batch) > 0:
        try:
            toDb.upsert_multi(batch)
            cnt += len(batch)
        except:
            logging.warning("Connection timeout. Try to break and update batch")
            for key, value in batch.items():
                toDb.upsert(key, value)
                cnt += 1
        logging.info("Copied %s docs" % cnt)
    print "Done"
        
def copy_couchbase_to_kafka(fromDb, kafka_producer, kafka_topic, batch_size=1000):
    batch = []
    for doc in get_pager(fromDb):
        batch.append(doc)
        if len(batch) > batch_size:
            kafka_producer.send_messages(kafka_topic, *[json.dumps(msg) for msg in batch])
            batch = []
    if len(batch) > 0:
        kafka_producer.send_messages(kafka_topic, *[json.dumps(msg) for msg in batch])
    logging.info("Saving Couchbase Bucket %s -> Kafka %s. Done!" % (fromDb.bucket, kafka_topic))

def copy_couchbase_to_kafka_default(fromDbName, kafka_topic, batch_size=1000):
    fromDb = getDb("couchbase://localhost/", fromDbName)
    from kafka.client import KafkaClient
    from kafka.producer import SimpleProducer
    kafka_client = KafkaClient("localhost:9092")
    kafka_producer = SimpleProducer(kafka_client,
                             req_acks=SimpleProducer.ACK_AFTER_LOCAL_WRITE,
                             batch_send=True, 
                             batch_send_every_n=batch_size,
                             batch_send_every_t=5
                            )
    copy_couchbase_to_kafka(fromDb, kafka_producer, kafka_topic, batch_size=batch_size)
    
class CouchbaseOperationType():
    DELETE = 1
    UPSERT = 0
     
class CouchbaseRecord(Item):
    def __init__(self, key=None, value=None, cas=0, op_type=CouchbaseOperationType.UPSERT):
        Item.__init__(self, key, value)
        self.cas = cas
        self.op_type = op_type
        
def createCouchbaseRecordFromValueResult(result):
    record = CouchbaseRecord()
    record.key = result.key
    record.value = result.value
    record.cas = result.cas
    return record

def main():
    pass
    
if __name__ == '__main__':
    main()
