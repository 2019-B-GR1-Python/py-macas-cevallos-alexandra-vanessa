import scrapy
from mercadolibre.items import ProductoMercado
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst



def exportar_csv(titulo, precio, link):
    with open('t.csv','a') as lista:
        lista.write(f'{titulo},{precio},{link}')
        lista.close()


class Detallesvehiculo(scrapy.Spider):
    name = 'vehiculos'
    urls = [
        'https://listado.mercadolibre.com.ec/vehiculos'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        resultados = response.css('div.item__info ')
        for producto in resultados:
           # detalle = producto.css('div.item__info')
            producto_loader = ItemLoader(
                item= ProductoMercado(),
                selector=producto
            )
            producto_loader.add_css(
                'titulo',
                'h2 > span::text'

            )
            producto_loader.add_css(
                'location',
                '.item__location::text'

            )
            yield producto_loader.load_item()