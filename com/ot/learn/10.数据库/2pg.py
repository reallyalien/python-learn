# pip install psycopg2-binary
import psycopg2

coon = psycopg2.connect(host="192.168.1.100",
                        port=5432,
                        database="local_cloud_test_shanxietyy",
                        user="sys",
                        password="sys")  # psycopg2.extensions.connection
# print(type(coon))
cursor = coon.cursor()

cursor.execute('select * from pat_info')
result = cursor.fetchall()

for x in result:
    print(x)

print(cursor.rowcount)