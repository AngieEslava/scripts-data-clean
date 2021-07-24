import pandas as pd
import os
import time

#for rutaEmergentes in os.listdir(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS"):
 #   rutaEmergentes = os.path.join(r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\TOALLITAS", rutaEmergentes)
  #  print('ruta general', time.strftime("%H:%M:%S"), rutaEmergentes)

def transform_file(filename, columns):
    variablesdf = pd.read_excel(filename, sheet_name=0,header=2)
    variablesdf.columns = ['eliminar','  Default Report', 'variable_list']
    variablesdf = variablesdf.drop(['  Default Report'], axis=1)
    serie = pd.Series(variablesdf['variable_list'])
    emergentesbd = pd.DataFrame()
    for x in range(1,156):#HOJAS 155
        emergentesdf = pd.read_excel(filename, sheet_name=x,header=2)
        emergentesdf = emergentesdf.melt(id_vars=columns) #, value_vars=['SEP 2017','OCT 2017','NOV 2017', 'DIC 2017', 'ENE 2018', 'FEB 2018', 'MAR 2018', 'ABR 2018', 'MAY 2018', 'JUN 2018', 'JUL 2018', 'AGO 2018', 'SEP 2018', 'OCT 2018', 'NOV 2018', 'DIC 2018', 'ENE 2019', 'FEB 2019', 'MAR 2019', 'ABR 2019', 'MAY 2019', 'JUN 2019'])
        emergentesdf = emergentesdf.dropna(subset=['LONG DESCRIPTION'])
        emergentesdf = emergentesdf.rename(columns={'variable':'fecha'})
        emergentesdf = emergentesdf.assign(variable=serie[x])
        emergentesbd = emergentesbd.append(emergentesdf)
        print(time.strftime("%H:%M:%S"), x)
        
    dsfechasGeles = pd.Series(emergentesbd['fecha'])
    dsfechasGeles = dsfechasGeles.drop_duplicates()

    fechaGELES=pd.read_excel(r'C:\Users\usuario\Documents\1-familia_all\fechas_geles.xlsx')
    fechaGELES.columns = ['eliminar','fecha', 'date_from', 'date_to']
    fechaGELES = fechaGELES.drop(['eliminar'], axis=1)
    fechaGELES = fechaGELES.set_index('fecha')
    geles_familia = pd.merge(left = emergentesbd, right = fechaGELES, left_on='fecha', right_on='fecha')
    geles_familia.to_csv(r'C:\Users\usuario\Documents\1-familia_all\Entregas\emergentes_geles.csv')

#parametros y llamamos la funcion
filename = r"C:\Users\usuario\Documents\1-familia_all\EMERGENTES\GELES JULIO 2014-JUNIO 2019.xls"
columns = ['CANAL', 'TAG', 'CATEGORY', 'FABRICANTES', 'MARCAS', 'VARIEDADES', 'PRESENTACION', 'EMPAQUE', 'LONG DESCRIPTION']
transform_file(filename=filename, columns=columns)