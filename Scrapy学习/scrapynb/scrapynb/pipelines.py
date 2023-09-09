# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapynbPipeline:
    def process_item(self, item, spider):
        return item


class CsvPipeline:
    def __init__(self):
        self.file = open('data.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['title', 'brief_comment'])  # 写入CSV文件的标题行

    def process_item(self, item, spider):
        self.writer.writerow([item['title'], item['brief_comment']])  # 写入CSV文件的数据行
        return item

    def close_spider(self, spider):
        self.file.close()
