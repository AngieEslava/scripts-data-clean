# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:29:48 2019

@author: usuario
"""

import pandas as pd
import os
import time
#%% Exploracion 
wetwipesbd = pd.DataFrame()
for rutaWetwipes in os.listdir(r"C:\Users\usuario\Documents\1-familia_all\FAMILY\FRAGANCIAS"):
    rutaWetwipes = os.path.join(r"C:\Users\usuario\Documents\1-familia_all\FAMILY\FRAGANCIAS", rutaWetwipes)
    print('ruta general', time.strftime("%H:%M:%S"), rutaWetwipes)
#variables-----------------------------    
    variablesdf = pd.read_excel(rutaWetwipes, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
#Edicion------------------------------    
    for x in range(1,3):
        wetWipesdf = pd.read_excel(rutaWetwipes, sheet_name=x,header=2)
        wetWipesdf = wetWipesdf.melt(id_vars=['CANAL', 'TAG', 'CATEGORIA', 'FABRICANTES', 'MARCAS', 'SUBMARCA', 'VARIEDAD', 'TAMANOS','LONG DESCRIPTION' ,'SEGMENTO' ]) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        wetWipesdf = wetWipesdf.dropna(subset=['LONG DESCRIPTION'])
        wetWipesdf = wetWipesdf.rename(columns={'variable':'fecha'})
        wetWipesdf = wetWipesdf.assign(variable=serie[x])
        wetwipesbd = wetwipesbd.append(wetWipesdf)
        print(time.strftime("%H:%M:%S"), rutaWetwipes)
        
    dsfechasww = pd.Series(wetwipesbd['fecha'])
    dsfechasww = dsfechasww.drop_duplicates()
    #fechaww=dsfechasww.to_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_babyww.xlsx')
#%%fechas y merge    
fechas=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_babyww.xlsx')
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
babywetwipes_familia = pd.merge(left = wetwipesbd, right = fechas, left_on='fecha', right_on='fecha')
babywetwipes_familia.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\baby_wetwipes.csv')

print(wetWipesdf.columns)
columnas = input("ingrese las columnas: ")

dato = input("Ingresa un dato: ")
print("Has insertado ", dato)
