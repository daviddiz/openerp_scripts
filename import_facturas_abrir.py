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
invoice_ids.sort()

for i in invoice_ids:
    if i>3157:
        break
    print "factura numero:  %s"%i
    a = oerp.exec_workflow('account.invoice', 'invoice_open', i)
    print "    resultado:  %s"%a