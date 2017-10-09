#!/usr/bin/env python
# encoding: utf-8
"""
gspread.py

Created by Toan Vinh Luu on 2014-03-27.
Copyright (c) 2014 __local.ch AG__. All rights reserved.
"""

import gspread

USERNAME = 'abc@hello.com'
PASSWORD = ''
TESTKEY = ''

def getWorksheet(key, wsNumOrTitle):
    gc = gspread.login(USERNAME, PASSWORD)
    sh = gc.open_by_key(key)
    if type(wsNumOrTitle) == int:
        return sh.get_worksheet(wsNumOrTitle)
    else:
        return sh.worksheet(wsNumOrTitle)
    
def updateTable(ws, list_of_list):
    numRows = len(list_of_list)
    numCols = 0
    for row in list_of_list:
        if len(row) > numCols: numCols = len(row)
    
    if  ws.row_count < numRows: ws.resize(rows = numRows)
    if  ws.col_count < numCols: ws.resize(cols = numCols)
    
    print 'Update table with rows =', numRows, ', cols =', numCols
    leftbottom = str(unichr(65 + numCols - 1)) + str(numRows)
    
    cells = ws.range('A1:' + leftbottom)
    for cell in cells:
        cell.value = list_of_list[cell.row - 1][cell.col - 1]
    ws.update_cells(cells)
    


def updateRow(key, ws_num, row_num, alist):
    ws = getWorksheet(key, ws_num)
    print 'Update row', row_num
    for col in range(len(alist)):
        ws.update_cell(row_num, col + 1, alist[col])
    print 'Done. View at https://docs.google.com/spreadsheet/ccc?key=' + key + '#gid=' + str(ws_num)
    
def readTable(key, ws_num, numRows, numCols):
    ws = getWorksheet(key, ws_num)
    leftbottom = str(unichr(65 + numCols - 1)) + str(numRows)
    cells = ws.range('A1:' + leftbottom)
    results = []
    for row in range(0, numRows):
        rows = []
        results.append(rows)
        for col in range(0, numCols):
            rows.append('')
            
    for cell in cells:
        results[cell.row - 1][cell.col - 1] = cell.value
    return results
    
def example1():
    #prepare data
    cells = []
    cells.append(['', 'l1', 'l2', 'l3'])
    for row in range(0,30):
        rows = ['day ' + str(row + 1)]
        for col in range(0,3):
            rows.append(row + col)
        cells.append(rows)
    #update:        
    updateTable(TESTKEY, 0, cells)

def example2():      
    table = readTable(TESTKEY, 0, 20, 3)
    for row in table:
        print row
        

def example3():
    #prepare data
    cells = []
    cells.append(['', 'l1', 'l2', 'l3'])
    for row in range(0,30):
        rows = ['day ' + str(row + 1)]
        for col in range(0,3):
            rows.append(row + col)
        cells.append(rows)
    #update:        
    updateTable(TESTKEY, 1, cells)
        
    
def main():
    example1()
    updateRow(TESTKEY, 0, 10, ['newValue1', 'newValue2', 'newValue3'])
    # example2()
    # example3()

if __name__ == '__main__':
	main()



