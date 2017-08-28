# -*- coding: utf-8 -*-
import scrapy
import random
from S0819Mtime_tiantang.items import S0819MtimeTiantangItem

class MtimeSpider(scrapy.Spider):
    name = "mtime"
    allowed_domains = ["http://www.mtime.com"]
    start_urls = (
        'http://movie.mtime.com/79055/posters_and_images/posters/hot.html',
    )

    def parse(self, response):
        #print response
        #allpics = response.xpath("//script[@type='text/javascript']").extract()[4]
        allpics = response.xpath("//script[@type='text/javascript']").re('\"img_1000\":\"(.+?jpg)\"')
        print len(allpics)
        #while True:
        #    pass
        #re('\"img_1000\":\"(.+?jpg)\"')
        #allpics = response.xpath("//")
        #print "000"
        #print allpics
        #print "1"
        nameList = []
        i = 0
        for pic in allpics:
            i = i+1
            #print "2"
            item = S0819MtimeTiantangItem()
            #print "3"
            # while True:
            #     #itemName = random.randint(0, 1000)*3
            #     #itemName = str(itemName)
            #     if itemName in nameList:
            #         pass
            #     else:
            #         name = str(i)
            #         nameList.append(itemName)
            #         #print "-----"+itemName
            #         print "-----"
            #         #print nameList
            #         break
            
            item['name'] = str(i)
            item['addr'] = pic
            print "+++++"+item['name']
            print "+++++"+item['addr']
            yield item
            
