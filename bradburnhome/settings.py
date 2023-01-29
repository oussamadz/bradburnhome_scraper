# Scrapy settings for bradburnhome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bradburnhome'

SPIDER_MODULES = ['bradburnhome.spiders']
NEWSPIDER_MODULE = 'bradburnhome.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'adsbot-google'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_EXPORT_FIELDS = ["additional_images","attrib__arm_height","attrib__bulb_type","attrib__color","attrib__designer","attrib__finish","attrib__material","attrib__number_bulbs","attrib__shade","attrib__switch_type","attrib__wattage","attrib__cord_length","cost_price","height","length","made_to_order","manufacturer","manufacturer_sku","min_price","preferred_shipment_type","product__collection","product__country_of_origin","product__description","lifestyle_images","product__sites","product__title","prop_65","shipment_boxes","width","Dimensions","Dimension","Shade Dimension","Carton Shade","Carton Body","Base Dims","Lamp Body Material","Number Of Lights","Shade Shape","Shade Type","Shade Color","Shade","Bulb Type","Shade Dim","Shade Other","Production Notes","Hardware","Bobesche","Candle Covers","Crystals","Other Notes","Mirror","Frame","Features","Carton2","Drawers","Carton1","Hanger","KD","Shelves","Lid","Top","Number Or Lights ","Shade Color ","Body Type And Wattage","Shade Type ","Body Material","Other","Interior Carton","Base","Made","Lights","Gross","Full","Height To Socket","Max Wattage","Note","Socket","Description","Trim","Finish","Carton","Sockets","Harp","Metal Finish","Harp Size","Small Ball","Small Stand","Large Ball","Large Stand","Net Small","Net Medium","Net Large","Net","Lamp Base Material","Lamp Body Shape","Feature","Small Net","Large Net","Medium Net","Sconce Body Material","Tall Net","Short Net","Material ","N Shade Material","Notes","Body Dims","Base Dimension","Lamp Body","Handle"]


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'bradburnhome.middlewares.BradburnhomeSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'bradburnhome.middlewares.BradburnhomeDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'bradburnhome.pipelines.BradburnhomePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
