# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:35:19 2019

@author: usuario
"""

import pandas as pd
import os
import time

bdvarfecha = pd.DataFrame()
dfdb = pd.DataFrame()

rutafile = r"C:\Users\usuario\Documents\Noel\Nielsen_Noel"
#%% Ciclo para archivos iguales
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    df = pd.read_excel(rutadoc)
    df.columns = [list(df.iloc[0]), list(df.iloc[1])]# Edicion de columnas dobles
    df = df.drop([0])
    df = df.drop([1])
    dfmelt = pd.melt(df, id_vars=[('var','fecha')])
    dfdb = dfdb.append(dfmelt)
    serie = pd.Series(df.iloc[:, 0])
    serie = serie.to_frame()
    serie = serie.drop_duplicates(subset=('var','fecha'))
    bdvarfecha=bdvarfecha.append(serie)
    bdvarfecha=bdvarfecha.drop_duplicates(subset=('var','fecha'))
    
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)

#%%Edicion final 
dfdb.columns = ['longDescription', 'variable', 'fecha', 'value']
segmento= pd.read_excel(r"C:\Users\usuario\Documents\Noel\segmentosNoel.xlsx")
segmento.columns = ['drop', 'longDescription', 'segmento', 'fabricante']
segmento = segmento.drop(['drop'], axis=1)
#%% eliminar datos con fechas repetidas
dfechas = pd.Series(dfdb.iloc[:, 2])
dfechas = dfechas.to_frame()
dfechas = dfechas.drop_duplicates()
dfecha = pd.read_excel(r"C:\Users\usuario\Documents\fechas\fechasNoel.xlsx")
dfecha = dfecha.drop(dfecha.columns[[0]], axis='columns')

noel = pd.merge(left = dfdb, right = segmento, left_on='longDescription', right_on='longDescription')
noelf = pd.merge(left = noel, right = dfecha, how='outer', left_on='fecha', right_on='fecha')
#noelf.to_csv(r"C:\Users\usuario\Documents\Noel\DBNOEL.csv")

#dividir texto separado por comas.str.split(',', n = 6, expand = True)
