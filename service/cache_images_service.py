# encoding: utf-8
'''
Created on Sep 26, 2016

@author: Quyet
'''

import config
from common.logger import logging
from PIL import Image
import boto
import urllib2
from urllib2 import HTTPError
import hashlib
import redis
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
    
conn_s3 = boto.connect_s3(config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)
bucket = conn_s3.get_bucket('bucket', validate=True)
S3_BUCKET_DOMAIN = 'https://bucket.amazonaws.com/'
POLICY = 'public-read'
HEADERS = {
    'Cache-Control': 'max-age=172800',
    'Content-Type': 'image/jpeg'
}
IMAGES_THUMBS = {
    'small': (50, 50),
    'normal': (180, 180),
    'big': (300, 300)
}
MIN_WIDTH = 50
MIN_HEIGHT = 50

r = redis.StrictRedis(host=config.REDIS, password=config.REDIS_AUTH)

def cache_images(image_urls):
    images_not_cached, images_cached = download_images(image_urls)
    cnt = 0
    images = {}
    images['base_url'] = config.BASE_URL
    images['images'] = []
    images_id = {}
    for image in images_not_cached:
        image_cached = {}
        width, height = image['image'].size
        if width < MIN_WIDTH or height < MIN_HEIGHT:
            continue
        try:
            image_full, path_full = create_path_image(image['image'], image['name'])
        except:
            continue
        save_to_s3(image_full[1], path_full)
        images_id[image['name']] = image['url']
        image_cached['image_id'] = image['name']
        image_cached['thumbs_type'] = []
        for thum_id, size in IMAGES_THUMBS.iteritems():
            thum_img, path = create_path_image(image['image'], image['name'], thum_id)
            save_to_s3(thum_img[1], path)
            image_cached['thumbs_type'].append(thum_id)
            
        if image_cached:
            images['images'].append(image_cached)
        if images_id:
            r.mset(images_id)
        cnt += 1
        
    logging.info("Cached %s images" % (cnt))
    
    for image_id in images_cached:
        image_cached = {}
        image_cached['image_id'] = image_id
        image_cached['thumbs_type'] = ['big', 'normal', 'small']
        images['images'].append(image_cached)
    return images

def download_images(image_urls):
    images_not_cached = []
    images_cached = []
    for image_url in image_urls:
        image_id = hashlib.sha1(image_url).hexdigest()
        image_cached = r.get(image_id)
        if image_cached:
            images_cached.append(image_id)
            continue
        try:
            fb = urllib2.urlopen(image_url)
        except:
            fb = None
        if fb:
            try:
                image = Image.open(BytesIO(fb.read()))
                images_not_cached.append({'image': image,
                               'name': image_id,
                               'url': image_url})
            except:
                continue
    return images_not_cached, images_cached

def create_path_image(image, name, size=None):
    if size is None:
        path = 'images/full/'+name+'.jpg'
        return convert_image(image), path
    path = 'images/thumbs/'+size+'/'+name+'.jpg'
    return convert_image(image, IMAGES_THUMBS[size]), path

def convert_image(image, size=None):
    if image.format == 'PNG' and image.mode == 'RGBA':
        background = Image.new('RGBA', image.size, (255, 255, 255))
        background.paste(image, image)
        image = background.convert('RGB')
    elif image.mode != 'RGB':
        image = image.convert('RGB')

    if size:
        image = image.copy()
        image.thumbnail(size, Image.ANTIALIAS)

    buf = BytesIO()
    image.save(buf, 'JPEG')
    return image, buf

def save_to_s3(image, path):
    bucket.new_key(path).set_contents_from_string(image.getvalue(), headers=HEADERS, policy=POLICY)
