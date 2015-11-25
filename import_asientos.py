#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ydbf
import oerplib
import vatnumber
import os
import csv
import unicodedata
import time
# import sys

host= 'localhost'
protocol= 'xmlrpc'
port=8069
dbname = 'test'
username = 'XXXXX'
pwd = 'XXXXX'
 
oerp = oerplib.OERP(host, dbname, protocol, port)
user = oerp.login(username, pwd)

ruta_dbf = os.path.abspath('../dbf/')
ruta_dbf2csv = os.path.abspath('../dbf2csv/')
csv.register_dialect('nuevo_dialecto', delimiter=',')

#Convertir Diario.dbf en un csv con los asientos de 2013

#csv_diario = open(ruta_dbf2csv + '/Diario.csv', 'wb')
#writer_diario = csv.writer(csv_diario, dialect='nuevo_dialecto')
#dbf_diario = ydbf.open(ruta_dbf + '/Diario.dbf', encoding='cp1252')
#i=0
#cont=0
#for record in dbf_diario:
#    cont+=1
#    print "traspasando dbf de Diario, linea numero:  %s"%cont
#    cabecera=[]
#    if i==0:
#        j=0
#        for key,value in record.iteritems():
#            cabecera.append("valor")
#            cabecera[j]=key
#            j+=1
#        writer_diario.writerow(cabecera)
#        i+=1
#
#    linea=[]
#    k=0
#    for key, value in record.iteritems():
#        linea.append("valor")
#        linea[k]=value
#        k+=1
#    writer_diario.writerow(linea)
#    
#csv_diario.close()
#dbf_diario.close()
#
## Simplifico el csv para prepararlo para la importacion
#
#csv_diario = open(ruta_dbf2csv + '/Diario.csv', 'rb')
#reader_diario = csv.reader(csv_diario, dialect='nuevo_dialecto')
#
#csv_diario_mod_2013_final = open(ruta_dbf2csv + '/Diario_mod_2013_final_ultimo.csv', 'wb')
#writer_diario_mod_2013_final = csv.writer(csv_diario_mod_2013_final, dialect='nuevo_dialecto')
#i=0
#cont2=0
#for linea_diario in reader_diario:
#    cont2+=1
#    print "arreglando csv de Diario, linea numero:  %s"%cont2
#    linea=[]
#    if i==0:
#        linea.append(linea_diario[76])
#        linea.append(linea_diario[31])
#        linea.append(linea_diario[7])
#        linea.append(linea_diario[74])
#        linea.append(linea_diario[71])
#        linea.append(linea_diario[46])
#        linea.append(linea_diario[56])
#        linea.append(linea_diario[4])
#        linea.append(linea_diario[12])
#        linea.append(linea_diario[27])
#        linea.append(linea_diario[75])
#        linea.append(linea_diario[41])
#        linea.append(linea_diario[43])
#        linea.append(linea_diario[2])
#        linea.append(linea_diario[0])
#        linea.append(linea_diario[22])
#        linea.append(linea_diario[88])
#        linea.append(linea_diario[36])
#        linea.append(linea_diario[37])
#        linea.append(linea_diario[39])
#        linea.append(linea_diario[47])
#        linea.append(linea_diario[21])
#        linea.append(linea_diario[87])
#        linea.append(linea_diario[89])
#        writer_diario_mod_2013_final.writerow(linea)
#        i+=1
#    else:
#        if linea_diario[76][:7] in ("2013-01", "2013-02", "2013-03", "2013-04"):
#            linea.append(linea_diario[76])
#            linea.append(linea_diario[31])
#            linea.append(linea_diario[7])
#            linea.append(linea_diario[74])
#            linea.append(linea_diario[71])
#            linea.append(linea_diario[46])
#            linea.append(linea_diario[56])
#            linea.append(linea_diario[4])
#            linea.append(linea_diario[12])
#            linea.append(linea_diario[27])
#            linea.append(linea_diario[75])
#            linea.append(linea_diario[41])
#            linea.append(linea_diario[43])
#            linea.append(linea_diario[2])
#            linea.append(linea_diario[0])
#            linea.append(linea_diario[22])
#            linea.append(linea_diario[88])
#            linea.append(linea_diario[36])
#            linea.append(linea_diario[37])
#            linea.append(linea_diario[39])
#            linea.append(linea_diario[47])
#            linea.append(linea_diario[21])
#            linea.append(linea_diario[87])
#            linea.append(linea_diario[89])
#            writer_diario_mod_2013_final.writerow(linea)
#
#csv_diario.close()
#csv_diario_mod_2013_final.close()

