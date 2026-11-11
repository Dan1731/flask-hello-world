import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Claudia in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://db_3308_database_user:Yi3E5AjI6zTbABQwewxtUBvuGKzppYQ6@dpg-dbpv8rjl550s7392gqsg-a/db_3308_database")
    conn.close()
    return "Database Connection Succesful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://db_3308_database_user:Yi3E5AjI6zTbABQwewxtUBvuGKzppYQ6@dpg-dbpv8rjl550s7392gqsg-a/db_3308_database")
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()

    return "Basketball Table Created"
