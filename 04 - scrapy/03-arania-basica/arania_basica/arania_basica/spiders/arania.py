import scrapy # importar un paquete de scrapy
# las arañas son clases
class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider' # nombre de la araña para ejecutar
# definir los url digitadas y guardamos como string
    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    # definir una funicion, self es el this
    # yield para que se complete la linea y no sea asincrono, se manda un parametro nombrado

    def start_requests (self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    # pasear los datos
    # se nesecita los css para sacar la informacion
    def parse(self, response):
        # definir variable para la etiqueta
        etiqueta_contenedora = response.css('article.product_pod')

     
        etiqueta_contenedora_precio = response.css('article.product_pod')
         precio = etiqueta_contenedora_precio.css('div.product_price >p.price_color::text').extract()
        for i in precio:
            titulos = etiqueta_contenedora.css('div.image_container>a::attr(href)').extract()
            
            shortLink = 'http://books.toscrape.com/catalogue'+titulos
        

            
        
        
        
      ##  for i in range(len(precio)):
          ##  precio[i]=float(precio[i])
        print(titulos,precios)
   





