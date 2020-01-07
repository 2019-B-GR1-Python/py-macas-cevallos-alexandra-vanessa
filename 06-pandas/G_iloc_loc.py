f# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:00 2019

@author: USRBET
"""

import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-macas-cevallos-alexandra-vanessa//06-pandas//data//artwork_data_completo.pickle"
df = pd.read_pickle(path_guardado_bin)
df.dtypes
df2 = df.set_index('id')
"""


"""
datos = {
        "Nota 1":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "Disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
        }
        
        

datos_notas = pd.DataFrame(datos) 
datos_notas.iloc[0]
datos_notas.loc["Pepito"]
datos_notas.loc["Pepito",["Disciplina","Nota 1"]]
datos_notas.loc[["Pepito","Juanita"],["Disciplina","Nota 1"]]
datos_notas[[True, False, True]]
condicion_nota = datos_notas["Nota 1"] < 7
condicion_dic = datos_notas["Disciplina"] < 7
mayores_siete = datos_notas.loc[condicion_nota,["Nota 1"]]
mayor_siete = datos_notas.loc[condicion_nota][condicion_dic]


# 1
datos_notas.loc["Maria":,"Disciplina"] = 7
#dn1 = datos_notas.loc[:,condicion_nota,[condicion_dic]] = 7
              


primero  = df.loc[0]
primero = df.iloc[0]
print(primero)