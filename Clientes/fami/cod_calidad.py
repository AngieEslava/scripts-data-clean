# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:58:36 2019

@author: usuario
"""
#%%######################################## Archivo Prueba ###############################################
import pandas as pd

dfa = pd.read_csv(r"C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\adult_familia.csv")

df = pd.DataFrame()
df1 = pd.read_csv(r"C:\Users\usuario\Documents\PAÑALESDB\baby_diapers_2010-2012.csv")
df2 = pd.read_csv(r"C:\Users\usuario\Documents\PAÑALESDB\baby_diapers_2013-2017.csv")
df3 = pd.read_csv(r"C:\Users\usuario\Documents\PAÑALESDB\baby_diapers_2017-2019.csv")
names1 = df1.columns.tolist()
names2 = df2.columns.tolist()
names3 = df3.columns.tolist()

df = df.append(df1)
df = df.append(df2)
df = df.append(df3)

df.to_csv(r'C:\Users\usuario\Documents\BD_custumers\Familia_all\EntregasFamilia\babyDiapers.csv')
#%%###############################################################################################################