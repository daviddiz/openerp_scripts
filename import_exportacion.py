#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ydbf
import oerplib
import os
import csv
import time
import sys
import unicodedata
import vatnumber

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

#Convierto Agentes.dbf en un csv: Agentes.csv 

# csv_agente = open(ruta_dbf2csv + '/Agentes.csv', 'wb')
# writer_agente = csv.writer(csv_agente, dialect='nuevo_dialecto')
# dbf_agente = ydbf.open(ruta_dbf + '/Agentes.dbf', encoding='cp1252')
# i=0
# cont=0
# for record in dbf_agente:
#     cont+=1
#     print "traspasando dbf de agentes, linea numero:  %s"%cont
#     cabecera=[]
#     if i==0:
#         j=0
#         for key,value in record.iteritems():
#             cabecera.append("valor")
#             cabecera[j]=key
#             j+=1
#         writer_agente.writerow(cabecera)
#         i+=1
#      
#     linea=[]
#     k=0
#     for key, value in record.iteritems():
#         linea.append("valor")
#         linea[k]=value
#         k+=1
#     writer_agente.writerow(linea)
#          
# csv_agente.close()
# dbf_agente.close()
#      
# # Convierto Facclit.dbf (cabeceras de facturas) en un csv con los campos que necesito y las facturas de 2013 
#      
# csv_facclit = open(ruta_dbf2csv + '/Facclit.csv', 'wb')
# writer_facclit = csv.writer(csv_facclit, dialect='nuevo_dialecto')
# dbf_facclit = ydbf.open(ruta_dbf + '/Facclit.dbf', encoding='cp1252')
# i=0
# cont=0
# for record in dbf_facclit:
#     cont+=1
#     print "traspasando dbf de cabeceras de facturas, linea numero:  %s"%cont
#     cabecera=[]
#     if i==0:
#         j=0
#         for key,value in record.iteritems():
#             cabecera.append("valor")
#             cabecera[j]=key
#             j+=1
#         writer_facclit.writerow(cabecera)
#         i+=1
#      
#     linea=[]
#     k=0
#     for key, value in record.iteritems():
#         linea.append("valor")
#         linea[k]=value
#         k+=1
#     writer_facclit.writerow(linea)
#          
# csv_facclit.close()
# dbf_facclit.close()
#      
# # Simplifico el csv para prepararlo para la importacion
#      
# csv_facclit = open(ruta_dbf2csv + '/Facclit.csv', 'rb')
# reader_facclit = csv.reader(csv_facclit, dialect='nuevo_dialecto')
#      
# csv_facclit_mod_2013_final = open(ruta_dbf2csv + '/Facclit_mod_2013_final.csv', 'wb')
# writer_facclit_mod_2013_final = csv.writer(csv_facclit_mod_2013_final, dialect='nuevo_dialecto')
# i=0
# cont2=0
# for linea_facclit in reader_facclit:
#     cont2+=1
#     print "arreglando csv de cabeceras de facturas, linea numero:  %s"%cont2
#     linea=[]
#     if i==0:
#         linea.append(linea_facclit[92])
#         linea.append(linea_facclit[62])
#         linea.append(linea_facclit[0])
#         linea.append(linea_facclit[4])
#         linea.append(linea_facclit[22])
#         linea.append(linea_facclit[28])
#         linea.append(linea_facclit[75])
#         linea.append(linea_facclit[34])
#         linea.append(linea_facclit[48])
#         linea.append(linea_facclit[100])
#         linea.append(linea_facclit[104])
#         linea.append(linea_facclit[107])
#         linea.append(linea_facclit[85])
#         linea.append(linea_facclit[95])
#         writer_facclit_mod_2013_final.writerow(linea)
#         i+=1
#     else:
#         if linea_facclit[62][:4]=="2013":
#             linea.append(linea_facclit[92])
#             linea.append(linea_facclit[62])
#             linea.append(linea_facclit[0])
#             linea.append(linea_facclit[4])
#             linea.append(linea_facclit[22])
#             linea.append(linea_facclit[28])
#             linea.append(linea_facclit[75])
#             linea.append(linea_facclit[34])
#             linea.append(linea_facclit[48])
#             linea.append(linea_facclit[100])
#             linea.append(linea_facclit[104])
#             linea.append(linea_facclit[107])
#             linea.append(linea_facclit[85])
#             linea.append(linea_facclit[95])
#             writer_facclit_mod_2013_final.writerow(linea)
#      
# csv_facclit.close()
# csv_facclit_mod_2013_final.close()
#      
# # Convierto Facclil.dbf (lineas de facturas) en un csv con los campos que necesito y en orden
#      
# csv_facclil = open(ruta_dbf2csv + '/Facclil.csv', 'wb')
# writer_facclil = csv.writer(csv_facclil, dialect='nuevo_dialecto')
# dbf_facclil = ydbf.open(ruta_dbf + '/Facclil.dbf', encoding='cp1252')
# i=0
# cont=0
# for record in dbf_facclil:
#     cont+=1
#     print "traspasando dbf de lineas de facturas, linea numero:  %s"%cont
#     cabecera=[]
#     if i==0:
#         j=0
#         for key,value in record.iteritems():
#             cabecera.append("valor")
#             cabecera[j]=key
#             j+=1
#         writer_facclil.writerow(cabecera)
#         i+=1
#      
#     linea=[]
#     k=0
#     for key, value in record.iteritems():
#         linea.append("valor")
#         linea[k]=value
#         k+=1
#     writer_facclil.writerow(linea)
#          
# csv_facclil.close()
# dbf_facclil.close()
#      
# # Simplifico el csv para prepararlo para la importacion
#      
# csv_facclil = open(ruta_dbf2csv + '/Facclil.csv', 'rb')
# reader_facclil = csv.reader(csv_facclil, dialect='nuevo_dialecto')
#      
# csv_facclil_mod_2013_final = open(ruta_dbf2csv + '/Facclil_mod_2013_final.csv', 'wb')
# writer_facclil_mod_2013_final = csv.writer(csv_facclil_mod_2013_final, dialect='nuevo_dialecto')
# i=0
# cont2=0
# for linea_facclil in reader_facclil:
#     cont2+=1
#     print "arreglando csv de lineas de facturas, linea numero:  %s"%cont2
#     linea=[]
#     if i==0:
#         linea.append(linea_facclil[7])
#         linea.append(linea_facclil[3])
#         linea.append(linea_facclil[5])
#         linea.append(linea_facclil[13])
#         linea.append(linea_facclil[33])
#         linea.append(linea_facclil[39])
#         linea.append(linea_facclil[10])
#         linea.append(linea_facclil[2])
#         linea.append(linea_facclil[8])
#         linea.append(linea_facclil[30])
#         writer_facclil_mod_2013_final.writerow(linea)
#         i+=1
#     else:
#         num_fac = int(linea_facclil[7])
#         importe = float(linea_facclil[5])
#         if (num_fac > 59635 or ((num_fac > 1684) and (num_fac < 10000))) and (importe > 0):
#             linea.append(linea_facclil[7])
#             linea.append(linea_facclil[3])
#             linea.append(linea_facclil[5])
#             linea.append(linea_facclil[13])
#             linea.append(linea_facclil[33])
#             linea.append(linea_facclil[39])
#             linea.append(linea_facclil[10])
#             linea.append(linea_facclil[2])
#             linea.append(linea_facclil[8])
#             linea.append(linea_facclil[30])
#             writer_facclil_mod_2013_final.writerow(linea)
#      
# csv_facclil.close()
# csv_facclil_mod_2013_final.close() 
# cont=0
# for record in dbf_facclil:
#     cont+=1
#     print "traspasando dbf de lineas de facturas, linea numero:  %s"%cont
#     cabecera=[]
#     if i==0:
#         j=0
#         for key,value in record.iteritems():
#             cabecera.append("valor")
#             cabecera[j]=key
#             j+=1
#         writer_facclil.writerow(cabecera)
#         i+=1
#      
#     linea=[]
#     k=0
#     for key, value in record.iteritems():
#         linea.append("valor")
#         linea[k]=value
#         k+=1
#     writer_facclil.writerow(linea)
#          
# csv_facclil.close()
# dbf_facclil.close()
#      
# # Simplifico el csv para prepararlo para la importacion
#      
# csv_facclil = open(ruta_dbf2csv + '/Facclil.csv', 'rb')
# reader_facclil = csv.reader(csv_facclil, dialect='nuevo_dialecto')
#      
# csv_facclil_mod_2013_final = open(ruta_dbf2csv + '/Facclil_mod_2013_final.csv', 'wb')
# writer_facclil_mod_2013_final = csv.writer(csv_facclil_mod_2013_final, dialect='nuevo_dialecto')
# i=0
# cont2=0
# for linea_facclil in reader_facclil:
#     cont2+=1
#     print "arreglando csv de lineas de facturas, linea numero:  %s"%cont2
#     linea=[]
#     if i==0:
#         linea.append(linea_facclil[7])
#         linea.append(linea_facclil[3])
#         linea.append(linea_facclil[5])
#         linea.append(linea_facclil[13])
#         linea.append(linea_facclil[33])
#         linea.append(linea_facclil[39])
#         linea.append(linea_facclil[10])
#         linea.append(linea_facclil[2])
#         linea.append(linea_facclil[8])
#         linea.append(linea_facclil[30])
#         writer_facclil_mod_2013_final.writerow(linea)
#         i+=1
#     else:
#         num_fac = int(linea_facclil[7])
#         importe = float(linea_facclil[5])
#         if (num_fac > 59635 or ((num_fac > 1684) and (num_fac < 10000))) and (importe > 0):
#             linea.append(linea_facclil[7])
#             linea.append(linea_facclil[3])
#             linea.append(linea_facclil[5])
#             linea.append(linea_facclil[13])
#             linea.append(linea_facclil[33])
#             linea.append(linea_facclil[39])
#             linea.append(linea_facclil[10])
#             linea.append(linea_facclil[2])
#             linea.append(linea_facclil[8])
#             linea.append(linea_facclil[30])
#             writer_facclil_mod_2013_final.writerow(linea)
#      
# csv_facclil.close()
# csv_facclil_mod_2013_final.close() 

