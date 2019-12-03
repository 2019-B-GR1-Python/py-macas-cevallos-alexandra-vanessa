# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:51 2019

@author: USRBET
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//06-pandas//data//artwork_data.pickle"

df3 = pd.read_pickle(path_guardado)

path_guardado_excel = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//ex.xlsx"
df3.to_excel(path_guardado_excel)
df3.to_excel(path_guardado_excel, index = False)
columnas = ['artist','title','year']
df3.to_excel(path_guardado_excel, columns = columnas)

path_guardado_multiple = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//mulex.xlsx"
df3.to_excel(path_guardado_multiple, columns = columnas)
num = df3['artist'].value_counts()
path_color = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//colores.xlsx"
df3.to_excel(path_color)
writer = pd.ExcelWriter(path_color, engine = 'xlsxwriter')
num.to_excel(writer, sheet_name = 'Artistas')
hoja_artistas = writer.sheets['Artistas']

rango = 'B2:B{}'.format(len(num.index)+1)

formato  = {
        "type":"2_color_scale",
        "min_value":"10",
        "min_type":"percentile",
        "max_value":"99",
        "max_type":"percentile"
        }
hoja_artistas.conditional_format(rango, formato)

workbook = ThisWorkbook(path_color)
worksheet = workbook.add_worksheet()
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('B2:B', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': '=$A$1:$A$6'})

# Insert the chart into the worksheet.
worksheet.insert_chart('D1', chart)

workbook.close()
