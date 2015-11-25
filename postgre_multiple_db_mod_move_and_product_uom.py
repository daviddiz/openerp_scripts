# -*- encoding: utf-8 -*-
import psycopg2

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
    'trescunados',
    'argel',
    'carloslopezamil']

productos = [("AMONITA 2I DE 26X200", "kg", 0.104),
            ("CORDTEX 6N 4X200M", "m", 200),
            ("EXAN 25KG", "kg", 25),
            ("PÓLVORA NEGRA", "kg", 2.5),
            ("Polvora negra de mina No 1. ; 10 x 2,5 kg", "kg", 2.5),
            ("RIOCORD 100 GRS.", "m", 50),
            ("RIOCORD 12 GRS.", "m", 250),
            ("RIOCORD 12 GRS. ROLLO 125 MTS.", "m", 125),
            ("RIOCORD 6 GRS.", "m", 400),
            ("RIODIN 50x380 MM (TR)", "kg", 1.042),
            ("RIODIN HE 26X200 MM (152 GRS)", "kg", 0.152),
            ("RIODIN HE 32X200 MM (238 GRS)", "kg", 0.238),
            ("RIODIN HE 50X380 MM (1042 GRS)", "kg", 1.042),
            ("RIODIN HE 60X570 MM (2300 GRS)", "kg", 2.3),
            ("RIOGEL TRONER 40x330 MM", "kg", 0.521),
            ("RIOGEL TRONER 50x500 MM", "kg", 1.2),
            ("RIOGEL TRONER 60x500 MM", "kg", 1.786),
            ("RIOPOL (POLVORA DE MINA Nº1)", "kg", 25),
            ("RIOXAM ST/ NAGOLITA ENSACADA", "kg", 25)]

for db in databases:
    
    connection = psycopg2.connect(database=db)
    connection.set_isolation_level(0)
    cr = connection.cursor() 


    for producto in productos:
        if producto[1]=="kg":
            uom_id_nuevo = 2
        elif producto[1]=="m":
            uom_id_nuevo = 7
            
        cr.execute('UPDATE stock_move SET product_uom = %s WHERE (product_id = (SELECT id FROM product_product WHERE name_template = %s) and product_uom<>%s)',(uom_id_nuevo, producto[0], uom_id_nuevo))
        connection.commit
        
        cr.execute('UPDATE stock_move SET product_qty = %s WHERE (product_id = (SELECT id FROM product_product WHERE name_template = %s) and picking_id IS NOT NULL)',(producto[2], producto[0]))
        connection.commit
        
        cr.execute('UPDATE product_template SET uom_id = %s WHERE (name=%s and uom_id<>%s)',(uom_id_nuevo, producto[0], uom_id_nuevo))
        connection.commit
        
    connection.close()

