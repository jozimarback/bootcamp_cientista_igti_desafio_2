from .conexao import connection
import pandas as pd

def inserir(grupos, estados):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `tb_cidade` (`nome`,`id_estado`) VALUES (%s,%s)"
        for d in grupos:
            cidade = d[0][1]
            cursor.execute(sql, (cidade, int(estados.loc[estados['sigla'] == d[0][0],['id']]['id'].values[0])))

    connection.commit()

def obter():
    with connection.cursor() as cursor:
        sql = "SELECT id as id_cidade, nome as nome_cidade FROM `tb_cidade`"
        cursor.execute(sql)
        return pd.DataFrame(cursor.fetchall())

