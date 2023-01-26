import scrapy


class DesignersSpider(scrapy.Spider):
    name = 'designers'
    allowed_domains = ['www.bradburnhome.com']
    start_urls = ['https://www.bradburnhome.com/pages/designers']

    def parse(self, response):
        designers = response.xpath("//ul[@class='slides']/li/a/@href").getall()
        for designer in designers:
            yield scrapy.Request(
                url="https://www.bradburnhome.com"+designer,
                callback=self.parseResult
            )

    def parseResult(self, response):
        title = response.xpath("//h1/a/@title").get()
        products = response.xpath("//div[@class='products']"
                                  "/div/a/div[@class='info']"
                                  "/span[@class='title']/text()").getall()
        for product in products:
            yield {
                "title": title,
                "product": product,
            }
        _next = response.xpath("//span[@class='next']/a/@href").get()
        if _next is not None:
            yield scrapy.Request(
                url="https://www.bradburnhome.com"+_next,
                callback=self.parseResult
            )
