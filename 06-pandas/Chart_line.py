# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:24:01 2019

@author: Ale
"""

import xlsxwriter
workbook = xlsxwriter.Workbook('C://Users//Ale//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//06-pandas//data//mi_df_colores.xlsx')
worksheet = workbook.add_worksheet()
data = numero_artistas.values
worksheet.write_column('B2',data)
chart = workbook.add_chart({'type':'line'})
chart.add_series({'values':'=Sheet1!$B$2:$B$85'})
worksheet.insert_chart('C1', chart)
workbook.close()