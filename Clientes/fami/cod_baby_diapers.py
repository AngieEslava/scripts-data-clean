# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:54:14 2019

@author: usuario
"""

import pandas as pd
import os
import time
#time.strftime("%H:%M:%S")
babydiapersbd = pd.DataFrame()
for rutaDiapers in os.listdir(r"C:\Users\usuario\Documents\1-familia_all\BABY\PAÑALES"):
    rutaDiapers = os.path.join(r"C:\Users\usuario\Documents\1-familia_all\BABY\PAÑALES", rutaDiapers)
    print("ruta archivo", time.strftime("%H:%M:%S"), rutaDiapers)


#%%##################################  Serie de variables de Base de Datos  ########################################################  
    #babydiapers=pd.read_excel(r"C:\Users\usuario\Documents\1-familia_all\BABY\PAÑALES\PAÑALES 2013-2017.xlsm")
    variablesdf = pd.read_excel(r"C:\Users\usuario\Documents\1-familia_all\BABY\PAÑALES\PAÑALES 2017-2019.xlsm", sheet_name=0,header=2)     #
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']                                                                  #
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)                                                                             #   
    serie = pd.Series(variablesdf['variable_list'])                                                                                          #       
#%%#############################################################################################################################################  
    
    for x in range(1,187):
        babydiapersdf = pd.read_excel(r"C:\Users\usuario\Documents\1-familia_all\BABY\PAÑALES\PAÑALES 2017-2019.xlsm", sheet_name=x,header=2)
        babydiapersdf = babydiapersdf.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'ETAPAS / TAMANOS', 'CONTENIDO', 'LONG DESCRIPTION', 'SEGMENTO' ]) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        babydiapersdf = babydiapersdf.rename(columns={'variable':'fecha'})  
        babydiapersdf = babydiapersdf.assign(variable=serie[x])          
        babydiapersbd = babydiapersbd.append(babydiapersdf)
        print(time.strftime("%H:%M:%S"), x)
        
    dsfechasbb13 = pd.Series(babydiapersbd['fecha'])
    dsfechasbb13 = dsfechasbb13.drop_duplicates()
    #fechaxl=dsfechasbb13.to_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_baby2017.xlsx')
    
fechas=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_baby2017.xlsx')
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
babydiapers_familia = pd.merge(left = babydiapersbd, right = fechas, left_on='fecha', right_on='fecha')
#%%babydiapers_familia.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\baby_diapers_2017-2019.csv')
