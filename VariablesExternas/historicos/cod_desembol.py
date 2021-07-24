# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:31:14 2019

@author: usuario
"""

import pandas as pd

ruta = r"C:\Users\usuario\Documents\Historicos\desembol_resumen.xlsx"
df = pd.read_excel(ruta)

#%%concatenar columnas para fechas
dfm = pd.melt(df, id_vars=['year', 'modalidad'])
dfm['fecha'] = dfm['year'].astype(str) + dfm['variable']
dsfechas = pd.Series(dfm['fecha'])
dsfechas = dsfechas.drop_duplicates()    
#dsfechas.to_excel(r"C:\Users\usuario\Documents\Historicos\fechas\fechasDesemb1.xlsx")        

#%%################################# Merge DB - fechas ####################################################################
fechas = pd.read_excel(r"C:\Users\usuario\Documents\Historicos\fechas\fechasDesemb1.xlsx")   #   
fechas.columns = ['eliminar','fecha', 'date']                                                           #
fechas = fechas.drop(['eliminar'], axis=1)                                                                              #    
fechas = fechas.set_index('fecha')   
                                                                                   #    
data = pd.merge(left = dfm, right = fechas, left_on='fecha', right_on='fecha')  
data = data.drop(['year','variable','fecha'], axis=1)  
data.to_excel(r"C:\Users\usuario\Documents\Historicos\desembol_editado.xlsx")


