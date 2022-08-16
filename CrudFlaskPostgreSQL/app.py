from flask import Flask
import psycopg2

app = Flask(__name__)

host = 'localhost'
port = '5432'
dbname = 'usersDbPython'
user = 'postgres'
password = '6146'
def get_connection():
    conn = psycopg2.connect(database=dbname, user=user, password=password)
    return conn

# @app.get('/')
# def home():
#     conn = get_connection()
#     cur = conn.cursor() # es la forma en que se pueden hacer las consultas
#     cur.execute("SELECT 1 + 1") 
#     result = cur.fetchone()
#     print(result)
#     return 'Hola Mundo!'




if __name__ == '__main__':
    app.run(debug=True)