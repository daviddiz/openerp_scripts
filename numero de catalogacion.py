#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv

csv.register_dialect('nuevo_dialecto', delimiter=',')

csv_productos_utilizados = open(os.path.abspath('/home/ddiz/Escritorio/Explosivos/scripts productos globales numero catalogacion')+'/productos_utilizados.csv', "rb")
reader_csv_productos_utilizados = csv.reader(csv_productos_utilizados, dialect='nuevo_dialecto')

csv_num_catalog = open(os.path.abspath('/home/ddiz/Escritorio/Explosivos/scripts productos globales numero catalogacion')+'/CatalogoExplosivos-26_09_2015.csv', "rb")
reader_csv_num_catalog = csv.reader(csv_num_catalog, dialect='nuevo_dialecto')
  
utilizados_no_encontrados = []  
  
for csv_productos_utilizados in reader_csv_productos_utilizados:
    nombre_producto_utilizado = csv_productos_utilizados[0]
    
    j = 0
    encontrado = 0
      
    for csv_catalog in reader_csv_num_catalog:
        if j==0:
            j=1
            continue
          
        nombre_producto_catalog = csv_catalog[7]
        if nombre_producto_utilizado.lower().strip() in nombre_producto_catalog.lower().strip().split("/"):
             encontrado = 1
             break
         
    if encontrado == 0:
        utilizados_no_encontrados.append(nombre_producto_utilizado)
        
cont=0
for i in utilizados_no_encontrados:
    print i
    cont+=1
print cont
        