# csv_diario_2013_compras = open(ruta_dbf2csv + '/Diario_2013_compras.csv', 'rb')
# reader_diario_2013_compras = csv.reader(csv_diario_2013_compras, dialect='nuevo_dialecto')
#  
# csv_diario_2013_compras_format = open(ruta_dbf2csv + '/Diario_2013_compras_format.csv', 'wb')
# writer_diario_2013_compras_format = csv.writer(csv_diario_2013_compras_format, dialect='nuevo_dialecto')
#  
# i=0
# cont=0
# for linea_diario_2013_compras in reader_diario_2013_compras:
#     cont+=1
#     print "arreglando csv de Diario, linea numero:  %s"%cont
#     linea=[]
#     code7 = linea_diario_2013_compras[2]
#  
#     if code7=="2180001":
#         code7 = "2180000000"
#     elif code7=="4751000":
#         code7 = "4751000000"
#     elif code7 == "4751110":
#         code7 = "4751110000"
#     elif code7 == "4751111":
#         code7 = "4751111000"
#     elif code7 == "5722000":
#         code7 = "5720000003"
#     elif code7 == "5722115":
#         code7 = "5720000002"
#     elif code7 == "5722116":
#         code7 = "5720000001"
#     elif code7 == "6021000":
#         code7 = "6020000000"
#     elif code7 == "6021100":
#         code7 = "6020000001"
#     elif code7 == "6200002":
#         code7 = "6200000001"
#     elif code7 == "6210004":
#         code7 = "6210000001"
#     elif code7 == "6210005":
#         code7 = "6210000002"    
#     elif code7 == "6210006":
#         code7 = "6210000003"    
#     elif code7 == "6210007":
#         code7 = "6210000004"
#     elif code7 == "6210008":
#         code7 = "6210000005"
#     elif code7 == "6210009":
#         code7 = "6210000006"
#     elif code7 == "6210010":
#         code7 = "6210000007"
#     elif code7 == "6210011":
#         code7 = "6210000008"
#     elif code7 == "6210012":
#         code7 = "6210000009"
#     elif code7 == "6210014":
#         code7 = "6210000010"
#     elif code7 == "6210017":
#         code7 = "6210000011"
#     elif code7 == "6210018":
#         code7 = "6210000012"
#     elif code7 == "6226000":
#         code7 = "6220000000"
#     elif code7 == "6230102":
#         code7 = "6230000004"
#     elif code7 == "6230006":
#         code7 = "6230000003"
#     elif (code7[:4]=="6231"):
#         code7 = "6230000001"
#     elif code7 == "6241001":
#         code7 = "6240000001"
#     elif code7 == "6271300":
#         code7 = "6270000002"
#     elif code7 == "6271401":
#         code7 = "6270000001"
#     elif code7 == "6282000":
#         code7 = "6280000000"
#     elif code7 == "6283000":
#         code7 = "6280000001"
#     elif code7 == "6284000":
#         code7 = "6280000002"
#     elif code7 == "6290003":
#         code7 = "6290000002"
#     elif code7 == "6291001":
#         code7 = "6290000003"
#     elif code7 == "6291002":
#         code7 = "6290000004"
#     elif code7 == "6291200":
#         code7 = "6290000005"
#     elif code7 == "6295000":
#         code7 = "6290000006"
#     elif code7 == "6295001":
#         code7 = "6290000007"
#     elif code7 == "6296100":
#         code7 = "6290000009"
#     elif code7 == "6296101":
#         code7 = "6290000010"
#     elif code7 == "6296111":
#         code7 = "6290000011"
#     elif code7 == "6296210":
#         code7 = "6290000012"
#     elif code7 == "6297000":
#         code7 = "6290000013"
#     elif code7 == "6297001":
#         code7 = "6290000014"
#     elif code7 == "6297002":
#         code7 = "6290000015"
#     elif code7 == "6297003":
#         code7 = "6290000016"
#     elif code7 == "6298110":
#         code7 = "6290000017"
#     elif code7 == "6300342":
#         code7 = "6300000030"
#     elif code7 == "6410001":
#         code7 = "6410000000"
#     elif code7 == "6440010":
#         code7 = "6440000000"
#     elif code7 == "6490000":
#         code7 = "6020000002"
#     elif code7 == "6490002":
#         code7 = "6020000003"
#     elif code7 == "6691000":
#         code7 = "6690000000"
#     elif code7 == "6691003":
#         code7 = "6690000001"
#     elif code7 == "7590001":
#         code7 = "7590000000"
#     elif code7 == "7690100":
#         code7 = "7690000000"
#     else:
#         code7 = code7[:3] + "000" + code7[3:]
#          
#      
#     if i==0:
#         linea.append(linea_diario_2013_compras[0])
#         linea.append(linea_diario_2013_compras[1])
#         linea.append(linea_diario_2013_compras[2])
#         linea.append(linea_diario_2013_compras[3])
#         linea.append(linea_diario_2013_compras[4])
#         linea.append(linea_diario_2013_compras[5])
#         linea.append(linea_diario_2013_compras[6])
#         linea.append(linea_diario_2013_compras[7])
#         linea.append(linea_diario_2013_compras[8])
#         linea.append(linea_diario_2013_compras[9])
#         linea.append(linea_diario_2013_compras[10])
#         linea.append(linea_diario_2013_compras[11])
#         linea.append(linea_diario_2013_compras[12])
#         linea.append(linea_diario_2013_compras[13])
#         linea.append(linea_diario_2013_compras[15])
#         linea.append(linea_diario_2013_compras[16])
#         linea.append(linea_diario_2013_compras[17])
#         linea.append(linea_diario_2013_compras[18])
#         linea.append(linea_diario_2013_compras[19])
#         linea.append(linea_diario_2013_compras[20])
#         linea.append(linea_diario_2013_compras[21])
#         linea.append(linea_diario_2013_compras[22])
#         linea.append(linea_diario_2013_compras[23])
#         writer_diario_2013_compras_format.writerow(linea)
#         i+=1
#     else:
#         linea.append(linea_diario_2013_compras[0])
#         linea.append(linea_diario_2013_compras[1])
#         linea.append(code7)
#         linea.append(linea_diario_2013_compras[3])
#         linea.append(linea_diario_2013_compras[4])
#         linea.append(linea_diario_2013_compras[5])
#         linea.append(linea_diario_2013_compras[6])
#         linea.append(linea_diario_2013_compras[7])
#         linea.append(linea_diario_2013_compras[8])
#         linea.append(linea_diario_2013_compras[9])
#         linea.append(linea_diario_2013_compras[10])
#         linea.append(linea_diario_2013_compras[11])
#         linea.append(linea_diario_2013_compras[12])
#         linea.append(linea_diario_2013_compras[13])
#         linea.append(linea_diario_2013_compras[15])
#         linea.append(linea_diario_2013_compras[16])
#         linea.append(linea_diario_2013_compras[17])
#         linea.append(linea_diario_2013_compras[18])
#         linea.append(linea_diario_2013_compras[19])
#         linea.append(linea_diario_2013_compras[20])
#         linea.append(linea_diario_2013_compras[21])
#         linea.append(linea_diario_2013_compras[22])
#         linea.append(linea_diario_2013_compras[23])
#         writer_diario_2013_compras_format.writerow(linea)
#  
# csv_diario_2013_compras.close()
# csv_diario_2013_compras_format.close()
 
