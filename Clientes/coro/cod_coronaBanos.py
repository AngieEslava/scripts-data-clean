# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:50:22 2019

@author: usuario
"""

import pandas as pd

rutadoc = r"C:\Users\usuario\Documents\BD_custumers\Corona\Importaciones Baños y Cocinas 2010-2019.xlsx"
df = pd.read_excel(rutadoc)

#%% Edicion inicial

df = df.rename(columns = {'SIC_CAL_VRMILESPESOS':'Value_pesos',
                            'SIC_TOTALCANTIDAD':'Volume_quantity',
                            'SIC_TOTALPESOSNETOENKILOS':'Volume_net_kilograms',
                            'SIC_VALORTOTALCIF':'Value_CIF'})

dfm = pd.melt(df,id_vars = ['SIC_ANO', 'SIC_MES', 'SIC_FECHA','COM_NIT', 'COM_RAZONSOCIAL', 'SIC_CLASE','POS_IDPOSICION','SUB_ID_SUBCATEGORIA','POS_DESCRPCIONARANCELARIA'], value_vars=['Value_pesos','Volume_quantity','Volume_net_kilograms','Value_CIF'])

#%% Concatenar
#dfm = dfm.set_index('fecha')

dfm['fecha'] = dfm['SIC_ANO'].astype(str) + dfm['SIC_MES'].astype(str)
dfm['fecha'] = dfm['fecha'].astype(int)
dsfechas = pd.Series(dfm['fecha'])
dsfechas = dsfechas.drop_duplicates()
#dsfechasg = dsfechas.groupby(['fecha'])
#fechas=dsfechas.to_excel(r'C:\Users\usuario\Documents\BD_custumers\Corona\fechas\fechasBanos.xlsx')
#%% Fechas
fechas=pd.read_excel(r'C:\Users\usuario\Documents\BD_custumers\Corona\fechas\fechasBanos.xlsx')
#fechas = fechas['fecha'].astype(int)        #
fechas.columns = ['eliminar','fecha', 'date']                                                                   #
fechas = fechas.drop(['eliminar'], axis=1)        
                                                                            #
fechas = fechas.set_index('fecha')                                                                                           #            

data_banos = pd.merge(left = dfm, right = fechas, left_on='fecha', right_on='fecha')                         #
data_banos = data_banos.drop(['SIC_ANO'], axis=1)
data_banos = data_banos.drop(['SIC_MES'], axis=1)  
data_banos = data_banos.drop(['fecha'], axis=1) 
data_banos.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Corona\EntregasCorona\data_banos.csv')
