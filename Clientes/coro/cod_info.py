# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:25:00 2019

@author: usuario
"""

import pandas as pd
#import numpy as pd

ruta = r"C:\Users\usuario\Documents\BD_custumers\Corona\INFO KAPUA 2015-2019 (1).xlsx"
#%% append de diferentes hojas
datadic=pd.read_excel(ruta, sheet_name = None)
dfull = pd.DataFrame()

for x in range(0,5):
    df = pd.read_excel(ruta,sheet_name = x)
    dfull = dfull.append(df, sort = False)

dfull.to_excel(r"C:\Users\usuario\Documents\BD_custumers\Corona\EntregasCorona\kapuaInfo.xlsx")
