import pymysql 

db_host = 'esd-basedatos-mysql.cfojfplxkq0l.us-east-1.rds.amazonaws.com'
db_port = 3306
db_user = 'admin'
db_password = 'fubuki00'
db_name = 'proyesd'

try:
    conn = pymysql.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM users')  
        result = cursor.fetchall()
        for row in result:
            print(row)

    conn.commit()
    print("Database connection and query successful!")

except Exception as e:
    print("Error:", e)

finally:
    conn.close()