#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import psycopg2.extensions
import sys
import oerplib
import os
import time
from datetime import date
import string

host= 'localhost'
protocol= 'xmlrpc'
port=8069
dbname = 'test'
username = 'XXXXX'
pwd = 'XXXXX'

oerp = oerplib.OERP(host, dbname, protocol, port)
user = oerp.login(username, pwd)

host1= 'localhost'
port1=5432
dbname1 = 'test'
username1 = 'XXXXX'
pwd1 = 'XXXXX'

connector = psycopg2.connect('host=%s port=%s dbname=%s user=%s password=%s' % (host1,port1,dbname1,username1,pwd1))
cursor = connector.cursor()

t_max=0
t0 = time.time()
cont=0

number_factura = 1099
number_abono = 26 

facturas_encontradas_cero=0
facturas_encontradas_una=0
facturas_encontradas_mas_de_una=0
asientos_factura_no_encontrada=[]
asientos_factura_encontrada=[]
asientos_factura_encontrada_mas_de_una=[]
error=0

asientos_arreglar_args = [('journal_id', 'in', [5,7]), ('period_id', 'in', [4,5,6,7])]
asientos_arreglar_ids = oerp.execute('account.move', 'search', asientos_arreglar_args)
print "Numero de asientos a recorrer: %s"%len(asientos_arreglar_ids)

for asientos_arreglar_id in asientos_arreglar_ids:
    cont+=1
    print cont
    
    number_abono+=1
    number_factura+=1
    
    asiento = oerp.get('account.move').browse(asientos_arreglar_id)
    fecha_asiento = asiento.date.strftime( '%Y-%m-%d')
    diario = asiento.journal_id.id
    periodo = asiento.period_id.id
    asiento_name = asiento.name
    asiento_ref = asiento.ref
    asiento_narration = asiento.narration
    proveedor_id = asiento.partner_id.id
    add = oerp.execute('res.partner.address', 'search', [('partner_id', '=', proveedor_id)])
    address_id = add[0]
#     bank = oerp.execute('res.partner.bank', 'search', [('partner_id', '=', proveedor_id)])
#     if bank:
#         bank_id = bank[0]
#     else:
#         bank_id=False
    if diario==5:
        number_factura+=1
        number = "FCOM/2013/" + string.zfill(number_factura, 3)  
        type="in_invoice"
    elif diario==7:
        number_abono+=1
        number = "ACOM/2013/" + string.zfill(number_abono, 3)
        type="in_refund"
    
    tax=0.00
    tax_irpf=0.00
    total=0.00
    base=0.00
    acc_invoice_tax = []
    invoice_line_tax_472 = 0
    apuntes_472 = []
    invoice_line_tax_475 = 0
    apuntes_475 = []
    
    apuntes = oerp.execute('account.move.line', 'search', [('move_id', '=', asientos_arreglar_id)])
    for apunte in apuntes:
        account_id = oerp.get('account.move.line').browse(apunte).account_id.id
        account_code = oerp.get('account.account').browse(account_id).code
        
        if account_code[:3]=="472":
            acc_472 = account_id
            invoice_line_tax_472+=1
            cuota_iva_code_id = oerp.get('account.move.line').browse(apunte).tax_code_id.id
            apuntes_472.append((apunte,cuota_iva_code_id, acc_472))
            if diario==5:
                tax = oerp.get('account.move.line').browse(apunte).debit
            elif diario==7:
                tax = oerp.get('account.move.line').browse(apunte).credit
#             total_debit += oerp.get('account.move.line').browse(apunte).debit
#             total_credit += oerp.get('account.move.line').browse(apunte).credit
#             apu_472.append(apunte)
        elif account_code[:3]=="400":
            acc = account_id
            nombre = oerp.get('account.move.line').browse(apunte).name
            if diario==5:
                total = oerp.get('account.move.line').browse(apunte).credit
            elif diario==7:
                total = oerp.get('account.move.line').browse(apunte).debit
