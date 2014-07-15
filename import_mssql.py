#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import ydbf
import oerplib
import os
import csv
import time
import sys
import pyodbc

host= 'localhost'
protocol= 'xmlrpc'
port=8069
dbname = 'test'
username = 'XXXXX'
pwd = 'XXXXX'
 
oerp = oerplib.OERP(host, dbname, protocol, port)
user = oerp.login(username, pwd)

conxn = pyodbc.connect('DSN=mssqldns;UID=XXXXX;PWD=XXXXX;')
cur = conxn.cursor()
cur.execute("""SELECT dbo.Cobros.cob_FechaCobro AS FechaCobro,
                  dbo.Clientes.cli_NombreEmpresa,
                  dbo.Cobros.cob_Facturada,
                  dbo.CategoriasComision.cat_DescripcionCategoria,
                  dbo.CategoriasComision.cat_NombreCategoria,
                  dbo.Gestorias.ges_NombreGestoria, 
                  dbo.Gestorias.ges_IdGestoria,
                  dbo.CategoriasComision.cat_Comision,
                  dbo.CategoriasComision.cat_ComisionSeg,
                  dbo.CategoriasComision.cat_IdCategoria, 
                  dbo.TiposCobro.IDTipoCobro,
                  dbo.TiposCobro.DescripcionCAT,
                  dbo.TiposCobro.DescripcionCAS,
                  dbo.TiposCobro.CodigoFacturaplus,
                  dbo.TiposCobro.TieneComision, 
                  dbo.TiposCobro.IVA,
                  ISNULL(dbo.GruposTiposCobro.EsParteTecnica, 1) AS EsParteTecnica,
                  ISNULL(dbo.GruposTiposCobro.EsVigilancia, 0) AS EsVigilancia, 
                  dbo.GruposTiposCobro.IDGrupoTipoCobro,
                  dbo.Cobros.cob_IdCobro,
                  dbo.Cobros.cob_IdCliente,
                  dbo.Cobros.cob_IdCobroEstado,
                  dbo.Cobros.cob_FechaCobro, 
                  dbo.Cobros.cob_PrecioPrevencion AS PrecioPrevencion,
                  dbo.Cobros.cob_Extras AS Extras,
                  dbo.Cobros.cob_ConceptoExtras,
                  dbo.Cobros.cob_Moroso,
                  dbo.Cobros.cob_Contar, 
                  dbo.Cobros.cob_Facturada,
                  dbo.Cobros.cob_Tratado,
                  dbo.Cobros.cob_NAlbaran_Facturaplus,
                  dbo.Cobros.cob_NFactura_Facturaplus,
                  dbo.Cobros.cob_IdTipoCobro, 
                  dbo.Cobros.cob_Unidades AS Unidades,
                  dbo.Clientes.cli_IdCliente,
                  dbo.Clientes.cli_NombreEmpresa,
                  dbo.Clientes.cli_Mutua,
                  dbo.Clientes.cli_IdGestoria, 
                  dbo.Clientes.cli_IdActividad,
                  dbo.Clientes.cli_CodigoCorrelativo,
                  dbo.Clientes.cli_ActividadE,
                  dbo.Clientes.cli_CIF,
                  dbo.Clientes.cli_Password, 
                  dbo.Clientes.cli_Direccion,
                  dbo.Clientes.cli_CP,
                  dbo.Clientes.cli_Ciudad,
                  dbo.Clientes.cli_Provincia,
                  dbo.Clientes.cli_IdTecnico,
                  dbo.Clientes.cli_Zona, 
                  dbo.Clientes.cli_Idioma,
                  dbo.Clientes.cli_Gerente,
                  dbo.Clientes.cli_CargoGerente,
                  dbo.Clientes.cli_SexoGerente,
                  dbo.Clientes.cli_DNIGerente, 
                  dbo.Clientes.cli_PersonaContacto,
                  dbo.Clientes.cli_CargoContacto,
                  dbo.Clientes.cli_TelfContacto,
                  dbo.Clientes.cli_Telf,
                  dbo.Clientes.cli_Movil1, 
                  dbo.Clientes.cli_Movil2,
                  dbo.Clientes.cli_FAX,
                  dbo.Clientes.cli_Email,
                  dbo.Clientes.cli_VigilanciaSalud,
                  dbo.Clientes.cli_ActividadProductiva,
                  dbo.Clientes.cli_CCC, 
                  dbo.Clientes.cli_CNAE,
                  dbo.Clientes.cli_DisciplinasConcertadas,
                  dbo.Clientes.cli_Observaciones,
                  dbo.Clientes.cli_RiesgoEmpresa,
                  dbo.Clientes.cli_FechaPriContrato, 
                  dbo.Clientes.cli_FechaUltContrato,
                  dbo.Clientes.cli_Vigente,
                  dbo.Clientes.cli_ContrataPEI,
                  dbo.Clientes.cli_ComercialActivo,
                  dbo.Clientes.cli_FechaBaja, 
                  dbo.Clientes.cli_MotivoBaja,
                  dbo.Clientes.cli_IdComercial,
                  dbo.Clientes.cli_NumCentros,
                  dbo.Clientes.cli_Centros,
                  dbo.Clientes.cli_NumTrabRAlto, 
                  dbo.Clientes.cli_NumTrabRMedio,
                  dbo.Clientes.cli_NumTrabRBajo,
                  dbo.Clientes.cli_Sector,
                  dbo.Clientes.cli_CosteInicial,
                  dbo.Clientes.cli_PlusDistancia, 
                  dbo.Clientes.cli_PlusUrgencia,
                  dbo.Clientes.cli_PlusComision,
                  dbo.Clientes.cli_PlanEmergencia,
                  dbo.Clientes.cli_PlanSeguridad,
                  dbo.Clientes.cli_ComisionGestoria, 
                  dbo.Clientes.cli_PrecioOfertado1,
                  dbo.Clientes.cli_PrecioOfertado2,
                  dbo.Clientes.cli_Comision,
                  dbo.Clientes.cli_HorasMin,
                  dbo.Clientes.cli_Activo, 
                  dbo.Clientes.cli_FechaInicial,
                  dbo.Clientes.cli_Comentario,
                  dbo.Clientes.cli_FechaOferta,
                  dbo.Clientes.cli_TipoPago,
                  dbo.Clientes.cli_PresupuestoRevisado, 
                  dbo.Clientes.cli_PresupuestoAceptado,
                  dbo.Clientes.cli_IdClienteDoom,
                  dbo.Clientes.cli_IdTipoBaja,
                  dbo.Clientes.cli_IdVigilanciaSalud,
                  dbo.Clientes.cli_Maquinas, 
                  dbo.Clientes._AnnexI,
                  dbo.Clientes.Eliminado,
                  dbo.Clientes.SonHerramientas,
                  dbo.Clientes.cli_subcuentacontable,
                  dbo.Clientes.cli_CodigoClienteFacturar, 
                  dbo.Clientes.cli_DireccionEntregaFacturar,
                  dbo.Clientes.cli_Longitud,
                  dbo.Clientes.cli_Latitud,
                  dbo.Clientes.cli_FuenteCoordenadas, 
                  dbo.Clientes.cli_GoogleMapsAccuracy,
                  dbo.Clientes.cli_GoogleMapsStatus,
                  dbo.Clientes.cli_IdEmpresaPrevenet,
                  dbo.Clientes.cli_ExportarPrevenet, 
                  dbo.Clientes.cli_SHE,
                  dbo.Clientes.cli_VS,
                  dbo.Clientes.cli_FechaContratoVigilanciaSalud,
                  dbo.Clientes.cli_IdTecnicoVs,
                  dbo.Clientes.cli_FechaProximaActuacionVs, 
                  dbo.Clientes.cli_EstadoClienteVs,
                  dbo.Clientes.cli_ObservacionesVs,
                  dbo.Clientes.cli_IdCentroMedico,
                  dbo.Clientes.cli_FechaPlaniVS, 
                  dbo.Clientes.cli_IdProductoContratado,
                  dbo.Clientes.cli_ZonaPrivada
        FROM      dbo.Gestorias INNER JOIN
                  dbo.Clientes ON dbo.Gestorias.ges_IdGestoria = dbo.Clientes.cli_IdGestoria INNER JOIN
                  dbo.CategoriasComision ON dbo.Gestorias.ges_IdCategoria = dbo.CategoriasComision.cat_IdCategoria INNER JOIN
                  dbo.Cobros ON dbo.Clientes.cli_IdCliente = dbo.Cobros.cob_IdCliente LEFT OUTER JOIN
                  dbo.TiposCobro ON dbo.Cobros.cob_IdTipoCobro = dbo.TiposCobro.IDTipoCobro LEFT OUTER JOIN
                  dbo.GruposTiposCobro ON dbo.GruposTiposCobro.IDGrupoTipoCobro = dbo.TiposCobro.IDGrupoTipoCobro
        WHERE     (dbo.Cobros.cob_Facturada = 0) AND (dbo.Cobros.cob_FechaCobro > CONVERT(DATETIME, '2007-01-01 00:00:00', 102)) AND 
                  (dbo.Cobros.cob_FechaCobro < CONVERT(DATETIME, DATEADD(day,1,GETDATE()), 102)) AND 
                  (dbo.Cobros.cob_Moroso = CAST(0 AS BIT)) AND (dbo.Cobros.cob_PrecioPrevencion <> 0) OR
                  (dbo.Cobros.cob_Facturada = 0) AND (dbo.Cobros.cob_FechaCobro > CONVERT(DATETIME, '2007-01-01 00:00:00', 102)) AND 
                  (dbo.Cobros.cob_FechaCobro < CONVERT(DATETIME, DATEADD(day,1,GETDATE()), 102)) AND 
                  (dbo.Cobros.cob_Moroso = CAST(0 AS BIT)) AND (dbo.Cobros.cob_Extras <> 0)
        ORDER BY dbo.Cobros.cob_FechaCobro desc""")
