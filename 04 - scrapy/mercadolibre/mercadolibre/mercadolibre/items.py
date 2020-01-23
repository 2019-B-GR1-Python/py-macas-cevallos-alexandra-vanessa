# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


def truncar_texto(texto):
    return texto[:15]


def shorten_mercado_libre_link(link):
    id_producto = link.split('/')[-1]  # ultimo elemento
    short_link = 'https://articulo.mercadolibre.com.ec/' + id_producto
   
    return short_link


class CelularItem(scrapy.Item):
    titulo = scrapy.Field(input_processor=MapCompose(truncar_texto))
    precio = scrapy.Field()
    link = scrapy.Field(input_processor=MapCompose(shorten_mercado_libre_link))


class MercadolibreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass