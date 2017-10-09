#!/usr/bin/env python
# encoding: utf-8
"""
util_file.py

Created by Toan Luu on 2011-08-28.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import csv, codecs, cStringIO

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

def UnicodeDictReader(utf8_data, **kwargs):
    """ A CSV DictReader that works with unicode.
    """
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class DictUnicodeWriter(object):
    """ Similar to UnicodeWriter but use csv.DictWriter api """
    def __init__(self, f, fieldnames, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.DictWriter(self.queue, fieldnames, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, D):
        self.writer.writerow(dict([(k,v.encode("utf-8")) for k,v in D.items()]))
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for D in rows:
            self.writerow(D)

    def writeheader(self):
        self.writer.writeheader()



# display a list of value as a csv row
def csvRow(aList):
    s = ''
    for a in aList:
        if type(a) is unicode:
            cell = str(a.encode('utf-8'))
        else:
            cell = str(a)
        s = s + ',"' + cell.strip() + '"'
    # print s.decode('utf-8')
    return s[1:].decode('utf-8') + '\n'

#read list of values for a file and store in the list
def file2list(fileName):
    results = []
    f = codecs.open(fileName, encoding = 'utf-8')
    while 1:
        line = f.readline().strip()
        if len(line) > 0:
            results.append(line)
        if not line: break
    f.close()
    return results
    
def list2file(aList, fileName):
    f = codecs.open(fileName, 'w', 'utf-8')
    for line in aList:
        f.write(line + '\n')
    f.close()
            
def openUtfFile(fileName, mode):
    return codecs.open(fileName, mode)

def main():
    print file2list('../../data/vietnamese_compound_noun.csv')

if __name__ == '__main__':
    main()

