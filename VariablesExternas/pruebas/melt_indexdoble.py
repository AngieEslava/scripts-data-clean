# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:27:18 2019

@author: usuario
"""

import pandas as pd
df = pd.read_excel(r"C:\Users\usuario\Documents\Noel\Nielsen_Noel\ON13-ON16.xlsx", sheet_name='Sheet1' )
df.columns = [list(df.iloc[0]), list(df.iloc[1])]
df = df.drop([0])
df = df.drop([1])

df1 = pd.melt(df, id_vars=[('var','fecha')])

value_vars=[('VENTAS EN VOLUMEN KILOS (000)',	'ON 2013'),
('VENTAS EN VOLUMEN KILOS (000)',	'DE 2014'),
('VENTAS EN VOLUMEN KILOS (000)',	'FM 2014'),
('VENTAS EN VOLUMEN KILOS (000)',	'AM 2014'),
('VENTAS EN VOLUMEN KILOS (000)',	'JJ 2014'),
('VENTAS EN VOLUMEN KILOS (000)',	'AS 2014'),
('VENTAS EN VOLUMEN KILOS (000)',	'ON 2014'),
('VENTAS EN VOLUMEN KILOS (000)',	'DE 2015'),
('VENTAS EN VOLUMEN KILOS (000)',	'FM 2015'),
('VENTAS EN VOLUMEN KILOS (000)',	'AM 2015'),
('VENTAS EN VOLUMEN KILOS (000)',	'JJ 2015'),
('VENTAS EN VOLUMEN KILOS (000)',	'AS 2015'),
('VENTAS EN VOLUMEN KILOS (000)',	'ON 2015'),
('VENTAS EN VOLUMEN KILOS (000)',	'DE 2016'),
('VENTAS EN VOLUMEN KILOS (000)',	'FM 2016'),
('VENTAS EN VOLUMEN KILOS (000)',	'AM 2016'),
('VENTAS EN VOLUMEN KILOS (000)',	'JJ 2016'),
('VENTAS EN VOLUMEN KILOS (000)',	'AS 2016'),
('VENTAS EN VOLUMEN KILOS (000)',	'ON 2016'),
('VENTAS EN VALOR $ (000000)',	'ON 2013'),
('VENTAS EN VALOR $ (000000)',	'DE 2014'),
('VENTAS EN VALOR $ (000000)',	'FM 2014'),
('VENTAS EN VALOR $ (000000)',	'AM 2014'),
('VENTAS EN VALOR $ (000000)',	'JJ 2014'),
('VENTAS EN VALOR $ (000000)',	'AS 2014'),
('VENTAS EN VALOR $ (000000)',	'ON 2014'),
('VENTAS EN VALOR $ (000000)',	'DE 2015'),
('VENTAS EN VALOR $ (000000)',	'FM 2015'),
('VENTAS EN VALOR $ (000000)',	'AM 2015'),
('VENTAS EN VALOR $ (000000)',	'JJ 2015'),
('VENTAS EN VALOR $ (000000)',	'AS 2015'),
('VENTAS EN VALOR $ (000000)',	'ON 2015'),
('VENTAS EN VALOR $ (000000)',	'DE 2016'),
('VENTAS EN VALOR $ (000000)',	'FM 2016'),
('VENTAS EN VALOR $ (000000)',	'AM 2016'),
('VENTAS EN VALOR $ (000000)',	'JJ 2016'),
('VENTAS EN VALOR $ (000000)',	'AS 2016'),
('VENTAS EN VALOR $ (000000)',	'ON 2016'),
('DISTRIBUCION MANEJANTES (POND)',	'ON 2013'),
('DISTRIBUCION MANEJANTES (POND)',	'DE 2014'),
('DISTRIBUCION MANEJANTES (POND)',	'FM 2014'),
('DISTRIBUCION MANEJANTES (POND)',	'AM 2014'),
('DISTRIBUCION MANEJANTES (POND)',	'JJ 2014'),
('DISTRIBUCION MANEJANTES (POND)',	'AS 2014'),
('DISTRIBUCION MANEJANTES (POND)',	'ON 2014'),
('DISTRIBUCION MANEJANTES (POND)',	'DE 2015'),
('DISTRIBUCION MANEJANTES (POND)',	'FM 2015'),
('DISTRIBUCION MANEJANTES (POND)',	'AM 2015'),
('DISTRIBUCION MANEJANTES (POND)',	'JJ 2015'),
('DISTRIBUCION MANEJANTES (POND)',	'AS 2015'),
('DISTRIBUCION MANEJANTES (POND)',	'ON 2015'),
('DISTRIBUCION MANEJANTES (POND)',	'DE 2016'),
('DISTRIBUCION MANEJANTES (POND)',	'FM 2016'),
('DISTRIBUCION MANEJANTES (POND)',	'AM 2016'),
('DISTRIBUCION MANEJANTES (POND)',	'JJ 2016'),
('DISTRIBUCION MANEJANTES (POND)',	'AS 2016'),
('DISTRIBUCION MANEJANTES (POND)',	'ON 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'ON 2013'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'DE 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'FM 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'AM 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'JJ 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'AS 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'ON 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'DE 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'FM 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'AM 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'JJ 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'AS 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'ON 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'DE 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'FM 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'AM 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'JJ 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'AS 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (POND)',	'ON 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'ON 2013'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'DE 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'FM 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'AM 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'JJ 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'AS 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'ON 2014'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'DE 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'FM 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'AM 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'JJ 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'AS 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'ON 2015'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'DE 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'FM 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'AM 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'JJ 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'AS 2016'),
('DISTRIBUCION TIENDAS VENDEDORAS (NUM)',	'ON 2016'),
('PROMEDIO VENTAS KILOS',	'ON 2013'),
('PROMEDIO VENTAS KILOS',	'DE 2014'),
('PROMEDIO VENTAS KILOS',	'FM 2014'),
('PROMEDIO VENTAS KILOS',	'AM 2014'),
('PROMEDIO VENTAS KILOS',	'JJ 2014'),
('PROMEDIO VENTAS KILOS',	'AS 2014'),
('PROMEDIO VENTAS KILOS',	'ON 2014'),
('PROMEDIO VENTAS KILOS',	'DE 2015'),
('PROMEDIO VENTAS KILOS',	'FM 2015'),
('PROMEDIO VENTAS KILOS',	'AM 2015'),
('PROMEDIO VENTAS KILOS',	'JJ 2015'),
('PROMEDIO VENTAS KILOS',	'AS 2015'),
('PROMEDIO VENTAS KILOS',	'ON 2015'),
('PROMEDIO VENTAS KILOS',	'DE 2016'),
('PROMEDIO VENTAS KILOS',	'FM 2016'),
('PROMEDIO VENTAS KILOS',	'AM 2016'),
('PROMEDIO VENTAS KILOS',	'JJ 2016'),
('PROMEDIO VENTAS KILOS',	'AS 2016'),
('PROMEDIO VENTAS KILOS',	'ON 2016'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'ON 2013'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'DE 2014'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'FM 2014'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'AM 2014'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'JJ 2014'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'AS 2014'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'ON 2014'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'DE 2015'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'FM 2015'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'AM 2015'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'JJ 2015'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'AS 2015'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'ON 2015'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'DE 2016'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'FM 2016'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'AM 2016'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'JJ 2016'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'AS 2016'),
('COMPRAS PROMEDIO POR TIENDA KILOS',	'ON 2016'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'ON 2013'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'DE 2014'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'FM 2014'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'AM 2014'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'JJ 2014'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'AS 2014'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'ON 2014'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'DE 2015'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'FM 2015'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'AM 2015'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'JJ 2015'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'AS 2015'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'ON 2015'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'DE 2016'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'FM 2016'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'AM 2016'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'JJ 2016'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'AS 2016'),
('INVENTARIO PROMEDIO POR TIENDA KILOS',	'ON 2016'),
('COMPRAS TOTALES KILOS (000)',	'ON 2013'),
('COMPRAS TOTALES KILOS (000)',	'DE 2014'),
('COMPRAS TOTALES KILOS (000)',	'FM 2014'),
('COMPRAS TOTALES KILOS (000)',	'AM 2014'),
('COMPRAS TOTALES KILOS (000)',	'JJ 2014'),
('COMPRAS TOTALES KILOS (000)',	'AS 2014'),
('COMPRAS TOTALES KILOS (000)',	'ON 2014'),
('COMPRAS TOTALES KILOS (000)',	'DE 2015'),
('COMPRAS TOTALES KILOS (000)',	'FM 2015'),
('COMPRAS TOTALES KILOS (000)',	'AM 2015'),
('COMPRAS TOTALES KILOS (000)',	'JJ 2015'),
('COMPRAS TOTALES KILOS (000)',	'AS 2015'),
('COMPRAS TOTALES KILOS (000)',	'ON 2015'),
('COMPRAS TOTALES KILOS (000)',	'DE 2016'),
('COMPRAS TOTALES KILOS (000)',	'FM 2016'),
('COMPRAS TOTALES KILOS (000)',	'AM 2016'),
('COMPRAS TOTALES KILOS (000)',	'JJ 2016'),
('COMPRAS TOTALES KILOS (000)',	'AS 2016'),
('COMPRAS TOTALES KILOS (000)',	'ON 2016'),
('INVENTARIO ACTIVO KILOS (000)',	'ON 2013'),
('INVENTARIO ACTIVO KILOS (000)',	'DE 2014'),
('INVENTARIO ACTIVO KILOS (000)',	'FM 2014'),
('INVENTARIO ACTIVO KILOS (000)',	'AM 2014'),
('INVENTARIO ACTIVO KILOS (000)',	'JJ 2014'),
('INVENTARIO ACTIVO KILOS (000)',	'AS 2014'),
('INVENTARIO ACTIVO KILOS (000)',	'ON 2014'),
('INVENTARIO ACTIVO KILOS (000)',	'DE 2015'),
('INVENTARIO ACTIVO KILOS (000)',	'FM 2015'),
('INVENTARIO ACTIVO KILOS (000)',	'AM 2015'),
('INVENTARIO ACTIVO KILOS (000)',	'JJ 2015'),
('INVENTARIO ACTIVO KILOS (000)',	'AS 2015'),
('INVENTARIO ACTIVO KILOS (000)',	'ON 2015'),
('INVENTARIO ACTIVO KILOS (000)',	'DE 2016'),
('INVENTARIO ACTIVO KILOS (000)',	'FM 2016'),
('INVENTARIO ACTIVO KILOS (000)',	'AM 2016'),
('INVENTARIO ACTIVO KILOS (000)',	'JJ 2016'),
('INVENTARIO ACTIVO KILOS (000)',	'AS 2016'),
('INVENTARIO ACTIVO KILOS (000)',	'ON 2016'),
('INVENTARIO TOTAL KILOS (000)',	'ON 2013'),
('INVENTARIO TOTAL KILOS (000)',	'DE 2014'),
('INVENTARIO TOTAL KILOS (000)',	'FM 2014'),
('INVENTARIO TOTAL KILOS (000)',	'AM 2014'),
('INVENTARIO TOTAL KILOS (000)',	'JJ 2014'),
('INVENTARIO TOTAL KILOS (000)',	'AS 2014'),
('INVENTARIO TOTAL KILOS (000)',	'ON 2014'),
('INVENTARIO TOTAL KILOS (000)',	'DE 2015'),
('INVENTARIO TOTAL KILOS (000)',	'FM 2015'),
('INVENTARIO TOTAL KILOS (000)',	'AM 2015'),
('INVENTARIO TOTAL KILOS (000)',	'JJ 2015'),
('INVENTARIO TOTAL KILOS (000)',	'AS 2015'),
('INVENTARIO TOTAL KILOS (000)',	'ON 2015'),
('INVENTARIO TOTAL KILOS (000)',	'DE 2016'),
('INVENTARIO TOTAL KILOS (000)',	'FM 2016'),
('INVENTARIO TOTAL KILOS (000)',	'AM 2016'),
('INVENTARIO TOTAL KILOS (000)',	'JJ 2016'),
('INVENTARIO TOTAL KILOS (000)',	'AS 2016'),
('INVENTARIO TOTAL KILOS (000)',	'ON 2016'),
('DISTRIBUCION MANEJANTES (NUM)',	'ON 2013'),
('DISTRIBUCION MANEJANTES (NUM)',	'DE 2014'),
('DISTRIBUCION MANEJANTES (NUM)',	'FM 2014'),
('DISTRIBUCION MANEJANTES (NUM)',	'AM 2014'),
('DISTRIBUCION MANEJANTES (NUM)',	'JJ 2014'),
('DISTRIBUCION MANEJANTES (NUM)',	'AS 2014'),
('DISTRIBUCION MANEJANTES (NUM)',	'ON 2014'),
('DISTRIBUCION MANEJANTES (NUM)',	'DE 2015'),
('DISTRIBUCION MANEJANTES (NUM)',	'FM 2015'),
('DISTRIBUCION MANEJANTES (NUM)',	'AM 2015'),
('DISTRIBUCION MANEJANTES (NUM)',	'JJ 2015'),
('DISTRIBUCION MANEJANTES (NUM)',	'AS 2015'),
('DISTRIBUCION MANEJANTES (NUM)',	'ON 2015'),
('DISTRIBUCION MANEJANTES (NUM)',	'DE 2016'),
('DISTRIBUCION MANEJANTES (NUM)',	'FM 2016'),
('DISTRIBUCION MANEJANTES (NUM)',	'AM 2016'),
('DISTRIBUCION MANEJANTES (NUM)',	'JJ 2016'),
('DISTRIBUCION MANEJANTES (NUM)',	'AS 2016'),
('DISTRIBUCION MANEJANTES (NUM)',	'ON 2016'),
('DISTRIBUCION AGOTADOS (NUM)',	'ON 2013'),
('DISTRIBUCION AGOTADOS (NUM)',	'DE 2014'),
('DISTRIBUCION AGOTADOS (NUM)',	'FM 2014'),
('DISTRIBUCION AGOTADOS (NUM)',	'AM 2014'),
('DISTRIBUCION AGOTADOS (NUM)',	'JJ 2014'),
('DISTRIBUCION AGOTADOS (NUM)',	'AS 2014'),
('DISTRIBUCION AGOTADOS (NUM)',	'ON 2014'),
('DISTRIBUCION AGOTADOS (NUM)',	'DE 2015'),
('DISTRIBUCION AGOTADOS (NUM)',	'FM 2015'),
('DISTRIBUCION AGOTADOS (NUM)',	'AM 2015'),
('DISTRIBUCION AGOTADOS (NUM)',	'JJ 2015'),
('DISTRIBUCION AGOTADOS (NUM)',	'AS 2015'),
('DISTRIBUCION AGOTADOS (NUM)',	'ON 2015'),
('DISTRIBUCION AGOTADOS (NUM)',	'DE 2016'),
('DISTRIBUCION AGOTADOS (NUM)',	'FM 2016'),
('DISTRIBUCION AGOTADOS (NUM)',	'AM 2016'),
('DISTRIBUCION AGOTADOS (NUM)',	'JJ 2016'),
('DISTRIBUCION AGOTADOS (NUM)',	'AS 2016'),
('DISTRIBUCION AGOTADOS (NUM)',	'ON 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'ON 2013'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'DE 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'FM 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'AM 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'JJ 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'AS 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'ON 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'DE 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'FM 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'AM 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'JJ 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'AS 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'ON 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'DE 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'FM 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'AM 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'JJ 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'AS 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (NUM)',	'ON 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'ON 2013'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'DE 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'FM 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'AM 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'JJ 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'AS 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'ON 2014'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'DE 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'FM 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'AM 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'JJ 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'AS 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'ON 2015'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'DE 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'FM 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'AM 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'JJ 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'AS 2016'),
('DISTRIBUCION TIENDAS COMPRADORAS (POND)',	'ON 2016'),
('DISTRIBUCION AGOTADOS (POND)',	'ON 2013'),
('DISTRIBUCION AGOTADOS (POND)',	'DE 2014'),
('DISTRIBUCION AGOTADOS (POND)',	'FM 2014'),
('DISTRIBUCION AGOTADOS (POND)',	'AM 2014'),
('DISTRIBUCION AGOTADOS (POND)',	'JJ 2014'),
('DISTRIBUCION AGOTADOS (POND)',	'AS 2014'),
('DISTRIBUCION AGOTADOS (POND)',	'ON 2014'),
('DISTRIBUCION AGOTADOS (POND)',	'DE 2015'),
('DISTRIBUCION AGOTADOS (POND)',	'FM 2015'),
('DISTRIBUCION AGOTADOS (POND)',	'AM 2015'),
('DISTRIBUCION AGOTADOS (POND)',	'JJ 2015'),
('DISTRIBUCION AGOTADOS (POND)',	'AS 2015'),
('DISTRIBUCION AGOTADOS (POND)',	'ON 2015'),
('DISTRIBUCION AGOTADOS (POND)',	'DE 2016'),
('DISTRIBUCION AGOTADOS (POND)',	'FM 2016'),
('DISTRIBUCION AGOTADOS (POND)',	'AM 2016'),
('DISTRIBUCION AGOTADOS (POND)',	'JJ 2016'),
('DISTRIBUCION AGOTADOS (POND)',	'AS 2016'),
('DISTRIBUCION AGOTADOS (POND)',	'ON 2016'),
('COMPRAS DIRECTAS KILOS (000)',	'ON 2013'),
('COMPRAS DIRECTAS KILOS (000)',	'DE 2014'),
('COMPRAS DIRECTAS KILOS (000)',	'FM 2014'),
('COMPRAS DIRECTAS KILOS (000)',	'AM 2014'),
('COMPRAS DIRECTAS KILOS (000)',	'JJ 2014'),
('COMPRAS DIRECTAS KILOS (000)',	'AS 2014'),
('COMPRAS DIRECTAS KILOS (000)',	'ON 2014'),
('COMPRAS DIRECTAS KILOS (000)',	'DE 2015'),
('COMPRAS DIRECTAS KILOS (000)',	'FM 2015'),
('COMPRAS DIRECTAS KILOS (000)',	'AM 2015'),
('COMPRAS DIRECTAS KILOS (000)',	'JJ 2015'),
('COMPRAS DIRECTAS KILOS (000)',	'AS 2015'),
('COMPRAS DIRECTAS KILOS (000)',	'ON 2015'),
('COMPRAS DIRECTAS KILOS (000)',	'DE 2016'),
('COMPRAS DIRECTAS KILOS (000)',	'FM 2016'),
('COMPRAS DIRECTAS KILOS (000)',	'AM 2016'),
('COMPRAS DIRECTAS KILOS (000)',	'JJ 2016'),
('COMPRAS DIRECTAS KILOS (000)',	'AS 2016'),
('COMPRAS DIRECTAS KILOS (000)',	'ON 2016'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'ON 2013'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'DE 2014'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'FM 2014'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'AM 2014'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'JJ 2014'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'AS 2014'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'ON 2014'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'DE 2015'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'FM 2015'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'AM 2015'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'JJ 2015'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'AS 2015'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'ON 2015'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'DE 2016'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'FM 2016'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'AM 2016'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'JJ 2016'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'AS 2016'),
('DISTRIBUCION MATERIAL P.O.P. (NUM)',	'ON 2016'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'ON 2013'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'DE 2014'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'FM 2014'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'AM 2014'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'JJ 2014'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'AS 2014'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'ON 2014'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'DE 2015'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'FM 2015'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'AM 2015'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'JJ 2015'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'AS 2015'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'ON 2015'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'DE 2016'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'FM 2016'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'AM 2016'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'JJ 2016'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'AS 2016'),
('DISTRIBUCION MATERIAL P.O.P. (POND)',	'ON 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'ON 2013'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'DE 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'FM 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'AM 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'JJ 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'AS 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'ON 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'DE 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'FM 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'AM 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'JJ 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'AS 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'ON 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'DE 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'FM 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'AM 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'JJ 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'AS 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (NUM)',	'ON 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'ON 2013'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'DE 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'FM 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'AM 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'JJ 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'AS 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'ON 2014'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'DE 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'FM 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'AM 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'JJ 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'AS 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'ON 2015'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'DE 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'FM 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'AM 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'JJ 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'AS 2016'),
('DISTRIBUCION EXHIBI. ESPECIALES (POND)',	'ON 2016'),
('DISTRIBUCION OFERTAS (NUM)',	'ON 2013'),
('DISTRIBUCION OFERTAS (NUM)',	'DE 2014'),
('DISTRIBUCION OFERTAS (NUM)',	'FM 2014'),
('DISTRIBUCION OFERTAS (NUM)',	'AM 2014'),
('DISTRIBUCION OFERTAS (NUM)',	'JJ 2014'),
('DISTRIBUCION OFERTAS (NUM)',	'AS 2014'),
('DISTRIBUCION OFERTAS (NUM)',	'ON 2014'),
('DISTRIBUCION OFERTAS (NUM)',	'DE 2015'),
('DISTRIBUCION OFERTAS (NUM)',	'FM 2015'),
('DISTRIBUCION OFERTAS (NUM)',	'AM 2015'),
('DISTRIBUCION OFERTAS (NUM)',	'JJ 2015'),
('DISTRIBUCION OFERTAS (NUM)',	'AS 2015'),
('DISTRIBUCION OFERTAS (NUM)',	'ON 2015'),
('DISTRIBUCION OFERTAS (NUM)',	'DE 2016'),
('DISTRIBUCION OFERTAS (NUM)',	'FM 2016'),
('DISTRIBUCION OFERTAS (NUM)',	'AM 2016'),
('DISTRIBUCION OFERTAS (NUM)',	'JJ 2016'),
('DISTRIBUCION OFERTAS (NUM)',	'AS 2016'),
('DISTRIBUCION OFERTAS (NUM)',	'ON 2016'),
('DISTRIBUCION OFERTAS (POND)',	'ON 2013'),
('DISTRIBUCION OFERTAS (POND)',	'DE 2014'),
('DISTRIBUCION OFERTAS (POND)',	'FM 2014'),
('DISTRIBUCION OFERTAS (POND)',	'AM 2014'),
('DISTRIBUCION OFERTAS (POND)',	'JJ 2014'),
('DISTRIBUCION OFERTAS (POND)',	'AS 2014'),
('DISTRIBUCION OFERTAS (POND)',	'ON 2014'),
('DISTRIBUCION OFERTAS (POND)',	'DE 2015'),
('DISTRIBUCION OFERTAS (POND)',	'FM 2015'),
('DISTRIBUCION OFERTAS (POND)',	'AM 2015'),
('DISTRIBUCION OFERTAS (POND)',	'JJ 2015'),
('DISTRIBUCION OFERTAS (POND)',	'AS 2015'),
('DISTRIBUCION OFERTAS (POND)',	'ON 2015'),
('DISTRIBUCION OFERTAS (POND)',	'DE 2016'),
('DISTRIBUCION OFERTAS (POND)',	'FM 2016'),
('DISTRIBUCION OFERTAS (POND)',	'AM 2016'),
('DISTRIBUCION OFERTAS (POND)',	'JJ 2016'),
('DISTRIBUCION OFERTAS (POND)',	'AS 2016'),
('DISTRIBUCION OFERTAS (POND)',	'ON 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'ON 2013'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'DE 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'FM 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'AM 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'JJ 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'AS 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'ON 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'DE 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'FM 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'AM 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'JJ 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'AS 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'ON 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'DE 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'FM 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'AM 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'JJ 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'AS 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (NUM)',	'ON 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'ON 2013'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'DE 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'FM 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'AM 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'JJ 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'AS 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'ON 2014'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'DE 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'FM 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'AM 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'JJ 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'AS 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'ON 2015'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'DE 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'FM 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'AM 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'JJ 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'AS 2016'),
('DISTRIB. ACTIVIDAD PROMOCIONAL (POND)',	'ON 2016')]

