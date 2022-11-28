import psycopg2

# Psycopg is the most popular PostgreSQL database adapter for the Python programming language.

from config import USER, PASSWORD

# PostgresQL credentials

try:
    conn = psycopg2.connect(
        f"host=127.0.0.1 dbname=sql_questions user={USER} password={PASSWORD}"
    )
except psycopg2.Error as e:
    print("Error:Could not make connection to the Postgres Database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error:Could not get cursor to the Database")
    print(e)

conn.set_session(autocommit=True)

values = [
    (1, "2020-01-09", "success", 70.59, 6.56),
    (2, "2020-01-24", "success", 93.36, 22.68),
    (3, "2020-02-08", "fail", 51.24, 11.39),
]

args = ",".join(cur.mogrify("(%s, %s, %s, %s, %s)", i).decode("utf-8") for i in values)

cur.execute("INSERT INTO uber_request_logs VALUES " + (args))

sql1 = """select * from uber_request_logs;"""

cur.execute(sql1)

for i in cur.fetchall():
    print(i)

cur.close()
conn.close()
