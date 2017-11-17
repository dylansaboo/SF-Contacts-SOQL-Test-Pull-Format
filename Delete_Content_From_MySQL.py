import pymysql.cursors
import sys

#Connection to Database

connection = pymysql.connect(host='localhost',
        user='root',
        password='HIDDEN',
        db='HIDDEN',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

#x = sys.argvx = str(x[1])

try:
    with connection.cursor() as cursor:
        #Delete Records
        sqld = "DELETE FROM users;"
        sqla = "ALTER TABLE users AUTO_INCREMENT=1;"
        cursor.execute(sqld)
        cursor.execute(sqla)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

finally:
    connection.close()
