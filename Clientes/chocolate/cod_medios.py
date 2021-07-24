# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:07:57 2019

@author: usuario
"""
#%%lectura de archivos
import pandas as pd

ruta = r"C:\Users\usuario\Documents\BD_custumers\chocolates\SOV-SOI Pasabocas 2015-2019 (Sep 19)  Mensual.xlsx"
sheets_dict = pd.read_excel(ruta, sheet_name=None, header=4)
sheet = pd.read_excel(ruta, sheet_name=None, header=4)

#%%ciclo edicion de archivo por cada hoja
full_table = pd.DataFrame()
for name, sheet in sheets_dict.items():
        
    sheet.columns = [list(sheet.iloc[0]), list(sheet.iloc[1])]
    sheet = sheet.drop([0])
    sheet = sheet.drop([1])
    df = pd.melt(sheet, id_vars=[('medios','pasabocas')])
    df.columns = ['pasabocas','variable_0','variable_1','value'] 
    df['sheet'] = name
    df = df.rename(columns=lambda x: x.split('\n')[-1])
    
    full_table = full_table.append(df)

#%%edicion de fechas
dsfechas = pd.Series(full_table['sheet'])
dsfechas = dsfechas.drop_duplicates()
dsfechas = dsfechas.to_frame()    
dsfechas = dsfechas.assign(date_from = pd.date_range(start='01/01/2015', end='09/01/2019',freq='MS'))
dsfechas = dsfechas.assign(date_to = pd.date_range(start='01/31/2015', end='09/30/2019',freq='M'))

#%%edicion de archivo final y exportar
full_tablef = full_table[full_table['pasabocas'] != 'Grand Total' ]
full_tablef = full_tablef[full_tablef['pasabocas'] != 'Total'  ]
full_tablef = full_tablef[full_tablef['pasabocas'] != 'Gran Total'  ]
full_tablef = full_tablef.dropna(subset=['pasabocas'])

data = pd.merge(left = full_tablef, right = dsfechas, left_on='sheet', right_on='sheet')
data.to_csv(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EntregasChocolates\pasabocas.csv")
#pasabocas = full_tablef.drop_duplicates('pasabocas')

#dsfechas.to_excel(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EdicionFechas\fechasPasabocas.xlsx")


#full_table.to_excel(r"C:\Users\usuario\Documents\BD_custumers\chocolates\EntregasChocolates\pasabocas.xlsx")

print(full_table)