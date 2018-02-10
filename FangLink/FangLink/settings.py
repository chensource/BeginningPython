# -*- coding: utf-8 -*-

# Scrapy settings for FangLink project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'FangLink'

SPIDER_MODULES = ['FangLink.spiders']
NEWSPIDER_MODULE = 'FangLink.spiders'

MONGO_URI = 'localhost'
MONGO_DB = 'FangLink'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'FangLink (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 如果启用，Scrapy 将会尊重 robots.txt 策略
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Scrapy downloader 并发请求(concurrent requests)的最大值。
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度，减轻服务器压力。同时也支持小数:
# 单位是秒
DOWNLOAD_DELAY = 3.5

# The download delay setting will honor only one of:
# 对单个网站进行并发请求的最大值。
CONCURRENT_REQUESTS_PER_DOMAIN = 32
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# Scrapy HTTP Request 使用的默认 header。
DEFAULT_REQUEST_HEADERS = {
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Host': 'newhouse.wuhan.fang.com',
    # 'Connection': 'keep-alive'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'FangLink.middlewares.FanglinkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# 保存项目中启用的下载中间件及其顺序的字典。
DOWNLOADER_MIDDLEWARES = {
    'FangLink.useragent.UserAgent': 1,
    # 'FangLink.proxymiddlewares.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware':
    350,
    'FangLink.middlewares.FanglinkSpiderMiddleware': 543,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     # 'FangLink.pipelines.MongoPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = False
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# CRAWLERA_PRESERVE_DELAY = True

# CRAWLERA_ENABLED = True
# # key
# CRAWLERA_USER = '96722585bb9c41f09dc0d70287574db9'

# CRAWLERA_PASS = ''

# HTTPERROR_ALLOWED_CODES = [407]

DOWNLOAD_TIMEOUT = 10