csv_diario_2013_compras_format = open(ruta_dbf2csv + '/Diario_2013_compras_format.csv', 'rb')
reader_diario_2013_compras_format = csv.reader(csv_diario_2013_compras_format, dialect='nuevo_dialecto')

def elimina_tildes(s):
    s=unicode(s)
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

#validar cif
def check_vat(nif):
    if ((len(nif)>0) and (len(nif)<9)) or (nif=="") or ((vatnumber.check_vat_es(nif))==False):
        vat = ""
    else:
        vat = "ES" + nif
    return vat

#comprobar la existencia del partner
#def _comprobar_existencia(nombre, vat, cuenta, sock, dbname, uid, pwd):
#    ids=[]
#    if vat:
#        args = [('vat', '=', vat)]
#        ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)
#        if not ids:
#            args = [('name', '=', nombre)]
#            ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)
#    else:
#        args = [('name', '=', nombre)]
#        ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)
#    return ids

#comprobar por el nombre formateado si ya existe el partner
def _comprobar_por_nombre(nombre):
    ids = []
    nombre = (nombre).replace(" ","")
    nombre = (nombre).replace(",","")
    nombre = (nombre).replace(";","")
    nombre = (nombre).replace(".","")
    nombre = (nombre).lower()
    nombre = elimina_tildes(nombre)
    ids_partners_todos = oerp.execute('res.partner', 'search', [])
    for id in ids_partners_todos:
        partner_existente = oerp.execute('res.partner', 'read', id, ['name'])
        partner_existente['name'] = (partner_existente['name']).replace(" ","")
        partner_existente['name'] = (partner_existente['name']).replace(",","")
        partner_existente['name'] = (partner_existente['name']).replace(";","")
        partner_existente['name'] = (partner_existente['name']).replace(".","")
        partner_existente['name'] = (partner_existente['name']).lower()
        partner_existente['name'] = elimina_tildes(partner_existente['name'])
        if nombre == partner_existente['name']:
            ids.append(id)
    return ids
        
