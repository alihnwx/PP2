import psycopg2

limit = int(input("Сколько записей показать? "))
offset = int(input("Сколько пропустить? "))

conn = psycopg2.connect(dbname="phonebook", user="alihaan", host="localhost")
cur = conn.cursor()

cur.execute("SELECT * FROM get_users_paginated(%s, %s);", (limit, offset))
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()