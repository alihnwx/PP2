import psycopg2

query = input("Введите имя или номер для удаления: ")

conn = psycopg2.connect(dbname="phonebook", user="alihaan", host="localhost")
cur = conn.cursor()

cur.execute("CALL delete_user_by_username_or_phone(%s);", (query,))
conn.commit()

print("Удалено.")

cur.close()
conn.close()