#             total_debit += oerp.get('account.move.line').browse(apunte).debit
#             total_credit += oerp.get('account.move.line').browse(apunte).credit
#             apu_400.append(apunte)
#             if asiento.journal_id.id==5:
#                 total = oerp.get('account.move.line').browse(apunte).credit
#             elif asiento.journal_id.id==7:
#                 total = oerp.get('account.move.line').browse(apunte).debit
        elif account_code[:3]=="475":
            acc_475 = account_id
            invoice_line_tax_475+=1
            cuota_irpf_code_id = oerp.get('account.move.line').browse(apunte).tax_code_id.id
            apuntes_475.append((apunte,cuota_irpf_code_id,acc_475))
            if diario==5:
                tax_irpf = oerp.get('account.move.line').browse(apunte).credit
            elif diario==7:
                tax_irpf = oerp.get('account.move.line').browse(apunte).debit
#             total_debit += oerp.get('account.move.line').browse(apunte).debit
#             total_credit += oerp.get('account.move.line').browse(apunte).credit
#             apu_475.append(apunte)
        elif (account_code[:1]=="2" or account_code[:1]=="6") and ((diario==5 and oerp.get('account.move.line').browse(apunte).debit>0.00) or (diario==7 and oerp.get('account.move.line').browse(apunte).credit>0.00)):
            account_line_id = account_id
            if diario==5:
                base = oerp.get('account.move.line').browse(apunte).debit
            elif diario==7:
                base = oerp.get('account.move.line').browse(apunte).credit
        else:
            error+=1
#             total_debit += oerp.get('account.move.line').browse(apunte).debit
#             total_credit += oerp.get('account.move.line').browse(apunte).credit
#             apu_otro.append(apunte)
    
    operation_key = "Nothing"
    company_id = 2
    currency_id = 1
    state = "paid"
    payment_term = 1
    payment_type = 1
    user_id = 3
    reference_type = "none"
    reconciled = False
    residual = 0.0
    is_ticket_summary = False
    partner_id = proveedor_id
    journal_id = diario
    period_id = periodo
    move_id = asientos_arreglar_id
    move_name = asiento_name
    address_invoice_id = address_id
    address_contact_id = address_id
