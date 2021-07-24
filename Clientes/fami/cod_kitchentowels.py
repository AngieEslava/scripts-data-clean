# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:33:14 2019

@author: usuario
"""

import pandas as pd
import os
import time

kitchentowelsbd = pd.DataFrame()
rutafile = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\TOALLAS DE COCINA" 
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\TOALLAS DE COCINA\TC 2013 (SO) 2014(MJ).xls"
ruta2 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\TOALLAS DE COCINA\TC 2014(JA) 2017(JA).xls"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\TOALLAS DE COCINA\TC 2017(SEP) 2019(JUL).xls"
ruta4 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\TOALLAS DE COCINA\TC2010(JA) 2013(JA).xls"
columns = ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTE', 'MARCA', 'VARIEDAD', 'CONTEO', 'METRAJE', 'SEGMENTO']
#%%exploracion
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, ruta4)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)    
    
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
#%%edicion    
    for x in range(1,125):
        df = pd.read_excel(rutadoc, sheet_name=1,header=2)
        if rutadoc==ruta1:
            df = df.drop(df.columns[[8]], axis='columns')
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            kitchentowelsbd = kitchentowelsbd.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        if rutadoc == ruta2:
            df = df.drop(df.columns[[8]], axis='columns')
            names = df.columns.tolist()            
            names[names.index('FABRICANTE')] = 'CATEGORY'
            names[names.index('MARCA')] = 'FABRICANTE'
            names[names.index('SUBMARCA')] = 'MARCA'
            names[names.index('VARIACION')] = 'VARIEDAD'
            df.columns = names
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            kitchentowelsbd = kitchentowelsbd.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        if rutadoc == ruta3:
            df = df.drop(df.columns[[8]], axis='columns')
            names = df.columns.tolist()            
            names[names.index('SUBMARCA')] = 'VARIEDAD'
            df.columns = names
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            kitchentowelsbd = kitchentowelsbd.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        if rutadoc == ruta4:
            df = df.drop(df.columns[[8]], axis='columns')
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.assign(variable=serie[x])
            kitchentowelsbd = kitchentowelsbd.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
            
#%%fechas y merge      
dsfechasww = pd.Series(kitchentowelsbd['fecha'])
dsfechasww = dsfechasww.drop_duplicates()            
#fechaww=dsfechasww.to_excel(r'C:\Users\usuario\Desktop\fechas_kt.xlsx')   
    
fechas=pd.read_excel(r'C:\Users\usuario\Desktop\fechas_kt.xlsx')
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
kitchentowels = pd.merge(left = kitchentowelsbd, right = fechas, left_on='fecha', right_on='fecha')
kitchentowels.to_csv(r'C:\Users\usuario\Desktop\kitchentowels.csv')
