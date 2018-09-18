# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from novel.items import NovelItem,ChapterItem
import os
import json

class NovelPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,NovelItem):
            os.mkdir('C:/Users/张/Desktop/个人项目/dingdian_novel/小说/%s' % item['name'])
            with open('C:/Users/张\Desktop/个人项目/dingdian_novel/小说\%s/小说介绍.txt' % item['name'],'w',encoding='gbk') as f:
                f.write('小说名:%s\n小说地址:%s\n作者:%s\n字数:%s\n更新:%s\n状态:%s' %\
                        (item['name'],item['novel_url'],item['author'],item['numbers'],item['last_time'],item['status']))
            return item
        if isinstance(item,ChapterItem):
            with open('C:/Users/张\Desktop/个人项目/dingdian_novel/小说/%s/%s.txt' % (item['name'],item['chapter_name']),'w',encoding='gbk') as f:
                f.write('                                                %s\n%s' % (item['chapter_name'],str(item['content'])))
            return item






