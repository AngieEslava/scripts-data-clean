# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:41:47 2019

@author: usuario
"""


import pandas as pd
import os
import time

tamponesbd = pd.DataFrame()
rutafile = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TAMPONES"
ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TAMPONES\TAMPONES 2010-2012.xlsm"
ruta2 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TAMPONES\TAMPONES 2013.xlsm"
ruta3 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TAMPONES\TAMPONES 2014-2018.xlsm"
ruta4 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\FEMPRO\TAMPONES\TAMPONES ENH.xlsm"

columns1 = ['CANAL', 'TAG', 'CATEGORY', 'MARCAS', 'SUBMARCAS','PRESENTACIONES','TAMANOS TAMPONES', 'SEGMENTO', 'LONG DESCRIPTION']
columns2 = ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCAS','PRESENTACIONES','TAMANOS TAMPONES', 'SEGMENTO', 'LONG DESCRIPTION']

#%%####-----------------Exploracion de archivos-------------------------####
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)

#%%####################  Serie de variables de Base de Datos  #####################################        
    variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)                                 #
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']                      #        
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)                                #
    serie = pd.Series(variablesdf['variable_list'])                                             #
#################################################################################################

#%%--------Edición según el archivo-----------------------   
    for x in range(1,156):#156
        df = pd.read_excel(rutadoc, sheet_name=1,header=2)
        if rutadoc == ruta1:
            names = df.columns.tolist()
            #names[names.index( 'F1.FABRICANTES')] = 'FABRICANTES'
            names[names.index( 'F1.MARCAS')] = 'MARCAS'
            names[names.index( 'F1.SUBMARCAS')] = 'SUBMARCAS'
            names[names.index( 'F1.PRESENTACIONES')] = 'PRESENTACIONES'
            names[names.index( 'F1.TAMANOS TAMPONES')] = 'TAMANOS TAMPONES'
            df.columns = names
            df = df.melt(id_vars=columns1)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            tamponesbd = tamponesbd.append(df)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
        elif rutadoc == ruta2:
            #df = df.drop(df.columns[[3]], axis='columns')
            names = df.columns.tolist()
            names[names.index( 'F1.MARCAS')] = 'MARCAS'
            names[names.index( 'F1.SUBMARCAS')] = 'SUBMARCAS'
            names[names.index( 'F1.PRESENTACIONES')] = 'PRESENTACIONES'
            names[names.index( 'F1.TAMANOS TAMPONES')] = 'TAMANOS TAMPONES'
            df.columns = names
            df = df.melt(id_vars=columns2)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            tamponesbd = tamponesbd.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
            
        elif rutadoc == ruta3:
            #df = df.drop(['LONG DESCRIPTION'], axis=1)
            #df = df.drop(df.columns[[3]], axis='columns')
            df = df.rename(columns={'TIPO TAMPON':'SEGMENTO'})
            df = df.melt(id_vars=columns2)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            tamponesbd = tamponesbd.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)
            
        elif rutadoc == ruta4:
            #df = df.drop(['LONG DESCRIPTION'], axis=1)
            #df = df.drop(df.columns[[3]], axis='columns')
            df = df.rename(columns={'TIPO TAMPON':'SEGMENTO'})
            df = df.melt(id_vars=columns2)
            df = df.rename(columns={'variable':'fecha'})
            df = df.dropna(subset=['CATEGORY'])
            df = df.assign(variable=serie[x])
            tamponesbd = tamponesbd.append(df, sort = False)
            print(x , time.strftime("%H:%M:%S"), rutadoc)

#%%-------- diccionario de fechas--------# 
dsfechas = pd.Series(tamponesbd['fecha'])
dsfechas = dsfechas.drop_duplicates()    
#dsfechas.to_excel(r"C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasTampones.xlsx")        
#--------------------------------------

#%%################################# Merge DB - fechas ####################################################################
fechas = pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\Familia_all\cod_Edicion\fechas\fechasTampones.xlsx")   #   
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']                                                           #
fechas = fechas.drop(['eliminar'], axis=1)                                                                              #    
fechas = fechas.set_index('fecha')                                                                                      #    
tampones = pd.merge(left = tamponesbd, right = fechas, left_on='fecha', right_on='fecha')                               #
#tampones.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\tampones.csv')                    #
#########################################################################################################################
            
        
            