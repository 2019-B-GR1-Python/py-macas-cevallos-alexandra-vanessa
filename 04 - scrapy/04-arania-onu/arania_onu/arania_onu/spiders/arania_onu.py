import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' # heredado (override)
    allowed_domains = [
        'un.org'
    ]
    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/'
    ]
    # al ver un ñink utiliza el parse page
    regla_uno = ( #busque en toda la pagina
        Rule(LinkExtractor(), callback= 'parse_page')
        ,
    )
    # busque en un link especifico con partes d ela url, segmentos de busqeuda
    url_segmento_permitido = ( # busque en un sitio especifico
        'funds-programmes-specialized-agencies-and-others'

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
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido,
                deny=url_segmento_restringido
            ),callback='parse_page'
        ),
    )
    rules = regla_tres

    def parse_page(self, response):
        lista_programas_onu = response.css(
            'div.field-items > div.field-item > h4::text'
        ).extract()
        for agencia in lista_programas_onu:
            with open('onu_agencias.txt', 'a+', encoding='utf-8') as archivo:
                archivo.write(agencia + '\n')

