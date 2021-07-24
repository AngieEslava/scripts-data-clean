# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:02:45 2019

@author: usuario
"""
################################  Archivo prueba  #############################################3
import pandas as pd
import xlrd
import openpyxl
#inco=pd.read_excel(r'C:\Users\usuario\Escritorio\INCO FUERTE SEPT 2017-JUN 2019.xlsx')
incomwb=openpyxl.load_workbook(r'INCO MODERADA  SEPT 2017-JUNIO 2019(1).xlsx')
hojas=incomwb.get_sheet_names()
print(hojas)
print(type(incomwb))

#acceder a una celda de una hoja
unahoja=incomwb.get_sheet_by_name('WSP_TOC')
print(unahoja['C5'].value)

"""#acceder a variasceldas de unahoja
variasceldas= unahoja['C5':'C190']
for row in variasceldas:
    for cell in row:
        print(cell.value)"""
        
#acceder a variasceldas de unahoja
unahoja1=incomwb.get_sheet_by_name('WSP_Sheet1')
df1=pd.DataFrame(unahoja1)
variasceldas= unahoja1['A3':'A52'] 
for row in variasceldas:
    for cell in row:
#incomwb.insert_cols(amount=1)
        ######################################################################################33333