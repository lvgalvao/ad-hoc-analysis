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

sql1 = """WITH my_cte_request_month_dist_to_cost AS (
        SELECT *,
            to_char(request_date::date, 'YYYY-MM') AS request_month,
            (distance_to_travel/monetary_cost) AS dist_to_cost
        FROM uber_request_logs
    ),

    avg_dist_to_cost_month AS (
        SELECT request_date, 
           dist_to_cost, 
           AVG(dist_to_cost) OVER(PARTITION BY request_month) AS avg_dist_to_cost_month
        FROM my_cte_request_month_dist_to_cost
)

SELECT request_date, round(abs(dist_to_cost-avg_dist_to_cost_month)::DECIMAL, 2) as mean_deviation
FROM avg_dist_to_cost_month"""

cur.execute(sql1)

for i in cur.fetchall():
    print(i)

cur.close()
conn.close()
