# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:59 2019

@author: USRBET
"""

import pandas as pd
import os

path = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//06-pandas//data//artwork_data.csv"
df1 = pd.read_csv(
        path,
        nrows = 10)

columnas = ['id','artist','title','medium','year','acquisitionYear','height','width','units']

df2 = pd.read_csv(
        path,
        nrows = 10,
        usecols= columnas)

df3 = pd.read_csv(
        path,
        nrows = 10,
        usecols= columnas,
        index_col = 'id')

path_guardado = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//06-pandas//data//artwork_data.pickle"

df3.to_pickle(path_guardado)

