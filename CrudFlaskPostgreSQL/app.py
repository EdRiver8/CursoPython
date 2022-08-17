from flask import Flask, request, jsonify, send_file
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
  """
  Obtener todos los usuarios registrados
  """
  conn = get_connection()
  cur = conn.cursor(cursor_factory=extras.RealDictCursor) # convierte a diccionario
  cur.execute('SELECT * FROM users')
  users = cur.fetchall()
  cur.close()
  conn.close()
  return jsonify(users) # dict a json

@app.get('/api/users/<id>')
def get_user(id):
  """
  Obtener un solo usuario registrado
  """
  conn = get_connection()
  cur = conn.cursor(cursor_factory=extras.RealDictCursor)
  cur.execute('SELECT * FROM users WHERE id = %s', (id))
  user = cur.fetchone()
  #print(user)
  
  cur.close()
  conn.close()
  
  if user is None:
    return jsonify({'message': 'user not found'}), 404   
  
  return jsonify(user)

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
  #print(new_created_user)
  conn.commit()
  
  cur.close()
  conn.close()
  
  return jsonify(new_created_user)

@app.delete('/api/users/<id>')
def delete_user(id):
  conn = get_connection()
  cur = conn.cursor(cursor_factory=extras.RealDictCursor)
  cur.execute('DELETE FROM users WHERE id = %s RETURNING * ', (id))
  user = cur.fetchone()
  
  conn.commit()# guarde los cambios
  cur.close()
  conn.close()
  
  if user is None:
    return jsonify({'message': 'user not found'}), 404    
  
  return jsonify(user)

@app.put('/api/users/<id>')
def update_user(id):
  conn = get_connection()
  cur = conn.cursor(cursor_factory=extras.RealDictCursor)
  
  user_update = request.get_json()
  username = user_update['username']
  email = user_update['email']
  password = Fernet(key).encrypt(bytes(user_update['password'], 'utf-8'))
  
  cur.execute('UPDATE users SET username = %s, email= %s, password = %s WHERE id = %s RETURNING *', (username, email, password, id))
  updated_user = cur.fetchone()
  
  conn.commit()
  cur.close()
  conn.close()
  
  if user is None:
    return jsonify({'message': 'user not found'}), 404 
  
  return jsonify(updated_user)
  
@app.get('/')
def home():
  return send_file('static/index.html')




if __name__ == '__main__':
  app.run(debug=True)