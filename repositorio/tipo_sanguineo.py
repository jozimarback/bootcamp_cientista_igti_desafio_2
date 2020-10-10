from .conexao import connection
import pandas as pd

def inserir(dados):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `tb_tiposanguineo` (`tipo`) VALUES (%s)"
        for d in dados:
            cursor.execute(sql, (d,))
    connection.commit()

def obter():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `tb_tiposanguineo`"
        cursor.execute(sql)
        return pd.DataFrame(cursor.fetchall())

