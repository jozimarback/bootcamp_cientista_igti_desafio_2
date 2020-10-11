from .conexao import connection
import pandas as pd
import datetime

def inserir(dados):
    with connection.cursor() as cursor:
        sql = """INSERT INTO `db_desafio`.`tb_pessoa`
(`nome`,
`idade`,
`data_nasc`,
`sexo`,
`signo`,
`altura`,
`peso`,
`id_cidade`,
`id_cor`,
`id_tiposanguineo`)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        for d in dados.iterrows():
            cursor.execute(sql, (d[1]['nome'],d[1]['idade'], d[1]['data_nasc']._date_repr,d[1]['sexo'][0],d[1]['signo'],
            float(d[1]['altura'].replace(',','.')), d[1]['peso'], d[1]['id_cidade'], d[1]['id_cor'], d[1]['id_tiposanguineo']))

    connection.commit()

def obter():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `tb_pessoa`"
        cursor.execute(sql)
        return pd.DataFrame(cursor.fetchall())