csv_cliente_no_encontrado = open(ruta_dbf2csv + '/Facclit_cliente_no_encontrado.csv', 'wb')
writer_cliente_no_encontrado = csv.writer(csv_cliente_no_encontrado, dialect='nuevo_dialecto')
      
csv_direccion_no_encontrada = open(ruta_dbf2csv + '/Facclit_direccion_no_encontrada.csv', 'wb')
writer_direccion_no_encontrada = csv.writer(csv_direccion_no_encontrada, dialect='nuevo_dialecto')
      
csv_agent_no_encontrado = open(ruta_dbf2csv + '/Facclit_agent_no_encontrado.csv', 'wb')
writer_agent_no_encontrado = csv.writer(csv_agent_no_encontrado, dialect='nuevo_dialecto')
      
csv_fpago_no_encontrada = open(ruta_dbf2csv + '/Facclit_fpago_no_encontrada.csv', 'wb')
writer_fpago_no_encontrada = csv.writer(csv_fpago_no_encontrada, dialect='nuevo_dialecto')
      
def elimina_tildes(s):
    s=unicode(s)
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
      
#arreglar el formato del código de cuenta para que tenga 10 dígitos
def _arreglar_cuenta(cuenta):
    cuenta = cuenta.replace(" ","")
    cuenta = cuenta[-4:]
    cuenta = "430000"+cuenta
    return cuenta
      