for row in cur:
    if Extras<0 or PrecioPrevencion<0 or Unidades<0:
        type = 'out_refund'
        journal_id = 6
    else:
        type = 'out_invoice'
        journal_id = 4
    cliente_args = [('vat', '=', cliente_cif)]
    cliente_ids = oerp.execute('res.partner', 'search', cliente_args)
    if cliente_ids:
        cliente_id = cliente_ids[0]
    else:
        cliente_args2 = [('name', '=', cliente_nombre)]
        cliente_ids = oerp.execute('res.partner', 'search', cliente_args2)
        if cliente_ids:
            cliente_id = cliente_ids[0]
        else:
            cliente_id = alta_cliente(cliente)
    address_args = [('partner_id', '=', cliente_id)]
    address_ids = oerp.execute('res.partner.address', 'search', address_args)
    if address_ids:
        address_id = address_ids[0]
    else:
        linea = []
        linea.append(cliente)
        num_fac_int=int(num_fac)
        linea.append(num_fac_int)
        writer_direcccion_no_encontrada.writerow(linea)
        return False

    csv_agentes = open(ruta_dbf2csv + '/Agentes.csv', 'rb')
    reader_agentes = csv.reader(csv_agentes, dialect='nuevo_dialecto')
    ag = 0
    j = 0
    for agente_csv in reader_agentes:
        if j==0:
            j+=1
            continue
        else:
            j+=1
            agente = int(agente)
            a_csv = agente_csv[0]
            a_csv = int(a_csv)
            if a_csv==agente:
                agente_nombre = agente_csv[2]
                agent_args = [('name', '=', agente_nombre)]
                agent_ids = oerp.execute('sale.agent', 'search', agent_args)
                if agent_ids:
                    agent_id = agent_ids[0]
                    ag = 1
                    break
    prov = 1569
    if ag==0:
        ccodagente = int(agente)
        dbf_agente = ydbf.open(ruta_dbf + '/Agentes.dbf', encoding='cp1252')
        find = 0
        for record in dbf_agente:
            record['CCODAGE'] = int(record['CCODAGE'])
            if record['CCODAGE'] == ccodagente:
                find = 1            
                print "        agente encontrado en el dbf"
                agent_id = _altas_agent(record, prov)         
                break    
        if find == 0:
            print "        no se ha encontrado en el dbf el agente:  %s"%ccodagente
