import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': '123456',
            'database': 'vsearchlogDB',}

connect = mysql.connector.connect(**dbconfig)
cursor = connect.cursor()
