import psycopg2

params = {
    "host": "postgres.postgres",
    "port": 5432,
    "dbname": "ros_gql_db",
    "user": "postgres",
    "password": "Rushi0321",
 
}

conn = psycopg2.connect(**params)

cur = conn.cursor()

cur.execute("SELECT version()")
version = cur.fetchone()
print(f"Postgres version: {version}")

cur.execute("SELECT * FROM books")
books = cur.fetchall()
print(f"Books: {books}")

cur.close()
conn.close()