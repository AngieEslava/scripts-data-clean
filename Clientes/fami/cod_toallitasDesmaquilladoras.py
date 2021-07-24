# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:34:09 2019

@author: usuario
"""

import pandas as pd 
import os
import time

desmaquillantesdb = pd.DataFrame()
rutafile = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EMERGENTES\TOALLITAS DESMAQUILLADORAS"
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EMERGENTES\TOALLITAS DESMAQUILLADORAS\TOALLITAS DESMAQUILLADORAS AGO 2017-JUN 2019.xls"
ruta2 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EMERGENTES\TOALLITAS DESMAQUILLADORAS\TOALLITAS DESMAQUILLADORAS EF 2010-SO 2012.xls"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EMERGENTES\TOALLITAS DESMAQUILLADORAS\TOALLITAS DESMAQUILLADORAS MARZO 2015-SEPT 2017.xls"
ruta4 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EMERGENTES\TOALLITAS DESMAQUILLADORAS\TOALLITAS DESMAQUILLADORAS ND 2012-FEB 2015.xls"

col1 = ['CANAL',	'TAG',	'CATEGORY',	'FABRICANTES',	'MARCAS',	'CONTEOPANITOS',	'LONG DESCRIPTION']

#%%#-----------Exploracion de archivos---------------------------
for rutadoc in os.listdir(rutafile):
    rutadoc = os.path.join(rutafile,rutadoc)
    print("ruta archivo", time.strftime("%H:%M:%S"), rutadoc)
    
    
#####################  Serie de variables de Base de Datos  #####################################      
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)                                 #
    print('archivo abierto')                                                                    #
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']                      #
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)                                #
    serie = pd.Series(variablesdf['variable_list'])                                             #
################################################################################################

#%%#--------Edición según el archivo----------------------    
    for x in range(1,156):#156
        df = pd.read_excel(rutadoc, sheet_name=x,header=2)
        if rutadoc == ruta1 or rutadoc == ruta3:
            df = df.rename(columns = {'CONTEO PANITOS':'CONTEOPANITOS'})
            df = df.melt(id_vars=col1)
            df = df.rename(columns = {'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            desmaquillantesdb = desmaquillantesdb.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)            
        elif rutadoc == ruta2 or rutadoc == ruta4:
            df = df.rename(columns = {'F2.CATEGORY':'CATEGORY'})
            df = df.rename(columns = {'F2.FABRICANTES':'FABRICANTES'})
            df = df.rename(columns = {'F2.MARCAS':'MARCAS'}) 
            df = df.assign(CONTEOPANITOS = 'nan')            
            df = df.melt(id_vars=col1)
            df = df.rename(columns = {'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            desmaquillantesdb = desmaquillantesdb.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)

#%%-------- diccionario de fechas--------#            
    dsfechas = pd.Series(desmaquillantesdb['fecha'])
    dsfechas = dsfechas.drop_duplicates()
    #fechas=dsfechas.to_excel(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasDesmaquillantes.xlsx')
#--------------------------------------
    
#%%################################# Merge DB - fechas #############################################################################      
fechas=pd.read_excel(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasDesmaquillantes.xlsx')      #
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']                                                                   #
fechas = fechas.drop(['eliminar'], axis=1)                                                                                      #
fechas = fechas.set_index('fecha')                                                                                              #            
desmaquillantes = pd.merge(left = desmaquillantesdb, right = fechas, left_on='fecha', right_on='fecha')                         #
#desmaquillantes.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\toallitasDesmaquillantes.csv')     #
##################################################################################################################################