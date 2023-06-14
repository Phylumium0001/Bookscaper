# Scrapy settings for bookscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import json
BOT_NAME = 'bookscraper'

SPIDER_MODULES = ['bookscraper.spiders']
NEWSPIDER_MODULE = 'bookscraper.spiders'

FEEDS = {
    'booksdata.json': {'format': 'json'},
}

SCRAPEOPS_API_KEY = '2f654702-7f6b-4eab-81c1-3b14e1962246' # signup at https://scrapeops.io
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 5

ROTATING_PROXY_LIST = [
'83.142.126.147:80',
 '66.135.227.178:4145',
 '89.43.5.134:3629',
 '165.231.101.229:80',
 '89.237.34.193:51549',
 '45.7.177.186:39867',
 '45.7.177.202:39867',
 '47.242.116.48:1080',
 '165.22.52.130:8000',
 '84.51.0.197:4145',
 '181.211.245.190:5678',
 '197.234.13.56:4145',
 '138.117.179.54:5678',
 '92.222.237.105:8888',
 '72.52.131.65:80',
 '75.119.203.42:15745',
 '46.148.163.119:5678',
 '43.153.103.219:443',
 '183.89.114.69:8080',
 '117.102.224.38:1080',
 '180.183.173.20:8291',
 '115.127.121.202:5678',
 '43.134.204.249:33126',
 '41.66.252.134:53281',
 '176.58.121.182:3128',
 '221.132.18.38:80',
 '185.204.197.25:8080',
 '192.12.112.65:4145',
 '5.1.104.67:33041',
 '210.4.194.196:80',
 '185.203.220.16:1080',
 '177.128.209.90:4673',
 '41.184.212.3:4153',
 '103.110.184.1:6037',
 '51.38.39.204:63028',
 '143.255.176.5:4153',
 '38.127.179.125:46656',
 '185.184.197.98:5678',
 '178.253.201.11:1080',
 '154.66.108.19:10081',
 '176.36.138.238:1080',
 '183.89.114.143:4145',
 '109.73.38.156:1080',
 '43.242.242.140:5678',
 '110.77.236.235:4153',
 '91.147.235.99:4145',
 '213.96.98.213:15724',
 '89.144.27.220:13800',
 '107.161.50.42:6401',
 '172.67.185.199:80',
 '82.200.117.130:1080',
 '178.128.232.123:8080',
 '103.85.60.129:3629',
 '103.47.95.81:1080',
 '103.86.1.25:4145',
 '157.185.161.100:26589',
 '103.127.56.236:5678',
 '185.81.106.52:3629',
 '188.119.103.157:45698',
 '49.0.2.243:5430',
 '181.40.90.26:999',
 '125.141.139.60:5566',
 '45.196.151.73:5432',
 '104.156.224.85:11184',
 '176.214.78.230:5678',
 '188.255.245.33:1080',
 '65.21.150.198:3068',
 '110.77.184.80:4145',
 '172.67.3.98:80',
 '172.67.200.220:80',
 '170.80.91.13:4145',
 '95.179.155.218:8080',
 '203.98.76.64:5678',
 '88.213.214.254:4145',
 '61.74.18.133:1080',
 '217.66.206.155:5678',
 '5.8.240.92:4153',
 '31.220.54.116:80',
 '202.159.35.33:443',
 '61.7.174.64:4153',
 '177.86.201.108:4145',
 '8.219.152.222:443',
 '36.95.56.66:5678',
 '104.16.224.33:80',
 '27.72.73.143:4153',
 '104.17.9.114:80',
 '177.38.5.51:4153',
 '109.125.128.71:5678',
 '85.92.165.225:4145',
 '177.104.123.30:5678',
 '202.124.46.65:4145',
 '5.9.139.240:30000',
 '103.79.96.165:4153',
 '102.66.237.39:5678',
 '89.132.207.82:4145',
 '103.119.55.155:8080',
 '185.171.54.34:4153',
 '132.148.153.131:14731',
 '184.178.172.13:153',
 '195.210.172.43:58350']

            #   OR


#   OR ROTATING_PROXY_LIST = filepath
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookscraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bookscraper.middlewares.BookscraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'bookscraper.middlewares.BookscraperDownloaderMiddleware': 543,
    'bookscraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 400,

    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware':620
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'bookscraper.pipelines.BookscraperPipeline': 300,
#    'bookscraper.pipelines.SaveToMySQLPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
