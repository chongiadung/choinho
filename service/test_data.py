#!/usr/bin/env python
# encoding: utf-8
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
'''
Created on Feb 28, 2017
Standardized and test item
@author: Quyet
'''

""" Output data form
{
    "category": ["...", "...", "..."],       -> Type list, multi element
    "description": ["..."],                  -> Type list, one element
    "price": ["..."],                        -> Type list, one element
    "name": "...",                           -> Type string, one element
    "source": "...",                         -> Type string, one element
    "images": ["...", "..."],                -> Type list, multi element
    "canonical": ["..."]                     -> Type list, one element
    ...
}
"""
import urlparse
from scraper.common import util_vietnamese
from service import category_blacklist
from bs4 import BeautifulSoup

BLACK_CHAR = [u"»"]
BLACK_PRODUCT_NAME = ['A PHP Error was encountered']
BLACK_PRODUCT_URL = ['http://www.sieuthimayvietnam.vn/sanpham/May-cay-lua-8-hang-tay-cay-Robot-2Z8238BGED/48268.html', 'http://www.vtconline.vn/may-cay-lua-8-hang-tay-cay-robot-2z8238bged-p37371.html']
BLACK_PRODUCT_NAME_CONTENT = [u'HAMCO', u'2Z-8238BG-E-D']
BLACK_CATEGORY = category_blacklist.BLACKLIST

def process_price(item):
    if item and 'price' in item and item['price']:
        prices = []
        for price in item['price']:
            if price != "":
                prices.append(price)
        if prices:
            item['price'] = prices
        else:
            del item['price']
    return item
        
def process_images(item):
    if item and 'images' in item and item['images']:
        images = []
        for image in item['images']:
            if image != '' and 'base64' not in image:
                images.append(image)
        # Build base_url
        if 'base_url' not in item or not item['base_url'] or item['base_url'][0] == '':
            url_parse = urlparse.urlparse(item['origin_url'])
            base_url = url_parse.scheme + '://' + url_parse.netloc
        else:
            base_url = item['base_url'][0]
        for i in range(len(images)):
            images[i] = normalization_image_url(images[i], base_url)
        if images:
            item['images'] = images
        else:
            del item['images']
    return item

def process_name(item):
    if item and 'name' in item and item['name']:
        names = []
        for name in item['name']:
            bool_contain = False
            for black_name in BLACK_PRODUCT_NAME:
                if black_name in name:
                    bool_contain = True
                    break
            if bool_contain:
                continue
            for char in BLACK_CHAR:
                name = name.replace(char, '')
            name = name.strip()
            if name != '':
                names.append(name)
        # Remove name duplicate
        names = list(set(names))
        if names:
            item['name'] = ' '.join(names).strip()
            if item['name'].isdigit():
                return None
        else:
            return None
    else:
        return None
    return item
    
def process_category(item):
    if item and 'category' in item and item['category'] and 'name' in item:
        item_name = item['name']
        categories = []
        for cat in item['category']:
            if cat != '' and cat != item_name:
                combinedCat = util_vietnamese.makePhraseToken(cat)
                if combinedCat not in BLACK_CATEGORY:
                    categories.append(cat)
        item['category'] = categories
    return item
    
def process_description(item):
    if item and 'description' in item and item['description']:
#             logging.info(type(str(' '.join(item['description']))))
        soup = BeautifulSoup(' '.join(item['description']), 'lxml')
        for img in soup.findAll('img'):
            if not img.has_attr('src'):
                continue
            if 'base64' in img['src']:
                img.extract()
                continue
            img['src'] = img['src'].replace('../', '')
            img['src'] = process_url(img['src'], item['origin_url'])
        item['description'] = [str(soup).replace('<html>', '').replace('</html>', '').replace('<body>', '').replace('</body>', '')]
    return item
    
def process_canonical(item):
    if item and 'canonical' in item and item['canonical'] is not None and len(item['canonical']) > 0:
        prop_canonical = item['canonical'][0]
        uri = urlparse.urlparse(item['origin_url'])
        if prop_canonical.startswith('/'):
            prop_canonical = uri.scheme + "://" + uri.netloc + prop_canonical
        elif not prop_canonical.startswith('/') and not prop_canonical.startswith('http'):
            prop_canonical = uri.scheme + "://" + uri.netloc + "/" + prop_canonical
        if 'http//' in prop_canonical:
            prop_canonical = prop_canonical.replace('http//', 'http://')
        if 'http:///' in prop_canonical:
            prop_canonical = prop_canonical.replace('http:///', 'http://'+uri.netloc+'/')
        item['canonical'] = [prop_canonical]
    return item

def process_url(url, origin_url):
    uri = urlparse.urlparse(origin_url)
    if url.startswith('/'):
        url = uri.scheme + "://" + uri.netloc + url
    elif not url.startswith('/') and not url.startswith('http'):
        url = uri.scheme + "://" + uri.netloc + "/" + url
    return url

def process_data(item):
    item = process_name(item)
    item = process_category(item)
    item = process_images(item)
    item = process_price(item)
    item = process_canonical(item)
    item = process_description(item)
    return item

def normalization_image_url(image_url, base_url):
    image_url = image_url.replace(' ', '%20').replace('../', '')
    if not image_url.startswith("http"):
        image_url = urlparse.urljoin(base_url, image_url)
    return image_url
