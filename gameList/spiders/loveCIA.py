# -*- coding: utf-8 -*-
import scrapy
import re
from gameList.items import GamelistItem
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

minLen = 12

URI = re.compile('[a-zA-z]+://[^\s]*')
class LoveciaSpider(scrapy.Spider):
    name = 'loveCIA'
    allowed_domains = ['lovecia.com']
    start_urls = ['http://lovecia.com/tag/%E4%B8%AD%E6%96%87/']

    def parse(self, response):
        gameList = response.xpath('//h2[@class="post-title"]/a[@itemtype="url"]/@href').extract()

        for val in gameList:
            yield scrapy.Request(val, callback = self.getGameContent) 
        
        nextPage = response.xpath('//*[@id="main"]/ol/li[@class="next"]/a/@href').extract()
        if nextPage:
            yield scrapy.Request(nextPage[0], callback = self.parse)
        else:
            return

    def getGameContent(self, response):
        items = GamelistItem()

        gameName = response.xpath('//div[@id="main"]/article/h1/a/text()').extract()[0]
        gamewebLink = response.xpath('//div[@id="main"]/article/h1/a/@href').extract()[0]

        gameContent = response.xpath('//div[@id="main"]/article/div/p/text()').extract()
        if not gameContent or len(gameContent[0]) < minLen:
            gameContent = response.xpath('//*[@id="main"]/article/div/p[2]/text()').extract()
            if len(gameContent) == 0:
                gameContent = response.xpath('//div[@id="main"]/article/div/p/span/text()').extract()
                
        if not gameContent or len(gameContent[0]) < minLen:
            gameContent = "该游戏暂不存在简介"
        else:
            gameContent = gameContent[0]

        tempDownload = response.xpath('//div[@id="main"]/article/div/p/a/@href').extract()
        if tempDownload:
            tempDownload = tempDownload[0]
        else:
            tempDownload = response.xpath('//*[@id="main"]/article/div/p[4]').extract()
            if not tempDownload:
                tempDownload = response.xpath('//*[@id="main"]/article/div/p[5]').extract()
                if not tempDownload:
                    tempDownload = response.xpath('//*[@id="main"]/article/div/p[3]').extract()
            elif len(tempDownload[0]) < minLen:
                tempDownload = response.xpath('//*[@id="main"]/article/div/p[5]').extract()
                if not tempDownload:
                    tempDownload = response.xpath('//*[@id="main"]/article/div/p[3]').extract()

            tempDownload = tempDownload[0]
                
        realDownload = URI.findall(tempDownload)[0]
        passwd = URI.sub("", tempDownload)[-4:]

        items["gameName"] = gameName.decode("utf-8")
        items["pageLink"] = gamewebLink
        items["gameContent"] = gameContent
        items["downLoad"] = realDownload
        items["passwd"] = passwd
        
        yield items
        # print "game name: ", gameName, " Link: ", gamewebLink
        # print "game Content: ", gameContent
        # print "game download: ", realDownload, " passwd: ", passwd

        # print "-----------------------------------------------------------"