def mod97(digit_string):
    """Modulo 97 for huge numbers given as digit strings.
    This function is a prototype for a JavaScript implementation.
    In Python this can be done much easier: long(digit_string) % 97.
    """
    m = 0
    for d in digit_string:
        m = (m * 10 + int(d)) % 97
    return m
      
#cálculo del formato iban de una cuenta bancaria
def calc_iban(acc_number):
    iban = "ES" + "00" + acc_number
    code     = iban[:2]
    checksum = iban[2:4]
    bban     = iban[4:]
    digits = ""
    for ch in bban.upper():
        if ch.isdigit():
            digits += ch
        else:
            digits += str(ord(ch) - ord("A") + 10)
    for ch in code:
        digits += str(ord(ch) - ord("A") + 10)
    digits += checksum
    checksum = 98 - mod97(digits)
    checksum = (str(checksum)).zfill(2)
    return "ES" + checksum + acc_number
      
#cálculo de los dígitos de control de una cuenta bancaria (ccc)
def digitos_control(entidad, oficina, cuenta):
    def proc(digitos):
#        if not digitos.isdigit() or len(digitos) != 10:
#            raise ValueError('Debe ser numero de 10 digitos: %s' % digitos)
        factores = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        resultado = 11 - sum(int(d)*f for d,f in zip(digitos, factores)) % 11
        if resultado == 10:  return 1
        if resultado == 11:  return 0
        return resultado
    return '%d%d' % (proc('00'+entidad+oficina), proc(cuenta))
      
#validación del cif
def check_vat(nif):
    if ((len(nif)>0) and (len(nif)<9)) or (nif=="") or ((vatnumber.check_vat_es(nif))==False):
        vat = ""
    else:
        vat = "ES" + nif
    return vat
      
#crear nuevo partner y su direccion
def _alta_partner_y_direccion(record, vat, nombre):
    ccodcli = str(record['CCODCLI'])
    comment = "El código de cliente en Facturaplus era: %s"%ccodcli
    if record['COBSCLI']:
        comment += "/n" + record['COBSCLI']
    partner = {
        'name': nombre,
        'ref': record['CCODCLI'],
        'comment': comment,
        'vat': vat,
        'vat_subjected': True,
        'vat_type': '1',
        'company_id': 2,
        'include_in_mod347': True,
        'customer': True,
        'active': True,
    }
    partner_id = oerp.execute('res.partner', 'create', partner)
    address = {
        'partner_id': partner_id,
        'type' : 'default',
        'street': record['CDIRCLI'],
        'zip': record['CPTLCLI'],
        'city': record['CPOBCLI'],
        'phone': record['CTFO1CLI'],
        'fax': record['CFAXCLI'],
        'mobile': record['CTFO2CLI'],
        'name': record['CCONTACTO'].strip(),
        'email': record['EMAIL'],
        'active': True,
        'company_id': 2,
        'country_id': 67,
    }
    address_id = oerp.execute('res.partner.address', 'create', address)
    print "        alta del cliente:  %s"%nombre
    return partner_id
      
#alta de la cuenta contable asociada al cliente
def _alta_cuenta_cliente(partner_id, cuenta, nombre):
    account = {
        'name': nombre,
        'code' : cuenta,
        'parent_id': 518,
        'type': "receivable",
        'user_type': 6,
        'active': True,
        'reconcile': True,
    }
    account_id = oerp.execute('account.account', 'create', account)
    print "        alta de la cuenta:  %s"%cuenta
    editado0 = oerp.execute('res.partner', 'write', partner_id, {'property_account_receivable':account_id,'customer':True} )
    return account_id
      
#alta de la cuenta bancaria (ccc) asociada al cliente
def _alta_banco(record, partner_id):
    record['CENTIDAD'] = (record['CENTIDAD'].replace(" ","")).zfill(4)
    record['CAGENCIA'] = (record['CAGENCIA'].replace(" ","")).zfill(4)
    record['CCUENTA'] = (record['CCUENTA'].replace(" ","")).zfill(10)
    dc = digitos_control(record['CENTIDAD'], record['CAGENCIA'], record['CCUENTA'])
    dc = dc.zfill(2)
    acc_number = record['CENTIDAD'] + record['CAGENCIA'] + dc + record['CCUENTA']
    bank_ids = []
    bank_args = [('code', '=', record['CENTIDAD'])]
    bank_ids = oerp.execute('res.bank', 'search', bank_args)
    iban = calc_iban(acc_number)
           
    if bank_ids:
        bank_id = bank_ids[0]
        bank = {
            'acc_country_id': 67,
            'country_id': 67,    
            'partner_id': partner_id,
            'bank': bank_id,
            'acc_number': acc_number,  
            'state': "bank",
            'default_bank': True,
            'iban': iban,
        }
        bank_partner_id = oerp.execute('res.partner.bank', 'create', bank)
        return bank_partner_id
    return True
      
