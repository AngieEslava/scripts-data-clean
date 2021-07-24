# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:05:07 2019

@author: usuario
"""

import pandas as pd
import os
import time
#%%exploracion de rutas, cada archivo requiere una edicion diferente
protectoresbd = pd.DataFrame()
rutafile = r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\PROTECTORES"
ruta1 = r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\PROTECTORES\PROTECTORES 2010-2012.xlsm"
ruta2 = r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\PROTECTORES\PROTECTORES 2013.xlsm"
ruta3 = r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\PROTECTORES\PROTECTORES 2014-2015.xlsm"
ruta4 = r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\PROTECTORES\PROTECTORES 2016-2017(JUL).xlsm"
ruta5= r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\PROTECTORES\PROTECTORES ENH.xlsm"
columnas= ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'C/S ALAS','GROSORES','SUBMARCAS', 'C/S CUBIERTAS','SEGMENTO', 'PRESENTACIONES']

for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
#%%capturar variables    
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
#%%edicion de archivos    
    for x in range(1,156):
        df = pd.read_excel(rutadoc, sheet_name=x,header=2)
        if rutadoc == ruta1:
            names = df.columns.tolist()
            names[names.index( 'F1.FABRICANTES')] = 'FABRICANTES'
            names[names.index( 'F1.MARCAS')] = 'MARCAS'
            names[names.index( 'F1.C/S ALAS')] = 'C/S ALAS'
            names[names.index( 'F1.GROSORES')] = 'GROSORES'
            names[names.index( 'F1.SUBMARCAS')] = 'SUBMARCAS'
            names[names.index( 'F1.C/S CUBIERTAS')] = 'C/S CUBIERTAS'
            names[names.index( 'F1.PRESENTACIONES')] = 'PRESENTACIONES'
            df.columns = names
            df = df.melt(id_vars=columnas)
            df = df.dropna(subset=['CATEGORY'])
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            protectoresbd = protectoresbd.append(df)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
        elif rutadoc == ruta2:
            names = df.columns.tolist()
            names[names.index( 'F1.FABRICANTES')] = 'FABRICANTES'
            names[names.index( 'F1.MARCAS')] = 'MARCAS'
            names[names.index( 'F1.C/S ALAS')] = 'C/S ALAS'
            names[names.index( 'F1.GROSORES')] = 'GROSORES'
            names[names.index( 'F1.SUBMARCAS')] = 'SUBMARCAS'
            names[names.index( 'F1.C/S CUBIERTAS')] = 'C/S CUBIERTAS'
            names[names.index( 'F1.PRESENTACIONES')] = 'PRESENTACIONES'
            df.columns = names
            df = df.melt(id_vars=columnas)
            df = df.dropna(subset=['CATEGORY'])
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            protectoresbd = protectoresbd.append(df)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
            
        elif rutadoc == ruta3:
            df = df.drop(['LONG DESCRIPTION'], axis=1)
            df = df.melt(id_vars=columnas)
            df = df.dropna(subset=['CATEGORY'])
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            protectoresbd = protectoresbd.append(df)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
            
        elif rutadoc == ruta4:
            df = df.drop(['LONG DESCRIPTION'], axis=1)
            df = df.melt(id_vars=columnas)
            df = df.dropna(subset=['CATEGORY'])
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            protectoresbd = protectoresbd.append(df)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
            
        elif rutadoc == ruta5:
            df = df.drop(['LONG DESCRIPTION'], axis=1)
            df = df.melt(id_vars=columnas)
            df = df.dropna(subset=['CATEGORY'])
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            protectoresbd = protectoresbd.append(df)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
        else:
            df = df.melt(id_vars=columnas)
            df = df.dropna(subset=['CATEGORY'])
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            protectoresbd = protectoresbd.append(df)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
            break
        
    
    #protectoresbd.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\protectoresdate.csv')

            
#%%edicion fechas y merge
    dsfechasww = pd.Series(protectoresbd['fecha'])
    dsfechasww = dsfechasww.drop_duplicates()
    #fechaww=dsfechasww.to_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_PROTECTORES.xlsx')
    
fechas=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_PROTECTORES.xlsx')
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
protectores_familia = pd.merge(left = protectoresbd, right = fechas, left_on='fecha', right_on='fecha')
#protectores_familia.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\protectores.csv')

