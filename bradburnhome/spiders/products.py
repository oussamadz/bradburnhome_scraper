import scrapy
import re
import csv
from word2number import w2n
from ..items import BradburnhomeItem


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.bradburnhome.com']
    start_urls = [
        'https://www.bradburnhome.com/collections/table-lamps',
        'https://www.bradburnhome.com/collections/accessories-1',
        'https://www.bradburnhome.com/collections/floor-lamps',
        'https://www.bradburnhome.com/collections/chandeliers',
        'https://www.bradburnhome.com/collections/accent-furniture',
        'https://www.bradburnhome.com/collections/wall-mirror',
        'https://www.bradburnhome.com/collections/sconces',
                  ]

    def browseTable(self, table, title):
        for tr in table.xpath(".//tr"):
            try:
                if title == tr.xpath(".//td/text()").getall()[0]:
                    return tr.xpath(".//td/text()").getall()[1]
            except IndexError:
                continue
        return ""

    def findBoxes(self, table):
        boxes = {}
        for tr in table.xpath(".//tr"):
            try:
                title = tr.xpath(".//td/text()").getall()[0]
            except IndexError:
                continue
            if "carton" in title.lower():
                values = tr.xpath(".//td/text()").getall()[1]
                boxes[title] = [
                    re.match('(\d*\.?\d*)(?=\s*"w)', values),
                    re.match('(\d*\.?\d*)(?=\s*"d)', values),
                    re.match('(\d*\.?\d*)(?=\s*"h)', values),
                ]
        return boxes

    def getDesigner(self, title):
        designers = csv.reader(open('designers.csv', "r"), delimiter=",")
        for row in designers:
            if title in row[1]:
                return row[0]
        return ""

    def parse(self, response):
        products_list = response.xpath(
            "//div[@class='products']/*/a/@href").getall()
        for product in products_list:
            yield scrapy.Request(
                url="https://www.bradburnhome.com"+product,
                callback=self.parseProduct
            )
        nextPage = response.xpath("//span[@class='next']/a/@href").get()
        if nextPage is not None:
            yield scrapy.Request(
                url="https://www.bradburnhome.com"+nextPage,
                callback=self.parse)

    def parseProduct(self, response):
        product = BradburnhomeItem()
        for field in product.fields:
            product.setdefault(field, "")
        table = response.xpath("//div[@class='description']/table/tbody")
        additional_images = []
        gallery = response.xpath("//div[contains(@class, 'product_slider')]/ul/li/a/img/@src").getall()
        for img in gallery:
            additional_images.append("https:"+img.split("?")[0].replace("_100x", ""))
        product['additional_images'] = additional_images
        if response.xpath("//a[@class='product_collection']/@title") == "Floor Lamps":
            dimentions = self.browseTable(table, "Dimensions")
            product['attrib__arm_height'] = re.match('(\d*\.?\d*)(?=\s*"h)', dimentions)
        product['attrib__bulb_type'] = self.browseTable(table, 'Bulb Type & Wattage').split(",")[0]
        product['attrib__color'] = self.browseTable(table, "Color")
        product['attrib__designer'] = self.getDesigner(response.xpath("//h1[@class='product_name']/text()").get())
        product['attrib__finish'] = re.match("(\w+)(?=\s*finish)", response.xpath("//div[@class='description']/p/text()").get(default=""))
        product['attrib__material'] = self.browseTable(table, "Material")
        try:
            product['attrib__number_bulbs'] = w2n.word_to_num(self.browseTable(table, "Number of Lights"))
        except ValueError:
            product['attrib__number_bulbs'] = ""
        product['attrib__shade'] = self.browseTable(table, 'Shade Material')
        product['attrib__switch_type'] = self.browseTable(table, "Switch")
        try:
            product['attrib__wattage'] = self.browseTable(table, "Bulb Type & Wattage").split(",")[1]
        except IndexError:
            product['attrib__wattage'] = ""
        product['attrib__cord_length'] = self.browseTable(table, "Cord").split(" ")[0]
        product['cost_price'] = response.xpath("//span[@class='current_price ']/*/text()").get().replace("$", "")
        product['height'] = re.match('(\d*\.?\d*)(?=\s*"h)', self.browseTable(table, 'Dimensions'))
        product['length'] = re.match('(\d*\.?\d*)(?=\s*"h)', self.browseTable(table, 'Dimentions'))
        stock = self.browseTable(table, "Stock Level")
        if stock != "":
            if "unavailable" in stock.lower():
                product['made_to_order'] = False
            elif "In Stock" or "Low Stock" in stock:
                product['made_to_order'] = True
        product['manufacturer'] = response.xpath("//div[contains(@class, 'header-logo')]/a/@title").get()
        product['manufacturer_sku'] = self.browseTable(table, "Sku")
        product['min_price'] = response.xpath("//span[@class='current_price ']/*/text()").get().replace("$", "")
        product['preferred_shipment_type'] = self.browseTable(table, "Shipping Method")
        product['product__collection'] = response.xpath("//a[@class='product_collection']/@title").get()
        product['product__country_of_origin'] = self.browseTable(table, "Made In")
        product['product__description'] = response.xpath("//div[@class='description']/p/text()").get()
        product['lifestyle_images'] = response.xpath("//a[@class='fancybox']/img/@src").get().split("?")[0].replace("//", "")
        product['product__sites'] = self.allowed_domains[0]
        product['product__title'] = response.xpath("//h1[@class='product_name']/text()").get()
        if response.xpath("//a[contains(.,'View Spec Sheet')]") is not []:
            product['prop_65'] = True
        boxes = self.findBoxes(table)
        product['shipment_boxes'] = boxes
        product['width'] = re.match('(\d*\.?\d*)(?=\s*"h)', self.browseTable(table, "Dimentions"))
        yield product
