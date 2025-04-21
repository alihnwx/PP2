import psycopg2

names = input("Введите имена через запятую: ").split(",")
phones = input("Введите номера через запятую: ").split(",")

if len(names) != len(phones):
    print("Ошибка: количество имен и номеров не совпадает.")
    exit()

conn = psycopg2.connect(dbname="phonebook", user="alihaan", host="localhost")
cur = conn.cursor()

cur.execute("CALL insert_many_users(%s, %s);", (names, phones))
cur.execute("SELECT insert_many_users(%s, %s);", (names, phones))  # получить невалидные

print("Некорректные записи (если есть):")
for row in cur.fetchall():
    print(row)

conn.commit()
cur.close()
conn.close()