# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 02:12:00 2019

@author: ANGIE ESLAVA
"""

#import openpyxl
import pandas as pd
import numpy as np
from datetime import datetime
inicio = datetime.today()
#from openpyxl import load_workbook
#import ExcelWriter as writer

#Edición de query maximos y mínimos
maxmin = pd.read_excel(r'C:\Users\ANGIE ESLAVA\Desktop\Todo_Proyecto_mIC\EntregaMIC\Agotados24052019\Query maximos y minimos.xlsx')
df1 = pd.DataFrame(maxmin)
df1['CODALMACEN']=df1['CODALMACEN'].astype(str)
df1 = df1.assign(SKU = 1)
df1 = df1.assign(dispo = df1['STOCK'] + df1['ENTRANSITO'])
df1 = df1.assign(Formula = df1['MINIMO'] - df1['dispo'])

df1['CEROS'] = df1['STOCK'].apply(lambda x: 1 if x == 0 else 0)
df1.loc [df1.Formula < 0 , 'faltante'] = 0   
df1.loc [df1.Formula >= 0 , 'faltante'] = df1.assign(faltante = df1['MINIMO'] - df1['dispo'])

#Edición de Maestra de Almacenes
malmacen = pd.read_excel(r'C:\Users\ANGIE ESLAVA\Desktop\Todo_Proyecto_mIC\EntregaMIC\Agotados24052019\MAESTRA DE ALMACENES.xlsx', sheel = 'Hoja 1')
df2 = pd.DataFrame(malmacen).drop(malmacen.columns[[20]], axis='columns')
#titulos COLUMNAS CON DATOS DE OTRA FILA
df2.columns = df2.iloc[0]
df2.drop([0], inplace = True)
print(df2.head())
#CAMBIAR NOMBRE DE UNA COLUMNA 
names = df2.columns.tolist()
names[names.index('ID')] = 'CODALMACEN'
df2.columns = names
#FILTRAR QUITANDO UNA INFO
df2_filtro = df2[df2['FORMATO'] != 'OUTLET' ]

#Edición Portafolio MIC
portafoliomic = pd.read_excel(r'C:\Users\ANGIE ESLAVA\Desktop\Todo_Proyecto_mIC\EntregaMIC\Agotados24052019\Portafolio MIC 20052019.xlsx',sheet_name="Datos sku")
df4 = pd.DataFrame(portafoliomic)
#CAMBIAR NOMBRE DE UNA COLUMNA 
names = df4.columns.tolist()
names[names.index('CodRef')] = 'REFPROVEEDOR'
names[names.index('CodTalla')] = 'TALLA'
#names[names.index('CodColor')] = 'COLOR'
df4.columns = names
#fILTRAR INFORMACIÓN DE UNA COLUMNA
df4_filtro = df4[df4['CLAS MTA'] == 'MTA' ]

#Edicion de Maestra de Parametrización
mparametrizacion = pd.read_excel(r'C:\Users\ANGIE ESLAVA\Desktop\Todo_Proyecto_mIC\EntregaMIC\Agotados24052019\MAESTRA PARAMETRIZACION.xlsx',sheet_name="PARAMETRIZACION")
df3 = pd.DataFrame(mparametrizacion).drop([0])
#titulos COLUMNAS CON DATOS DE OTRA FILA
df3.columns = df3.iloc[0]
df3.drop([1], inplace = True)
print(df3.head())
names = df3.columns.tolist()
names[names.index('REFERENCIA')] = 'REFPROVEEDOR'
df3.columns = names
#fILTRAR INFORMACIÓN DE UNA COLUMNA
df3_filtro = df3[df3['GRUPO'] == 'TEXTIL' ]

##Buscarv: con maestra de almacenes
df2_filtro['CODALMACEN']=df2_filtro['CODALMACEN'].astype(str)
BValmacen = pd.merge(left = df1, right = df2_filtro, left_on='CODALMACEN', right_on='CODALMACEN')

##Buscarv: con maestra de parametrizacion
BVparametrizacion = pd.merge(left = BValmacen, right = df3_filtro, left_on='REFPROVEEDOR', right_on='REFPROVEEDOR')

##Buscarv: con portafolio
df4_filtro['REFPROVEEDOR']=df4_filtro['REFPROVEEDOR'].astype(str)
#df4_filtro['COLOR']=df4_filtro['COLOR'].astype(str)
BVportaf = pd.merge(left = BVparametrizacion, right = df4_filtro, how = 'inner', on=['REFPROVEEDOR', 'TALLA'])

#tabla dinamica1 para tabla datos por referencia
pivotagotados1 = BVportaf.pivot_table(index = ['MARCA_x','TOP DEMANDA X VOLUMEN', 'REFPROVEEDOR'], values = ['STOCK', 'MINIMO', 'ENTRANSITO', 'SKU', 'CEROS', 'Inv 100\nBodega FS', 'Tránsitos'], aggfunc = np.sum)
tablaagotados1 = pd.DataFrame(pivotagotados1)
tablaagotados1 = tablaagotados1.assign(AGOTADOS = tablaagotados1['CEROS'] / tablaagotados1['SKU']*100)
tablaagotados1.to_excel (r'C:\Users\ANGIE ESLAVA\Desktop\Todo_Proyecto_mIC\EntregaMIC\Agotados24052019\TablaAgotados.xlsx', header = True, index = True, sheet_name = 'Agotados')


#tabla dinamica1 para tabla datos por referencia
pivot1 = BVportaf.pivot_table(index = ['REFPROVEEDOR', 'TALLA', 'COLOR'], values = ['STOCK', 'MINIMO', 'ENTRANSITO', 'SKU', 'CEROS'], aggfunc = np.sum)
tabla1 = pd.DataFrame(pivot1)
tabla1 = tabla1.assign(AGOTADOS = tabla1['CEROS'] / tabla1['SKU']*100)
tabla1 = pd.DataFrame(tabla1).reset_index()
tabla1['COLOR']=tabla1['COLOR'].astype(str)
tabla1['concatabla1'] = np.where(((tabla1['REFPROVEEDOR']== '93107461') | ((tabla1['REFPROVEEDOR']== '93108650'))), tabla1['REFPROVEEDOR']+tabla1['TALLA']+tabla1['COLOR'], tabla1['REFPROVEEDOR']+ tabla1['TALLA'])

#Transformación inventario100
inv100 = pd.read_excel(r'C:\Users\ANGIE ESLAVA\Desktop\Todo_Proyecto_mIC\EntregaMIC\Agotados24052019\b100.xlsx')
dfinv100 = pd.DataFrame(inv100)
dfinv100['concatinv100'] = np.where(((dfinv100['Referencia']== '93107461') | ((dfinv100['Referencia']== '93108650'))), dfinv100['Referencia']+dfinv100['Desc. detalle ext. 2']+dfinv100['Desc. detalle ext. 1'], dfinv100['Referencia']+ dfinv100['Desc. detalle ext. 2']) #& np.where(tabla1['REFPROVEEDOR']=='93108650',tabla1['REFPROVEEDOR']+tabla1['TALLA']+tabla1['COLOR'],tabla1['REFPROVEEDOR']+tabla1['TALLA'])   #, tabla1['REFPROVEEDOR']+tabla1['TALLA']+tabla1['COLOR'],tabla1['REFPROVEEDOR']+tabla1['TALLA'])
dfinv100 = pd.DataFrame(dfinv100).reset_index()#.drop(dfinv100.columns[[0]], axis='columns')
dfinv100 = pd.DataFrame(dfinv100).drop(dfinv100.columns[[0]], axis='columns')

#Transformación wip
wip = pd.read_excel(r'C:\Users\ANGIE ESLAVA\Desktop\Todo_Proyecto_mIC\EntregaMIC\Agotados24052019\Copia de WIP Tod.xlsm',sheet_name="PROCESOFINAL")
dfwip = pd.DataFrame(wip)
dfwip['CDPRNDA']=dfwip['CDPRNDA'].astype(str)
pivotwip = dfwip.pivot_table(index = ['CDPRNDA','CDTLLA', 'CDCLOR'], values = ['FALTANTEREAL'], aggfunc = np.sum)
pivotwip = pd.DataFrame(pivotwip).reset_index()
pivotwip['CDCLOR']=dfwip['CDCLOR'].astype(str)
pivotwip['concawip'] = np.where(((pivotwip['CDPRNDA']== '93107461') | ((pivotwip['CDPRNDA']== '93108650'))), pivotwip['CDPRNDA']+pivotwip['CDTLLA']+pivotwip['CDCLOR'], pivotwip['CDPRNDA']+pivotwip['CDTLLA']) #& np.where(tabla1['REFPROVEEDOR']=='93108650',tabla1['REFPROVEEDOR']+tabla1['TALLA']+tabla1['COLOR'],tabla1['REFPROVEEDOR']+tabla1['TALLA'])   #, tabla1['REFPROVEEDOR']+tabla1['TALLA']+tabla1['COLOR'],tabla1['REFPROVEEDOR']+tabla1['TALLA'])

##Buscarv: con inventario bodega 100
BVinv100 = pd.merge(left = tabla1, right = dfinv100, left_on='concatabla1', right_on='concatinv100')

BVwip = pd.merge(left = BVinv100, right = pivotwip, left_on='concatabla1', right_on='concawip')

###_________probar otra idea: primero cargar los datos inv100 y wip__ segun concatenados
###_________y despues unirlos a una base de datos unificada__ segun refproveedor

#tabla dinamica2 para tabla datos por codalmacen
pivot2 = BVportaf.pivot_table(index = ['CODALMACEN','REFPROVEEDOR'], values = ['STOCK', 'MINIMO', 'ENTRANSITO', 'SKU', 'CEROS'], aggfunc = np.sum)
tabla2 = pd.DataFrame(pivot2)
tabla2 = pd.DataFrame(tabla2 ).reset_index()

##Buscarv: con MAESTRA DE ALMACENES
BValm = pd.merge(left = tabla2, right = df2_filtro, left_on='CODALMACEN', right_on='CODALMACEN')
BValm = BValm.assign(AGOTADOS = BValm['CEROS'] / BValm['SKU']*100)
##tABLA DE AGOTADOSXCODALMACEN
pivot_almacenes = BValm.pivot_table(index = ['ZONA','RANKING VTA','CODALMACEN','TIENDAS II'], values = ['STOCK', 'MINIMO', 'ENTRANSITO','SKU', 'CEROS'], aggfunc = np.sum)
tabla_almacenes = pd.DataFrame(pivot_almacenes)
tabla_almacenes = tabla_almacenes.assign(AGOTADOS = tabla_almacenes['CEROS'] / tabla_almacenes['SKU']*100)



#tabla dinamica AGOTADOSXREFPROVEEDOR
#pivot = BVwip.pivot_table(index = ['TOP DEMANDA X VOLUMEN', 'MARCA_x', 'REFPROVEEDOR'], values = ['STOCK', 'MINIMO', 'ENTRANSITO', 'SKU', 'CEROS'], aggfunc = np.sum)
#tabla1_2 = pd.DataFrame(pivot)
#tabla1_2 = tabla1.assign(AGOTADOS = tabla1['CEROS'] / tabla1['SKU']*100)


#tabla1.to_excel (r'C:\Users\ANGIE ESLAVA\Desktop\EntregaMIC\TablaAgotados.xlsx', header = True, index = True, sheet_name = 'Agotados')
#BVportaf.to_excel (r'C:\Users\ANGIE ESLAVA\Desktop\EntregaMIC\BasedeDatos.xlsx', header = True, index = True, sheet_name = 'BasedeDatos')

fin = datetime.today()

print(fin - inicio)
#with ExcelWriter(r'C:\Users\ANGIE ESLAVA\Desktop\tabla1.xlsx') as writer:
#writer = pd.ExcelWriter(r'C:\Users\ANGIE ESLAVA\Desktop\tabla1.xlsx') 
    #tabla1.to_excel(writer, sheet_name='Sheet1')
    #BVportaf.to_excel(writer, sheet_name='Sheet2')

#writer = pd.ExcelWriter(r'C:\Users\ANGIE ESLAVA\Desktop\tabla1.xlsx',engine='xlsxwriter')   # Creating Excel Writer Object from Pandas  
#workbook=writer.book
#tabla1.to_excel(writer,sheet_name='Sheet1',startrow=0 , startcol=0)   
#BVportaf.to_excel(writer,sheet_name='Sheet2',startrow=20, startcol=0) 

#tabla dinamica
#pivot = BVportaf.pivot_table (index = ['TOP DEMANDA X VOLUMEN', 'REFPROVEEDOR'], values = ['STOCK', 'MINIMO', 'ENTRANSITO', 'Inv 100\nBodega FS', 'Tránsitos'], aggfunc = 'sum')
#Documento final de excel
#export_excelBVportaf = BVportaf.to_excel (r'C:\Users\ANGIE ESLAVA\Desktop\BVportaf.xlsx', header = True)
#export_excelBVparametrizacion = BVparametrizacion.to_excel (r'C:\Users\ANGIE ESLAVA\Desktop\BVparametrizacion.xlsx', header = True)
