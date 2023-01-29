# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from alexber.scrapyitem import GeneralItem

class RawItem(GeneralItem):
    pass


class BradburnhomeItem(scrapy.Item):
    additional_images = scrapy.Field()
    attrib__arm_height = scrapy.Field()
    attrib__assembly_required = scrapy.Field()
    attrib__back_material = scrapy.Field()
    attrib__blade_finish = scrapy.Field()
    attrib__bulb_included = scrapy.Field()
    attrib__bulb_type = scrapy.Field()
    attrib__color = scrapy.Field()
    attrib__cord_length = scrapy.Field()
    attrib__design_id = scrapy.Field()
    attrib__designer = scrapy.Field()
    attrib__distressed_finish = scrapy.Field()
    attrib__fill = scrapy.Field()
    attrib__finish = scrapy.Field()
    attrib__frame_color = scrapy.Field()
    attrib__hardwire = scrapy.Field()
    attrib__kit = scrapy.Field()
    attrib__leg_color = scrapy.Field()
    attrib__leg_finish = scrapy.Field()
    attrib__material = scrapy.Field()
    attrib__number_bulbs = scrapy.Field()
    attrib__orientation = scrapy.Field()
    attrib__outdoor_safe = scrapy.Field()
    attrib__pile_height = scrapy.Field()
    attrib__seat_depth = scrapy.Field()
    attrib__seat_height = scrapy.Field()
    attrib__seat_width = scrapy.Field()
    attrib__shade = scrapy.Field()
    attrib__size = scrapy.Field()
    attrib__switch_type = scrapy.Field()
    attrib__ul_certified = scrapy.Field()
    attrib__warranty_years = scrapy.Field()
    attrib__wattage = scrapy.Field()
    attrib__weave = scrapy.Field()
    attrib__weight_capacity = scrapy.Field()
    attributes = scrapy.Field()
    cost_price = scrapy.Field()
    height = scrapy.Field()
    lead_time = scrapy.Field()
    length = scrapy.Field()
    lifestyle_images = scrapy.Field()
    made_to_order = scrapy.Field()
    manufacturer = scrapy.Field()
    manufacturer_sku = scrapy.Field()
    min_price = scrapy.Field()
    preferred_shipment_type = scrapy.Field()
    product__brand = scrapy.Field()
    product__bullets = scrapy.Field()
    product__collection = scrapy.Field()
    product__configuration = scrapy.Field()
    product__country_of_origin = scrapy.Field()
    product__description = scrapy.Field()
    product__multipack_quantity = scrapy.Field()
    product__parent_id = scrapy.Field()
    product__product_class = scrapy.Field()
    product__sites = scrapy.Field()
    product__title = scrapy.Field()
    product__variants = scrapy.Field()
    product__white_labels = scrapy.Field()
    prop_65 = scrapy.Field()
    shipment_boxes = scrapy.Field()
    shipment_boxes__weight = scrapy.Field()
    shipment_boxes__height = scrapy.Field()
    shipment_boxes__length = scrapy.Field()
    shipment_boxes__width = scrapy.Field()
    silo_images = scrapy.Field()
    upc = scrapy.Field()
    weight = scrapy.Field()
    width = scrapy.Field()




































