#crear nuevo partner y su direccion
def _alta_partner_y_direccion(nombre, vat):
    partner = {
        'name': nombre,
        'vat': vat,
        'vat_subjected': True,
        'vat_type': '1',
        'company_id': 2,
        'include_in_mod347': True,
        'supplier': True,
        'active': True,
    }
    partner_id = oerp.execute('res.partner', 'create', partner)
    print "alta de partner: %s"%partner_id
#    address = {
#        'partner_id': partner_id,
#        'type' : 'default',
#        'street': record['DOMICILIO'],
#        'zip': record['CODPOSTAL'],
#        'city': record['POBLACION'],
#        'phone': record['TELEF01'],
#        'fax': record['FAX01'],
#        'name': record['TITULO'].strip(),
#        'email': record['EMAIL'],
#        'active': True,
#        'company_id': 2,
#        'country_id': 67,
#    }
#    address_id = sock.execute(dbname, uid, pwd, 'res.partner.address', 'create', address)
#    print "alta de partner: %s"%partner_id
    return partner_id

#alta de la cuenta contable asociada al proveedor
def _alta_cuenta_proveedor(partner_id, subcta, nombre):
    account_args = [('code', '=', subcta)]
    account_ids = oerp.execute('account.account', 'search', account_args)
    if account_ids:    
        account_id = account_ids[0]
    else: 
        account = {
            'name': nombre,
            'code' : subcta,
            'parent_id': 477,
            'type': "payable",
            'user_type': 7,
            'active': True,
            'reconcile': True,
        }
        account_id = oerp.execute('account.account', 'create', account)
    editado0 = oerp.execute('res.partner', 'write', partner_id, {'property_account_payable':account_id,'supplier':True} )
    print "alta de cuenta: %s"%account_id
    return account_id

