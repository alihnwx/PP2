import psycopg2

name = input("Введите имя: ")
phone = input("Введите номер: ")

conn = psycopg2.connect(dbname="phonebook", user="alihaan", host="localhost")
cur = conn.cursor()

cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
conn.commit()

print("Готово.")

cur.close()
conn.close()