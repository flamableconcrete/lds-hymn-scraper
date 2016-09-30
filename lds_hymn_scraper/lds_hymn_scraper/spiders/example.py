# -*- coding: utf-8 -*-
import scrapy

from lds_hymn_scraper.items import LdsHymnScraperItem


class ExampleSpider(scrapy.Spider):
    name = "hymnspider"
    allowed_domains = ["lds.org"]

    hymn_library ='https://www.lds.org/music/library/hymns?lang=eng'
    hymn_1 = 'https://www.lds.org/music/library/hymns/the-morning-breaks?lang=eng'
    hymn_2 = 'https://www.lds.org/music/library/hymns/the-spirit-of-god?lang=eng'
    hymn_3 = 'https://www.lds.org/music/library/hymns/now-let-us-rejoice?lang=eng'
    hymn_4 = 'https://www.lds.org/music/library/hymns/truth-eternal?lang=eng'
    hymn_5 = 'https://www.lds.org/music/library/hymns/high-on-the-mountain-top?lang=eng'

    start_urls = [
        hymn_1
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #    f.write(response.body)
        hymn_link = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div/ul/li[1]/a'

        xpath_title = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/h1'
        xpath_number = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/dl/dd[2]/a'
        xpath_music = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/dl/dd[3]/a'
        xpath_text = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/dl/dd[4]/a'
        xpath_scriptures = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/dl/dd[5]'
        xpath_meter = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/dl/dd[6]/a'
        xpath_topic = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/dl/dd[9]'
        xpath_tune = '/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[3]/dl/dd[10]/a'

        item = LdsHymnScraperItem()
        item['title'] = response.xpath(xpath_title).extract()
        item['number'] = response.xpath(xpath_number).extract()
        item['music'] = response.xpath(xpath_music).extract()
        item['text'] = response.xpath(xpath_text).extract()
        item['scriptures'] = response.xpath(xpath_scriptures).extract()
        item['meter'] = response.xpath(xpath_meter).extract()
        item['topic'] = response.xpath(xpath_topic).extract()
        item['tune'] = response.xpath(xpath_tune).extract()

        yield item
