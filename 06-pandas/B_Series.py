# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:58:07 2019

@author: USRBET
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(
        lista_numeros
        )
serie_b = pd.Series(
        tupla_numeros
        )
serie_c = pd.Series(
        np_numeros
        )
series_d = pd.Series([
        True,
        False,
        12,
        12.2,
        "Ale",
        None,
        (),
        [],
        {"nombre": "Ale"}
        ])
serie_d[3]
lista_ciudades = ["Ambato", 
                  "cuenca",
                  "loja", 
                  "quito"
                  ]
serie_ciudades = pd.Series(
        lista_ciudades,
        index = [
                "a",
                "c",
                "l",
                "q",
                ])
serie_ciudades["q"]
serie_ciudades[3]

valores_ciudad = {
        "ibarra":9500,
        "guayaquil":10000,
        "cuenca":7000,
        "loja":800
        }
serie_valor_ciudad = pd.Series(valores_ciudad)
serie_valor_ciudad[0]

menor_5000 = serie_valor_ciudad < 5000

serie_valor_ciudad[menor_5000]

s5 = serie_valor_ciudad[menor_5000]

serie_valor_ciudad = serie_valor_ciudad*1.10

serie_valor_ciudad["loja"] = serie_valor_ciudad - 50

print("Lima" in serie_valor_ciudad )

print("loja" in serie_valor_ciudad )

serie_valor_ciudad = np.square(serie_valor_ciudad)
serie_valor_ciudad = np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
        "Montañita":300,
        "Gye": 1000,
        "Quito":2000
        })

ciudades_dos = pd.Series({
        "Loja":3000,
        "Gye": 1000
        })

print(ciudades_uno + ciudades_dos)

ciudad_add = ciudades_uno.add(ciudades_dos)
ciudad_concat = pd.concat([
        ciudades_uno,
        ciudades_dos])
ciudad_concat_v = pd.concat([
        ciudades_uno,
        ciudades_dos], verify_integrity = True
)


ciudades_uno.sort_values().tail(2)

ciudades_uno.min

def calculo(valor):
    if(valor <= 1000):
        return valor *1.05
    if(valor > 1000 and valor <= 5000):
        return valor *1.10
    if(valor > 5000):
        return valor *1.15    
    
    
    
    

ciud_cal = ciudades_uno.map(calculo)
ciudades_uno.where(ciudades_uno < 1000,
                   ciudades_uno * 1.05)


