def _import_record_proveedor(ternom, ternif, subcta):
    nombre = ternom.strip()
    if len(nombre)>40:
        nombre = nombre[:40] 
    ternif = ternif.replace(" ","")
    ternif = ternif.replace("/","")
    ternif = ternif.replace("-","")
    vat = check_vat(ternif)
    ids = []
    if vat:
        args = [('vat', '=', vat)]
        ids = oerp.execute('res.partner', 'search', args)
        if not ids:
            ids = _comprobar_por_nombre(nombre)
    else:
        args = [('name', '=', nombre)]
        ids = oerp.execute('res.partner', 'search', args)
        if not ids:
            ids = _comprobar_por_nombre(nombre)
    if ids:                
        partner_id = ids[0]
        partner_existente = []
        partner_existente = oerp.execute('res.partner', 'read', partner_id, ['name','vat','supplier'])
        name_partner_existente = partner_existente['name']
        dni_partner_existente = partner_existente['vat']
        supplier_partner_existente = partner_existente['supplier']
        if not supplier_partner_existente:
            editado_supplier = oerp.execute('res.partner', 'write', partner_id, {'supplier':True} )
            print "se pone como proveedor: %s"%editado_supplier
        if vat and dni_partner_existente=="":
            dni = vat
            vals1 = {'vat':dni}
            editado_vat = oerp.execute('res.partner', 'write', partner_id, vals1 )
            print "se edita el cif: %s"%editado_vat
        if nombre and name_partner_existente=="":
            vals2 = {'name':nombre}
            editado_name = oerp.execute('res.partner', 'write', partner_id, vals2 )
            print "se edita el nombre: %s"%editado_name
            
        #busco si el partner tiene account no genérica
        p = oerp.execute('res.partner', 'read', partner_id, ['property_account_payable'])
        if p['property_account_payable']:
            account_id = p['property_account_payable'][0]
            if account_id == 507:
                account_id = _alta_cuenta_proveedor(partner_id, subcta, nombre)
        else:
            account_id = _alta_cuenta_proveedor(partner_id, subcta, nombre)
#         else:
#             if account_id != subcta:
#                 print "CUIDADO"
        res = (partner_id, account_id)
        return res
#        account_id = _alta_cuenta_proveedor(partner_id, cuenta, nombre)
#        vals3 = {'supplier':True, 'property_account_payable': account_id}
#        editado = oerp.execute('res.partner', 'write', partner_id, vals3 )   
 
#        address_ids = oerp.execute('res.partner.address', 'search', [('partner_id', '=', partner_id)])
#        if address_ids:
##            address_id = address_ids[0]
#            existe=0
#            for address_id in address_ids:
#                address_id_street_list = []
#                address_id_street_list = oerp.execute('res.partner.address', 'read', address_id, ['street'])
#                address_id_street = address_id_street_list['street']
#                if address_id_street == record['DOMICILIO']:
#                    existe=1
#            if existe==0:
#                address = {
#                    'partner_id': partner_id,
#                    'type' : 'contact',
#                    'street': record['DOMICILIO'],
#                    'zip': record['CODPOSTAL'],
#                    'city': record['POBLACION'],
#                    'phone': record['TELEF01'],
#                    'fax': record['FAX01'],
#                    'name': record['TITULO'].strip(),
#                    'email': record['EMAIL'],
#                    'active': True,
#                    'company_id': 2,
#                    'country_id': 67,
#                }
#                address_id = oerp.execute('res.partner.address', 'create', address)
#            print "alta de direccion: %s"%address_id
#        else:
#            #alta de direccion principal para ese cliente
#            address = {
#                'partner_id': partner_id,
#                'type' : 'default',
#                'street': record['DOMICILIO'],
#                'zip': record['CODPOSTAL'],
#                'city': record['POBLACION'],
#                'phone': record['TELEF01'],
#                'fax': record['FAX01'],
#                'name': record['TITULO'].strip(),
#                'email': record['EMAIL'],
#                'active': True,
#                'company_id': 2,
#                'country_id': 67,
#            }
#            address_id = oerp.execute('res.partner.address', 'create', address)
#            print "alta de direccion: %s"%address_id

    else:
        partner_id = _alta_partner_y_direccion(nombre, vat)
        account_id = _alta_cuenta_proveedor(partner_id, subcta, nombre)
        vals4 = {'property_account_payable': account_id}
        editado2 = oerp.execute('res.partner', 'write', partner_id, vals4 )
        print "alta de partner completamente nuevo: %s"%partner_id
        res = (partner_id, account_id)
        return res

name_ultimo_asiento_2013 = 6900
asien_previo = 1
w = 0
cont3 = 0
 
for asiento in reader_diario_2013_compras_format:
    if w==0:
        w+=1
        continue
    cont3+=1
    print "recorriendo asientos para importarlos:  %s"%cont3
    
    fecha = asiento[0]
    asien = int(asiento[1])
    subcta = asiento[2]
    concepto = asiento[3]
    ternom = asiento[4]
    ternif = asiento[5]
    baseeuro = asiento[8]
    eurohaber = asiento[9]
    eurodebe = asiento[10]
    iva = asiento[11]
    
    eurohaber = float(eurohaber)
    eurodebe = float(eurodebe)
    
    if eurohaber<0:
        aux=eurohaber*(-1)
        eurohaber=eurodebe
        eurodebe=aux
    elif eurodebe<0:
        aux=eurodebe*(-1)
        eurodebe=eurohaber
        eurohaber=aux
    
