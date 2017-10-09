#!/usr/bin/env python
# encoding: utf-8
"""
common.util_image.py

Created by Tien M. Le on Sep 26, 2014.
Copyright (c) 2014 __ChonGiaDung.com CGD__. All rights reserved.
"""

import json
import requests

from common.logger import logging

USER_AGENT = "Mozilla/5.0"
# IMAGE_API = "http://localhost:8098/image_cacher"
IMAGE_API = "http://localhost:8098/image_cacher"
IMAGE_API_INSERT = IMAGE_API + "/insert"

cachedImageTerms = ["ggpht.com", "cgddata"]

# Return cached image, not cached image
def cachedOrNot(image_urls):
    willBeCachedImages = []
    cachedImages = []
    for url in image_urls:
        cached = False
        for term in cachedImageTerms:
            if term in url:
                cached = True
                cachedImages.append(url)
                break
        if not cached:
            willBeCachedImages.append(url)
    return cachedImages, willBeCachedImages

def cache(image_urls, model, cache_type="SYNC"):
    payload = []
    cachedImages, willBeCachedImages = cachedOrNot(image_urls)
    for image in willBeCachedImages:
        payload.append({"originUrl": image, "model": model})
    url = IMAGE_API_INSERT + "?type=" + cache_type
    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        if cache_type == "ASYNC":
            return image_urls
        data = json.loads(response.text)
        print data
        for image in data:
            if image["googleUrl"]:
                cachedImages.append(image["googleUrl"])
        return cachedImages
    else:
        return False

def main():
    image_urls = [
        "http://static-02.lazada.vn/p/canon-0224-683602-1-zoom.jpg",
        "http://static-02.lazada.vn/p/canon-0226-683602-2-zoom.jpg",
        "https://cgddata.storage.googleapis.com/imgcacher/2014/02/09ea4087271701ea9a15526cbebc92bc.jpe"
    ]
    print cache(image_urls, "adfasf")
#     insert(image_urls)
    pass

if __name__ == "__main__":
    main()