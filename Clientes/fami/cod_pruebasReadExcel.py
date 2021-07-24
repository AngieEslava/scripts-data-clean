# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:57:04 2019

@author: usuario
"""
#%%leer el archivo
import pandas as pd

ruta1 = r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EMERGENTES\TOALLITAS DESMAQUILLADORAS\TOALLITAS DESMAQUILLADORAS AGO 2017-JUN 2019.xls"
sheets_dict = pd.read_excel(ruta1, sheet_name=None, header=2)

#%%crear df vacio para adjuntar todas las hojas
full_table = pd.DataFrame()

#%% For sobre un diccionario de objetos
for name, sheet, index in sheets_dict.items():
    if index == 0:
        break

    sheet['sheet'] = name
    sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
    
    """
    sheet = sheet.rename(columns = {'F1.FABRICANTES':'FABRICANTES',
                                      'F1.MARCAS':'MARCAS',
                                      'F1.C/S ALAS':'C/S ALAS',
                                      'F1.GROSORES':'GROSORES',
                                      'F1.SUBMARCAS':'SUBMARCAS',
                                      'F1.C/S CUBIERTAS':'C/S CUBIERTAS',
                                      'F1.PRESENTACIONES':'PRESENTACIONES'})
    """
    print('rename')
    full_table = full_table.append(sheet)#llenar tabla con cada ciclo for


full_table.reset_index(inplace=True, drop=True)

print(full_table)