#     partner_bank_id = bank_id
    date_invoice = fecha_asiento
    invoice_number = number
    reference = asiento_ref
    name = nombre
    account_id = acc
    check_total = total
    amount_total = total
    cc_amount_total = total
    amount_tax = tax+tax_irpf
    cc_amount_tax = tax+tax_irpf
    amount_untaxed = base
    cc_amount_untaxed = base
    
    ############# alta de factura ########################################
    cursor.execute(
        """INSERT INTO account_invoice (type, number, operation_key, company_id, currency_id, state, payment_term, payment_type, user_id, reference_type, reconciled, residual, is_ticket_summary, partner_id, journal_id, period_id, move_id, move_name, address_invoice_id, address_contact_id, date_invoice, invoice_number, reference, name, account_id, check_total, amount_total, cc_amount_total, amount_tax, cc_amount_tax, amount_untaxed, cc_amount_untaxed )
                                VALUES (%s  , %s    , %s           , %s        , %s         , %s   , %s          , %s          , %s     , %s            , %s        , %s      , %s               , %s        , %s        , %s       , %s     , %s       , %s                , %s                , %s          , %s            , %s       , %s  , %s        , %s         , %s          , %s             , %s        , %s           , %s            , %s) RETURNING number;""",
                                       (type, number, operation_key, company_id, currency_id, state, payment_term, payment_type, user_id, reference_type, reconciled, residual, is_ticket_summary, partner_id, journal_id, period_id, move_id, move_name, address_invoice_id, address_contact_id, date_invoice, invoice_number, reference, name, account_id, check_total, amount_total, cc_amount_total, amount_tax, cc_amount_tax, amount_untaxed, cc_amount_untaxed))
    number_factura_nueva = cursor.fetchone()[0]
    connector.commit()
    print "NUEVA FACTURA CREADA"
    
    factura_nueva_ids = oerp.execute('account.invoice', 'search', [('number', '=', number_factura_nueva)])
    factura_nueva_id = factura_nueva_ids[0]
    
    uos_id = 1
    discount = 0.00
    sequence = 0
    state2 = "article"
    name = nombre
    invoice_id = factura_nueva_id
    quantity = 1
    price_unit = base 
    price_subtotal = base
    partner_id = proveedor_id
    
    ############# alta de linea factura ########################################
    cursor.execute(
        """INSERT INTO account_invoice_line (uos_id, company_id, discount, sequence, state , account_id     , name, invoice_id, quantity, price_unit, price_subtotal, partner_id)
                                VALUES      (%s    , %s        , %s      , %s      , %s    , %s             , %s  , %s        , %s      , %s        , %s            , %s) RETURNING *;""",
                                            (uos_id, company_id, discount, sequence, state2, account_line_id, name, invoice_id, quantity, price_unit, price_subtotal, partner_id))
    linea_nueva_id = cursor.fetchone()[0]
    connector.commit()
    print "    NUEVA LINEA DE FACTURA CREADA"
    
    ############# alta de lineas de impuestos ########################################
    seq = 0
    manual = False
    acc_tax_code_id = []
    
    for apunte_472 in apuntes_472:
        tax_code = apunte_472[1]
        ac=apunte_472[2]
        if tax_code==187:
            base_code=3
            acc_tax_code_id.append(121)
        elif tax_code==94:
            base_code=40
            acc_tax_code_id.append(2)
        elif tax_code==93:
            base_code=39
            acc_tax_code_id.append(3)
        elif tax_code==91:
            base_code=37
            acc_tax_code_id.append(9)
        elif tax_code==90:
            base_code=36
            acc_tax_code_id.append(7)
        elif tax_code==89:
            base_code=35
            acc_tax_code_id.append(5)
        elif tax_code==88:
            base_code=34
            acc_tax_code_id.append(122)
        else:
            print "ERRRRRRRRRRRRRRRRRRORRRRRRRRRRR"
            
        if diario==5:
            tax_am = tax
            am = tax
            ba_am = base
            ba = base
        elif diario==7:
            tax_am = -tax
            am = tax
            ba_am = -base
            ba = base
        cursor.execute(
            """INSERT INTO account_invoice_tax (sequence, company_id, manual, tax_amount, base_amount , amount , base, tax_code_id, base_code_id, account_id , invoice_id      , name)
                                    VALUES     (%s      , %s        , %s    , %s        , %s          , %s     , %s  , %s         , %s          , %s         , %s              , %s) RETURNING *;""",
                                               (seq     , company_id, manual, tax_am    , ba_am       , am     , ba  , tax_code   , base_code   , ac         , factura_nueva_id, name))
        linea_tax_nueva_id = cursor.fetchone()[0]
        connector.commit()
        print "            NUEVA LINEA DE IMPUESTOS CREADA"
        seq+=1
        
        
    for apunte_475 in apuntes_475:
        tax_code = apunte_475[1]
        ac=apunte_475[2]
        if tax_code==162:
            base_code=152
            acc_tax_code_id.append(124)
        elif tax_code==158:
            base_code=148
            acc_tax_code_id.append(127)
        elif tax_code==157:
            base_code=147
            acc_tax_code_id.append(125)
        elif tax_code==154:
            base_code=144
            acc_tax_code_id.append(126)
        else:
            print "ERRRRRRRRRRRRRRRRRRORRRRRRRRRRR"
            
        if diario==5:
            tax_am = -tax_irpf
            am = -tax_irpf
            ba_am = base
            ba = base
        elif diario==7:
            tax_am = tax_irpf
            am = -tax_irpf
            ba_am = -base
            ba = base
        cursor.execute(
            """INSERT INTO account_invoice_tax (sequence, company_id, manual, tax_amount, base_amount , amount , base, tax_code_id, base_code_id, account_id , invoice_id      , name)
                                    VALUES     (%s      , %s        , %s    , %s        , %s          , %s     , %s  , %s         , %s          , %s         , %s              , %s) RETURNING *;""",
                                               (seq     , company_id, manual, tax_am    , ba_am       , am     , ba  , tax_code   , base_code   , ac         , factura_nueva_id, name))
        linea_tax_nueva_id = cursor.fetchone()[0]
        connector.commit()
        print "            NUEVA LINEA DE IMPUESTOS CREADA"
        seq+=1
        
    for t in acc_tax_code_id:
        cursor.execute(
            """INSERT INTO account_invoice_line_tax (invoice_line_id, tax_id)
                                    VALUES          (%s             , %s    ) RETURNING *;""",
                                                    (linea_nueva_id , t))
        linea_t_nueva_id = cursor.fetchone()[0]
        connector.commit()
        print "                        NUEVA SUB-LINEA DE IMPUESTOS CREADA"
        
print error
print time.time()-t0