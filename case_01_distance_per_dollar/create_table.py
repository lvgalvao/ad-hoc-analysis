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

try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS uber_request_logs   (request_id int, \
                                                        request_date date, \
                                                        request_status varchar, \
                                                        distance_to_travel float, \
                                                        monetary_cost float);"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

cur.close()
conn.close()
