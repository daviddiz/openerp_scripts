# -*- encoding: utf-8 -*-
import psycopg2
from collections import OrderedDict
import csv
import os

csv.register_dialect('nuevo_dialecto', delimiter=',')
csv_resultado = open(os.path.abspath('productos_utilizados_en_cada_bbdd.csv') , 'wb')
writer_resultado = csv.writer(csv_resultado, dialect='nuevo_dialecto')
csv_resumen = open(os.path.abspath('productos_resumen.csv') , 'wb')
writer_resumen = csv.writer(csv_resumen, dialect='nuevo_dialecto')

databases = ['granitoslalin',
    'rocasmaresgra',
    'granitosdelval',
    'pizarrasdequiroga',
    'penido',
    'villarbacu',
    'sanclodio',
    'pizarrasuniversal',
    'carucedo',
    'aridosastariz',
    'filloy',
    'caborcooscuro',
    'proinor',
    'cuficadoscampos',
    'cufica',
    'graexcom',
    'fidelgomez',
    'dragadosdelmar',
    'casayo',
    'aplistone',
    'intradima',
    'pedrina',
    'graniorega',
    'leymon',
    'lostrescunados',
    'argel',
    'carloslopezamil']

host = 'localhost'
user = ''
password = ''

resumen = []

for db in databases:
    connection = psycopg2.connect(host=host, database=db, user=user, password=password)
    cursor = connection.cursor()
    cursor.execute("""SELECT DISTINCT
                        pp.name_template,pu.name
                    FROM 
                        stock_move m
                            LEFT JOIN product_product pp ON (m.product_id=pp.id)
                            LEFT JOIN product_template pt ON (pp.product_tmpl_id=pt.id)
                            LEFT JOIN product_uom pu ON (pt.uom_id=pu.id)
                    
                    ORDER BY pp.name_template""")
    for query in cursor:
        r = [query[0],query[1],db]
        writer_resultado.writerow(r)
        resumen.append((query[0],query[1]))
resumen = list(OrderedDict.fromkeys(resumen))
for r in resumen:
    writer_resumen.writerow(r)