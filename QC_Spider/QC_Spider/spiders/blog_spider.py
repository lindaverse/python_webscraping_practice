from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dateutil.parser import parse
import urlparse
from QC_Spider.items import BlogItem


class QCSpider(CrawlSpider):

    name = 'blog_spider'
    allowed_domains = ['uk.queryclick.com', 'us.queryclick.com']
    start_urls = ['http://uk.queryclick.com/seo-news']
    rules = [Rule(LinkExtractor(allow=['/seo-news/\?page']), 'parse_index_page')]

    def parse_index_page(self, response):
        for news_listing in response.xpath("//ul[@class='news_listing']/li"):
            blog_item = BlogItem()
            blog_item['url'] = urlparse.urljoin(response.url, news_listing.xpath("./h3/a/@href").extract()[0])
            blog_item['title'] = news_listing.xpath("./h3/a/@title").extract()[0]
            post_date = news_listing.xpath("./p/span[@class='date']/text()").extract()
            blog_item['date'] = parse(post_date[0]) if post_date else None
            yield blog_item
