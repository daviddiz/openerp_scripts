# -*- encoding: utf-8 -*-
import psycopg2

# databases = ['granitoslalin',
#     'rocasmaresgra',
#     'granitosdelval',
#     'pizarrasdequiroga',
#     'penido',
#     'villarbacu',
#     'sanclodio',
#     'pizarrasuniversal',
#     'carucedo',
#     'aridosastariz',
#     'filloy',
#     'caborcooscuro',
#     'proinor',
#     'cuficadoscampos',
#     'cufica',
#     'graexcom',
#     'fidelgomez',
#     'dragadosdelmar',
#     'casayo',
#     'aplistone',
#     'intradima',
#     'pedrina',
#     'graniorega',
#     'leymon',
#     'trescunados',
#     'argel',
#     'carloslopezamil']

databases = ['traza']

host = 'localhost'
user = ''
password = ''

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
 
for db in databases:
    
    for producto in productos:
        if producto[1]=="kg":
            uom_id_nuevo = 2
        elif producto[1]=="m":
            uom_id_nuevo = 7
             
        connection = psycopg2.connect(host=host, database=db, user=user, password=password)
        cursor = connection.cursor()
        cursor.execute('SELECT id FROM product_product WHERE name_template = %s',(producto[0],))
        if cursor.rowcount == 0:
            connection.close()
            continue
        product_id = cursor.fetchone()[0]
        print "producto: ",product_id
        connection.close()
             
        conn = psycopg2.connect(host=host, database=db, user=user, password=password)
        cr = conn.cursor()     
        cr.execute('UPDATE stock_move SET product_uom = %s WHERE product_id = %s and product_uom<>%s',(uom_id_nuevo, product_id, uom_id_nuevo))
        conn.commit
        print "numero de moves mod: ",cr.rowcount
        cr.execute('select * from pg_stat_activity')
        print cr.fetchone()
        print '\n\n'
        conn.close()

