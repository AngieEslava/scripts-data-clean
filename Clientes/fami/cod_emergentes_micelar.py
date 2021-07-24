# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:24:44 2019

@author: usuario
"""


import pandas as pd
import os
import time
emergentesbd = pd.DataFrame()
#for rutaEmergentes in os.listdir(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS"):
 #   rutaEmergentes = os.path.join(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS", rutaEmergentes)
  #  print('ruta general', time.strftime("%H:%M:%S"), rutaEmergentes)
    
variablesdf = pd.read_excel(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\AGUA MICELAR JULIO 2014-JUNIO 2019.xls", sheet_name=0,header=2)
variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
variablesdf = variablesdf.drop(['  Default Report'], axis=1)
serie = pd.Series(variablesdf['variable_list'])

for x in range(1,156):#155
    emergentesdf = pd.read_excel(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\AGUA MICELAR JULIO 2014-JUNIO 2019.xls", sheet_name=x,header=2)
    emergentesdf = emergentesdf.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'VARIEDADES', 'PRESENTACION','LONG DESCRIPTION']) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
    emergentesdf = emergentesdf.dropna(subset=['LONG DESCRIPTION'])
    emergentesdf = emergentesdf.rename(columns={'variable':'fecha'})
    emergentesdf = emergentesdf.assign(variable=serie[x])
    emergentesbd = emergentesbd.append(emergentesdf)
    print(time.strftime("%H:%M:%S"), x)
    
dsfechasmice = pd.Series(emergentesbd['fecha'])
dsfechasmice = dsfechasmice.drop_duplicates()
#fechaasMICE=dsfechasmice.to_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_descargaMICE.xlsx')
#%%edicion final
fechaasMICE=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_descargaMICE.xlsx')
fechaasMICE.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechaasMICE = fechaasMICE.drop(['eliminar'], axis=1)
fechaasMICE = fechaasMICE.set_index('fecha')
emergentes_micelar = pd.merge(left = emergentesbd, right = fechaasMICE, left_on='fecha', right_on='fecha')
#emergentes_micelar.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\emergentes_micelar.csv')
