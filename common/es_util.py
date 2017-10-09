#!/usr/bin/env python
# encoding: utf-8
"""
es_util.py

Created by Cuong Pham on 2012-09-06.
Copyright (c) 2012 ChonGiaDung.vn. All rights reserved.
"""

from logger import logging
from elasticsearch import helpers, Elasticsearch
import time
import threading
import json
from decorators import command

logging.getLogger('elasticsearch').setLevel(logging.WARNING)

class ESClient(object):

    def __init__(self, hosts, batchSize=1000, **kwargs):
        self.esConn = Elasticsearch(hosts, **kwargs)
        self.bulker = ListBulker()
        self.batchSize = batchSize
        self.ID_FIELD = "_id"
    
    def _isOk(self, response):
        return response.get('acknowledged', False)
    
    def createIndex(self, indexName = "test", body = None, mappings = None, settings = None):
        if self.esConn.indices.exists(indexName):
            self.deleteIndex(indexName)
        return self._createIndex(indexName, body, mappings, settings)
    
    def createIndexIfNotExist(self, indexName = "test", body = None, mappings = None, settings = None):
        if not self.esConn.indices.exists(indexName):
            return self._createIndex(indexName, body, mappings, settings)
        return True
    
    def _createIndex(self, indexName, body, mappings, settings):
        logging.info('Create index %s ...', indexName)
        body = self._createIndexConfig(body, mappings, settings)
        logging.debug(json.dumps(body, ensure_ascii=False, indent=4))
        
        response = self.esConn.indices.create(index=indexName, body=body)
        return self._isOk(response)
        
    def _createIndexConfig(self, body, mappings, settings):
        if not body:
            body = {}
            if settings:
                if 'settings' in settings:
                    body.update(settings)
                else:
                    body['settings'] = settings
            
            if mappings:
                if 'mappings' in mappings:
                    body.update(mappings)
                else:
                    body['mappings'] = mappings
        return body
    
    def closeIndex(self, indexName = "test"):
        response = self.esConn.indices.close(index=indexName)
        return self._isOk(response)
    
    def openIndex(self, indexName = "test"):
        response = self.esConn.indices.open(index=indexName)
        return self._isOk(response)
    
    def updateSetting(self, indexName = "test", settings = {}):
        logging.info('Update setting for index %s ...', indexName)
        self.esConn.indices.put_settings(index=indexName, body=settings)
    
    def deleteIndex(self, indexName = "test"):
        logging.info('Delete index %s ...', indexName)
        response = self.esConn.indices.delete(indexName)
        return self._isOk(response)

    def getDocById(self, indexName, indexType, docid):
        return self.esConn.get(index=indexName, doc_type=indexType, id=docid).get('_source', self.esConn.get(index=indexName, doc_type=indexType, id=docid))
    
    def getKeysAndDocsByIds(self, indexName, indexType, docids):
        docs = self.esConn.mget(index=indexName, doc_type=indexType, body={"ids": docids})
        for doc in docs:
            yield doc.get_id(), doc if doc != {} else None
    
    def getDocsByIds(self, indexName, indexType, docids):
        for _, doc in self.getKeysAndDocsByIds(indexName, indexType, docids):
            yield doc
    
    def indexDoc(self, indexName, indexType, doc, docid = None, bulk = False):
        if bulk:
            action = {
                '_op_type': 'index',
                '_index': indexName,
                '_type': indexType,
                '_source': doc
            }
            if docid:
                action['_id'] = docid
                
            self.bulker.add(action)
            return self.force_bulk()
        else:
            response = self.esConn.index(index=indexName, doc_type=indexType, id=docid, body=doc)
            return 'created' in response

    def deleteDoc(self, indexName, indexType, docid, bulk=False):
        if bulk:
            self.bulker.add({
                '_op_type': 'delete',
                '_index': indexName,
                '_type': indexType,
                '_id': docid
            })
            
            self.force_bulk()
        else:
            self.esConn.delete(index=indexName, doc_type=indexType, id=docid)


    def deleteDocs(self, indexName, indexType, docids):
        self.delete_batch(indexName, indexType, docids)

    def delete_batch(self, indexName, indexType, docids):
        actions = self._buildDeleteActions(indexName, indexType, docids)
        success, errors = helpers.bulk(self.esConn, actions)  # @UnusedVariable
        if errors:
            logging.error("Delete batch: there are some errors %s", errors)
    
    def upsert_batch(self, indexName, indexType, docs, batchSize = 1000, idField = None):
        actions = self._buildIndexActions(indexName, indexType, docs, idField)
        success, errors = helpers.bulk(self.esConn, actions, chunk_size=batchSize)  # @UnusedVariable
        if errors:
            logging.error("Upsert batch: there are some errors %s", errors)
     
    @command('return_bool')       
    def force_bulk(self, bulk = False):
        if bulk or len(self.bulker) >= self.batchSize == 0:
            success, errors = helpers.bulk(self.esConn, self.bulker.pop_all(), chunk_size=self.batchSize)  # @UnusedVariable
            if errors:
                logging.error("Force bulk: there are some errors %s", errors)
                return False
            
        return True
            
    def _buildDeleteActions(self, indexName, indexType, docids):
        actions = []
        for docid in docids:
            actions.append({
                '_op_type': 'delete',
                '_index': indexName,
                '_type': indexType,
                '_id': docid
            })
        
        return actions
    
    def _buildIndexActions(self, indexName, indexType, docs, idField = None):
        if type(docs) == list:
            return self._buildIndexActionsFromList(indexName, indexType, docs, idField)
        elif type(docs) == dict:
            return self._buildIndexActionsFromDict(indexName, indexType, docs)
        else:
            return []
    
    def _buildIndexActionsFromList(self, indexName, indexType, docs, idField):
        actions = []
        for doc in docs:
            _id = doc[idField]
            del doc[idField]
            action = {
                '_op_type': 'index',
                '_index': indexName,
                '_type': indexType,
                '_id' : _id,
                '_source': doc
            }
                
            actions.append(action)
            
        return actions
    
    def _buildIndexActionsFromDict(self, indexName, indexType, docs):
        actions = []
        for docid, doc in docs.items():
            actions.append({
                '_op_type': 'index',
                '_index': indexName,
                '_type': indexType,
                '_id': docid,
                '_source': doc
            })
            
        return actions

    def countIndexDocs(self, indexName, typeName = None):
        time.sleep(3)
        return self.esConn.count( index = indexName, doc_type = typeName )
    
    def search(self, indexName, typeName = None, query = None, params = None):
        ''' 
        :param indexName: list or string of indices
        :param typeName: list or string of types
        '''
        if type(indexName) == list:
            indexName = ','.join(indexName)
        if type(typeName) == list:
            typeName = ','.join(typeName)

        if params:
            return self.esConn.search(index=indexName, doc_type=typeName, body=query, params=params)
        else:
            return self.esConn.search(index=indexName, doc_type=typeName, body=query)
        
    def scroll(self, indexName, typeName = None, query = None, scroll = '10m', size = 1000):
        return helpers.scan(self.esConn, index=indexName, doc_type=typeName, query=query, scroll=scroll, size=size)

    def existsType(self, indexName, typeName=None):
        return self.esConn.indices.exists_type(index=indexName, doc_type=typeName)
    
    def existsIndex(self, indexName):
        return self.esConn.indices.exists_index(indexName)
    
    def putMapping(self, indexName, typeName, mapping={}):
        response = self.esConn.indices.put_mapping(index=indexName, doc_type=typeName, body=mapping)
        return self._isOk(response)
        
        
class ListBulker(object):
    '''
    A bulker that stores data in a list with synchronize operations
    '''
    
    def __init__(self):
        self.bulk_data = []
        self.bulk_lock = threading.RLock()
        
    def add(self, content):
        with self.bulk_lock:
            self.bulk_data.append(content)
            
    def pop_all(self):
        with self.bulk_lock:
            batch = self.bulk_data
            self.bulk_data = []
            return batch 
        
    def __len__(self):
        with self.bulk_lock:
            return len(self.bulk_data)   
    

def normalizeMappings(mapping, typeName, dynamic=False):
    if typeName in mapping:
        mappings = mapping
    elif 'properties' in mapping:
        mapping['dynamic'] = dynamic
        mappings = {
            typeName: mapping
        }
    else:
        mappings = {
            typeName: {
                'dynamic': dynamic,
                'properties': mapping
            }
        }
    
    return mappings


def getElasticDocs(response):
    '''
    :param response: a response from normal search 
    '''
    docs = []
    for hit in response['hits']['hits']:
        if hit.get('_source'):
            docs.append(hit['_source'])
    return docs
