============bra.py====================================================================================
# -*- coding: utf-8 -*-
import scrapy
import re
import json
from JD.items import BraItem

#分析网页的主要思路
    #（1）我们主要是为了获取商品的销售数据（评论数据），首先找到商品的销售数据，跟网页呈现的相同
    #（2）找到对应的链接，分析链接里面包含的主要信息：有商品的ID——ProductId、评论数据的页码——page
    #（3）接下来主要考虑不同的商品对应的ID，看网站的URL会发现有ProductID的信息，就可以以此确定通过京东搜索页面，
    #     输入关键字，我们可以基于呈现的页面来分析，可以获取商品的ProductID

#爬虫的主要思路：
    #（1）通过搜索商品关键字，来得到关于商品的页面，点击“销量”进行排序，基于该页面的URL完成，发送请求，获取商品ProductID
    #（2）得到商品ProductID之后，构建评论数据对应的链接，进行请求，获得该商品的评论数据最大页码maxpage
    #（3）得到最大页码之后，可以重新基于商品ProductId和页数page，重新构建评论数据的URL，进行请求，获得每个商品，每页下面的销售数据
    #（4）获得响应进行解析，提取感兴趣的数据，并进行保存。


class BraSpider(scrapy.Spider):
    name = 'bra'
    # allowed_domains = ['search.jd.com/Search?keyword=bra']
    start_urls = ['https://search.jd.com/search?keyword=%E5%86%85%E8%A1%A3%E5%A5%B3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.def.0.V00--&wq=%E5%86%85%E8%A1%A3&cid3=1364']

    def parse(self, response):
        '''
        解析响应，获取产品ID,确定下一步请求
        :param response:
        :return:
        '''
        #提取产品ID,并进行去重
        results=list(set(response.css('#J_goodsList > ul > li.gl-item::attr(data-sku)').extract()))
        for productID in results:
            #下一步请求，主要是为了获取每个产品的评论页码数
            url='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv5427&productId='+productID+'&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
            yield scrapy.Request(url=url,callback=self.parse_page,meta={'productID':productID})
        
        



    def parse_page(self,response):
        '''
        提取产品的评论页码数，并确定下一步请求
        :param response:
        :return:
        '''
        productID=response.meta['productID']#获得产品ID
        page=int(re.search(r'maxPage.*?:(\d+),',response.text,re.S).group(1))#提取页码数

        results = response.text.replace('fetchJSON_comment98vv5427(', '').replace(');', '')
        results = json.loads(results)
        for comment in results['comments']:
            yield self.get_item(comment)

        for pn in range(1,page):#翻页
            #下一步的请求，主要是为了获取每一步的评论数
            url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv5427&productId='+productID+'&score=0&sortType=5&page='+str(pn)+'&pageSize=10&isShadowSku=0&fold=1'
            yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_item(self,response):
        '''
        提取评论数
        :param response:
        :return:
        '''
        #将响应体改造成类似json的字符串
        results=response.text.replace('fetchJSON_comment98vv5427(','').replace(');','')
        results = json.loads(results)
        for comment in results['comments']:
            yield self.get_item(comment)

    def get_item(self,comment):
        item = BraItem()
        item['content'] = comment['content']
        item['id'] = comment['id']
        item['productColor'] = comment['productColor']
        item['productSize'] = comment['productSize']
        item['referenceName'] = comment['referenceName']
        item['score'] = comment['score']
        return item
=============pipelines.py=============================================================

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JdPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db1):
        self.mongo_url = mongo_uri
        self.mongo_db = mongo_db1

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONOGO_URL'),
            mongo_db1=crawler.settings.get('MONOGO_DB'),
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].update_one({'id':item['id']},{'$set':dict(item)},True)
        return item

============middlewares.py=====================================================================
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class JdSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JdDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
        
===========items.py==================================================================
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class BraItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content=Field()
    id=Field()
    productColor=Field()
    productSize=Field()
    referenceName=Field()
    score=Field()
    
    
================settings.py=======================================================
# -*- coding: utf-8 -*-

# Scrapy settings for JD project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JD'

SPIDER_MODULES = ['JD.spiders']
NEWSPIDER_MODULE = 'JD.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JD (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'JD.middlewares.JdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'JD.middlewares.JdDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'JD.pipelines.MongoPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MONOGO_URL = 'localhost'
MONOGO_DB = 'JD'

DOWNLOAD_DELAY = 3
