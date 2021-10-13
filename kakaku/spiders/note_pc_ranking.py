import logging
import scrapy
from kakaku.items import KakakuItem
from scrapy.loader import ItemLoader


class NotePcRankingSpider(scrapy.Spider):
    name = 'note_pc_ranking'
    allowed_domains = ['kakaku.com']
    start_urls = ['https://kakaku.com/pc/note-pc/ranking_0020/']


    def parse(self, response):

        sel = response.xpath('//div[contains(@class,"rkgBox noGraph")]')
        for s in sel:
            logging.info(s.get())
            loader = ItemLoader(item=KakakuItem(), selector=s)

            loader.add_xpath('rank', './/span[@class="rkgBoxNum"]//span[@class="num"]/text()')
            loader.add_xpath('price', './/span[@class="price"]/a/text()')
            loader.add_xpath('name', './/span[@class="rkgBoxNameItem"]/text()')

            yield loader.load_item()

        next_page = response.xpath('//li[@class="next"]/a')

        if next_page:
            yield response.follow(url=next_page[0], callback=self.parse)
