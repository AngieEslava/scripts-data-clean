# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:58:28 2019

@author: usuario
"""

import pandas as pd
import numpy as np

ruta = r"C:\Users\usuario\Documents\Historicos\pib_desestacionalizado_2015_010.xlsx"
#%%leer archivo
df = pd.read_excel(ruta, header=5)
df = df.drop([1,2,3,4,5,6,7,9,10,11])
df.columns = df.iloc[0]
df = df.drop([0])
#%% editar columnas
names = df.columns.tolist()
names[0] = 'fecha'
df.columns = names

#%% Fundir datos
df = pd.melt(df)
df = df.assign(count = 3)
df = df.drop([0])
df = df[df['fecha'] != 'Anual']

#%% Repetir datos para pasar serie trimestral a mensual
dfc = pd.DataFrame(np.repeat(df.values,df['count'].values,axis=0))
dfc.columns = ['fecha', 'pib', 'count']


#%% Asignar fechas
dfc = dfc.assign(fecha = pd.date_range(start='01/01/2005', end='06/01/2019',freq='MS'))
dfc = dfc.drop(['count'], axis = 1)

#%% Exportar archivo
dfc.to_excel(r'C:\Users\usuario\Documents\Historicos\Historico_pib_2005_2019.xlsx')
