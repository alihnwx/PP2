import psycopg2 

conn = psycopg2.connect(
    dbname="phonebook",
    user="alihaan",
    password="alihan007",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
""")

conn.commit()
cur.close()
conn.close()