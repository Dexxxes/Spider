# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    novel_url = scrapy.Field()#小说地址
    name = scrapy.Field()     #书名
    author = scrapy.Field()   #作者
    status = scrapy.Field()   #状态
    numbers = scrapy.Field()  #字数
    last_time = scrapy.Field()#更新时间

class ChapterItem(scrapy.Item):
    name = scrapy.Field()           #小说名
    content = scrapy.Field()        #章节内容
    chapter_name = scrapy.Field()   #章节名
    chapter_numbers = scrapy.Field()#章节数
    chapter_url = scrapy.Field()    #章节地址

