# Scrapy
## Scrapy instalacion
Ejecutar dentro del `Anaconda promt`
```
$ pip install scrapy
```
## comandos generales
da `las carcateristicas `para poder hacer Web Scraping o Web crawling de ese computador
```
$ scrapy bench
```
Visualizar las `configuraciones extras`
```
$ scrapy settings
```
Visualizamos la `version`de scrapy
```
$ scrapy version
```
### scrapy  view `url`
permite ver que datos puede el scrapy ontener de una pagina web
del sri es por que algunos servidores se conectan y se debe instalar demas plugins

```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```
 ### scrapy shell `url`
 permite `interactuar con la respuesta`
  del scrapy
 ```
$ scrapy shell http://quotes.toscrape.com/
```
 ```
$ response.css('title')
```
 ```
$ response.css('title').extract()
```
 ```
$ response.css('title::text').extract()
```
 ```
$  response.css('.author').extract()
``` 
```
$ response.css('.author::text').extract()
```
```
$  type(response.css('.author::text'))
```
```
$  response.css('.author::text').extract()[0]
```

```
$  response.css('.author::text')[0].extract()
```

```
$  response.css('.author::text').extract_first()
```
```
$  response.css('span.text').extract()
```
```
$  response.css('span.text::text').extract()
```
```
$  len(response.css('div.tags>a.tag::text').extract())
```
```
$  response.css('div.quote>span>a::attr(href)').extract()
```
## Xpath

```
$  response.xpath('/html/head/title').extract()
```
```
$  response.xpath('/html/body/div/div[2]/div[2]/h2/text()').extract()
```
```
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
```
todos los div
```
$ response.xpath('//div').extract()
```
```
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
```
```
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
```
```
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()
```
```
$ response.xpath("//div[@class='quote']/span/a/text()").extract_first()
```
## scrapy startproject `nombre_proyecto`

```
$ scrapy startproject arania_basica
```
```
$ scrapy crawl introduccion_spider
```
```
$ response.xpath('//div').extract()
```
