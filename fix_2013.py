#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
#note that we have to import the Psycopg2 extras library! modifico porque si
import psycopg2.extras
import psycopg2.extensions
import sys
import os
import time
import string
from datetime import date
import oerplib

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

####################### 1.- BORRAR FACTURAS Y ABONOS DE COMPRAS DE ENRO-ABRIL 2013
print "1.- BORRAR FACTURAS Y ABONOS DE COMPRAS DE ENRO-ABRIL 2013"
  
d1 = cursor.execute("""DELETE FROM account_invoice_line_tax WHERE invoice_line_id=ANY(
    SELECT id FROM account_invoice_line
    WHERE invoice_id=ANY(
        SELECT id FROM account_invoice
        WHERE (account_invoice.journal_id=5 or account_invoice.journal_id=7) and 
              (account_invoice.period_id=4 or account_invoice.period_id=5 or 
              account_invoice.period_id=6 or account_invoice.period_id=7)));""")
connector.commit()
   
d2 = cursor.execute("""DELETE FROM account_invoice_tax WHERE invoice_id=ANY(
    SELECT id FROM account_invoice
    WHERE (account_invoice.journal_id=5 or account_invoice.journal_id=7) and 
          (account_invoice.period_id=4 or account_invoice.period_id=5 or 
          account_invoice.period_id=6 or account_invoice.period_id=7));""")
connector.commit()
   
d3 = cursor.execute("""DELETE FROM account_invoice_line WHERE invoice_id=ANY(
    SELECT id FROM account_invoice
    WHERE (account_invoice.journal_id=5 or account_invoice.journal_id=7) and 
          (account_invoice.period_id=4 or account_invoice.period_id=5 or 
          account_invoice.period_id=6 or account_invoice.period_id=7));""")
connector.commit()
   
d4 = cursor.execute("""DELETE FROM account_invoice 
    WHERE (account_invoice.journal_id=5 or account_invoice.journal_id=7) and 
          (account_invoice.period_id=4 or account_invoice.period_id=5 or 
          account_invoice.period_id=6 or account_invoice.period_id=7);""")
connector.commit()
  
####################### 2.- CREAR APUNTE QUE REPRESENTE LA BASE PARA LOS ASIENTOS CON APUNTES 475 IRPF
print "2.- CREAR APUNTE QUE REPRESENTE LA BASE PARA LOS ASIENTOS CON APUNTES 475 IRPF"
  
cursor.execute(
    """SELECT 
        *
    FROM account_move_line,account_account 
    WHERE (account_move_line.account_id=account_account.id) and (account_move_line.journal_id=5) and 
          (account_move_line.period_id=4 or account_move_line.period_id=5 or account_move_line.period_id=6 or
           account_move_line.period_id=7) and account_account.code like '475%';""")
apuntes_cuota_irpf = cursor.fetchall()
for apunte in apuntes_cuota_irpf:
    journal_id = apunte[6]
    period_id = apunte[21]
    date_created = apunte[22]
    date = apunte[23]
    partner_id = apunte[9]
    move_id = apunte[24]
    ref = apunte[19]
    name=apunte[25]
      
    currency_id = 1
    blocked = False
    credit = 0.00
    debit = 0.00
    tax_amount=0.00
    quantity=0.00
    state = "valid"
    centralisation = "normal"
    amount_currency = 0.00
    received_check = False
    company_id=2
    tax_code_id=152
      
    cursor.execute(
        """SELECT 
            id,credit,debit,account_id
        FROM account_move_line
        WHERE account_move_line.move_id=%i;"""%move_id)
    base = cursor.fetchall()
    for b in base:
        b_account_id = oerp.get('account.move.line').browse(b[0]).account_id.id
        b_account_code = oerp.get('account.account').browse(b_account_id).code
        if (b_account_code[:1]=="6" or b_account_code[:1]=="2") and b[2]>0.0:
            account_id=b_account_id
            tax_amount=b[2]
            break
          
    cursor.execute(
        """INSERT INTO account_move_line (journal_id, currency_id, partner_id, blocked, credit, centralisation, company_id, tax_code_id, state, debit, ref, account_id, period_id, date_created, date, move_id, name, tax_amount, amount_currency, quantity, received_check)
                                  VALUES (%s        , %s         , %s        , %s     , %s    , %s            , %s        , %s         , %s   , %s   , %s , %s        , %s       , %s          , %s  , %s     , %s  , %s        , %s             , %s      , %s            );""",
                                         (journal_id, currency_id, partner_id, blocked, credit, centralisation, company_id, tax_code_id, state, debit, ref, account_id, period_id, date_created, date, move_id, name, tax_amount, amount_currency, quantity, received_check))
    connector.commit()
      
