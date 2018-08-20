# -*- coding: utf-8 -*-
import scrapy
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

MAX = -1

class QiyunSpider(scrapy.Spider):
    name = 'qiyun'
    # allowed_domains = ['qiyun.org']
    # start_urls = ['http://www.gamersky.com/news/pc/zx/']
    start_urls = ['http://tvgdb.duowan.com/3ds?area=1&a=1']
    count = 1

    def parse(self, response):
        # print response.body
        if self.count == MAX: 
            print "Scrapy run finsh." 
            return
        print "---------------------------------------------------------------------------------------------"
        gameName = response.xpath("//div[@id='main']/div[@class='item']//dd/h4/a/text()").extract()
        gameBornTime = response.xpath("//div[@id='main']/div[@class='item']//dd/ul/li[4]/b/a/text()").extract()
        gameClass = response.xpath("//div[@id='main']/div[@class='item']//dd/ul/li[6]/b/a/text()").extract()
        nextPage = response.xpath("//div[@id='yw0']/a[13]/@href").extract()

        for index in range(len(gameName)):
            # print "游戏名称: ", gameName[index], " 发售时间: ", gameBornTime[index], " 游戏类型: ", gameClass[index]
            print "游戏名称: ", gameName[index]

        self.count += 1
        yield scrapy.Request(nextPage[0], callback = self.parse )
