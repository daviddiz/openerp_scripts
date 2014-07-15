#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ydbf
import os
import csv
import glob

ruta_script_actual = os.path.abspath('')
ruta_dbf = os.path.abspath('../dbf/')
ruta_dbf2csv = os.path.abspath('../dbf2csv/')
csv.register_dialect('nuevo_dialecto', delimiter=',')

#a = os.system("cp /mnt/conta/CON2012/EMP/*.dbf /home/ddiz/workspace/openerp/trunk/oerp/addons/prevencontrol_import/data/dbf/")
#print a
b = os.system("cp /mnt/conta/CON2012/EmpAF/*.dbf /home/ddiz/workspace/openerp/trunk/oerp/addons/prevencontrol_import/data/dbf/")
print b
c = os.system("cp /mnt/conta/GES2012/DBF03/*.dbf /home/ddiz/workspace/openerp/trunk/oerp/addons/prevencontrol_import/data/dbf/")
print c

os.chdir(ruta_dbf)
lista_dbf = glob.glob("*.dbf")
print "lista de ficheros:   %s"%lista_dbf
os.chdir(ruta_script_actual)

for f in lista_dbf:
#    if f == "dCarta.dbf" or f == "pygpnor.dbf" or f == "DTalon.dbf" or f == "Importar.dbf" or f == "DCarta.dbf":
    if (f != "Facclit.dbf") and (f != "Facclil.dbf") and (f != "Facclib.dbf") and (f != "Clientes.dbf") and (f != "Agentes.dbf") and (f != "Albclil.dbf") and (f != "Albclib.dbf") and (f != "Albclit.dbf") and (f != "Articulo.dbf") and (f != "BancosCl.dbf") and (f != "Claves.dbf") and (f != "Diario.dbf") and (f != "Dircli.dbf") and (f != "Familias.dbf") and (f != "Fpago.dbf") and (f != "Pedclit.dbf") and (f != "Preclit.dbf") and (f != "RatSit.dbf") and (f != "Recibos.dbf") and (f != "Rutas.dbf") and (f != "SCtaB.dbf") and (f != "Stocks.dbf") and (f != "SubCta.dbf") and (f != "Subnic.dbf") and (f != "Agentes.dbf") and (f != "Cta_Rem.dbf") and (f != "Liquidl.dbf") and (f != "Liquidt.dbf"):
        continue
    print "Convirtiendo:   %s"%f
    dbf_f = ydbf.open(ruta_dbf + '/' + f, encoding='cp1252')
    f_mod = f[:-4]
    csv_f = open(ruta_dbf2csv + '/' + f_mod + '.csv', 'wb')
    writer_f = csv.writer(csv_f, dialect='nuevo_dialecto')
    i=0
    contt=0
    for record in dbf_f:
        contt+=1
        print "linea del archivo numero::   %s"%contt
        cabecera=[]
        if i==0:
            j=0
            for key,value in record.iteritems():
                cabecera.append("valor")
                cabecera[j]=key
                j+=1
            writer_f.writerow(cabecera)
            i+=1
    
        linea=[]
        k=0
        for key, value in record.iteritems():
            linea.append("valor")
            linea[k]=value
            k+=1
        writer_f.writerow(linea)
        
    csv_f.close()
