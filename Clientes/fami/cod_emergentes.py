# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:29:09 2019

@author: usuario
"""
#%%  Archivo de prueba
import pandas as pd
import os
import time
emergentesbd = pd.DataFrame()
for rutaEmergentes in os.listdir(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS"):
    rutaEmergentes = os.path.join(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS", rutaEmergentes)
    print('ruta general', time.strftime("%H:%M:%S"), rutaEmergentes)
    
    variablesdf = pd.read_excel(rutaEmergentes, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
    
    for x in range(1,3):#155
        emergentesdf = pd.read_excel(rutaEmergentes, sheet_name=x,header=2)
        emergentesdf = emergentesdf.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'VARIEDADES', 'PRESENTACION','LONG DESCRIPTION']) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        emergentesdf = emergentesdf.dropna(subset=['LONG DESCRIPTION'])
        emergentesdf = emergentesdf.rename(columns={'variable':'fecha'})
        emergentesdf = emergentesdf.assign(variable=serie[x])
        emergentesbd = emergentesbd.append(emergentesdf)
        print(time.strftime("%H:%M:%S"), rutaEmergentes)
        
    dsfechasEmer = pd.Series(emergentesbd['fecha'])
    dsfechasEmer = dsfechasEmer.drop_duplicates()
