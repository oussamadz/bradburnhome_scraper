import scrapy
import re
import csv
from word2number import w2n
from ..items import BradburnhomeItem
import xml.etree.ElementTree as ET


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.bradburnhome.com']
    start_urls = [
        "https://bradburnhome.com/sitemap.xml"
    ]

    usedRows = [
        "Bulb Type & Wattage", "Cord", "Stock Level",
        "Sku", "Shipping Method", "Made In",
        "Color", "Material", "Number of Lights",
        "Shade Material", "Switch"
    ]

    def convertTable(self, table, title):
        for tr in table.xpath(".//tr"):
            try:
                if title == tr.xpath(".//td/text()").getall()[0]:
                    return tr.xpath(".//td/text()").getall()[1]
            except IndexError:
                continue
        return ""

    def parseTable(self, table):
        tableDict = {}
        for tr in table.xpath(".//tr"):
            try:
                key = tr.xpath(".//td/text()").getall()[0]
                if key not in self.usedRows:
                    tableDict[key] = tr.xpath(".//td/text()").getall()[1]
            except IndexError:
                pass
        return tableDict

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
                    re.findall('(\d*\.?\d*)(?=\s*"w)', values),
                    re.findall('(\d*\.?\d*)(?=\s*"d)', values),
                    re.findall('(\d*\.?\d*)(?=\s*"h)', values),
                ]
        return boxes

    def getDesigner(self, title):
        designers = csv.reader(open('designers.csv', "r"), delimiter=",")
        for row in designers:
            if title in row[1]:
                return row[0]
        return ""

    def parse(self, response):
        root = ET.fromstring(response.text)
        productsLinks = []
        for r in root:
            if "products" in r[0].text:
                productsLinks.append(r[0].text)
        for product in productsLinks:
            yield scrapy.Request(
                url=product,
                callback=self.listProducts
            )

    def listProducts(self, response):
        root = ET.fromstring(response.text)
        products = []
        for r in root:
            products.append(r[0].text)
        for pr in products:
            yield scrapy.Request(
                url=pr,
                callback=self.parseProduct
            )

    def parseProduct(self, response):
        table = response.xpath("//div[@class='description']/table/tbody")
        product = self.parseTable(table)
        # product = BradburnhomeItem()
        # for field in product.fields:
        #     product.setdefault(field, "")
        additional_images = []
        gallery = response.xpath(
            "//div[contains(@class, 'product_slider')]/ul/li/a/img/@src").getall()
        for img in gallery:
            additional_images.append(
                "https:"+img.split("?")[0].replace("_100x", ""))
        product['additional_images'] = additional_images
        if response.xpath("//a[@class='product_collection']/@title") == "Floor Lamps":
            dimentions = self.convertTable(table, "Dimensions")
            product['attrib__arm_height'] = re.findall(
                '(\d*\.?\d*)(?=\s*"h)', dimentions)
        product['attrib__bulb_type'] = self.convertTable(
            table, 'Bulb Type & Wattage').split(",")[0]
        product['attrib__color'] = self.convertTable(table, "Color")
        product['attrib__designer'] = self.getDesigner(
            response.xpath("//h1[@class='product_name']/text()").get())
        product['attrib__finish'] = re.findall(
            "(\w+)(?=\s*finish)", response.xpath("//div[@class='description']/p/text()").get(default=""))
        product['attrib__material'] = self.convertTable(table, "Material")
        try:
            product['attrib__number_bulbs'] = w2n.word_to_num(
                self.convertTable(table, "Number of Lights"))
        except ValueError:
            product['attrib__number_bulbs'] = ""
        product['attrib__shade'] = self.convertTable(table, 'Shade Material')
        product['attrib__switch_type'] = self.convertTable(table, "Switch")
        try:
            product['attrib__wattage'] = self.convertTable(
                table, "Bulb Type & Wattage").split(",")[1]
        except IndexError:
            product['attrib__wattage'] = ""
        product['attrib__cord_length'] = self.convertTable(
            table, "Cord").split(" ")[0]
        product['cost_price'] = response.xpath(
            "//span[@class='current_price ']/*/text()").get().replace("$", "")
        product['height'] = re.findall(
            '(\d*\.?\d*)(?=\s*"h)', self.convertTable(table, 'Dimensions'))
        product['length'] = re.findall(
            '(\d*\.?\d*)(?=\s*"h)', self.convertTable(table, 'Dimentions'))
        stock = self.convertTable(table, "Stock Level")
        if stock != "":
            if "unavailable" in stock.lower():
                product['made_to_order'] = False
            elif "In Stock" or "Low Stock" in stock:
                product['made_to_order'] = True
        product['manufacturer'] = response.xpath(
            "//div[contains(@class, 'header-logo')]/a/@title").get()
        product['manufacturer_sku'] = self.convertTable(table, "Sku")
        product['min_price'] = response.xpath(
            "//span[@class='current_price ']/*/text()").get().replace("$", "")
        product['preferred_shipment_type'] = self.convertTable(
            table, "Shipping Method")
        product['product__collection'] = response.xpath(
            "//a[@class='product_collection']/@title").get()
        product['product__country_of_origin'] = self.convertTable(
            table, "Made In")
        product['product__description'] = response.xpath(
            "//div[@class='description']/p/text()").get()
        product['lifestyle_images'] = response.xpath(
            "//a[@class='fancybox']/img/@src").get().split("?")[0].replace("//", "")
        product['product__sites'] = self.allowed_domains[0]
        product['product__title'] = response.xpath(
            "//h1[@class='product_name']/text()").get()
        if response.xpath("//a[contains(.,'View Spec Sheet')]") is not []:
            product['prop_65'] = True
        boxes = self.findBoxes(table)
        product['shipment_boxes'] = boxes
        product['width'] = re.findall(
            '(\d*\.?\d*)(?=\s*"h)', self.convertTable(table, "Dimentions"))
        yield product
