# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:24:15 2019

@author: usuario
"""
#%%
import pandas as pd
import os 
import time

colls=['Centro de coste', 'Descripcion Centro de coste',	'Línea de Producto','Descripcion Linea de Producto','Marca de Producto','Ejercicio/Período']
ruta = r"C:\Users\usuario\Documents\BD_custumers\chocolates\Inversión de Mercadeo Nacional La Especial y Tosh 2013 - 2018 mensualizado.xlsx"
sheets_dict = pd.read_excel(ruta, sheet_name=None)
##Edicion inicial
full_table = pd.DataFrame()
for name, sheet in sheets_dict.items():
    sheet['sheet'] = name
    sheet = sheet.melt(id_vars=colls)  
    sheet = sheet.rename(columns={'variable':'fecha'})
    sheet = sheet[sheet['fecha'] != 'sheet']
    full_table = full_table.append(sheet)
    print('archivo ejecutado', time.strftime("%H:%M:%S"))

#%% Fechas

dsfechas = pd.Series(full_table['fecha'])
dsfechas = dsfechas.drop_duplicates()
#dsfechas.to_excel(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EdicionFechas\fechasPublicidad.xlsx")
fecha = pd.read_excel(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EdicionFechas\fechasPublicidad.xlsx")
fecha.columns = ['eliminar','fecha', 'date']
fecha = fecha.drop(['eliminar'], axis=1)
fecha = fecha.set_index('fecha')


data = pd.merge(left = full_table, right = fecha, left_on='fecha', right_on='fecha')
data.to_csv(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EntregasChocolates\inversionMercadeo.csv")


#%%    
#full_table.to_excel(r"C:\Users\usuario\Desktop\dataPublicidad.xlsx")

