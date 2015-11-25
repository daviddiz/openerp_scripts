# -*- encoding: utf-8 -*-
import psycopg2
    
connection = psycopg2.connect(host='localhost', 
    database='XXXX', user='XXXXX', password='XXXXXX')
connection.set_isolation_level(0)
cr = connection.cursor()

cr.execute("""SELECT
                    pp.name_template
                FROM 
                    product_product pp
                ORDER BY pp.name_template""")

records = cr.fetchall()

for record in records:
    product_name_template = record[0]
    modificar = 0
    
    if ("POLVORA" in product_name_template) or \
        ("polvora" in product_name_template) or \
        ("pólvora" in product_name_template) or \
        ("RIOPOL" in product_name_template):
        num_catalog = 37
        modificar = 1
    elif ("AMONITA" in product_name_template):
        num_catalog = 12
        modificar = 1
    elif ("CORDTEX" in product_name_template):
        num_catalog = 1224
        modificar = 1
    elif ("RIODET IZ" in product_name_template):
        num_catalog = 166
        modificar = 1
    elif ("RIODET" in product_name_template) or \
        ("Riodet" in product_name_template) or \
        ("riodet" in product_name_template) or \
        ("RIODET IM" in product_name_template):
        num_catalog = 168
        modificar = 1
    elif ("Daveydet" in product_name_template):
        num_catalog = 216
        modificar = 1
    elif ("DAVEYNEL LP" in product_name_template):
        num_catalog = 1144
        modificar = 1
    elif ("Daveynel SP" in product_name_template):
        num_catalog = 1145
        modificar = 1
    elif ("daveynel" in product_name_template) or \
        ("Daveynel" in product_name_template) or \
        ("DAVEYNEL" in product_name_template):
        num_catalog = 229
        modificar = 1
    elif ("DET.ORDINARIO" in product_name_template) or \
        ("DETONADOR" in product_name_template) or \
        ("DETONADORES" in product_name_template) or \
        ("detonadores" in product_name_template):
        num_catalog = 184
        modificar = 1
    elif ("ergodyn" in product_name_template) or \
        ("ERGODYN" in product_name_template) or \
        ("Eegodyn" in product_name_template):
        num_catalog = 1233
        modificar = 1
    elif ("EURODYN" in product_name_template):
        num_catalog = 1043
        modificar = 1
    elif ("EXAN" in product_name_template):
        num_catalog = 1196
        modificar = 1
    elif ("mecha lenta" in product_name_template) or \
        ("MECHA LENTA" in product_name_template):
        num_catalog = 68
        modificar = 1
    elif ("NITRAM" in product_name_template):
        num_catalog = 1091
        modificar = 1
    elif ("Pax" in product_name_template):
        num_catalog = 271
        modificar = 1
    elif ("RELES" in product_name_template):
        num_catalog = 67
        modificar = 1
    elif ("RIOCORD 100" in product_name_template) or \
        ("100 GR. Riocord" in product_name_template):
        num_catalog = 1065
        modificar = 1
    elif ("RIOCORD 80" in product_name_template) or \
        ("80 GR. Riocord" in product_name_template):
        num_catalog = 1064
        modificar = 1
    elif ("RIOCORD 40" in product_name_template):
        num_catalog = 1063
        modificar = 1
    elif ("RIOCORD 20" in product_name_template):
        num_catalog = 1062
        modificar = 1
    elif ("RIOCORD 15" in product_name_template):
        num_catalog = 1061
        modificar = 1
    elif ("RIOCORD 12" in product_name_template) or \
        ("12 GR. Riocord" in product_name_template):
        num_catalog = 1060
        modificar = 1
    elif ("RIOCORD RF 10" in product_name_template) or \
        ("RIOCORD 10 GRS. REFORZADO" in product_name_template):
        num_catalog = 1059
        modificar = 1
    elif ("RIOCORD 10" in product_name_template):
        num_catalog = 1058
        modificar = 1
    elif ("RIOCORD RF 6" in product_name_template) or \
        ("RIOCORD 6 G. REF" in product_name_template) or \
        ("RIOCORD 6 GRS. REFORZADO" in product_name_template):
        num_catalog = 1057
        modificar = 1
    elif ("RIOCORD 6" in product_name_template) or \
        ("6 GR. Riocord" in product_name_template):
        num_catalog = 1056
        modificar = 1
    elif ("RIOCORD 3" in product_name_template):
        num_catalog = 1112
        modificar = 1
    elif ("RIOMEX" in product_name_template):
        num_catalog = 1276
        modificar = 1
    elif ("RIOPER G" in product_name_template):
        num_catalog = 6
        modificar = 1
    elif ("RIOPER P" in product_name_template):
        num_catalog = 8
        modificar = 1
    elif ("UNITRONIC" in product_name_template):
        num_catalog = 1246
        modificar = 1
    elif ("RIODIN" in product_name_template) or \
        ("Riodin" in product_name_template):
        num_catalog = 10
        modificar = 1
    elif ("RIOGEL" in product_name_template) or \
        ("Riogel" in product_name_template):
        num_catalog = 1
        modificar = 1
    elif ("RIONEL SCX" in product_name_template) or \
        ("Rionel SCX" in product_name_template) or \
        ("Rionel LLX" in product_name_template) or \
        ("RIONEL LLX" in product_name_template) or \
        ("Primadet EZTL" in product_name_template) or \
        ("PRIMADET EZTL" in product_name_template) or \
        ("Primadet EZTL" in product_name_template) or \
        ("EZTL/Rionel SCX" in product_name_template) or \
        ("EZTL/RIONEL SCX" in product_name_template):
        num_catalog = 1001
        modificar = 1
    elif ("RIONEL MS" in product_name_template) or \
        ("RIONEL  MS" in product_name_template) or \
        ("Rionel MS" in product_name_template) or \
        ("PRIMADET MS" in product_name_template) or \
        ("primadet Ms" in product_name_template) or \
        ("Primadet/Rionel MS" in product_name_template) or \
        ("PRIMADET/RIONEL MS" in product_name_template):
        num_catalog = 1002
        modificar = 1
    elif ("RIONEL LP" in product_name_template) or \
        ("RIONEL  LP" in product_name_template) or \
        ("Rionel LP" in product_name_template) or \
        ("PRIMADET/ RIONEL LP" in product_name_template):
        num_catalog = 1003
        modificar = 1
    elif ("RIONEL DDX" in product_name_template) or \
        ("Rionel DDX" in product_name_template) or \
        ("PRIMADET EZDET" in product_name_template) or \
        ("Primadet EZDET" in product_name_template) or \
        ("Primadet EZ" in product_name_template) or \
        ("Primadet  EZ" in product_name_template):
        num_catalog = 1004
        modificar = 1
    elif ("RIONEL BC" in product_name_template) or \
        ("Rionel BC" in product_name_template):
        num_catalog = 1141
        modificar = 1
    elif ("RIONEL S" in product_name_template) or \
        ("Rionel S" in product_name_template) or \
        ("Primadet S" in product_name_template) or \
        ("PRIMADET S" in product_name_template):
        num_catalog = 1157
        modificar = 1
    elif ("RIONEL SCE" in product_name_template) or \
        ("Rionel SCE" in product_name_template):
        num_catalog = 1280
        modificar = 1
    elif ("RIONEL UG" in product_name_template) or \
        ("Rionel UG" in product_name_template):
        num_catalog = 1281
        modificar = 1
    elif ("RIONEL DDE" in product_name_template) or \
        ("Rionel DDE" in product_name_template):
        num_catalog = 1282
        modificar = 1
    elif ("RIOXAM" in product_name_template) or \
        ("NAGOLITA" in product_name_template):
        num_catalog = 5
        modificar = 1
    elif ("SEICORD" in product_name_template):
        num_catalog = 1199
        modificar = 1
    elif ("ALNAFO" in product_name_template):
        num_catalog = 2
        modificar = 1
    elif ("BOOSTER" in product_name_template):
        num_catalog = 1116
        modificar = 1
    elif ("DAVEYCORD 70" in product_name_template):
        num_catalog = 250
        modificar = 1
    elif ("DAVEYCORD 40" in product_name_template):
        num_catalog = 249
        modificar = 1
    elif ("DAVEYCORD 20" in product_name_template):
        num_catalog = 248
        modificar = 1
    elif ("DAVEYCORD 15" in product_name_template):
        num_catalog = 247
        modificar = 1
    elif ("DAVEYCORD 10" in product_name_template):
        num_catalog = 246
        modificar = 1
    elif ("DAVEYCORD 5" in product_name_template):
        num_catalog = 245
        modificar = 1
        
    if modificar == 1:
        cr.execute("""UPDATE product_product SET num_catalog = %s 
            WHERE name_template = %s""",(num_catalog, product_name_template))
        connection.commit
        
connection.close()