def alta_cliente(cliente):
    cliente_id = False
    dbf_cliente = ydbf.open(ruta_dbf + '/Clientes.dbf', encoding='cp1252')
    i=0
    cont=0
    for record in dbf_cliente:
        ccodcli = int(record['CCODCLI'])
        if ccodcli == cliente:
            record['CDNICIF'] = record['CDNICIF'].replace(" ","")
            record['CDNICIF'] = record['CDNICIF'].replace("/","")
            record['CDNICIF'] = record['CDNICIF'].replace("-","")
            vat = check_vat(record['CDNICIF'])
                  
            cuenta = _arreglar_cuenta(record['CSUBCTA'])
                  
            nombre = record['CNOMCLI']
            if len(nombre)>40:
                nombre = nombre[:40]
                      
            cliente_id = _alta_partner_y_direccion(record, vat, nombre)
            account_id = _alta_cuenta_cliente(cliente_id, cuenta, nombre)
            banco_id = _alta_banco(record, cliente_id)
            break
#        else:
#            linea = []
#            linea.append(cliente)
#            num_fac_int=int(num_fac)
#            linea.append(num_fac_int)
#            writer_cliente_no_encontrado.writerow(linea)
    dbf_cliente.close()
    return cliente_id
      
#comprobar por el nombre formateado si ya existe el partner
def _comprobar_por_nombre(nombre):
    ids = []
    nombre0 = (nombre).replace(" ","")
    nombre0 = (nombre0).replace(",","")
    nombre0 = (nombre0).replace(";","")
    nombre0 = (nombre0).replace(".","")
    nombre0 = (nombre0).replace("SL","")
    nombre0 = (nombre0).replace("ASSESSORAMENT","")
    nombre0 = (nombre0).replace("ASSESSORES","")
    nombre0 = (nombre0).replace("ASSESSORIA","")
    nombre0 = (nombre0).replace("ASSESSORA","")
    nombre0 = (nombre0).replace("ASSESSORS","")
    nombre0 = (nombre0).replace("ASSESSOR","")
    nombre0 = (nombre0).replace("ASESORÍA","")
    nombre0 = (nombre0).lower()
    nombre0 = elimina_tildes(nombre)
    args = [('active', '=', True)]
    ids_clientes_todos = oerp.execute('res.partner', 'search', args)
    for id in ids_clientes_todos:
        partner_existente = oerp.execute('res.partner', 'read', id, ['name'])
        partner_existente['name'] = (partner_existente['name']).replace(" ","")
        partner_existente['name'] = (partner_existente['name']).replace(",","")
        partner_existente['name'] = (partner_existente['name']).replace(";","")
        partner_existente['name'] = (partner_existente['name']).replace(".","")
        partner_existente['name'] = (partner_existente['name']).replace("SL","")
        partner_existente['name'] = (partner_existente['name']).replace("ASSESSORAMENT","")
        partner_existente['name'] = (partner_existente['name']).replace("ASSESSORES","")
        partner_existente['name'] = (partner_existente['name']).replace("ASSESSORÍA","")
        partner_existente['name'] = (partner_existente['name']).replace("ASSESSORA","")
        partner_existente['name'] = (partner_existente['name']).replace("ASSESSORS","")
        partner_existente['name'] = (partner_existente['name']).replace("ASSESSOR","")
        partner_existente['name'] = (partner_existente['name']).replace("ASESORÍA","")
        partner_existente['name'] = (partner_existente['name']).lower()
        partner_existente['name'] = elimina_tildes(partner_existente['name'])
        if nombre0 == partner_existente['name']:
            ids.append(id)
    return ids
      
      
def _altas_agent(record, prov):
    record['CDNINIF'] = record['CDNINIF'].replace(" ","")
    record['CDNINIF'] = record['CDNINIF'].replace("/","")
    record['CDNINIF'] = record['CDNINIF'].replace("-","")
    vat = check_vat(record['CDNINIF'])
    nombre = record['CAPEAGE'].strip()
    if len(nombre)>40:
        nombre = nombre[:40] 
    ids = []
    if vat:
        args = [('vat', '=', vat)]
        ids = oerp.execute('res.partner', 'search', args)
        if not ids:
            ids = _comprobar_por_nombre(nombre)
    else:
        ids = _comprobar_por_nombre(nombre)
              
    if ids:
        partner_id = ids[0]
        partner_existente = []
        partner_existente = oerp.execute('res.partner', 'read', partner_id, ['name','vat','property_account_receivable','property_account_payable'])
        name_partner_existente = partner_existente['name']
        dni_partner_existente = partner_existente['vat']
        account_receivable_id = partner_existente['property_account_receivable'][0]
        account_payable_id = partner_existente['property_account_payable'][0]
        if account_payable_id==507:
            cuenta_prov = "400000"+str(prov)
            prov+=1
            account = {
                'name': nombre,
                'code' : cuenta_prov,
                'company_id': 2,
                'parent_id': 477,
                'type': "payable",
                'user_type': 7,
                'active': True,
                'reconcile': True,
            }
            account_payable_id = oerp.execute('account.account', 'create', account)
            vals3 = {'property_account_payable': account_payable_id}
            editado = oerp.execute('res.partner', 'write', partner_id, vals3 ) 
        if vat and dni_partner_existente=="":
            dni = vat
            vals1 = {'vat':dni}
            editado_vat = oerp.execute('res.partner', 'write', partner_id, vals1 )
        if nombre and name_partner_existente=="":
            vals2 = {'name':nombre}
            editado_name = oerp.execute('res.partner', 'write', partner_id, vals2 )
        vals4 = {'supplier':True, 'agent':True}
        editado_agent = oerp.execute('res.partner', 'write', partner_id, vals4 )
        address_ids = oerp.execute('res.partner.address', 'search', [('partner_id', '=', partner_id)])
        if address_ids:
