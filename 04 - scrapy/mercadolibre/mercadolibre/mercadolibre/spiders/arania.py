import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
def exportar_csv(titulo,precio,detalle,lugar):
   import csv
   with open('vehiculo.csv','a', newline='') as csvfile:
       spamwriter = csv.writer(csvfile, delimiter = ',')
       data = list(zip(titulo,precio,detalle,lugar))
       for row in data:
           row = list(row)
           spamwriter.writerow(row)

class AraniaCrawlMercado(CrawlSpider):
    name = 'autos' # heredado (override)
    allowed_domains = [
        'mercadolibre.com.ec'
    ]
    start_urls = [
        'https://autos.mercadolibre.com.ec/autos-camionetas/vehiculo'
    ]
    # al ver un ñink utiliza el parse page
    regla_uno = ( #busque en toda la pagina
        Rule(LinkExtractor(), callback= 'parse_page')
        ,
    )
    # busque en un link especifico con partes d ela url, segmentos de busqeuda
    url_segmento_permitido = ( # busque en un sitio especifico
        'autos-camionetas/vehiculo',
        'autos-camionetas/vehiculo_Desde_49',
        'autos-camionetas/vehiculo_Desde_97',
        'autos-camionetas/vehiculo_Desde_145',
        'autos-camionetas/vehiculo_Desde_193',
        'autos-camionetas/vehiculo_Desde_241',
        'autos-camionetas/vehiculo_Desde_289',
        'autos-camionetas/vehiculo_Desde_337',
        'autos-camionetas/vehiculo_Desde_385',
        'autos-camionetas/vehiculo_Desde_433',
        'autos-camionetas/vehiculo_Desde_481',
        'autos-camionetas/vehiculo_Desde_529',
        'autos-camionetas/vehiculo_Desde_577',
        'autos-camionetas/vehiculo_Desde_625',
        'autos-camionetas/vehiculo_Desde_673',
        'autos-camionetas/vehiculo_Desde_721',
        'autos-camionetas/vehiculo_Desde_769',
        'autos-camionetas/vehiculo_Desde_817',
        'autos-camionetas/vehiculo_Desde_865',
        'autos-camionetas/vehiculo_Desde_913',
        'autos-camionetas/vehiculo_Desde_961',
        'autos-camionetas/vehiculo_Desde_1009',
        'autos-camionetas/vehiculo_Desde_1057',
        'autos-camionetas/vehiculo_Desde_1105',
        'autos-camionetas/vehiculo_Desde_1153',
        'autos-camionetas/vehiculo_Desde_1201',
        'autos-camionetas/vehiculo_Desde_1249',
        'autos-camionetas/vehiculo_Desde_1297',
        'autos-camionetas/vehiculo_Desde_1345',
        'autos-camionetas/vehiculo_Desde_1393',
        'autos-camionetas/vehiculo_Desde_1441',
        'autos-camionetas/vehiculo_Desde_1489',
        'autos-camionetas/vehiculo_Desde_1537',
        'autos-camionetas/vehiculo_Desde_1585',
        'autos-camionetas/vehiculo_Desde_1633',
        'autos-camionetas/vehiculo_Desde_1681',
        'autos-camionetas/vehiculo_Desde_1729',
        'autos-camionetas/vehiculo_Desde_1777',
        'autos-camionetas/vehiculo_Desde_1825',
        'autos-camionetas/vehiculo_Desde_1873',
        'autos-camionetas/vehiculo_Desde_1921',
        'autos-camionetas/vehiculo_Desde_1969'





    )
    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido
            ), callback='parse_page'
        ),
    )
    
    url_segmento_restringido = (
        'guayas',
        'pichincha--quito-',
        'manabi',
        'azuay',
        'imbabura',
        'tungurahua',
        'santo-domingo-de-los-tsachilas',
        'chimborazo',
        'el-oro',
        'bolivar',
        'carchi',
        'canar',
        'cotopaxi',
        'esmeraldas',
        'loja',
        'los-rios',
        'morona-santiago',
        'napo',
        'orellana',
        'pastaza',
        'santa-elena',
        'sucumbios',
        'zamora-chinchipe'





    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido,
               # deny=url_segmento_restringido
            ),callback='parse_page'
        ),
    )
    
    
    rules = regla_tres

    def parse_page(self, response):
        titulo = response.css(
           'div.item__info > h2 >span::text'
        ).extract()
        precio = response.css(
           '.price__fraction::text'
        ).extract()
        detalle = response.css(
            '.item__attrs::text'
        ).extract()
        lugar = response.css(
            '.item__location::text'
        ).extract()
        print(titulo,precio,detalle,lugar)

        exportar_csv(titulo,precio,detalle,lugar)

        for agencia in titulo:
            with open('onu_agencias.txt', 'a+', encoding='utf-8') as archivo:
                archivo.write(agencia + '\n')
        

