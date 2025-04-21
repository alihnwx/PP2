import psycopg2

pattern = input("Введите шаблон (часть имени или номера): ")

conn = psycopg2.connect(dbname="phonebook", user="alihaan", host="localhost")
cur = conn.cursor()

cur.execute("SELECT * FROM search_user(%s);", (pattern,))
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()