#            address_id = address_ids[0]
            existe=0
            for address_id in address_ids:
                address_id_street_list = []
                address_id_street_list = oerp.execute('res.partner.address', 'read', address_id, ['street'])
                address_id_street = address_id_street_list['street']
                if address_id_street == record['CDIRAGE']:
                    existe=1
            if existe==0:
                address = {
                    'partner_id': partner_id,
                    'type' : 'contact',
                    'street': record['CDIRAGE'],
                    'city': record['CPOBAGE'],
                    'name': record['CAPEAGE'].strip(),
                    'active': True,
                    'company_id': 2,
                    'country_id': 67,
                }
                address_id = oerp.execute('res.partner.address', 'create', address)
        else:
            #alta de direccion principal para ese cliente
            address = {
                'partner_id': partner_id,
                'type' : 'default',
                'street': record['CDIRAGE'],
                'city': record['CPOBAGE'],
                'name': record['CAPEAGE'].strip(),
                'active': True,
                'company_id': 2,
                'country_id': 67,
            }
            address_id = oerp.execute('res.partner.address', 'create', address)
            print "alta de direccion: %s"%address_id
    else:
        cuenta_prov = "400000"+str(prov)
        prov+=1
        account = {
            'name': nombre,
            'code' : cuenta_prov,
            'company_id': 2,
            'parent_id': 477,
            'type': "payable",
            'user_type': 7,
            'active': True,
            'reconcile': True,
        }
        account_payable_id = oerp.execute('account.account', 'create', account)
        partner = {
                'name': nombre,
                'vat': vat,
                'agent': True,
                'supplier': True,
                'vat_subjected': True,
                'vat_type': '1',
                'company_id': 2,
                'include_in_mod347': True,
                'active': True,
                'property_account_payable': account_payable_id,
        }
        partner_id = oerp.execute('res.partner', 'create', partner)
              
        address = {
                'partner_id': partner_id,
                'type' : 'default',
                'street': record['CDIRAGE'],
                'city': record['CPOBAGE'],
                'active': True,
                'company_id': 2,
                'country_id': 67,
        }
        address_id = oerp.execute('res.partner.address', 'create', address)
    NCOM6 = int(record['NCOM6'])
    NCOM6 = str(NCOM6) + "%"
    NCOM5 = int(record['NCOM5'])
    NCOM5 = str(NCOM5) + "%"
          
    if NCOM6 != "0%":
        args = [('name', '=', NCOM6)]
        ids = oerp.execute('commission', 'search', args)
        commission_id = ids[0]
    elif NCOM5 != "0%":
        args = [('name', '=', NCOM5)]
        ids = oerp.execute('commission', 'search', args)
        commission_id = ids[0]
    else:
        args = [('name', '=', "0%")]
        ids = oerp.execute('commission', 'search', args)
        commission_id = ids[0]
              
    agent = {
            'name': record['CAPEAGE'],
            'partner_id': partner_id,
            'commission': commission_id,
            'settlement': "m",
    }
          
    agent_id = oerp.execute('sale.agent', 'create', agent)
          
    print "        nuevo agente:  %s"%agent_id
          
    res_partner_agent = {
            'partner_id': partner_id,
            'commission_id': commission_id,
            'agent_id': agent_id,
    }
    res_partner_agent_id = oerp.execute('res.partner.agent', 'create', res_partner_agent)
    return agent_id
      
