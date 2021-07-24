# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:50:39 2019

@author: usuario
"""

import pandas as pd
import os
import time

filename = r"C:\Users\usuario\Documents\1-familia_all\FEMPRO\JABON INTIMO"        
#rutaArchivos = r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\GELES JULIO 2014-JUNIO 2019.xls"
columns = ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCAS SCA', 'FRAGANCIA', 'PRESENTACION INTIMO', 'LONG DESCRIPTION']
consolidadobd = pd.DataFrame()
#%% exploracion de archivos
for rutaArchivos in os.listdir(filename):
    rutaArchivos = os.path.join(filename, rutaArchivos)
    print('ruta', time.strftime("%H:%M:%S"), rutaArchivos)
    #transform_file(rutaArchivos, columns)
    #%% Capturar variables para asignar a cada hoja del archivo
    variablesdf = pd.read_excel(rutaArchivos, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
        
    #%%edicion interna del archivo
    #consolidadobd = pd.DataFrame()
    for x in range(1,156):#155
        emergentesdf = pd.read_excel(rutaArchivos, sheet_name=x,header=2)
        emergentesdf = emergentesdf.melt(id_vars=columns) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        emergentesdf = emergentesdf.dropna(subset=['LONG DESCRIPTION'])
        emergentesdf = emergentesdf.rename(columns={'variable':'fecha'})
        emergentesdf = emergentesdf.assign(variable=serie[x])
        consolidadobd = consolidadobd.append(emergentesdf)
        print(time.strftime("%H:%M:%S"), x, rutaArchivos)
    dsfechas = pd.Series(consolidadobd['fecha'])#editar fechas
    dsfechas = dsfechas.drop_duplicates()
    #return(consolidadobd, dsfechas)
    #dsfechas.to_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_femsoap.xlsx') 
#%%unir con fechas y exportar    
fechas=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_femsoap.xlsx')
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
femsoap_familia = pd.merge(left = consolidadobd, right = fechas, left_on='fecha', right_on='fecha')
#femsoap_familia.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\femsoap_familia.csv')

#names[names.index('CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'C/S ALAS','GROSORES','SUBMARCAS', 'C/S CUBIERTAS','SEGMENTO', 'PRESENTACIONES')] = 'CANAL', 'TAG', 'CATEGORY', 'F1.FABRICANTES', 'F1.MARCAS', 'F1.C/S ALAS','F1.GROSORES','F1.SUBMARCAS', 'F1.C/S CUBIERTAS','SEGMENTO', 'F1.PRESENTACIONES'
#names[names.index('CANAL', 'TAG', 'CATEGORY', 'F1.FABRICANTES', 'F1.MARCAS', 'F1.C/S ALAS','F1.GROSORES','F1.SUBMARCAS', 'F1.C/S CUBIERTAS','SEGMENTO', 'F1.PRESENTACIONES')] = 'CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'C/S ALAS','GROSORES','SUBMARCAS', 'C/S CUBIERTAS','SEGMENTO', 'PRESENTACIONES'
                   