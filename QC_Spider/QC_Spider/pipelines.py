# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class QcSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy import log
import sqlite3

class DataSQLitePipeline(object):
    def __init__(self):
        self.connection = sqlite3.connect('./QC_scraped_data.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS QC_scraped_data ' \
                    '(id INTEGER PRIMARY KEY, url TEXT, title TEXT, date TEXT)')

    def process_item(self, item, spider):
        self.cursor.execute("SELECT * FROM QC_scraped_data where url=?", (item['url'], ))
        result = self.cursor.fetchone()
        if result:
            log.msg("Item already in database: %s" % item, level=log.DEBUG)
        else:
            self.cursor.execute(
                "INSERT INTO QC_scraped_data (url, title, date) VALUES (?, ?, ?)",
                    (item['url'], item['title'], item['date']))
            self.connection.commit()
            log.msg("Item stored : " % item, level=log.DEBUG)
        return item

    def handle_error(self, e):
        log.err(e)