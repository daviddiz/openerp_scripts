#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oerplib
import os
import time

host= 'localhost'
protocol= 'xmlrpc'
port=8069
dbname = 'prevencontrol'
username = 'XXXXX'
pwd = 'XXXXX'

oerp = oerplib.OERP(host, dbname, protocol, port)
user = oerp.login(username, pwd)

import unicodedata
def elimina_tildes(s):
    s=unicode(s)
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

###### quitar espacios en ccc de la cuentas de prevencontrol ##################
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

#recorrer todas las cuentas bancarias calculando el iban
bank_ids = oerp.execute('res.partner.bank', 'search', [])
# bank_ids=[4]
l=len(bank_ids)
c=0
for bank_id in bank_ids:
    c+=1
    print (c,l)
    bank = oerp.browse('res.partner.bank', bank_id)
    print bank.id
    bank_owner_name=bank.owner_name
    bank_city=bank.city
    bank_zip=bank.zip
    country_id = 67
    acc_country_id = 67
    if bank.acc_number:
        acc_number = (bank.acc_number).replace(" ","")
        acc_number = acc_number.replace("-","")
        iban = calc_iban(acc_number)
        print acc_number
        print iban
        oerp.write('res.partner.bank', [bank_id], {'city':bank_city, 'owner_name':bank_owner_name, 'zip':bank_zip, 'country_id':country_id, 'acc_country_id':acc_country_id, 'acc_number': acc_number, 'iban':iban})
    elif bank.iban:
        acc_number = (bank.iban)[2:]
        print acc_number
        print iban
        oerp.write('res.partner.bank', [bank_id], {'city':bank_city, 'owner_name':bank_owner_name, 'zip':bank_zip, 'country_id':country_id, 'acc_country_id':acc_country_id, 'acc_number': acc_number, 'iban':iban})        
