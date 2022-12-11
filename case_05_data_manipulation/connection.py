import psycopg2

try:
    conn = psycopg2.connect("dbname=stratascratch")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)
conn.set_session(autocommit=True)

try:
    cur.execute(
        """CREATE TABLE sf_restaurant_health_violations (
                business_id int,
                business_name varchar,
                business_address varchar,
                business_city varchar,
                business_state varchar,
                business_postal_code float,
                business_latitude float,
                business_longitude float,
                business_location varchar,
                business_phone_number float,
                inspection_id varchar,
                inspection_date date,
                inspection_score float,
                inspection_type varchar,
                violation_id varchar,
                violation_description varchar,
                risk_category varchar
);"""
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)
