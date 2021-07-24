    # -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:28:20 2019

@author: usuario
"""

import pandas as pd
import os
MyEmptydf = pd.DataFrame()
for y in os.listdir(r"C:\Users\usuario\Documents\1-familia_all\ADULT"):
    y = os.path.join(r"C:\Users\usuario\Documents\1-familia_all\ADULT", y)
    print(y)
    #lista de variables iniciales
    
    df2 = pd.read_excel(y, sheet_name=0,header=2)
    df2.columns = ['eliminar','  Default Report', 'variable_list']
    df2 = df2.drop(['  Default Report'], axis=1)
    serie = pd.Series(df2['variable_list'])
    
    for x in range(1,187):
        df1 = pd.read_excel(y, sheet_name=x,header=2)
        df1 = df1.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCA FAMILIA', 'TAMANOS', 'CONTENIDO ADULTO', 'LONG DESCRIPTION' ]) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        df1 = df1.dropna(subset=['LONG DESCRIPTION'])
        df1 = df1.rename(columns={'variable':'fecha'})
        df1 = df1.assign(variable=serie[x])
        MyEmptydf = MyEmptydf.append(df1)
        print(y)
    #modificación de fechas en el archivo
    dsfechas = pd.Series(MyEmptydf['fecha'])
    dsfechas = dsfechas.drop_duplicates()

#fechaas=dsfechas.to_excel('fechas_descarga.xls')

fechas=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\ADULT_codigo\fechas_excel.xlsx')
fechas.columns = ['eliminar','fecha', 'date_from', 'date_to']
fechas = fechas.drop(['eliminar'], axis=1)
fechas = fechas.set_index('fecha')
adult_familia = pd.merge(left = MyEmptydf, right = fechas, left_on='fecha', right_on='fecha')
#archivo de salida
adult_familia.to_csv(r'C:\Users\usuario\Documents\1-familia_all\ADULT\adult_familia.csv')
