#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ydbf
import oerplib
import os
import csv
import time
import sys

host= 'localhost'
protocol= 'xmlrpc'
port=8069
dbname = 'test'
username = 'XXXXX'
pwd = 'XXXXX'

oerp = oerplib.OERP(host, dbname, protocol, port)
user = oerp.login(username, pwd)

csv.register_dialect('nuevo_dialecto', delimiter=',')

csv_cuenta_no_existe = open('/home/likewise-open/HELIOS/ddiz/openerp/trunk/oerp/addons/prevencontrol_import/data/dbf2csv/Diario_cuenta_no_existe.csv', 'wb')
writer_cuenta_no_existe = csv.writer(csv_cuenta_no_existe, dialect='nuevo_dialecto')

csv_asiento_apertura = open('/home/likewise-open/HELIOS/ddiz/openerp/trunk/oerp/addons/prevencontrol_import/data/dbf2csv/Asiento_Apertura_Diario_mod.csv', 'rb')
reader_asiento_apertura = csv.reader(csv_asiento_apertura, dialect='nuevo_dialecto')

cont=0
i=0
for apunte in reader_asiento_apertura:
    cont+=1
    print "asiento de apertura, apunte numero:  %s"%cont
    if i==0:
        i+=1
        continue
    else:
        i+=1
        subcta = apunte[0]
        haber = apunte[1]
        debe = apunte[2]
        
        haber = float(haber)
        debe = float(debe)
        
        if subcta[:2]=="40" or subcta[:2]=="43":
            subcta1 = subcta[:2]
            subcta2 = subcta[-4:]
            subcta = subcta1 + "0000" + subcta2
        elif subcta[:3]=="475":
            subcta = subcta + "000"
        else:
            subcta1 = subcta[:4]
            subcta2 = subcta[-3:]
            subcta = subcta1 + "000" + subcta2
            
        if len(subcta)!=10:
            sys.exit("Error! longitud de subcta no correcta")
            
        cuenta_args = [('code', '=', subcta)]
        cuenta_ids = oerp.execute('account.account', 'search', cuenta_args)
        
        if cuenta_ids:
            cuenta_id = cuenta_ids[0]
        else:
#            sys.exit("cuenta no encontrada")
            linea = []
            linea.append(subcta)
            writer_cuenta_no_existe.writerow(linea)
            continue
            
        cuenta_nombre = (oerp.execute('account.account', 'read', cuenta_id, ['name']))['name']
            
        apunte = {
            'company_id': 2,
            'currency_id': 1,
            'blocked': False,
            'centralisation': "normal",
            'move_id': 1,
            'journal_id': 12,
            'period_id': 1,
            'date': "2013-01-01",
            'date_created': "2013-01-01",
#            'state': "valid",
            'account_id': cuenta_id,
            'credit': haber,
            'debit': debe,
            'name': cuenta_nombre,
        }
        apunte_id = oerp.execute('account.move.line', 'create', apunte)
        print "se creó el apunte_id:  %s"%apunte_id
        
    
csv_cuenta_no_existe.close()
csv_asiento_apertura.close()