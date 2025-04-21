import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook",
    user="alihaan",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", row)

conn.commit()
cur.close()
conn.close()
print("CSV data inserted successfully.")