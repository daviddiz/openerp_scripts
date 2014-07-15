#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import psycopg2.extensions
import sys
import csv
import ydbf
import oerplib
import os
import time
from datetime import date

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
            
############# alta de apunte de base de irpf ########################################
    cursor.execute(
        """INSERT INTO account_move_line (journal_id, currency_id, partner_id, blocked, credit, centralisation, company_id, tax_code_id, state, debit, ref, account_id, period_id, date_created, date, move_id, name, tax_amount, amount_currency, quantity, received_check)
                                  VALUES (%s        , %s         , %s        , %s     , %s    , %s            , %s        , %s         , %s   , %s   , %s , %s        , %s       , %s          , %s  , %s     , %s  , %s        , %s             , %s      , %s            );""",
                                         (journal_id, currency_id, partner_id, blocked, credit, centralisation, company_id, tax_code_id, state, debit, ref, account_id, period_id, date_created, date, move_id, name, tax_amount, amount_currency, quantity, received_check))
    connector.commit()