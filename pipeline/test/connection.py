import pymysql

conn = pymysql.connect(
    host='mysql',
    user='root',
    password='1234',
    port=3306,
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()