# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:06:23 2019

@author: usuario
"""
#%%
import pandas as pd
#import os
import time

col = ['TAG LINEA', 'MARCA', 'SEGMENTOS', 'VARIEDAD']
peanutdb = pd.DataFrame()
rutadoc = r"C:\Users\usuario\Documents\BD_custumers\chocolates\SABANA - DATOS HISTORICOS PASABOCAS.xlsx"
#%%
#####################  Serie de variables de Base de Datos  ###################################################                                                          
variablesdf = pd.read_excel(rutadoc, sheet_name=0,header=2)                                                   #              
print('archivo abierto')                                                                                      #  
variablesdf.columns = ['eliminar','  Default Report', 'variable_list']                                        #  
variablesdf = variablesdf.drop(['  Default Report'], axis=1)                                                  #  
serie = pd.Series(variablesdf['variable_list'])                                                               #  
###############################################################################################################
#%%
##--------Edición según el archivo---------------------
for x in range(1,21):#156
    df = pd.read_excel(rutadoc, sheet_name=x,header=2)
    df = df.melt(id_vars=col)
    print(x , time.strftime("%H:%M:%S"), rutadoc)
    df = df.rename(columns = {'variable':'fecha'})
    df = df.dropna(subset=['MARCA'])
    df = df.assign(variable=serie[x])
    peanutdb = peanutdb.append(df)
    print(x , time.strftime("%H:%M:%S"), rutadoc)
    
#-------- diccionario de fechas--------#
dsfechas = pd.Series(peanutdb['fecha'])
dsfechas = dsfechas.drop_duplicates()
#fechas=dsfechas.to_excel(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EdicionFechas\fechaspeanut.xlsx")
#--------------------------------------#
#%%
################################## Merge DB - fechas #############################################################  
fechas=pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EdicionFechas\fechaspeanut.xlsx")      # 
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']                                                    #   
fechas = fechas.drop(['eliminar'], axis=1)                                                                       #
fechas = fechas.set_index('fecha')                                                                               #
peanut = pd.merge(left = peanutdb, right = fechas, left_on='fecha', right_on='fecha')                            #    
#peanut.to_csv(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EntregasChocolates\SabanaPasabocas.csv")     #
##################################################################################################################
#%%
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(peanut['date_from'], peanut['value'], 'o')
plt.show()

peanut['SEGMENTOS'].describe()
peanut['MARCA'].describe()
peanut['VARIEDAD'].describe()
peanut['TAG LINEA'].describe()

p=peanut.dropna(subset=['value'])
p['value'].describe()
sns.distplot(p['value']);
