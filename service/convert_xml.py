# -*- coding: utf-8 -*-
"""
Read RSS xml file and save its data to couchdb

Created by Giang Nguyen Truong on 2014-09-23.
Copyright (c) 2014 Chongiadung All rights reserved.
"""

from collections import defaultdict
import json, io, os
import sys
import xml.etree.ElementTree as ET
import time
import math
import re

def parse_xml(file_name):
    events = ("start", "end")
    context = ET.iterparse(file_name, events=events)

    return print_json(context)

def print_json(context, cur_elem=None):
    items = defaultdict(list)

    if cur_elem:
        items.update(cur_elem.attrib)
    text = ""
    for action, elem in context:
        if action == "start":
            items[elem.tag].append(print_json(context, elem))
        elif action == "end":
            text = elem.text.strip() if elem.text else ""
            break
    if len(items) == 0:
        return text

    return { k: v[0] if len(v) == 1 else v for k, v in items.items() }

def debugXML(source_file):
    result = []
    json_data = parse_xml(source_file)
    data= json_data['Products']['Product']
    ts = time.time()
    total_rows = len(data)
    limit = 1000
    total_page  = int(math.ceil(total_rows/limit))
    #return total_page
    for page in range(1, total_page):
        start   = (page - 1)* limit
        for item in data[start:start+limit]:
            product = {}
            product['category'] = []
            product['images'] = []
            product['price'] = []
            product['origin_price'] = []
            product['description'] = []

            product['source']           = 'lazada.vn'
            product['name']             = item['product_name']
            product['origin_price'].append(item['price'].split('.', 1)[0])
            product['price'].append(item['discounted_price'].split('.', 1)[0])
            product['images'].append(item['zoom_picture_url'])
            product['category'].append(item['cat_m'])
            product['category'].append(item['parent_of_cat_1'])
            product['category'].append(item['category_1'])
            product['description'].append(item['description'])
            product['url']              = re.sub('%26offer_ref%3D%7Boffer_ref%7D','', item['URL'])
            product['timestamp']        = ts
            result.append(product)
            
        file_name = './data_res_' + str(start) + '.txt'
        with io.open(file_name, 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps(result, ensure_ascii=False)))
        result = []
    return "Done"

if __name__ == "__main__":
    debugXML("./feed.php")