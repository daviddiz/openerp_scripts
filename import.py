#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ydbf
import os
import csv
import glob
import xmlrpclib
import vatnumber

PATH_CSV = '/home/ddiz/Escritorio/Pan-Velpa/'

ruta_script_actual = os.path.abspath('')

ruta_csv = os.path.abspath(PATH_CSV)
csv.register_dialect('nuevo_dialecto', delimiter=',')
 
url = 'http://localhost:8069'
db = 'v8spain'
username = 'admin'
password = 'admin'
 
# test API
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
 
# login
uid = common.authenticate(db, username, password, {})
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))


# # CREAR GRUPOS DE CLIENTES DESDE EL CSV ######################################
# csv_grupoclientes = open(ruta_csv+'/GRUPCLI.csv', "rb")
# reader_csv_grupoclientes = csv.reader(csv_grupoclientes, dialect='nuevo_dialecto')
# 
# i=0 
# for csv_grupoclientes in reader_csv_grupoclientes:
#     if i==0:
#         i=1
#         continue
#     new_category_id = models.execute_kw(db, uid, password, 'res.partner.category', 'create', [
#         {'name': csv_grupoclientes[1],
#          'active': True
#          }])
 
 
# # CREAR CLIENTES DESDE EL CSV ################################################
# csv_clientes = open(ruta_csv+'/CLIENTES.csv', "rb")
# reader_csv_clientes = csv.reader(csv_clientes, dialect='nuevo_dialecto')
#  
# i=0
# vats_incorrectos = []
#  
# for csv_cliente in reader_csv_clientes:
#     if i==0:
#         i=1
#         continue
#      
#     pais = csv_cliente[20].replace(" ","")
#     if pais == 'ALEM':
#         res_country_id = 58
#     elif pais == 'AUS':
#         res_country_id = 14
#     elif pais == 'BELG':
#         res_country_id = 21
#     elif pais == 'CAN':
#         res_country_id = 39
#     elif pais == 'CHI':
#         res_country_id = 47
#     elif pais == 'DK':
#         res_country_id = 60
#     elif pais == 'ENGL':
#         res_country_id = 233
#     elif pais == 'ESPA':
#         res_country_id = 69
#     elif pais == 'GBR':
#         res_country_id = 233
#     elif pais == 'HOL':
#         res_country_id = 166
#     elif pais == 'JAP':
#         res_country_id = 114
#     elif pais == 'MEX':
#         res_country_id = 157
#     elif pais == 'SUIZ':
#         res_country_id = 44
#     elif pais == 'USA':
#         res_country_id = 235
#     elif pais == 'VIET':
#         res_country_id = 243
#     else:
#         res_country_id = 69
#      
#     if csv_cliente[14] <> "":
#         vat = csv_cliente[14].replace("-","")
#         vat = csv_cliente[14].replace(":","")
#         if vatnumber.check_vat(vat) == False:
#             country_code = models.execute_kw(db, uid, password, 'res.country', 'search_read', [[['id', '=', res_country_id]]], {'fields': ['code'], 'limit': 5})
#             country_code = country_code[0]['code']
#             vat = country_code + vat
#             if vatnumber.check_vat(vat) == False:
#                 vats_incorrectos.append({'empresa':csv_cliente[64], 'vat':vat})
#                 vat = ""
#     else:
#         vat = ""
#      
#     models.execute_kw(db, uid, password, 'res.partner', 'create', [
#         {'name': csv_cliente[64],
#          'street': csv_cliente[3],
#          'zip': csv_cliente[9],
#          'email': csv_cliente[10],
#          'phone': csv_cliente[65],
#          'mobile': csv_cliente[66],
#          'city': csv_cliente[55],
#          'fax': csv_cliente[45],
#          'customer': True,
#          'vat': vat,
#          'country_id': res_country_id
#          }])
#  
# print "VATs incorrectos: ",vats_incorrectos

# # CREAR DIRECCIONES DESDE EL CSV ###########################################
# csv_direcciones = open(ruta_csv+'/DIRCLI.csv', "rb")
# reader_csv_direcciones = csv.reader(csv_direcciones, dialect='nuevo_dialecto')
#  
# j = 0
#  
# for csv_direccion in reader_csv_direcciones:
#     if j==0:
#         j=1
#         continue
#      
#     prov = csv_direccion[2]
#     direc = csv_direccion[3]
#     ciudad = csv_direccion[4]
#     pais = csv_direccion[5]
#     codcli = int(csv_direccion[7])
#     tlfno = csv_direccion[8]
#     nomcom = csv_direccion[9]
#     cp = csv_direccion[10]
#     email = csv_direccion[11]

# # CREAR PROVEEDORES DESDE EL CSV ###########################################
# csv_proveedores = open(ruta_csv+'/PROVEEDO.csv', "rb")
# reader_csv_proveedores = csv.reader(csv_proveedores, dialect='nuevo_dialecto')
#  
# k = 0
#  
# for csv_proveedor in reader_csv_proveedores:
#     if k==0:
#         k=1
#         continue
#       
#     prov = csv_proveedor[2]