####################### 3.- CREAR FACTURAS, SUS LINEAS Y SUS IMPUESTOS A PARTIR DE LOS ASIENTOS ENERO-ABRIL 2013
print "3.- CREAR FACTURAS, SUS LINEAS Y SUS IMPUESTOS A PARTIR DE LOS ASIENTOS ENERO-ABRIL 2013"
  
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
        elif account_code[:3]=="400":
            acc = account_id
            nombre = oerp.get('account.move.line').browse(apunte).name
            if diario==5:
                total = oerp.get('account.move.line').browse(apunte).credit
            elif diario==7:
                total = oerp.get('account.move.line').browse(apunte).debit
        elif account_code[:3]=="475":
            acc_475 = account_id
            invoice_line_tax_475+=1
            cuota_irpf_code_id = oerp.get('account.move.line').browse(apunte).tax_code_id.id
            apuntes_475.append((apunte,cuota_irpf_code_id,acc_475))
            if diario==5:
                tax_irpf = oerp.get('account.move.line').browse(apunte).credit
            elif diario==7:
                tax_irpf = oerp.get('account.move.line').browse(apunte).debit
        elif (account_code[:1]=="2" or account_code[:1]=="6") and ((diario==5 and oerp.get('account.move.line').browse(apunte).debit>0.00) or (diario==7 and oerp.get('account.move.line').browse(apunte).credit>0.00)):
            account_line_id = account_id
            if diario==5:
                base = oerp.get('account.move.line').browse(apunte).debit
            elif diario==7:
                base = oerp.get('account.move.line').browse(apunte).credit
        else:
            error+=1
      
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
        #antes de dar el alta busco si ya existe
#         acc_inv_line_tax_ids = oerp.execute('account.invoice.line.tax', 'search', [('invoice_line_id', '=', linea_nueva_id), ('tax_id', '=', t)])
        cursor.execute(
            """SELECT 
                *
            FROM account_invoice_line_tax
            WHERE invoice_line_id=%s and tax_id=%s;""",(linea_nueva_id, t))
        acc_inv_line_tax_ids = cursor.fetchall()
        if len(acc_inv_line_tax_ids)>0:
            continue
        else:
            cursor.execute(
                """INSERT INTO account_invoice_line_tax (invoice_line_id, tax_id)
                                        VALUES          (%s             , %s    ) RETURNING *;""",
                                                        (linea_nueva_id , t))
            linea_t_nueva_id = cursor.fetchone()[0]
            connector.commit()
            print "                        NUEVA SUB-LINEA DE IMPUESTOS CREADA"
        
####################### 4.- DESCONCILIAR, COMPUTAR IMPUESTOS Y VOLVER A CONCILIAR FACTURAS DE COMPRA DE ABRIL-DICIEMBRE 2013
print "4.- DESCONCILIAR, COMPUTAR IMPUESTOS Y VOLVER A CONCILIAR FACTURAS DE COMPRA DE ABRIL-DICIEMBRE 2013"

invoice_obj = oerp.get('account.invoice')
invoice_ids = invoice_obj.search([('journal_id', '=', 5), ('period_id', 'in', [8, 9, 10, 11, 12, 13, 14, 15])])
print len(invoice_ids)
c=0

for invoice_id in invoice_ids:
    sin_arreglar=[]
    c+=1
    print "Factura numero: %s"%c
    inv = oerp.get('account.invoice').browse(invoice_id)
    state_factura = inv.state
    if state_factura<>"paid" and state_factura<>"open":
#         sin_arreglar.append(inv.number)
        continue
    account_factura_id = inv.account_id.id
    account_code = oerp.get('account.account').browse(account_factura_id).code
    partner_factura_id = inv.partner_id.id
    if not inv.move_id:
#         sin_arreglar.append(inv.number)
        continue
    move_factura_id = inv.move_id.id
    reconciled_factura_id = inv.reconciled
    move_line_desconciliar_ids = oerp.execute('account.move.line', 'search', [('move_id', '=', move_factura_id),('debit', '>', 0)])
    if len(move_line_desconciliar_ids)<>1:
