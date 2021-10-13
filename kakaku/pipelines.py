# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request, request


class KakakuPipeline:
    def process_item(self, item, spider):
        price = item.get('price')
        if not price > 100000:
            raise DropItem('less than 100000')

        return item

class customImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        image_guid = request.meta['img_name'] + '.' + image_guid.split('.')[1]
        return 'full/%s' % (image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['img']:
            request = Request(image_url)
            request.meta['img_name'] = item['name']
            yield request

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item