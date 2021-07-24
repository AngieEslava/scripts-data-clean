# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:02:45 2019

@author: usuario
"""

import pandas as pd
import xlrd
import openpyxl
import os


#Ruta archivo prueba "C:\Users\usuario\Desktop\INCO MODERADA  SEPT 2017-JUNIO 2019(1).xlsx"
df1 = pd.read_excel(r'C:\Users\usuario\Desktop\INCO MODERADA  SEPT 2017-JUNIO 2019(1).xlsx', sheet_name=1,header=2)
df1 = df1.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCA FAMILIA', 'TAMANOS', 'CONTENIDO ADULTO', 'LONG DESCRIPTION' ], value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
df1 = df1.dropna(subset=['LONG DESCRIPTION'])
df1 = df1.rename(columns={'variable':'fecha'})
df1 = df1.assign(variable='Volume sales in boxes (\'000) - TOTAL COLOMBIA')
#repeticion
df2 = pd.read_excel(r'C:\Users\usuario\Desktop\INCO MODERADA  SEPT 2017-JUNIO 2019(1).xlsx', sheet_name=2,header=2)
df2 = df2.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCA FAMILIA', 'TAMANOS', 'CONTENIDO ADULTO', 'LONG DESCRIPTION' ], value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
df2 = df2.dropna(subset=['LONG DESCRIPTION'])
df2 = df2.rename(columns={'variable':'fecha'})
df2 = df2.assign(variable='Volume sales in boxes (\'000) - SUPERMERCADOS CADENA COLOMBIA')

df3 = pd.read_excel(r'C:\Users\usuario\Desktop\INCO MODERADA  SEPT 2017-JUNIO 2019(1).xlsx', sheet_name=3,header=2)
df3 = df3.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCA FAMILIA', 'TAMANOS', 'CONTENIDO ADULTO', 'LONG DESCRIPTION' ], value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
df3 = df3.dropna(subset=['LONG DESCRIPTION'])
df3 = df3.rename(columns={'variable':'fecha'})
df3 = df3.assign(variable='Volume sales in boxes (\'000) - SUPERMERCADOS INDEPENDIENTES COLOMBIA')

df4 = pd.read_excel(r'C:\Users\usuario\Desktop\INCO MODERADA  SEPT 2017-JUNIO 2019(1).xlsx', sheet_name=4,header=2)
df4 = df4.melt(id_vars=['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'SUBMARCA FAMILIA', 'TAMANOS', 'CONTENIDO ADULTO', 'LONG DESCRIPTION' ], value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
df4 = df4.dropna(subset=['LONG DESCRIPTION'])
df4 = df4.rename(columns={'variable':'fecha'})
df4 = df4.assign(variable='Volume sales in boxes (\'000) - TRADICIONALES COLOMBIA')







        
