# -*- coding: utf-8 -*-
import scrapy
from novel.items import NovelItem,ChapterItem

class DingdianNovelSpider(scrapy.Spider):
    name = 'dingdian_novel'
    allowed_domains = ['www.x23us.com']
    start_urls = ['https://www.x23us.com/class/1_1.html']

    def parse(self, response):
        books = response.xpath('//dd/table/tr[@bgcolor="#FFFFFF"]')
        for book in books:
            item = NovelItem()
            item['novel_url'] = book.xpath('./td[1]/a[2]/@href').extract()[0]
            item['name'] = book.xpath('./td[1]/a[2]/text()').extract()[0]
            item['author'] = book.xpath('./td[3]/text()').extract()[0]
            item['numbers'] = book.xpath('./td[4]/text()').extract()[0]
            item['last_time'] = book.xpath('./td[5]/text()').extract()[0]
            item['status'] = book.xpath('./td[6]/text()').extract()[0]
            yield item
            yield scrapy.Request(item['novel_url'],callback=self.get_chapter,meta={'novel_url':item['novel_url'],
                                                                                   'name':item['name']})
        next_page = response.xpath('//dd[@class="pages"]/div/a[12]/@href').extract()
        if next_page:
            yield scrapy.Request(next_page[0])
    def get_chapter(self,response):
        chapters = response.xpath('//tr/td/a')
        numbers  = len(chapters)
        for chapter in chapters:
            chapter_name = chapter.xpath('./text()').extract()[0]
            chapter_url = response.meta['novel_url'] + chapters.xpath('./@href').extract()[0]
            yield scrapy.Request(chapter_url,callback=self.get_content,meta={'chapter_numbers':numbers,
                                                                             'chapter_name':chapter_name,
                                                                             'chapter_url':chapter_url,
                                                                             'name':response.meta['name']})
    def get_content(self,response):
        content = response.xpath('//dd[@id="contents"]/text()').extract()
        item = ChapterItem()
        item['content'] = content
        item['name'] = response.meta['name']
        item['chapter_name'] = response.meta['chapter_name']
        item['chapter_numbers'] = response.meta['chapter_numbers']
        item['chapter_url'] = response.meta['chapter_url']
        return item







