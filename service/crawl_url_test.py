#!/usr/bin/env python
# encoding: utf-8
import unittest
import crawl_url_script as cus

'''
    Test crawl data from url: http://hc.com.vn/ti-vi-sony-kdl-40r550c.html
'''

data_test = cus.parse_url('http://hc.com.vn/ti-vi-sony-kdl-40r550c.html')

class TestCrawlUrl(unittest.TestCase):
    def testGetSpiderNameFromUrl(self):
        spider_name = cus.getSpidersName("http://hc.com.vn/ti-vi-sony-kdl-40r550c.html")                
        self.assertTrue(".com" in spider_name)
        self.assertTrue(".vn" in spider_name)            
                
    def testGetSpidersXpathFromSpiderName(self):        
        result = cus.getXpathFromSpider('hc.com.vn')
        self.assertTrue(result)
        self.assertTrue(result['name'] is not None)
                
    def testParseItemFromXpath(self):
        result = cus.getValueFromXpath("//div[@class='product-name']/h1",data_test)
        self.assertTrue(result)
        

if __name__ == '__main__':
    unittest.main()

