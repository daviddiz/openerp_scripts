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

invoice_args = [('state', '=', "draft")]
invoice_ids = oerp.execute('account.invoice', 'search', invoice_args)

for i in invoice_ids:
    print "factura numero:  %s"%i
    invoice_obj = oerp.get('account.invoice')
    bool = invoice_obj.button_compute([i])
    print "se computó?:  %s"%bool