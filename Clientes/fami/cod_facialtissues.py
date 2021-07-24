# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:19:32 2019

@author: usuario
"""

import pandas as pd
import os
import time

facialtissuesdb = pd.DataFrame()

rutafile = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\PAÑUELOS FACIALES"
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\PAÑUELOS FACIALES\PF 2010(MJ) 2011(MJ).xlsx"
ruta2 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\PAÑUELOS FACIALES\PF 2011(JA) 2014(MJ).xlsx"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\PAÑUELOS FACIALES\PF 2014(JA) 2017 (JA).xlsx"
ruta4 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\PAÑUELOS FACIALES\PF2017(SEP) 2019(JUN).xlsx"

columns = ['CANALES', 'TAG', 'CATEGORY', 'FABRICANTE', 'MARCA', 'EMPAQUE','TIPO DE EMPAQUE', 'TIPO HOJA', 'PRESENTACION', 'PAQUETES', 'CONTEO', 'LEVEL', 'SEGMENTO']
#%% Exploracion inicial
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
    
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
#%% Edicion
    for x in range(1,156):
        df = pd.read_excel(rutadoc, sheet_name=x,header=2)
        print(time.strftime("%H:%M:%S"),rutadoc)
        
        if rutadoc == ruta1:
            df = df.drop(df.columns[[9]], axis='columns')
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            facialtissuesdb = facialtissuesdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        
        if rutadoc == ruta2:
            df = df.drop(df.columns[[9]], axis='columns')
            df = df.rename(columns={'FORMA EMPAQUE':'TIPO DE EMPAQUE'})
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            facialtissuesdb = facialtissuesdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
            
        if rutadoc == ruta3:
            df = df.drop(df.columns[[9]], axis='columns')
            df = df.rename(columns={'CANAL':'CANALES'})
            df = df.rename(columns={'PAQUETE':'PAQUETES'})
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            facialtissuesdb = facialtissuesdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
            
        if rutadoc == ruta4:
            df = df.drop(df.columns[[9]], axis='columns')
            df = df.rename(columns={'TIPO DE HOJA':'TIPO HOJA'})
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            facialtissuesdb = facialtissuesdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
            
         #%% fechas merge bd   
#facialtissuesdb.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\facialtissuesdb.csv')            
facialtissuesdb = pd.read_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\facialtissuesdb.csv')

dsfechas = pd.Series(facialtissuesdb['fecha'])
dsfechas = dsfechas.drop_duplicates()
fecha=pd.read_excel(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasfacialt.xlsx') 
fecha = fecha.drop(fecha.columns[[0]], axis='columns')
fecha = fecha.set_index('fecha')
facialtissues = pd.merge(left = facialtissuesdb, right = fecha, left_on='fecha', right_on='fecha')
#facialtissues.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\facialtissuesdb.csv')














