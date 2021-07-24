# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:44:41 2019

@author: usuario
"""


import pandas as pd
import os
import time

bdvarfecha = pd.DataFrame()
dfdb = pd.DataFrame()

rutafile = r"C:\Users\usuario\Documents\BD_custumers\Noel\Nielsen_Noel - copia (3)"
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Noel\Nielsen_Noel - copia (2)\AS09-AS12.xlsx"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Noel\Nielsen_Noel - copia (2)\JJ10-JJ13.xlsx"
ruta4 = r"C:\Users\usuario\Documents\BD_custumers\Noel\Nielsen_Noel - copia (2)\JJ13-JJ16.xlsx"
ruta5 = r"C:\Users\usuario\Documents\BD_custumers\Noel\Nielsen_Noel - copia (2)\JJ15-JJ18.xlsx"
ruta6 = r"C:\Users\usuario\Documents\BD_custumers\Noel\Nielsen_Noel - copia (2)\ON13-ON16.xlsx"
#%%ediciones diferentes
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    df = pd.read_excel(rutadoc)
    if rutadoc==ruta1:
        df.columns = df.iloc[1]
        df = df.drop(['JJ 2010', 'AS 2010','ON 2010','DE 2011','FM 2011','AM 2011','JJ 2011','AS 2011','ON 2011','DE 2012','FM 2012','AM 2012','JJ 2012','AS 2012'], axis = 1)
        df.columns = [list(df.iloc[0]), list(df.iloc[1])]
        df = df.drop([0])
        df = df.drop([1])
        dfmelt = pd.melt(df, id_vars=[('nombre','archivo'),('var','fecha')])
        dfdb = dfdb.append(dfmelt)
        print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
    if rutadoc==ruta3:
        df.columns = df.iloc[1]
        df = df.drop(['JJ 2013'], axis = 1)
        df.columns = [list(df.iloc[0]), list(df.iloc[1])]
        df = df.drop([0])
        df = df.drop([1])
        dfmelt = pd.melt(df, id_vars=[('nombre','archivo'),('var','fecha')])
        dfdb = dfdb.append(dfmelt)
        print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)              
    if rutadoc==ruta4:
       df.columns = df.iloc[1]                   
       df = df.drop(['ON 2013','DE 2014','FM 2014','AM 2014','JJ 2014','AS 2014','ON 2014','DE 2015','FM 2015','AM 2015','JJ 2015','AS 2015','ON 2015','DE 2016','FM 2016','AM 2016','JJ 2016'], axis = 1)
       df.columns = [list(df.iloc[0]), list(df.iloc[1])]
       df = df.drop([0])
       df = df.drop([1])
       dfmelt = pd.melt(df, id_vars=[('nombre','archivo'),('var','fecha')])
       dfdb = dfdb.append(dfmelt)
       print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
    if rutadoc==ruta6:
       df.columns = df.iloc[1]
       df = df.drop(['JJ 2015','AS 2015','ON 2015','DE 2016','FM 2016','AM 2016','JJ 2016','AS 2016','ON 2016'], axis = 1)
       df.columns = [list(df.iloc[0]), list(df.iloc[1])]
       df = df.drop([0])
       df = df.drop([1])
       dfmelt = pd.melt(df, id_vars=[('nombre','archivo'),('var','fecha')])
       dfdb = dfdb.append(dfmelt)
       print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
    if rutadoc == ruta5:
       df.columns = [list(df.iloc[0]), list(df.iloc[1])]
       df = df.drop([0])
       df = df.drop([1])
       dfmelt = pd.melt(df, id_vars=[('nombre','archivo'),('var','fecha')])
       dfdb = dfdb.append(dfmelt)
       print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
       
       
    serie = pd.Series(df.iloc[:, 0])
    serie = serie.to_frame()
    serie = serie.drop_duplicates(subset=('var','fecha'))
    bdvarfecha=bdvarfecha.append(serie)
    bdvarfecha=bdvarfecha.drop_duplicates(subset=('var','fecha'))
    
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)

#%%fechas
dfdb.columns = ['nombre archivo','longDescription', 'variable', 'fecha', 'value']

segmento= pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\Noel\cod_Edicion\segmentosNoel.xlsx")
segmento.columns = ['drop', 'longDescription', 'segmento', 'fabricante']
segmento = segmento.drop(['drop'], axis=1)

dfechas = pd.Series(dfdb.iloc[:, 2])
dfechas = dfechas.to_frame()
dfechas = dfechas.drop_duplicates()
dfecha = pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\Noel\cod_Edicion\fechas\fechasNoel.xlsx", sheet_name = 0)
dfecha = dfecha.drop(dfecha.columns[[0]], axis='columns')

noel = pd.merge(left = dfdb, right = segmento, left_on='longDescription', right_on='longDescription')
noelf = pd.merge(left = noel, right = dfecha, how='outer', left_on='fecha', right_on='fecha')
#noelf.to_csv(r"C:\Users\usuario\Documents\BD_custumers\Noel\EntregasNoel\DBNOEL_filename.csv")

#dividir texto separado por comas.str.split(',', n = 6, expand = True)