# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:45:59 2019

@author: usuario
"""


import pandas as pd
import os
import time
#%%exploracion de rutas
papelhigienicobd = pd.DataFrame()
rutafile = r"C:\Users\usuario\Documents\1-familia_all\FAMILY\PAPEL HIGIENICO"
columnas= ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTE', 'MARCA', 'SUBMARCA', 'CONTEO', 'TIPO HOJA', 'METROS','SEGMENTO', 'LONG DESCRIPTION']
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)
    
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
   #%% edicion del archivo 
    for x in range(1,156):
        df = pd.read_excel(rutadoc, sheet_name=x,header=2)
        df = df.melt(id_vars=columnas)
        df = df.dropna(subset=['CATEGORY'])
        df = df.rename(columns={'variable':'fecha'})
        df = df.assign(variable=serie[x])
        papelhigienicobd = papelhigienicobd.append(df)
        print(x , time.strftime("%H:%M:%S"),rutadoc)
        
 #%%fechas y merge       
dsfechasww = pd.Series(papelhigienicobd['fecha'])
dsfechasww = dsfechasww.drop_duplicates()
#fechaww=dsfechasww.to_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_papelhigienico.xlsx')

#papelhigienicobd.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\papelHigienicoR.csv')

    
fechas=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_PROTECTORES.xlsx')
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
papelhigienico_familia = pd.merge(left = papelhigienicobd, right = fechas, left_on='fecha', right_on='fecha')
#papelhigienico_familia.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\papelHigienico.csv')
