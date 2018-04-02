import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': '123456',
            'database': 'vsearchlogDB',}

connect = mysql.connector.connect(**dbconfig)

cursor = connect.cursor()

_SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
          values 
            (%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, params=('fuck', 'xyz', '127.0.0.1', 'Safari', 'set()'))
connect.commit()


_SQL = """select * from log"""
cursor.execute(_SQL)
res = cursor.fetchall()
print(res)
print('================================================================================================================')
for row in res:
    print(row)

cursor.close()
connect.close()

