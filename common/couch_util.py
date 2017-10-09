import couchdb

from couchdb.http import ResourceConflict
from common.logger import logging


def getDocsByIds(db, keys, include_docs=True):
    # curl -d '{"keys":["key1","key2"]}' -X POST http://127.0.0.1:5984/foo/_all_docs?include_docs=true
    options= {}
    options['include_docs'] = include_docs
    view = db.view('_all_docs', keys = keys, **options)
    rows = view.rows
    for row in rows:
        yield row.doc

def delete(db, docid):
    try:
        db.delete(db[docid])
        logging.info("Doc %s is deleted!" % docid)
    except:
        logging.warning("Can not delete doc %s in %s" % (docid, db.name))
        pass

def deleteDocsByIds(db, docids):
    docBatch = []
    for doc in getDocsByIds(db, docids):
        if doc:
            doc["_deleted"] = True
            docBatch.append(doc)
    responses = db.update(docBatch)
    
    deleteCount = 0
    for (success, docid, _) in responses:
        if not success:
            logging.info("Failed to delete doc %s", docid)
        else:
            deleteCount += 1
    logging.info("Deleted %d docs", deleteCount)

def createOrUpdate(db, docid, doc):
    """ Create an entry or update existing one.
    """
    try:
        db[docid] = doc
    except ResourceConflict:
        db.delete(db[docid])
        db[docid] = doc

def createOrUpdateBatch(db, doc_batch):
    """ createOrUpdate in batch.
    
    Input is a list of couchdb.Document objects.
    """
    assert type(doc_batch) == list, "Bad input %s" % type(doc_batch)
    # break down doc_batch if doc_batch too large
    try:
        responses = db.update(doc_batch)
    except:
        logging.warning("Error with doc batch of size %s. Try to break it down" % len(doc_batch))
        responses = []
        for doc in doc_batch:
            responses.extend(db.update([doc]))
    failed_docs = []
    failed_keys = []
    for (success, docid, rev_or_exc), doc in zip(responses, doc_batch):
        if not success:
            assert type(rev_or_exc) == ResourceConflict
            logging.warning("  ---  try updating %s" % `docid`)
            failed_keys.append(docid)
            failed_docs.append(doc)
    existing_docs = getDocsByIds(db, failed_keys)
    for existing_doc, failed_doc in zip(existing_docs, failed_docs):
        if existing_doc["_id"] != failed_doc["_id"]:
            logging.warning("mismatch docid %s != %s" % (existing_doc["_id"], failed_doc["_id"]))
            continue
        # Copy _rev so that we can update a new version.
        failed_doc["_rev"] = existing_doc["_rev"]
    
    responses = db.update(failed_docs)
    num_failed = 0
    for (success, docid , exc) in responses:
        if not success:
            logging.error('Can not update %s %s' % (`docid`, `exc`))
            num_failed += 1
    if num_failed:
        logging.error("%d out of %d updates failed" % (num_failed, len(responses)))

            
def mergeDoc(existing_doc, new_doc):
    """ existing_doc is merged with new_doc. 
    
    Returns true/false if existing_doc is modified.
    """
    records = existing_doc.setdefault("records", [])   
    if 'records' not in new_doc:
        return False
    isModified = False
    for new_record in new_doc['records']:
        if new_record not in records:
            records.append(new_record)
            isModified = True
    logging.info("# merged records %d " % len(records))

    # Merge images.
    images = existing_doc.setdefault("images", [])   
    for new_image in new_doc['images']:
        if new_image not in images:
            images.append(new_image)
            isModified = True
    logging.info("# merged images %d " % len(images))

    # Merge sources.
    sources = existing_doc.setdefault("sources", [])   
    for new_source in new_doc['source']:
        if new_source not in sources:
            sources.append(new_source)
            isModified = True
    logging.info("# merged sources %d " % len(sources))

    return isModified
    
def createOrMergeBatch(db, doc_batch):
    """ create new or merge with existing in batch.
    
    Input is a list of couchdb.Document objects.
    """
    assert type(doc_batch) == list, "Bad input %s" % type(doc_batch)
        
    # break down doc_batch if doc_batch too large
    try:
        responses = db.update(doc_batch)
    except:
        logging.warning("Error with doc batch of size %s. Try to break it down" % len(doc_batch))
        responses = []
        for doc in doc_batch:
            responses.extend(db.update([doc]))
    for (success, docid, rev_or_exc), doc in zip(responses, doc_batch):
        if not success:
            assert type(rev_or_exc) == ResourceConflict
            if docid == doc["_id"]: continue   #same doc, updated twice.
            logging.info("Merging doc %s with %s" % (doc["_id"], docid))
            newDoc = db[docid]
            if mergeDoc(newDoc, doc):
                db[docid] = newDoc

def getCouch(server):
    """ Return a couch server object
    """
    return couchdb.Server(server)
                

def getDb(server, dbname, new = False):
    """ Return a db given server, db.
    If new is True then delete old db and create new 
    """
    if type(server) == str:
        logging.warning("getDb() with server string is deprecated, please " +
                        "pass a  Server object instead")
        server = couchdb.Server(server)
    if new:
        try:
            server.delete(dbname)
        except:
            logging.error('Database %s not found!' % dbname)
        db = server.create(dbname)
    else:
        db = server[dbname]
    return db

def getLastSequence(db):
    changes = db.changes(limit = 1, descending= True)
    return changes['last_seq']
    
def getOrCreateNew(couchServer, dbName):
    """ Get a couch Database object given dbName. If dbName is not existed,
        create a new database.
    """
    try:
        db = couchServer[dbName]
    except:   # couchdb.http.ResourceNotFound
        db = couchServer.create(dbName)
    return db

def getPager(db, view_name='_all_docs', startkey=None, startkey_docid=None, endkey=None, endkey_docid=None, bulk=10000, include_docs=True):
    """ Iterate over all docs of db by bulk
    """
    # Request one extra row to resume the listing there later.
    options = {'limit': bulk + 1}
    if startkey:
        options['startkey'] = startkey
        if startkey_docid:
            options['startkey_docid'] = startkey_docid
    if endkey:
        options['endkey'] = endkey
        if endkey_docid:
            options['endkey_docid'] = endkey_docid

    options['include_docs'] = include_docs
    done = False
    while not done:    
        view = db.view(view_name, **options)
        rows = []
        # If we got a short result (< limit + 1), we know we are done.
        if len(view) <= bulk:
            done = True
            rows = view.rows
        else:
            # Otherwise, continue at the new start position.
            rows = view.rows[:-1]
            last = view.rows[-1]
            options['startkey'] = last.key
            options['startkey_docid'] = last.id

        for row in rows:
            if row.key.startswith("_design"):   # Skip design docs.
                continue
            yield row.doc
            
def deleteAllDocs(db):
    for doc in getPager(db):
        print 'Deleting', doc['_id']
        db.delete(doc)
        
def copyDatabase(fromDb, toDb, batchSize = 1000):
    batch = []
    cnt = 0
    #from random import randint
    for doc in getPager(fromDb):
        #doc['level'] = len(doc['category_names'])
        #doc['order'] = 1
        batch.append(doc)
        if len(batch) >= batchSize:
            toDb.update(batch)
            cnt += len(batch)
            print 'Copied', cnt
            batch = []
    if len(batch) > 0: 
        toDb.update(batch)
        cnt += len(batch)
        print 'Copied', cnt
