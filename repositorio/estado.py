from .conexao import connection
import pandas as pd

def inserir(dados):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `tb_estado` (`sigla`) VALUES (%s)"
        for d in dados:
            cursor.execute(sql, (d,))

    connection.commit()

def obter():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `tb_estado`"
        cursor.execute(sql)
        return pd.DataFrame(cursor.fetchall())

