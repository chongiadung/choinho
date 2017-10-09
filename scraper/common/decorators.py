'''
Created on Jul 28, 2016

@author: ThuyNC
'''

from functools import wraps
from  logger import logging

def command(_return):
    '''
    :param _return: 'return_bool' or 'no_return'
    '''
    if _return == 'return_bool':
        return _commandReturnBool
    else:
        return _commandNoReturn
        


def _commandReturnBool(func):
    
    @wraps(func)
    def _wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logging.error(func.__name__, exc_info=True)
            return False
    
    return _wrapped


def _commandNoReturn(func): 
    
    @wraps(func)
    def _wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            logging.error(func.__name__, exc_info=True)
    
    return _wrapped


def query(mode):
    '''
    :param mode: 'one' or 'many'
    '''
    if mode == 'one':
        return _queryOne
    else:
        return _queryMany


def _queryOne(func):

    @wraps(func)
    def _wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logging.error(func.__name__, exc_info=True)
            return None
            
    return _wrapped


def _queryMany(func):

    @wraps(func)
    def _wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logging.error(func.__name__, exc_info=True)
            return []
            
    return _wrapped


def main():
    
    @query('one')
    def aaa():
        raise ValueError('Error')
    
    @query('many')
    def bbb():
        raise ValueError('Error')
    
    @command('return_bool')
    def ccc():
        raise ValueError('Error')
    
    @command('no_return')
    def ddd():
        return True
    print aaa()    
    print bbb()
    print ccc()
    print ddd()
    

if __name__ == '__main__':
    main()
        