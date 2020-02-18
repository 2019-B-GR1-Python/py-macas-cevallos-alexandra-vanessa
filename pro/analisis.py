# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:12:34 2019

@author: Ale
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path_csv = "C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\world_marathon_majors2.csv"
data_frame_test = pd.read_csv(path_csv,  encoding = 'unicode_escape',sep = ";",parse_dates=[2],infer_datetime_format=True)
data_frame_test.dropna()
temp = pd.DatetimeIndex(data_frame_test['time'])
data_frame_test['Date'] = temp.date
data_frame_test['Time'] = temp.time
del data_frame_test['time']
data_frame_test.dtypes

print(data_frame_test.shape)

print ("Han existido un total de: ",data_frame_test["winner"].size," ganadores de los seis Grandes Maratones Mundiales de la historia")
print (data_frame_test["winner"])

plt.figure(figsize=(15,6))
plt.title('Top 10 de los ganadores de los maratones')
ganadores_count = data_frame_test['winner'].value_counts()[:10].sort_values().plot(kind='barh')
count_ganadores = data_frame_test['winner'].value_counts()[:10]
print(count_ganadores)
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Top 10 de los ganadores de los maratones.jpg")
plt.show()

plt.figure(figsize=(10,6))
plt.title('Maratones que ha ganado Grete Waitz')
ganadors_count = data_frame_test.marathon[data_frame_test.winner=='Grete Waitz'].value_counts().sort_values().plot(kind='barh')
count_ganador = data_frame_test.marathon[data_frame_test.winner=='Grete Waitz'].value_counts()
print(count_ganador)
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Maratones que ha ganado Grete Waitz.jpg")
plt.show()

genero = data_frame_test['gender'].value_counts()
tipo_genero = ['Male','Female']
plt.figure(figsize=(5,6))
plt.title('Segregación de ganadores por genero')
plt.bar(tipo_genero, genero, color = 'orangered')
for a,b in zip(tipo_genero, genero):
    plt.text(a,b,str(b),  horizontalalignment='center', fontsize=15, family = 'fantasy',fontweight = 'bold')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Segregación de ganadores por genero.jpg")
plt.show()

print("El genero del campeon Grete Witz es:", data_frame_test.gender[data_frame_test.winner=='Grete Waitz'])

plt.title('Particiaciones por edad de mujeres')
edades_mujeres = data_frame_test.age[data_frame_test.gender=='Female'].value_counts()[:10].plot(kind = 'bar')
data_frame_test.age[data_frame_test.gender=='Female'].value_counts()[:10]
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Participación por edad en mujeres.jpg")
plt.show()

plt.title('Participaciones por edad de hombres')
edades_hombres = data_frame_test.age[data_frame_test.gender=='Male'].value_counts()[:10].plot(kind='bar')
data_frame_test.age[data_frame_test.gender=='Male'].value_counts()[:10]
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Participación por edad en hombres.jpg")
plt.show()

edad = data_frame_test['age'].value_counts()[:10]
edadNum = [int(x) for x in edad]
#edadNum.sort()
a = 0 
b = 0 
c = 0
d = 0 
e = 0 
f = 0
for i in edadNum:
    if(i<=25):
        a = a+1
    elif(i<=35 and i>25):
        b = b+1
    elif(i<=45 and i>35):
        c = c+1
    elif(i<=55 and i>45):
        d = d+1
    elif(i<=65 and i>55):
        e = e+1
    else:
        f = f+1

edades = [a,b,c,d,e,f]
edadesCat = ['De 18 a 25 años', 'De 26 a 35 años', 'De 36 a 45 años', 
             'De 46 a 55 años', 'De 56 a 65 años', 'De 65 años en adelante']

plt.title("Porcetanjes de participantes por rango de edad")
plt.pie(edades, labels=edadesCat, autopct='%1.1f%%',
        shadow=True, startangle=90, radius = 1800)
plt.axis('equal')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Porcetanjes de participantes por rango de edad.jpg")
plt.show()


tiempo = data_frame_test['Time'].value_counts()[:10]
tiemposM = ['< 2h05m', '< 2h10m', '< 2h20m', '< 2h30m', '< 2h40m', 
           '< 2h50m', '< 3h00m', '< 3h10m', '< 3h20m', '< 3h30m']
y_tiempo = np.arange(len(tiemposM))
plt.figure(figsize=(10,8))
plt.title('Tiempos de llegada de los Participantes')
plt.barh(y_tiempo, tiempo)
for i, v in enumerate(tiempo):
    plt.text(v + 3, i + .25, str(v), va='center', color='blue', fontweight='bold')
plt.yticks(y_tiempo, tiemposM)
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Tiempos de llegada de los Participantes.jpg")
plt.show()

plt.figure(figsize=(10,8))
plt.title('Pais con mayor numero de participantes')
data_frame_test['country'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Pais con mayor numero de participantes.jpg")

plt.figure(figsize=(30,5))
plt.title("Total de Participantes por año")
ganadores_anio = data_frame_test['year'].value_counts()[:40].plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Total de Participantes por año.jpg")
plt.show()

plt.title('Participantes en marathon')
data_frame_test['marathon'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\participantes en marathon.jpg")


plt.title('paises que participan en Boston')
data_frame_test.country[data_frame_test.marathon=='Boston'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\ciudades que participan en Boston.jpg")

plt.figure(figsize=(30,8))
plt.title('Participantes de EEUU')
data_frame_test.winner[data_frame_test.country=='United States'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\evidence\\Participantes de EEUU.jpg")



