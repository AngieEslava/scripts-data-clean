# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:19:47 2019

@author: usuario
"""

import pandas as pd
import os
import time

fragancesdb = pd.DataFrame()

rutafile = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\FRAGANCIAS"
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\FRAGANCIAS\FR 2011(SO) 2014 (MJ).xlsx"
ruta2 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\FRAGANCIAS\FR 2014(JA) 2017(JA).xlsx"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\FRAGANCIAS\FR 2017(SEP) - 2019(JUN).xlsx"

columns = ['CANAL', 'TAG', 'CATEGORY', 'TIPO', 'FABRICANTE','MARCA', 'SUBMARCA', 'CONTEO', 'VOLUMEN', 'FRAGANCIA', 'LONG DESCRIPTION', 'SEGMENTO']
#%% Exploracion, cada archivpo es diferente
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
    
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])

    for x in range(1,125):
        df = pd.read_excel(rutadoc, sheet_name=1,header=2)
        print(time.strftime("%H:%M:%S"),rutadoc)
        
        if rutadoc == ruta1:
            df = df.rename(columns={'CANTIDAD':'CONTEO'})
            df = df.drop(df.columns[[10]], axis='columns')
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            fragancesdb = fragancesdb.append(df)
            print('change', x , time.strftime("%H:%M:%S"),rutadoc)
        else:
            df = df.drop(df.columns[[10]], axis='columns')
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            fragancesdb = fragancesdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        
#%%fechas y merge   
dsfechas = pd.Series(fragancesdb['fecha'])
dsfechas = dsfechas.drop_duplicates()         
#dsfechas.to_excel(r"C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasFragancias.xlsx")        

fechas = pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasFragancias.xlsx")      
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
fragances = pd.merge(left = fragancesdb, right = fechas, left_on='fecha', right_on='fecha')
fragances.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\fragances.csv')
