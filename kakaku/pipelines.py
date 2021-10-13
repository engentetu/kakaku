# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class KakakuPipeline:
    def process_item(self, item, spider):
        price = item.get('price')
        if not price > 100000:
            raise DropItem('less than 100000')

        return item