#     tipo_cuenta = str(record['COD'])[:3]
#     if tipo_cuenta == "400":
#         i = _import_record_proveedor(tipo_cuenta, i, record, sock, dbname, uid, pwd)
#         
#     account_id
#     partner_id  

    if ternom == "":
        account_args = [('code', '=', subcta)]
        account_ids = oerp.execute('account.account', 'search', account_args)
        if account_ids:    
            account_id = account_ids[0]
        else: 
            account = {
                'name': "/",
                'code' : subcta,
                'parent_id': 477,
                'type': "payable",
                'user_type': 7,
                'active': True,
                'reconcile': True,
            }
            account_id = oerp.execute('account.account', 'create', account)
    else:
        res = _import_record_proveedor(ternom, ternif, subcta)
        partner_id = res[0]
        account_id = res[1]
    
    if fecha[:7]=="2013-01":
        period_id = 4
    elif fecha[:7]=="2013-02":
        period_id = 5
    elif fecha[:7]=="2013-03":
        period_id = 6
    elif fecha[:7]=="2013-04":
        period_id = 7
    else:
        print "ESTA FECHA NO TIENE PERIODO!!!!!!!!!!!!!!!!!!!!!!!!!:  %s"%fecha
        
#    date = time.strptime( fecha , '%Y-%m-%d')
    
    if asien != asien_previo : 
        if ternom == "":
            sin_partner = 1
            move = {
                'company_id': 2,
                'state': "draft",
                'to_check': True,
                'name': name_ultimo_asiento_2013+1,
                'ref': asien,
                'journal_id': 5,
                'period_id': period_id,
                'date': fecha,
            }
            move_id = oerp.execute('account.move', 'create', move)
            name_ultimo_asiento_2013 += 1
            asien_previo = asien
            print "se creó el asiento_id:  %s"%move_id
        else:
            sin_partner = 0
            move = {
                'company_id': 2,
                'state': "draft",
                'to_check': True,
                'name': name_ultimo_asiento_2013+1,
                'ref': asien,
                'journal_id': 5,
                'period_id': period_id,
                'partner_id': partner_id,
                'date': fecha,
            }
            move_id = oerp.execute('account.move', 'create', move)
            name_ultimo_asiento_2013 += 1
            asien_previo = asien
            print "se creó el asiento_id:  %s"%move_id
    
    if sin_partner == 1: 
        move_line = {
            'company_id': 2,
            'currency_id': 1,
            'blocked': False,
            'centralisation': "normal",
            'state': "valid",
    #        'product_uom_id': 
            'move_id': move_id,
            'journal_id': 5,
            'period_id': period_id,
            'account_id': account_id,
            'date': fecha,
            'date_created': fecha,
            'credit': eurohaber,
            'debit': eurodebe,
            'name': concepto,
        }
        move_line_id = oerp.execute('account.move.line', 'create', move_line)
        print "se creó el apunte_id:  %s"%move_line_id
    elif sin_partner == 0:
        move_line = {
            'company_id': 2,
            'currency_id': 1,
            'blocked': False,
            'centralisation': "normal",
            'state': "valid",
    #        'product_uom_id': 
            'move_id': move_id,
            'journal_id': 5,
            'period_id': period_id,
            'partner_id': partner_id,
            'account_id': account_id,
            'date': fecha,
            'date_created': fecha,
            'credit': eurohaber,
            'debit': eurodebe,
            'name': concepto,
        }
        move_line_id = oerp.execute('account.move.line', 'create', move_line)
        print "se creó el apunte_id:  %s"%move_line_id        
        
    
#     if partner_id != 0:
#         vals40 = {'partner_id': partner_id}
#         editadop = oerp.execute('account.move', 'write', move_id, vals40 )
#         editadop2 = oerp.execute('account.move.line', 'write', move_id, vals40 )
 
csv_diario_2013_compras_format.close()