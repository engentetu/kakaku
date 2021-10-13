# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Join


def strip_yen(item):
    if item:
        return item.replace('¥', '')
    return item

def strip_newline(item):
    if item:
        return item.replace('/', '')
    return item


def strip_comma(item):
    if item:
        return item.replace(',', '')
    return item


def convert_int(item):
    if item:
        return int(item)
    return 0


class KakakuItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field(
        input_processor=MapCompose(convert_int),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(strip_yen, strip_comma,  convert_int),
        output_processor = TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(str.lstrip, strip_newline),
        output_processor = TakeFirst()
    )

    img = scrapy.Field()
