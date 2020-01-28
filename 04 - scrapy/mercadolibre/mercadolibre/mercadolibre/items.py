# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
def transformar_url(texto):
    punto = 'fibeca.com'
    cadena = '../..'
    return texto.replace(cadena, punto)


class ProductoMercado(scrapy.Item):

    titulo = scrapy.Field()
    location = scrapy.Field(
     input_processor = MapCompose(
         transformar_url
         ),
         output_processor = TakeFirst()
         )
    #detalle = scrapy.Field()

class MercadolibreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
  
  
    pass