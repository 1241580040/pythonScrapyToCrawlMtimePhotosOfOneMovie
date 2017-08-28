# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib2
from time import sleep
import os
import requests

#import random

class S0819MtimeTiantangPipeline(object):
    def process_item(self, item, spider):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        
        webHost = item["addr"].split("/")[2]
        print webHost

        headers = {
#                    (Request-Line)    GET /pi/2014/02/28/042456.50965899_1000X1000.jpg HTTP/1.1
                    "Host":    webHost, #'img31.mtime.cn',
                    "User-Agent":    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0',
                    "Accept":    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    "Accept-Language":   'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                    "Accept-Encoding":    'gzip, deflate',
                    "Connection":    'keep-alive',
                    "Upgrade-Insecure-Requests": "1",             
                }
        
        


        #OLD METHOD
        # req = urllib2.Request(url=item['addr'], headers=headers)
        # res = urllib2.urlopen(req)
            
        #New METHOD
        res = requests.get(item["addr"], headers=headers)

        file_name = os.path.join(os.path.curdir, "down_pic", item['name'] + '.jpg')
        with open(file_name, 'wb') as fp:
            #OLD METHOD urllib2
            #fp.write(res.read())
            #NEW METHOD
            fp.write(res.content)

        fileSize = os.path.getsize(file_name)
        print fileSize
        
        if fileSize > 5000:
            pass
        else:
            with open("./pic2KB.txt", "a") as fh:                
                fh.write(item["addr"]+"\n")

        sleep(0.5) #avoid IP was masked by mtime server
        


