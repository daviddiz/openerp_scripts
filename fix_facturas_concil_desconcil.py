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

host= 'localhost'
protocol= 'xmlrpc'
port=8069
dbname = 'prevencontrol'
username = 'XXXXX'
pwd = 'XXXXX'

oerp = oerplib.OERP(host, dbname, protocol, port)
user = oerp.login(username, pwd)

t0 = time.time()
invoice_obj = oerp.get('account.invoice')
invoice_ids = invoice_obj.search([('journal_id', '=', 5), ('period_id', 'in', [15, 14, 13, 12, 11, 10, 9, 8])])
print len(invoice_ids)
c=0

for invoice_id in invoice_ids:
    sin_arreglar=[]
    sin_arreglar2=[]
    sin_arreglar3=[]
    sin_arreglar4=[]
    sin_arreglar5=[]
    sin_arreglar6=[]
    c+=1
    print "Factura numero: %s"%c
    print "Factura id: %s"%invoice_id
    inv = oerp.get('account.invoice').browse(invoice_id)
    state_factura = inv.state
    if state_factura<>"paid" and state_factura<>"open":
        sin_arreglar.append(inv.number)
        continue
    account_factura_id = inv.account_id.id
    account_code = oerp.get('account.account').browse(account_factura_id).code
    partner_factura_id = inv.partner_id.id
    if not inv.move_id:
        sin_arreglar2.append(inv.number)
        continue
    move_factura_id = inv.move_id.id
    reconciled_factura_id = inv.reconciled
    move_line_desconciliar_ids = oerp.execute('account.move.line', 'search', [('move_id', '=', move_factura_id),('reconcile_id', '<>', 0)])
    if len(move_line_desconciliar_ids)<>1:
        sin_arreglar3.append(inv.number)
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
            for pay in i['payment_ids']:
                payment_moves.append(pay)
    #ahora desconcilio
    context = {'active_ids':move_line_desconciliar_ids}
    descon = oerp.get('account.unreconcile').trans_unrec(move_line_desconciliar_ids, context)
    context = {'active_ids':[invoice_id]}
    state_factura = oerp.execute('account.invoice', 'read', invoice_id, ['state'])
    state_factura = state_factura['state']
    if state_factura<>"open":
        sin_arreglar4.append(inv['number'])
        continue
    cancelar = oerp.get('account.invoice.cancel').invoice_cancel([invoice_id], context)
    cambiar_a_borrador = oerp.get('account.invoice').action_cancel_draft([invoice_id], context)
    #recalculo los impuestos
    calcular_impuestos = oerp.get('account.invoice').button_reset_taxes([invoice_id], context)
    #ahora debo validar la factura antes de conciliar
    try:
        factura_validada = oerp.get('account.invoice.confirm').invoice_confirm([invoice_id], context)
    except Exception,e:
        sin_arreglar5.append(inv['number'])
        continue
    #ahora debo conciliar el apunte con cuenta 43 de la factura y el del pago
    state_factura = oerp.execute('account.invoice', 'read', invoice_id, ['state'])
    if state_factura['state'] == "open":
        lineas_a_desconciliar = []
#         for apunte_viejo_guardado in apuntes_viejos_guardados:
#             lineas_a_desconciliar = oerp.execute('account.move.line', 'search', [('partner_id', '=', apunte_viejo_guardado['partner_id'][0]), ('credit', '=', apunte_viejo_guardado['credit']), ('debit', '=', apunte_viejo_guardado['debit']), ('journal_id', '=', apunte_viejo_guardado['journal_id'][0]), ('ref', '=', apunte_viejo_guardado['ref']), ('account_id', '=', apunte_viejo_guardado['account_id'][0]), ('date', '=', apunte_viejo_guardado['date']), ('name', '=', apunte_viejo_guardado['name'])])
        #puedo buscar la linea a conciliar a partir del nuevo asiento creado
        nuevo_move_id = oerp.execute('account.invoice', 'read', invoice_id, ['move_id'])
        lineas_a_desconciliar = oerp.execute('account.move.line', 'search', [('move_id', '=', nuevo_move_id['move_id'][0]), ('account_id', '=', account_factura_id)])
        if len(lineas_a_desconciliar)<>1:
            sin_arreglar6.append(inv['number'])
            continue
        payment_moves.extend(lineas_a_desconciliar)
        factura_validada = oerp.get('account.move.line').reconcile(payment_moves)
        
print "##################################################"
print sin_arreglar
print sin_arreglar2
print sin_arreglar3
print sin_arreglar4
print sin_arreglar5
print sin_arreglar6
print time.time()-t0