# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:20:05 2019

@author: usuario
"""

import pandas as pd
import os 
import time

napkinsdb = pd.DataFrame()
rutafile = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\SERVILLETAS"
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\SERVILLETAS\SV 2010(AM) 2011(JJ).xls"
ruta2 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\SERVILLETAS\SV 2011(AS) 2014(JJ).xls"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\SERVILLETAS\SV 2014(AGO) 2017 (JUL).xls"
ruta4 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FAMILY\SERVILLETAS\SV 2017 (AGO) 2019 (JUL).xls"
columns = ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTE', 'MARCA', 'VARIEDAD', 'CONTEO', 'LEVEL', 'SEGMENTO']

#%%Exploracion
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)

#%%    Seleccion de variables
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])

#%%Edicion de archivo
    for x in range(1,156):
        df = pd.read_excel(rutadoc, sheet_name=x,header=2)
        
        if rutadoc==ruta1:
            df = df.rename(columns={'CANALES':'CANAL'})
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            napkinsdb = napkinsdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        
        if rutadoc==ruta2:
            df = df.drop(df.columns[[9]], axis='columns')
            df = df.rename(columns={'SUBMARCA':'VARIEDAD'})
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            napkinsdb = napkinsdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        
        if rutadoc==ruta3:
            df = df.drop(df.columns[[8]], axis='columns')
            df = df.rename(columns={'NIVEL':'LEVEL'})
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            napkinsdb = napkinsdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
        
        if rutadoc==ruta4:
            df = df.drop(df.columns[[9]], axis='columns')
            df = df.rename(columns={'CONTEP':'CONTEO'})
            df = df.rename(columns={'Unnamed: 8':'SEGMENTO'})
            df = df.melt(id_vars=columns)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            napkinsdb = napkinsdb.append(df)
            print(x , time.strftime("%H:%M:%S"),rutadoc)
            
#%%          Fechas  
dsfechas = pd.Series(napkinsdb['fecha'])
dsfechas = dsfechas.drop_duplicates()      
#fecha=dsfechas.to_excel(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasNapkins.xlsx') 

#%% correccion fechas napkins
fechas=pd.read_excel(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasNapkins.xlsx')
napkinsdata=pd.read_csv(r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\napkins.csv")
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')

napkinsdata = napkinsdata.drop(['date_from'], axis=1)
napkinsdata = napkinsdata.drop(['date_to'], axis=1)

napkins = pd.merge(left = napkinsdata, right = fechas, left_on='fecha', right_on='fecha')
napkins.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\napkins.csv')