def alta_factura(factura):
    num_fac = int(factura[0])
    fecha = factura[1]
    agente = factura[2]
    comision = factura[3]
    base = factura[4]
    total_iva = factura[5]
    total = factura[6]
    imp_comision = factura[7]
    cliente = int(factura[8])
    tipo_fac = factura[9]
    fecha_vencimiento = factura[10]
    tipo_pago = factura[11]
    cliente_nombre = factura[12]
    cliente_cif = factura[13]
          
    if tipo_fac == "C":
        type = 'out_refund'
        journal_id = 6
    else:
        type = 'out_invoice'
        journal_id = 4
              
    cliente_args = [('ref', '=', cliente)]
    cliente_ids = oerp.execute('res.partner', 'search', cliente_args)
    if cliente_ids:
        cliente_id = cliente_ids[0]
    else:
        comment = "El código de cliente en Facturaplus era: "+str(cliente)
        cliente_args2 = [('comment', '=', comment)]
        cliente_ids = oerp.execute('res.partner', 'search', cliente_args2)
        if cliente_ids:
            cliente_id = cliente_ids[0]
        else:
            cliente_args2 = [('vat', '=', cliente_cif)]
            cliente_ids = oerp.execute('res.partner', 'search', cliente_args2)
            if cliente_ids:
                cliente_id = cliente_ids[0]
            else:
                cliente_args2 = [('name', '=', cliente_nombre)]
                cliente_ids = oerp.execute('res.partner', 'search', cliente_args2)
                if cliente_ids:
                    cliente_id = cliente_ids[0]
                else:
                    cliente_id = alta_cliente(cliente)
          
    address_args = [('partner_id', '=', cliente_id)]
    address_ids = oerp.execute('res.partner.address', 'search', address_args)
    if address_ids:
        address_id = address_ids[0]
    else:
        linea = []
        linea.append(cliente)
        num_fac_int=int(num_fac)
        linea.append(num_fac_int)
        writer_direcccion_no_encontrada.writerow(linea)
        return False
      
    csv_agentes = open(ruta_dbf2csv + '/Agentes.csv', 'rb')
    reader_agentes = csv.reader(csv_agentes, dialect='nuevo_dialecto')
    ag = 0
    j = 0
    for agente_csv in reader_agentes:
        if j==0:
            j+=1
            continue
        else:
            j+=1
            agente = int(agente)
            a_csv = agente_csv[0]
            a_csv = int(a_csv)
            if a_csv==agente:
                agente_nombre = agente_csv[2]
                agent_args = [('name', '=', agente_nombre)]
                agent_ids = oerp.execute('sale.agent', 'search', agent_args)
                if agent_ids:
                    agent_id = agent_ids[0]
                    ag = 1
                    break
    prov = 1570
    if ag==0:
        ccodagente = int(agente)
        dbf_agente = ydbf.open(ruta_dbf + '/Agentes.dbf', encoding='cp1252')
        find = 0
        for record in dbf_agente:
            record['CCODAGE'] = int(record['CCODAGE'])
            if record['CCODAGE'] == ccodagente:
                find = 1            
                print "        agente encontrado en el dbf"
                agent_id = _altas_agent(record, prov)         
                break    
        if find == 0:
            print "        no se ha encontrado en el dbf el agente:  %s"%ccodagente
#            linea = []
#            linea.append(ccodagente)
#            writer_restos2.writerow(linea)
#            continue
        dbf_agente.close()
              
        linea = []
        linea.append(agente)
        writer_agent_no_encontrado.writerow(linea)
          
    payment_term_args = [('name', '=', "180 días")]
    payment_term_ids = oerp.execute('account.payment.term', 'search', payment_term_args)
          
    if not payment_term_ids:
        term = {
            'active': True,
            'note': "180 días",
            'name': "180 días",
            }
        p_term = oerp.execute('account.payment.term', 'create', term)
        term_line = {
                'payment_id': p_term,
                'name': "180 días",
                'sequence': 5,
                'days2': 0,
                'days': 180,
                'value': "balance",
                }
        p_term_line = oerp.execute('account.payment.term.line', 'create', term_line)
          
    acc = oerp.execute('res.partner', 'read', cliente_id, ['property_account_receivable'])
    account_id = acc['property_account_receivable'][0]
    comision
    fecha_p = time.strptime( fecha , '%Y-%m-%d')
    mes = fecha_p.tm_mon
    if mes==1:
        period_id=4
    elif mes==2:
        period_id=5
    elif mes==3:
        period_id=6
    elif mes==4:
         period_id=7
    elif mes==5:
         period_id=8
    elif mes==6:
         period_id=9
    elif mes==7:
         period_id=10
    elif mes==8:
         period_id=11
    elif mes==9:
         period_id=12
    elif mes==10:
         period_id=13
    elif mes==11:
         period_id=14
    elif mes==12:
         period_id=15
      
    if tipo_pago in ("0", "1", "CO"):
        payment_type = 6
        payment_term =  2
    elif tipo_pago=="2":
        payment_type = 1
        payment_term =  3
    elif tipo_pago=="34":
        payment_type = 1
        payment_term =  8
    elif tipo_pago=="8":
        payment_type = 1
        payment_term =  4
    elif tipo_pago=="15":
        payment_type = 1
        payment_term =  2
    elif tipo_pago=="18":
        payment_type = 1
        payment_term =  5
    elif tipo_pago=="29":
        payment_type = 1
        payment_term =  10
    elif tipo_pago=="10":
        payment_type = 4
        payment_term =  3
    elif tipo_pago=="13":
        payment_type = 4
        payment_term =  5
    elif tipo_pago=="11":
        payment_type = 3
        payment_term =  3
    elif tipo_pago=="22":
        payment_type = 3
        payment_term =  2
    elif tipo_pago=="14":
        payment_type = 3
        payment_term =  5
    elif tipo_pago=="16":
        payment_type = 3
        payment_term =  4
    elif tipo_pago=="19":
        payment_type = 6
        payment_term =  3
    elif tipo_pago=="12":
        payment_type = 2
        payment_term =  2
    elif tipo_pago=="17":
        payment_type = 2
        payment_term =  5
    elif tipo_pago=="20":
        payment_type = 2
        payment_term =  3
    elif tipo_pago=="21":
        payment_type = 2
        payment_term =  3
    elif tipo_pago=="23":
        payment_type = 2
        payment_term =  4
    elif tipo_pago=="24":
        payment_type = 2
        payment_term =  2
    elif tipo_pago=="26":
        payment_type = 2
        payment_term =  10
    elif tipo_pago=="31":
        payment_type = 2
        payment_term =  5
    elif tipo_pago=="33":
        payment_type = 2
        payment_term =  9
    elif tipo_pago=="30":
        payment_type = 2
        payment_term = 11
    else:
        #######################   alta de la forma de pago   ##################################################
        linea = []
        linea.append(tipo_pago)
        writer_fpago_no_encontrada.writerow(linea)
        return False
          
    factura = {
        'type': type,
        'operation_key': "Nothing",
        'number_tickets': 0,
        'company_id': 2,
        'currency_id': 1,
        'state': "draft",
        'partner_id': cliente_id,
        'address_invoice_id': address_id,
        'address_contact_id': address_id,
        'journal_id': journal_id,
        'account_id': account_id,
        'agent_id': agent_id,
        'date_invoice': fecha,
        'period_id': period_id,
#             'date_due': fecha_vencimiento,
        'payment_term': payment_term,
        'payment_type': payment_type,
        'name': num_fac,
    }
    factura_id = oerp.execute('account.invoice', 'create', factura)
    print "se creó la factura_id:  %s"%factura_id
    return factura_id
      
