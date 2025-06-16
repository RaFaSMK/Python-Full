import pymysql.cursors

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
    #Se não passar nada no parametro port, ele usa a padrão 3306
)