#            linea = []
#            linea.append(ccodagente)
#            writer_restos2.writerow(linea)
#            continue
        dbf_agente.close()
        
        linea = []
        linea.append(agente)
        writer_agent_no_encontrado.writerow(linea)
    
    payment_term_args = [('name', '=', "180 días")]
    payment_term_ids = oerp.execute('account.payment.term', 'search', payment_term_args)
    
    if not payment_term_ids:
        term = {
            'active': True,
            'note': "180 días",
            'name': "180 días",
            }
        p_term = oerp.execute('account.payment.term', 'create', term)
        term_line = {
                'payment_id': p_term,
                'name': "180 días",
                'sequence': 5,
                'days2': 0,
                'days': 180,
                'value': "balance",
                }
        p_term_line = oerp.execute('account.payment.term.line', 'create', term_line)
    
    acc = oerp.execute('res.partner', 'read', cliente_id, ['property_account_receivable'])
    account_id = acc['property_account_receivable'][0]
    comision
    fecha_p = time.strptime( fecha , '%Y-%m-%d')
    mes = fecha_p.tm_mon
    if mes==1:
        period_id=4
    elif mes==2:
        period_id=5
    elif mes==3:
        period_id=6
    elif mes==4:
         period_id=7
    elif mes==5:
         period_id=8
    elif mes==6:
         period_id=9
    elif mes==7:
         period_id=10
    elif mes==8:
         period_id=11
    elif mes==9:
         period_id=12
    elif mes==10:
         period_id=13
    elif mes==11:
         period_id=14
    elif mes==12:
         period_id=15

    if tipo_pago in ("0", "1", "CO"):
        payment_type = 6
        payment_term =  2
    elif tipo_pago=="2":
        payment_type = 1
        payment_term =  3
    elif tipo_pago=="34":
        payment_type = 1
        payment_term =  8
    elif tipo_pago=="8":
        payment_type = 1
        payment_term =  4
    elif tipo_pago=="15":
        payment_type = 1
        payment_term =  2
    elif tipo_pago=="18":
        payment_type = 1
        payment_term =  5
    elif tipo_pago=="29":
        payment_type = 1
        payment_term =  10
    elif tipo_pago=="10":
        payment_type = 4
        payment_term =  3
    elif tipo_pago=="13":
        payment_type = 4
        payment_term =  5
    elif tipo_pago=="11":
        payment_type = 3
        payment_term =  3
    elif tipo_pago=="22":
        payment_type = 3
        payment_term =  2
    elif tipo_pago=="14":
        payment_type = 3
        payment_term =  5
    elif tipo_pago=="16":
        payment_type = 3
        payment_term =  4
    elif tipo_pago=="19":
        payment_type = 6
        payment_term =  3
    elif tipo_pago=="12":
        payment_type = 2
        payment_term =  2
    elif tipo_pago=="17":
        payment_type = 2
        payment_term =  5
    elif tipo_pago=="20":
        payment_type = 2
        payment_term =  3
    elif tipo_pago=="21":
        payment_type = 2
        payment_term =  3
    elif tipo_pago=="23":
        payment_type = 2
        payment_term =  4
    elif tipo_pago=="24":
        payment_type = 2
        payment_term =  2
    elif tipo_pago=="26":
        payment_type = 2
        payment_term =  10
    elif tipo_pago=="31":
        payment_type = 2
        payment_term =  5
    elif tipo_pago=="33":
        payment_type = 2
        payment_term =  9
    elif tipo_pago=="30":
        payment_type = 2
        payment_term = 11
    else:
        #######################   alta de la forma de pago   ##################################################
        linea = []
        linea.append(tipo_pago)
        writer_fpago_no_encontrada.writerow(linea)
        return False
    
    factura = {
        'type': type,
        'operation_key': "Nothing",
        'number_tickets': 0,
        'company_id': 2,
        'currency_id': 1,
        'state': "draft",
        'partner_id': cliente_id,
        'address_invoice_id': address_id,
        'address_contact_id': address_id,
        'journal_id': journal_id,
        'account_id': account_id,
        'agent_id': agent_id,
        'date_invoice': fecha,
        'period_id': period_id,
#             'date_due': fecha_vencimiento,
        'payment_term': payment_term,
        'payment_type': payment_type,
        'name': num_fac,
    }
    factura_id = oerp.execute('account.invoice', 'create', factura)
    print "se creó la factura_id:  %s"%factura_id
    return factura_id


