# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:47:05 2019

@author: usuario
"""

import pandas as pd
import os
import time

    
def transform_file(rutaArchivos, columns):    
    variablesdf = pd.read_excel(rutaArchivos, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
    
    consolidado_df = pd.DataFrame()
    
    for x in range(1,3):#155
        emergentesdf = pd.read_excel(rutaArchivos, sheet_name=x,header=2)
        emergentesdf = emergentesdf.melt(id_vars=columns) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        emergentesdf = emergentesdf.dropna(subset=['LONG DESCRIPTION'])
        emergentesdf = emergentesdf.rename(columns={'variable':'fecha'})
        emergentesdf = emergentesdf.assign(variable=serie[x])
        consolidado_df = consolidado_df.append(emergentesdf)
        print(time.strftime("%H:%M:%S"), x, rutaArchivos)
        
    dsfechas = pd.Series(consolidado_df['fecha'])
    dsfechas = dsfechas.drop_duplicates()
    return consolidado_df
    
consolidadobd = pd.DataFrame()
filename = r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\JABON INTIMO"        
#rutaArchivos = r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\GELES JULIO 2014-JUNIO 2019.xls"
columns = ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCAS SCA', 'FRAGANCIA', 'PRESENTACION INTIMO', 'LONG DESCRIPTION']

for rutaArchivos in os.listdir(filename):
    rutaArchivos = os.path.join(filename, rutaArchivos)
    print('ruta', time.strftime("%H:%M:%S"), rutaArchivos)
    consolidadobd = consolidadobd.append(transform_file(rutaArchivos, columns))
    fechas = transform_file(rutaArchivos, columns)