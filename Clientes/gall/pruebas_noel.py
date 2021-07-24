# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:10:46 2019

@author: usuario
"""


import pandas as pd

df = pd.read_excel(r"C:\Users\usuario\Documents\Noel\Nielsen_Noel\ON13-ON16.xlsx", sheet_name='Sheet1' )
#%%columnas multi-index en df 
df.columns = [list(df.iloc[0]), list(df.iloc[1])]
df = df.drop([0])
df = df.drop([1])

#%%dividir texto separado por comas
dfcol1 = df[('var','fecha')].str.split(',', n = 6, expand = True)
serie = pd.Series(df[('var','fecha')])
serie = serie.drop_duplicates()
#serie.to_excel(r'C:\Users\usuario\Documents\Noel\segmentonoel.xlsx')


names = dfcol1.columns.tolist()
names[names.index(0)] = 'producto'
names[names.index(1)] = 'tamanos'
names[names.index(2)] = 'sabores'
names[names.index(3)] = 'presentacion'
names[names.index(4)] = 'cte'
names[names.index(5)] = 'fabricante'
names[names.index(6)] = 'size'
dfcol1.columns = names
dfcol1=dfcol1.drop_duplicates(subset='producto')
#dfcol1.to_excel(r'C:\Users\usuario\Documents\Noel\segmentonoel2.xlsx')


dfcol2 = dfcol1[('producto')].str.split(' ', n = 1, expand = True)
names = dfcol2.columns.tolist()
names[names.index(0)] = 'total'
names[names.index(1)] = 'producto'
dfcol2.columns = names
dfcol2=dfcol2.drop_duplicates()
#dfcol2.to_excel(r'C:\Users\usuario\Documents\Noel\segmentonoel2.xlsx')

#%%para segmentar
dfseg = pd.read_excel(r"C:\Users\usuario\Documents\Noel\db_kantar\DB_KANTAR - copia1.xlsx")
dfseg1=dfseg.drop_duplicates(subset='producto')
dfseg2=dfseg.drop_duplicates(subset='fabricante')
dfseg3=dfseg.drop_duplicates(subset='segmento')


dfmerge=pd.merge(left = dfcol1, right = dfseg, left_on='producto', right_on='producto')




