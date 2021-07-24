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
        
    consolidadobd = pd.DataFrame()
    for x in range(1,156):#155
        emergentesdf = pd.read_excel(rutaArchivos, sheet_name=x,header=2)
        emergentesdf = emergentesdf.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'CONTEO PANITOS','LONG DESCRIPTION']) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        emergentesdf = emergentesdf.dropna(subset=['LONG DESCRIPTION'])
        emergentesdf = emergentesdf.rename(columns={'variable':'fecha'})
        emergentesdf = emergentesdf.assign(variable=serie[x])
        consolidadobd = consolidadobd.append(emergentesdf)
        print(time.strftime("%H:%M:%S"), x, rutaArchivos)
        
    dsfechasTOALLITAS = pd.Series(consolidadobd['fecha'])
    dsfechasTOALLITAS = dsfechasTOALLITAS.drop_duplicates()
        

for rutaArchivos in os.listdir(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS"):
    rutaArchivos = os.path.join(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS", rutaArchivos)
    print('ruta', time.strftime("%H:%M:%S"), rutaArchivos)
    transform_file(rutaArchivos, )
