# -*- encoding: utf-8 -*-
import psycopg2

productos = [("AMONITA 2I DE 26X200", "kg"),
            ("CORDTEX 6N 4X200M", "m"),
            ("EXAN 25KG", "kg"),
            ("PÓLVORA NEGRA", "kg"),
            ("Polvora negra de mina No 1. ; 10 x 2,5 kg", "kg"),
            ("RIOCORD 100 GRS.", "m"),
            ("RIOCORD 12 GRS.", "m"),
            ("RIOCORD 12 GRS. ROLLO 125 MTS.", "m"),
            ("RIOCORD 6 GRS.", "m"),
            ("RIODIN 50x380 MM (TR)", "kg"),
            ("RIODIN HE 26X200 MM (152 GRS)", "kg"),
            ("RIODIN HE 32X200 MM (238 GRS)", "kg"),
            ("RIODIN HE 50X380 MM (1042 GRS)", "kg"),
            ("RIODIN HE 50X380 MM (1042 GRS)", "kg"),
            ("RIODIN HE 60X570 MM (2300 GRS)", "kg"),
            ("RIOGEL TRONER 40x330 MM", "kg"),
            ("RIOGEL TRONER 50x500 MM", "kg"),
            ("RIOGEL TRONER 60x500 MM", "kg"),
            ("RIOPOL (POLVORA DE MINA Nº1)", "kg"),
            ("RIOXAM ST/ NAGOLITA ENSACADA", "kg")]
 
connection = psycopg2.connect(host='localhost', database='traza', user='ddiz', password='Milonga_25') 
cursor = connection.cursor()

q = cursor.execute('SELECT id,product_id,product_uom FROM stock_move WHERE product_id=5 and product_uom=2')
print q

todo = cursor.fetchall()
print todo

one = cursor.fetchone()
print one

connection.close()

