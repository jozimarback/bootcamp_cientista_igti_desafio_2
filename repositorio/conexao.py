import pymysql

connection = pymysql.connect(host='localhost',
                             user='jozimar',
                             password='',
                             db='db_desafio',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)