#Comprobar si ya existen las facturas o si han sido modificadas para editarlas o crearlas en OpenERP
      
csv_fac_editadas = open(ruta_dbf2csv + '/Facclit_fac_editadas.csv', 'wb')
writer_fac_editadas = csv.writer(csv_fac_editadas, dialect='nuevo_dialecto')
      
csv_fac_nuevas = open(ruta_dbf2csv + '/Facclit_fac_nuevas.csv', 'wb')
writer_fac_nuevas = csv.writer(csv_fac_nuevas, dialect='nuevo_dialecto')
      
csv_facturas = open(ruta_dbf2csv + '/Facclit_mod_2013_final.csv', 'rb')
reader_facturas = csv.reader(csv_facturas, dialect='nuevo_dialecto')
      
primera_linea = 0
cont3 = 0
for factura in reader_facturas:
    cont3+=1
    print "revisando la factura numero:  %s"%cont3
    if primera_linea==0:
        primera_linea+=1
        continue
    else:
        num_fac = factura[0]
#        lim = int(num_fac)
#        lim = 2000
#        if (lim<1862) or (lim>5000 and lim<62617):
#            continue
#        else:
        fec_fac = factura[1]
        factura_args = [('name', '=', num_fac)]
        factura_ids = oerp.execute('account.invoice', 'search', factura_args)
        if factura_ids:
            factura_id = factura_ids[0]
            fec_fac_openerp = oerp.execute('account.invoice', 'read', factura_id, ['date_invoice'])
            fec_fac_openerp = fec_fac_openerp['date_invoice']
            if fec_fac_openerp != fec_fac:
                   oerp.write('account.invoice', factura_id, {'date_invoice': fec_fac})
                   print "        se ha modificado la fecha de una factura:  %s"%cont3
                   linea = []
                   linea.append(num_fac)
                   linea.append("editada")
                   writer_fac_editadas.writerow(linea)
                         
            p = oerp.execute('account.invoice', 'read', factura_id, ['partner_id'])
            partner = (p['partner_id'])[0]
            p_bank_args = [('partner_id', '=', partner),('default_bank', '=', True)]
            p_bank_ids = oerp.execute('res.partner.bank', 'search', p_bank_args)
            if p_bank_ids:
                p_bank_id = p_bank_ids[0]
                bank =  oerp.execute('account.invoice', 'write', factura_id, {'partner_bank_id': p_bank_id} )
        else:
            #doy de alta la factura porque no existe
            f_nueva_id = alta_factura(factura)
            linea = []
            linea.append(int(factura[0]))
            linea.append("nueva")
            writer_fac_nuevas.writerow(linea)
                  
            p = oerp.execute('account.invoice', 'read', f_nueva_id, ['partner_id'])
            partner = (p['partner_id'])[0]
            p_bank_args = [('partner_id', '=', partner),('default_bank', '=', True)]
            p_bank_ids = oerp.execute('res.partner.bank', 'search', p_bank_args)
            if p_bank_ids:
                p_bank_id = p_bank_ids[0]
                bank =  oerp.execute('account.invoice', 'write', f_nueva_id, {'partner_bank_id': p_bank_id} )
      
csv_cliente_no_encontrado.close()
csv_direccion_no_encontrada.close()
csv_agent_no_encontrado.close()
csv_fpago_no_encontrada.close()
csv_facturas.close()
csv_fac_nuevas.close()
csv_fac_editadas.close()
      
# Importar líneas de facturas
      
csv_factura_no_encontrada = open(ruta_dbf2csv + '/Facclil_factura_no_encontrada.csv', 'wb')
writer_factura_no_encontrada = csv.writer(csv_factura_no_encontrada, dialect='nuevo_dialecto')
      
csv_producto_no_encontrado = open(ruta_dbf2csv + '/Facclil_producto_no_encontrado.csv', 'wb')
writer_producto_no_encontrado = csv.writer(csv_producto_no_encontrado, dialect='nuevo_dialecto')
      
csv_facclil_mod_2013_final = open(ruta_dbf2csv + '/Facclil_mod_2013_final.csv', 'rb')
reader_facclil_mod_2013_final = csv.reader(csv_facclil_mod_2013_final, dialect='nuevo_dialecto')
      
