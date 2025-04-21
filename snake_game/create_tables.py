import psycopg2

conn = psycopg2.connect(
    dbname="phonebook",  # Можно использовать ту же базу
    user="alihaan",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

conn.commit()
cur.close()
conn.close()
print("Tables created.")