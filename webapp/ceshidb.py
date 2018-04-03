from DBcm import UseDatabase


def chq():
    with UseDatabase({'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': '123456',
                          'database': 'vsearchlogDB',}) as cursor:
        cursor.execute('select * from log')
        contents = cursor.fetchall()
        return contents


if __name__ == '__main__':
    print(chq())
    print(chq()[1][-2])