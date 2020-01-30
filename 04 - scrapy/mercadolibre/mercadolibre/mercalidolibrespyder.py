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

path_csv = "C:\\Users\\Estudiante\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\04 - scrapy\\mercadolibre\\mercadolibre\\mercadolibre\\vehiculo.csv"
data_frame_test = pd.read_csv(path_csv,  encoding = 'unicode_escape',sep = ";")
data_frame_test.dropna()
#data_frame_test['anio n'] = data_frame_test['anio'].astype('int')
data_frame_test.dtypes
d = data_frame_test['titulo'].str.split(' ').str[0]
df = pd.DataFrame(d)
data_frame_test['marca'] = df
cols = data_frame_test.columns.tolist()
cols = cols[-1:] + cols[:-1]
data_frame_test = data_frame_test[cols]


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