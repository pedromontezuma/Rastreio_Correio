import pymysql

pymysql.install_as_MySQLdb()
try:
    db = pymysql.connect(host="177.190.196.250",
                         port=4455,
                         user="ControladoriaDigital",
                         passwd="@Powerb1",
                         db="master")
    cur = db.cursor()
    query = 'SELECT vd_transp_num FROM master.venda where  vd_entrega <> "S"  AND vd_pago = "S"  and vd_cancelada = "N"  and vd_transp_data <> " "'
    cur.execute(query)
    result = cur.fetchall()
    a = 1
    print("Consulta concluída com sucesso!")
    for i in result:
        i = str(i)
        print("Resultado %s: %s" %(a, i.replace("('", "").replace("',)", "")))
        a +=1
except Exception as erro:
    print(erro)