# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class GamelistPipeline(object):
    def __init__(self):
        file_name = "chineseCIA.txt"
        self.fp = open(file_name, 'w')
        
    def process_item(self, item, spider):

        stringLink = "游戏名称: %s\n游戏页面: %s\n游戏简介: %s\n下载地址: %s\n下载密码: %s\n" % (item["gameName"], item["pageLink"], item["gameContent"], item["downLoad"], item["passwd"])

        DivLine = "==================================================================================="
        self.fp.write(stringLink + DivLine + "\n")
        return item

    def close(self):
        self.fp.close()
        