cont2 = 0
j = 0
newlin = 0
for linea_factura in reader_facclil_mod_2013_final:
    cont2+=1
    print "traspasando lineas de facturas, linea numero:  %s"%cont2
    if j==0:
        j+=1
        continue
    else:
        j+=1
        num_fac = linea_factura[0]
#        lim = int(num_fac)
#        lim = 2000
#        if (lim<1862) or (lim>5000 and lim<62617):
#            continue
#        else:
        producto = linea_factura[1]
        precio_unidad = linea_factura[2]
        cantidad = linea_factura[3]
        total = linea_factura[4]
        tipo_iva = linea_factura[5]
        agente = linea_factura[7]
        comision = linea_factura[8]
        fecha = linea_factura[9]
              
        producto_descripcion = producto
              
        invoice_args = [('name', '=', num_fac)]
        invoice_ids = oerp.execute('account.invoice', 'search', invoice_args)
        if invoice_ids:
            invoice = invoice_ids[0]
            ref = oerp.execute('account.invoice', 'read', invoice, ['name'])
            ref = ref['name']
                  
            fac_nueva=0
            csv_fac_nuevas = open(ruta_dbf2csv + '/Facclit_fac_nuevas.csv', 'rb')
            reader_fac_nuevas = csv.reader(csv_fac_nuevas, dialect='nuevo_dialecto')
            for lf in reader_fac_nuevas:
                if lf[0]==ref:
                    fac_nueva=1
                    break
            csv_fac_nuevas.close()
            if fac_nueva==0:
                continue
        else:
            linea = []
            linea.append(num_fac)
            linea.append(producto)
            writer_factura_no_encontrada.writerow(linea)
            continue
              
        ir_translation_args = [('name', '=', "product.template,name")]
        ir_translation_ids = oerp.execute('ir.translation', 'search', ir_translation_args)
        aux = 0
        for ir_trans in ir_translation_ids:
            ir_trans_product_name = oerp.execute('ir.translation', 'read', ir_trans, ['value'])
            ir_trans_product_name = ir_trans_product_name['value']
            producto = elimina_tildes(producto)
            producto = (producto.split("("))[0]
            producto = producto.strip()
            producto = (producto).replace(".","")
            producto = (producto).replace("  "," ")
            producto = producto.lower()
            producto = (producto).replace("ellaboracio","elaboracio")
            producto = (producto).replace("subcontractacio","subcontratacio")
            ir_trans_product_name = elimina_tildes(ir_trans_product_name)
            ir_trans_product_name = (ir_trans_product_name.split("("))[0]
            ir_trans_product_name = ir_trans_product_name.strip()
            ir_trans_product_name = (ir_trans_product_name).replace(".","")
            ir_trans_product_name = (ir_trans_product_name).replace("  "," ")
            ir_trans_product_name = ir_trans_product_name.lower()
            ir_trans_product_name = (ir_trans_product_name).replace("ellaboracio","elaboracio")
            ir_trans_product_name = (ir_trans_product_name).replace("subcontractacio","subcontratacio")
            if producto == ir_trans_product_name:
                product_id = oerp.execute('ir.translation', 'read', ir_trans, ['res_id'])
                product_id = product_id['res_id']
                aux = 1
                break
              
        if aux == 0:
            linea = []
            linea.append(producto)
            writer_producto_no_encontrado.writerow(linea)
            continue
              
        res = "product.template,"+str(product_id)
        property_args = [('res_id', '=', res)]
        property_ids = oerp.execute('ir.property', 'search', property_args)
        property_id = property_ids[0]
        value_reference = oerp.execute('ir.property', 'read', property_id, ['value_reference'])
        val_ref = value_reference['value_reference']
        cuenta = (val_ref.split(","))[1]
        precio_unidad = float(precio_unidad)
        cantidad = float(cantidad)
        p = oerp.execute('account.invoice', 'read', invoice, ['partner_id'])
        partner = (p['partner_id'])[0]
              
#        tax_args = [('prod_id', '=', product_id)]
#        taxes_rel_ids = oerp.execute('product_taxes_rel', 'search', tax_args)
#        invoice_line_tax = [(6, 0, taxes_rel_ids)]
      
        product_taxes_m2m = oerp.execute('product.template', 'read', product_id, ['taxes_id'])
        taxes = product_taxes_m2m['taxes_id']
        invoice_line_tax = [(6, 0, taxes)]
              
#dar de alta el agente y la comision:   invoice.line.agent : agent_id , commission_id
#ver si al meter el producto , se cubren automáticamente la descripcion (name) y el impuesto
#calcular impuestos , botón de la cabecera de la factura para meter impuestos
              
        linea_factura = {
            'origin': num_fac,
            'invoice_id': invoice,
            'uos_id': 1,
            'product_id': product_id,
            'name': producto_descripcion,
            'account_id': cuenta,
            'price_unit': precio_unidad,
            'quantity': cantidad,
            'invoice_line_tax_id': invoice_line_tax,
#                'account_analytic_id': ,
            'company_id': 2,
            'partner_id': partner,
            'state': "article",
        }
        linea_factura_id = oerp.execute('account.invoice.line', 'create', linea_factura)
        newlin += 1
      
print "numero de lineas nuevas:  %s"%newlin
              
csv_facclil_mod_2013_final.close()
csv_factura_no_encontrada.close()
csv_producto_no_encontrado.close()