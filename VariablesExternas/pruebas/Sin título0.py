# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:58:40 2019

@author: usuario
"""



import pandas as pd
import os
import time

bdvarfecha = pd.DataFrame()
dfdb = pd.DataFrame()

rutafile = r"C:\Users\usuario\Documents\Noel\Nielsen_Noel"
for rutadoc in os.listdir(rutafile):
    rutadoc= os.path.join(rutafile, rutadoc)
    df = pd.read_excel(rutadoc)
    df.columns = [list(df.iloc[0]), list(df.iloc[1])]
    df = df.drop([0])
    df = df.drop([1])
    dfmelt = pd.melt(df, id_vars=[('var','fecha')])
    dfdb = dfdb.append(dfmelt)
    serie = pd.Series(df.iloc[:, 0])
    serie = serie.to_frame()
    serie = serie.drop_duplicates(subset=('var','fecha'))
    bdvarfecha=bdvarfecha.append(serie)
    bdvarfecha=bdvarfecha.drop_duplicates(subset=('var','fecha'))
    print('archivo ejecutado', time.strftime("%H:%M:%S"), rutadoc)

bdvar = pd.read_excel(r"C:\Users\usuario\Documents\Noel\bdvar.xlsx")
dfbd1= pd.read_csv(r"C:\Users\usuario\Documents\Noel\dfbd.csv")
noel = pd.merge(left = dfbd1, right = bdvar, left_on='var', right_on='var')
