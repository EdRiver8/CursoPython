import imp
from flask import Flask, request, jsonify
from psycopg2 import connect, extras
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()

host = 'localhost'
port = '5432'
dbname = 'usersDbPython'
user = 'postgres'
password = '6146'
def get_connection():
    """
    Creando la cadena de conexion con la base de datos, para asi poder usar 'cursor'
    de esta y poder ejecutar consultas u operaciones SQL
    """
    conn = connect(database=dbname, user=user, password=password)
    return conn

# @app.get('/')
# def home():
#     conn = get_connection()
#     cur = conn.cursor() # es la forma en que se pueden hacer las consultas
#     cur.execute("SELECT 1 + 1") 
#     result = cur.fetchone()
#     print(result)
#     return 'Hola Mundo!'

@app.get('/api/users')
def get_users():
    return 'Getting Users'

@app.post('/api/users')
def create_user():
    #print(request.get_json())
    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
    #print(username, email, password)
    
    conn = get_connection()
    # permite obtener la info ya no en tupla sino en forma de clave valor
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    # postgres despues de insertar, se puede retornar todos los datos
    # usandor 'Returning'
    cur.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING *', (username, email, password))
    
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()
    
    cur.close()
    conn.close()
    
    return jsonify(new_created_user)

@app.delete('/api/users/')
def delete_user():
    return 'Deleting Users'

@app.put('/api/users/')
def update_user():
    return 'Updating Users'

@app.get('/api/users/')
def get_user():
    return 'Gettin User'

if __name__ == '__main__':
    app.run(debug=True)