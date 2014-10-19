# -*- coding: utf-8 -*-

# Scrapy settings for QC_Spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'QC_Spider'

SPIDER_MODULES = ['QC_Spider.spiders']
NEWSPIDER_MODULE = 'QC_Spider.spiders'

ITEM_PIPELINES = {
    'QC_Spider.pipelines.DataSQLitePipeline': 1
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'QC_Spider (+http://www.yourdomain.com)'
