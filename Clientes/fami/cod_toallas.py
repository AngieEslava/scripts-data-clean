# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:50:24 2019
#df = df[df['fecha'] != 'GROSORES']

@author: usuario
"""

import pandas as pd
import os
import time

toallasdb = pd.DataFrame()
rutafile= r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TOALLAS"
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TOALLAS\TOALLAS 2010-2012.xlsm"
ruta2 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TOALLAS\TOALLAS 2013.xlsm"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TOALLAS\TOALLAS 2014-2015.xlsm"
ruta4 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TOALLAS\TOALLAS 2016-2017(JUL).xlsm"
ruta5 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TOALLAS\TOALLAS ENH.xlsm"

cols = ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'C/S ALAS','GROSORES' ,'SUBMARCAS', 'C/S CUBIERTAS', 'SEGMENTO','PRESENTACIONES']

#%%#--------------Exploración archivos------------------------------
for rutadoc in os.listdir(rutafile):
    rutadoc = os.path.join(rutafile, rutadoc)
    print('archivo ejecucion', time.strftime("%H:%M:%S"), rutadoc)
    
#######################  Serie de variables de Base de Datos  ######################################    
    variablesdf = pd.read_excel(rutadoc, sheet_name=0, header=2)                                 #
    print('archivo bierto')                                                                         #
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']                          #
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)                                    #
    serie = pd.Series(variablesdf['variable_list'])                                                 #
####################################################################################################
    
#%%#-------------Edicion según el archivo-------------------------    
    for x in range(1,156):#156
        df = pd.read_excel(rutadoc, sheet_name=x, header=2)
        if rutadoc == ruta1 or rutadoc == ruta2:
            df = df.rename(columns = {'F1.FABRICANTES':'FABRICANTES',
                                      'F1.MARCAS':'MARCAS',
                                      'F1.C/S ALAS':'C/S ALAS',
                                      'F1.GROSORES':'GROSORES',
                                      'F1.SUBMARCAS':'SUBMARCAS',
                                      'F1.C/S CUBIERTAS':'C/S CUBIERTAS',
                                      'F1.PRESENTACIONES':'PRESENTACIONES'})
            df = df.melt(id_vars=cols)
            df = df.rename(columns = {'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            toallasdb = toallasdb.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
        elif rutadoc == ruta3 or rutadoc == ruta4:
            df = df.drop(df.columns[[11]], axis=1)
            df = df.melt(id_vars=cols)
            df = df.rename(columns = {'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            toallasdb = toallasdb.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
        elif rutadoc == ruta5:
            df = df.drop(df.columns[[10]], axis=1)
            df = df.rename(columns = {'SEGMENTOS':'CATEGORY'})
            df = df.assign(SEGMENTO = 'nan')
            df = df.melt(id_vars=cols)
            df = df.rename(columns = {'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            toallasdb = toallasdb.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
##-----------------------------------------------------------------
#%%-------- diccionario de fechas--------#            
    dsfechas = pd.Series(toallasdb['fecha'])
    dsfechas = dsfechas.drop_duplicates()
    #fechas=dsfechas.to_excel(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasToallas.xlsx')
#%%--------------------------------------

fechas=pd.read_excel(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasToallas.xlsx')      #
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']                                                                   #
fechas = fechas.drop(['eliminar'], axis=1)                                                                                      #
fechas = fechas.set_index('fecha')                                                                                              #            
db = pd.merge(left = toallasdb, right = fechas, left_on='fecha', right_on='fecha')                         #
#db.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\toallasH.csv')     #
