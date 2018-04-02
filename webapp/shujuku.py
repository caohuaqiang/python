import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': '123456',
            'database': 'vsearchlogDB',}
connect = mysql.connector.connect(**dbconfig)
cursor = connect.cursor()
_SQL = """describe log"""
cursor.execute(_SQL)
res = cursor.fetchall()
print(res)
print('========================================================================')
for row in res:
    print(row)
