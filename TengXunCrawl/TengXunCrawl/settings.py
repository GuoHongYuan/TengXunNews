# -*- coding: utf-8 -*-
import random
import sys
sys.path.append('E:\DataAnalysis\\tools\python3\project\DistributedCrawler\Setting')
from UserAgent import *
# Scrapy settings for TengXunCrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'TengXunCrawl'

SPIDER_MODULES = ['TengXunCrawl.spiders']
NEWSPIDER_MODULE = 'TengXunCrawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'TengXunCrawl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
#    'TengXunCrawl.middlewares.TengxuncrawlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'TengXunCrawl.middlewares.TengxuncrawlDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'TengXunCrawl.pipelines.TengxuncrawlPipeline': 300,
#}

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


ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline' : 400,
}

DOWNLOADER_MIDDLEWARES = {
    #seleium+chrom无头浏览器
    'TengXunCrawl.middlewares.Url_SM': 543,

    #scrapy ip 代理
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    #'DC.middlewares.IPPOOlS' : 125

}
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

SCHEDULER_PERSIST = True

USER_AGENT = random.choice(MY_USER_AGENT)

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

REDIS_PARAMS = {'db':0}

IPPOOL = [
{"ipaddr": "119.101.116.6:9999"},
{"ipaddr": "119.101.117.76:9999"},
{"ipaddr": "119.101.116.127:9999"},
{"ipaddr": "110.52.235.54:9999"},
{"ipaddr": "119.101.119.22:9999"},
{"ipaddr": "115.151.2.73:808"},
{"ipaddr": "119.101.113.121:9999"},
{"ipaddr": "121.61.0.197:9999"},
{"ipaddr": "119.101.118.94:9999"},
{"ipaddr": "119.101.115.141:9999"},
{"ipaddr": "119.101.117.202:9999"},
{"ipaddr": "119.101.113.58:9999"},
{"ipaddr": "119.101.112.35:9999"},
{"ipaddr": "119.101.116.146:9999"},
{"ipaddr": "119.101.113.245:9999"},
{"ipaddr": "121.61.1.239:9999"},
{"ipaddr": "119.101.114.182:9999"},
{"ipaddr": "119.101.113.238:9999"},
{"ipaddr": "119.101.114.97:9999"},
{"ipaddr": "119.101.115.2:9999"},
{"ipaddr": "119.101.118.142:9999"},
{"ipaddr": "119.101.113.57:9999"},
{"ipaddr": "110.52.235.96:9999"},
{"ipaddr": "119.101.116.177:9999"},
{"ipaddr": "119.101.116.227:9999"},
{"ipaddr": "119.101.118.5:9999"},
{"ipaddr": "119.101.116.131:9999"},
{"ipaddr": "119.101.117.56:9999"},
{"ipaddr": "119.101.117.15:9999"},
{"ipaddr": "119.101.112.180:9999"},
{"ipaddr": "119.101.114.4:9999"},
{"ipaddr": "119.101.116.205:9999"},
{"ipaddr": "119.101.113.70:9999"},
{"ipaddr": "119.101.112.4:9999"},
{"ipaddr": "221.206.100.133:34073"},
{"ipaddr": "119.101.115.28:9999"},
{"ipaddr": "119.101.112.64:9999"},
{"ipaddr": "119.101.113.202:9999"},
{"ipaddr": "119.101.117.203:9999"},
{"ipaddr": "140.207.25.114:41471"},
{"ipaddr": "119.101.115.70:9999"},
{"ipaddr": "110.52.235.35:9999"},
{"ipaddr": "119.101.115.237:9999"},
{"ipaddr": "119.101.113.56:9999"},
{"ipaddr": "58.50.3.174:9999"},
{"ipaddr": "119.101.115.196:9999"},
{"ipaddr": "119.101.118.120:9999"},
{"ipaddr": "119.101.115.114:9999"},
{"ipaddr": "119.101.112.12:9999"},
{"ipaddr": "119.101.118.147:9999"},
{"ipaddr": "119.101.118.151:9999"},
{"ipaddr": "125.109.195.174:33883"},
{"ipaddr": "180.118.77.29:9999"},
{"ipaddr": "119.101.117.93:9999"},
{"ipaddr": "119.101.113.97:9999"},
{"ipaddr": "180.118.77.11:9999"},
{"ipaddr": "119.101.112.43:9999"},
{"ipaddr": "110.52.235.165:9999"},
{"ipaddr": "119.101.113.11:9999"},
{"ipaddr": "119.101.112.152:9999"},
{"ipaddr": "115.46.74.18:8123"},
{"ipaddr": "119.101.116.140:9999"},
{"ipaddr": "119.101.112.109:9999"},
{"ipaddr": "119.101.115.87:9999"},
]

# 配置Scrapy执行的最大并发请求（默认值：16）
CONCURRENT_REQUESTS = 2





