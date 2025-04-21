import psycopg2

conn = psycopg2.connect(
    dbname="phonebook",
    user="alihaan",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

with open("sql/functions_and_procedures.sql", "r") as file:
    cur.execute(file.read())

conn.commit()
cur.close()
conn.close()

print("Все функции и процедуры успешно применены.")