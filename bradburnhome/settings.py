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

#FEED_EXPORT_FIELDS = ["additional_images", "attrib__arm_height", "attrib__assembly_required", "attrib__back_material", "attrib__blade_finish", "attrib__bulb_included", "attrib__bulb_type", "attrib__color", "attrib__cord_length", "attrib__design_id", "attrib__designer", "attrib__distressed_finish", "attrib__fill", "attrib__finish", "attrib__frame_color", "attrib__hardwire", "attrib__kit", "attrib__leg_color", "attrib__leg_finish", "attrib__material", "attrib__number_bulbs", "attrib__orientation", "attrib__outdoor_safe", "attrib__pile_height", "attrib__seat_depth", "attrib__seat_height", "attrib__seat_width", "attrib__shade", "attrib__size", "attrib__switch_type", "attrib__ul_certified", "attrib__warranty_years", "attrib__wattage", "attrib__weave", "attrib__weight_capacity", "attributes", "cost_price", "height", "lead_time", "length", "lifestyle_images", "made_to_order", "manufacturer", "manufacturer_sku", "min_price", "preferred_shipment_type", "product__brand", "product__bullets", "product__collection", "product__configuration", "product__country_of_origin", "product__description", "product__multipack_quantity", "product__parent_id", "product__product_class", "product__sites", "product__title", "product__variants", "product__white_labels", "prop_65", "shipment_boxes", "shipment_boxes__weight", "shipment_boxes__height", "shipment_boxes__length", "shipment_boxes__width", "silo_images", "upc", "weight", "width"]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'adsbot-google'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
