# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class SpidersPipeline:
    def process_item(self, item, spider):
        title =item['title']
        link = item['link']
        ca = item['ca']
        date = item['date']
        output =f'|{title}|\t|{ca}|\t|{date}|\n\n'
        with open('.spiders.txt', 'a+', encoding='utf-8')as article:
            article.write(output)
        return item
