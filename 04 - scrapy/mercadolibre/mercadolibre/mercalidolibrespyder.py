# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:44:00 2020

@author: Estudiante
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import nltk
import seaborn as sns

path_csv = "C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\vehiculo.csv"
data_frame_test = pd.read_csv(path_csv,  encoding = 'unicode_escape',sep = ";")
data_frame_test.dropna()
data_frame_test.dtypes
d = data_frame_test['titulo'].str.split(' ').str[0]
df = pd.DataFrame(d)
data_frame_test['marca'] = df
cols = data_frame_test.columns.tolist()
cols = cols[-1:] + cols[:-1]
data_frame_test = data_frame_test[cols]

# Numero de filas y columnas
print(data_frame_test.shape)
#Top 10 de las marcas más vendida
plt.figure(figsize=(10,8))
plt.title('Top 10 de marcas mas vendidas en Mercado libre')
data_frame_test['marca'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Top 10 de marcas mas vendidas.jpg")
plt.show()
# Año del modelo mas vendido
plt.figure(figsize=(10,8))
plt.title('Año del modelo mas vendido')
data_frame_test['anio'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Año del modelo mas vendidos.jpg")
plt.show()
# Kilometraje que mas se vende
plt.figure(figsize=(15,8))
plt.title('Kilometraje que mas se vende')
data_frame_test['kilometraje'].value_counts()[:15].plot(kind='bar')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Kilometraje que mas se vende.jpg")
plt.show()
# sitios que mas venden los vehiculos
plt.figure(figsize=(15,8))
plt.title('sitios que mas venden los vehiculos')
data_frame_test['lugar'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\sitios.jpg")
plt.show()
# Las 5 mejores marcas vendidas en Pichincha ( Quito )
plt.title("Las 5 mejores marcas vendidas en Pichincha ( Quito )")
valor =  data_frame_test.marca[data_frame_test.lugar=='Pichincha ( Quito )'].value_counts()[:5]
marca = ['Chevrolet','Toyota','Ford','Hyundai','Kia']
plt.pie(valor, labels=marca, autopct='%1.1f%%',
        shadow=True, startangle=90, radius = 1800)
plt.axis('equal')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Las 5 mejores marcas vendidas en Pichincha ( Quito ).jpg")
plt.show()
# Año de los vehiculo mas vendidos en Pichincha ( Quito )
plt.title("Año de los vehiculo mas vendidos en Pichincha ( Quito )")
valor_anio =  data_frame_test.anio[data_frame_test.lugar=='Pichincha ( Quito )'].value_counts()[:10]
valor_anio_etiqueta = [2013,2007,2014,2011,2009,2019,2018,2012,2006,2008]
plt.pie(valor_anio, labels=valor_anio_etiqueta, autopct='%1.1f%%',
        shadow=True, startangle=90, radius = 1800)
plt.axis('equal')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Año de los vehiculo mas vendidos en Pichincha ( Quito ).jpg")
plt.show()
# Precio de los vehiculo mas vendidos en Pichincha ( Quito )
plt.title("Precio de los vehiculo mas vendidos en Pichincha ( Quito )")
data_frame_test.valor[data_frame_test.lugar=='Pichincha ( Quito )'].value_counts()[:5].plot(kind='bar')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Precio de los vehiculo mas vendidos en Pichincha ( Quito ).jpg")
plt.show()
# Kilometraje de los vehiculo mas vendidos en Pichincha ( Quito )
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1)
ax.plot(data_frame_test.kilometraje[data_frame_test.lugar=='Pichincha ( Quito )'].value_counts()[:10],'ko--')
ax.set_title('Kilometraje de los vehiculo mas vendidos en Pichincha ( Quito )')
ax.set_xlabel('Kilometraje')
ax.set_ylabel('N. ofertas')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Kilometraje de los vehiculo mas vendidos en Pichincha ( Quito ).jpg")
# Precios ofertados en la marca Chevrolet
plt.figure(figsize=(20,8))
plt.title('Precios ofrecidos en los vehiculos de Chevrolet')
edades_hombres = data_frame_test.valor[data_frame_test.marca=='Chevrolet'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Precios ofrecidos en los vehiculos de Chevrolet.jpg")
plt.show()
# Auto que vale 45.0
data_frame_test.titulo[data_frame_test.valor==45.0]
# Top 10 de los kilometrajes de chevrolet mas vendidos
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(1, 1, 1)
ax.plot(data_frame_test.kilometraje[data_frame_test.marca=='Chevrolet'].value_counts()[:10],'ko--')
ax.set_title('Top 10 de los kilometrajes de chevrolet mas vendidos')
ax.set_xlabel('Kilometraje')
ax.set_ylabel('N. veces')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Top 10 de los kilometrajes de chevrolet mas vendidos.jpg")
# Top 10 de los años que chevrolet mas vendidos
plt.figure(figsize=(20,8))
plt.title('Top 10 de los años que chevrolet mas vendidos')
edades_hombres = data_frame_test.anio[data_frame_test.marca=='Chevrolet'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Top 10 de los años que chevrolet mas vendidos.jpg")
plt.show()
# Top 10 de los lugares que mas se vende chevrolet
plt.figure(figsize=(20,8))
plt.title('Top 10 de los años que chevrolet mas vendidos')
edades_hombres = data_frame_test.lugar[data_frame_test.marca=='Chevrolet'].value_counts().plot(kind='barh')
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Top 10 de los lugares que mas se vende chevrolet.jpg")
plt.show()
# Marca Vs Precio
plot = data_frame_test.plot(x='marca', y='valor')
plot.set_ylim(0, 1000)
plt.savefig("C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\Marca Vs Precio.jpg")
# 








#df1 = pd.DataFrame(arr_pand)

#pandas.core.series.Series


#data_frame_test['anio n'] = data_frame_test['anio'].
'''
splitwords = [nltk.word_tokenize( str(data_frame_test['titulo'])) for a in data_frame_test['titulo']]
print(splitwords)

a= data_frame_test.apply(lambda row: nltk.word_tokenize(row['titulo']), axis=1)
b = pd.DataFrame(a)
c = a.str.split(expand=True)
'''
#df1['DIA']=df1['DIA'].astype('i
'''  df = pd.DataFrame(data)
>>> filtro = df[df['col1'].str.contains(r"\bGRANEL\b", regex=True)]
>>> filtro'''