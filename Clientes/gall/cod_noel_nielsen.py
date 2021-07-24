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

rutafile = r"C:\Users\usuario\Documents\BD_custumers\Noel\Nielsen_Noel"
#%% Exploracion inicial
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    df = pd.read_excel(rutadoc)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
#%% Edicion de archivo
    df.columns = [list(df.iloc[0]), list(df.iloc[1])] #editar columnas con forma de dos titulos relevantes en diferentes filas
    df = df.drop([0])
    df = df.drop([1])
    dfmelt = pd.melt(df, id_vars=[('nombre','archivo'),('var','fecha')])
    dfdb = dfdb.append(dfmelt)
    
    serie = pd.Series(df.iloc[:, 0])#elimirar duplicados de fechas
    serie = serie.to_frame()
    serie = serie.drop_duplicates(subset=('var','fecha'))
    bdvarfecha=bdvarfecha.append(serie)
    bdvarfecha=bdvarfecha.drop_duplicates(subset=('var','fecha'))
    
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)

#%%edicion archivo final
dfdb.columns = ['nombre archivo','longDescription', 'variable', 'fecha', 'value']

segmento= pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\Noel\cod_Edicion\segmentosNoel.xlsx")
segmento.columns = ['drop', 'longDescription', 'segmento', 'fabricante']
segmento = segmento.drop(['drop'], axis=1)

dfechas = pd.Series(dfdb.iloc[:, 2])
dfechas = dfechas.to_frame()
dfechas = dfechas.drop_duplicates()
#dfecha = pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\Noel\cod_Edicion\fechas\fechasNoel.xlsx", sheet_name = 0)
dfecha = dfecha.drop(dfecha.columns[[0]], axis='columns')

#%%merge de archivos final y fechas
noel = pd.merge(left = dfdb, right = segmento, left_on='longDescription', right_on='longDescription')
noelf = pd.merge(left = noel, right = dfecha, how='outer', left_on='fecha', right_on='fecha')
noelf.to_csv(r"C:\Users\usuario\Documents\BD_custumers\Noel\EntregasNoel\DBNOEL_filename.csv")

duplicados = pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\Noel\cod_Edicion\fechas\fechasNoel.xlsx", sheet_name = 2)

duplicados.columns = ['nombre archivo', 'fecha', 'include']

data = noelf.merge(duplicados, how='left', left_on=['nombre archivo', 'fecha'], right_on=['nombre archivo', 'fecha'])
data2 = data[data['include'] == 1]
data2.to_csv(r"C:\Users\usuario\Documents\BD_custumers\Noel\EntregasNoel\DBNOELfinal.csv")

#dividir texto separado por comas.str.split(',', n = 6, expand = True)
