#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc

conn = pyodbc.connect(r'DRIVER={SQL Server Native};SERVER=XXXXX;DATABASE=XXXXXX;UID=XXXXX;PWD=XXXXXXX')

cur = conn.cursor()

for row in cur.tables():
    print(row.table_name)

# cur.execute("""SELECT * FROM dbo.Gestorias""")
# for row in cur:
#     print row