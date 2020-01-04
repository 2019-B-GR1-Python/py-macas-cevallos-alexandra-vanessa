# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:23:24 2020

@author: USRBET
"""

import pandas as pd
import math
import numpy as np

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//06-pandas//data//artwork_data_completo.pickle"
df = pd.read_pickle(path_guardado_bin)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)

for columna_agrupada,df_completo in df_agrupado:
    print(columna_agrupada)
    print(df_completo)
    
a = seccion_df['units'].value_counts()
a.empty

def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            #promedio = np.nanmean(series)
            #serie_valores_llenos = series.fillna(promedio)
            #return serie_valores_llenos
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie,str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
                else:
                    pass                   
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        
        if(tipo == 'value_counts'):
            for valor_serie in series:
                if(isinstance(valor_serie, str)):
                    #valor = int(valor_serie)
                    #numero_valores = numero_valores + 1
                    #suma = suma + valor
                    #valor = valor_serie
                    valor = valor_serie
                else:
                    pass
            #promedio = suma / numero_valores
            serie_valores_llenos = series.fillna(valor)
            return serie_valores_llenos           
        
        
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
        copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
        copia.loc[:,'units'] = llenar_valores_vacios(serie_u, 'value_counts')
        copia.loc[:,'inscription'] = llenar_valores_vacios(serie_i, 'value_counts')
        lista_df.append(copia)
        
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores

df_valores_llenos = transformar_df(seccion_df)