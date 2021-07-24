# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:01:54 2019

@author: usuario
"""


import pandas as pd
#import os
import time

columnas= ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTE', 'MARCA', 'VARIEDAD' ,'CONTEO', 'METRAJE','LEVEL','SEGMENTO']
columnas2= ['CANAL', 'TAG', 'FABRICANTE', 'MARCA', 'SUBMARCA', 'VARIACION' ,'CONTEO', 'METRAJE','NIVEL','SEGMENTO']
columnas3= ['CANAL', 'TAG', 'CATEGORY','FABRICANTE', 'MARCA', 'SUBMARCA', 'CONTEO', 'METRAJE','LEVEL','SEGMENTO']
columnas4= ['CANAL', 'TAG', 'CATEGORY','FABRICANTE', 'MARCA', 'VARIEDAD' ,'CONTEO', 'METRAJE','LONG DESCRIPTION','SEGMENTO']
toallascocinabd = pd.DataFrame()

df = pd.read_excel(r"C:\Users\usuario\Documents\1-familia_all\FAMILY\TOALLAS DE COCINA\TC2010(JA) 2013(JA).xls", sheet_name=2,header=2)
#names = df.columns.tolist()
#names[names.index( 'F1.FABRICANTES')] = 'FABRICANTES'
#df.columns = names
df = df.melt(id_vars=columnas4)
df = df.dropna(subset=['CATEGORY'])
df = df.dropna(subset=['FABRICANTE'])
df = df.rename(columns={'variable':'fecha'})
#df = df.assign(variable=serie[x])
toallascocinabd = toallascocinabd.append(df)
print('1' , time.strftime("%H:%M:%S"))