#         sin_arreglar.append(inv.number)
        continue 
    #ahora toca desconciliar este apunte pero antes hay que acordarse del apunte 43 del pago para volver a conciliar despues
    if state_factura == "paid":
        num_lineas_a_desconciliar = 0
        apuntes_viejos_guardados = []
        payment_moves = []
        for move_line_desconciliar in move_line_desconciliar_ids:
            num_lineas_a_desconciliar+=1
            apunte_viejo_guardado = oerp.execute('account.move.line', 'read', move_line_desconciliar, ['partner_id', 'credit', 'debit', 'journal_id', 'ref', 'account_id', 'date', 'name' ])
            apuntes_viejos_guardados.append(apunte_viejo_guardado)
            i = oerp.execute('account.invoice', 'read', invoice_id, ['payment_ids'])
            payment_moves.append(i['payment_ids'])
    #ahora desconcilio
    context = {'active_ids':move_line_desconciliar_ids}
    descon = oerp.get('account.unreconcile').trans_unrec(move_line_desconciliar_ids, context)
    context = {'active_ids':[invoice_id]}
    state_factura = oerp.execute('account.invoice', 'read', invoice_id, ['state'])
    state_factura = state_factura['state']
#     if state_factura<>"paid" and state_factura<>"open":
    if state_factura<>"open":
#         sin_arreglar.append(inv['number'])
#         writer_facturas_compra_sin_arreglar.writerow(sin_arreglar)
        continue
    cancelar = oerp.get('account.invoice.cancel').invoice_cancel([invoice_id], context)
    cambiar_a_borrador = oerp.get('account.invoice').action_cancel_draft([invoice_id], context)
    #ahora debo colocar el impuesto 0% correcto en las líneas de la factura para despues ejecutar calcular impuestos
    invoice_line_ids = oerp.execute('account.invoice.line', 'search', [('invoice_id', '=', invoice_id),('state','=',"article")])
    if len(invoice_line_ids)<1:
#         print "FFFFFFFFFFFFFFFFalla no hay lineas de factura de tipo article\n"
#         sin_arreglar.append(inv['number'])
#         writer_facturas_compra_sin_arreglar.writerow(sin_arreglar)
        continue
    for invoice_line_id in invoice_line_ids:
        invoice_line_iva_ids = oerp.execute('account.invoice.line', 'read', invoice_line_id, ['invoice_line_tax_id'])
        nuevo_invoice_line_iva_ids = []
        for tax in invoice_line_iva_ids['invoice_line_tax_id']:
            nuevo_invoice_line_iva_ids.append(tax)
        editado = oerp.execute('account.invoice.line', 'write', invoice_line_id, {'invoice_line_tax_id': [(6, 0, nuevo_invoice_line_iva_ids)]} )
    #recalculo los impuestos
    calcular_impuestos = oerp.get('account.invoice').button_reset_taxes([invoice_id], context)
    #ahora debo validar la factura antes de conciliar
    try:
        factura_validada = oerp.get('account.invoice.confirm').invoice_confirm([invoice_id], context)
    except Exception,e:
        sin_arreglar.append(inv['number'])
        writer_facturas_compra_sin_arreglar.writerow(sin_arreglar)
        continue
    #ahora debo conciliar el apunte con cuenta 43 de la factura y el del pago
    if state_factura == "paid":
        lineas_a_desconciliar = []
        for apunte_viejo_guardado in apuntes_viejos_guardados:
            lineas_a_desconciliar = oerp.execute('account.move.line', 'search', [('partner_id', '=', apunte_viejo_guardado['partner_id'][0]), ('credit', '=', apunte_viejo_guardado['credit']), ('debit', '=', apunte_viejo_guardado['debit']), ('journal_id', '=', apunte_viejo_guardado['journal_id'][0]), ('ref', '=', apunte_viejo_guardado['ref']), ('account_id', '=', apunte_viejo_guardado['account_id'][0]), ('date', '=', apunte_viejo_guardado['date']), ('name', '=', apunte_viejo_guardado['name'])])
        payment_moves.append(lineas_a_desconciliar)
        factura_validada = oerp.get('account.move.line').reconcile(payment_moves)
        
print "numero de apuntes cuyo account_code no fue identificado: %s"%error
print time.time()-t0