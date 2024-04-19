# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose


def process_name(value):
    value = value[0].strip()
    return value


# def process_price(value):
#     value = value[0].strip().replace('\xa0', ' ').split()
#     if value[0].isdigit():
#         value[0] = int(value[0])
#     if value[1].isdigit():
#         value[1] = int(value[1])
#     return value
def process_price(value):
    if not value:
        return None
    price_str = value[0].strip().replace('\xa0', '').strip()
    currency_index = price_str.find('₽')
    if currency_index == -1:
        return None
    price_num = price_str[:currency_index].strip()
    currency = price_str[currency_index:].strip()
    if price_num.isdigit():
        return int(price_num), currency
    return None


def process_photos(value: str):
    if value.startswith('//'):
        value = 'https:' + value.strip()[0]
    else:
        value = value.split()[1]
    return value


class Book24ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(process_price))
    url = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(process_photos))
    _id = scrapy.Field()
