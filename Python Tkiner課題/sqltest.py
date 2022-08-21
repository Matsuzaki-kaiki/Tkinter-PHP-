import pymysql.cursors
 
# Connect to the database

connection = pymysql.connect(host='127.0.0.1',
                             user='root ',
                             password='',
                             db='apri01',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:

        cursor = connection.cursor()

        # Create a new record
        sql = "insert into kinds_type_table(kinds_type_ID, kinds_type) values('1', '学校' );"
        cursor.execute(sql)

        cursor.execute("insert into kinds_type_table(kinds_type_ID, kinds_type) values('1', '学校' );"


#        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
 
    # connection is not autocommit by default. 
    # So you must commit to save your changes.
    connection.commit()
    '''
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
    '''
except:
    print('error')
finally:
        connection.close()
