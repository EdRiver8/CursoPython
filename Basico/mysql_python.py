#pip install mysql-connector-python
#https://www.w3schools.com/python/python_mysql_insert.asp
import mysql.connector

# CONEXION CON LA DB
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_python" # si ya tengo la db 
)

#print(mydb)

mycursor = mydb.cursor()# permite ejecutar las instrucciones sql

# MOTRAR DBS EN MYSQL
mycursor.execute("SHOW DATABASES")
#Imprimir las DB que se tienen
for x in mycursor:
  print(x)
#mycursor.execute("CREATE DATABASE IF NOT EXISTS db_python")

#MOSTRAR TABLAS DE LA DB SELECCIONADA
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
  
#ELIMINAR LAS TABLAS DE LA DB
mycursor.execute("DROP TABLE IF EXISTS db_python.customers")


#CREAR TABLAS DENTRO DE LA DB
# Con PK =>
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#Sin PK=>
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255));")
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


#INSERTAR DATOS DENTRO DE LA DB
mycursor.execute("INSERT INTO db_python.customers (name, address) VALUES ('Kate', '9 Aveneu')")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mila", "17 Road Spring")
mycursor.execute(sql, val)
print("1 record inserted, ID:", mycursor.lastrowid)
# Multiples datos =>
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
print(mycursor.rowcount, "record inserted.")


# LEER LOS DATOS
# todos los datos
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# el primer dato de la tabla
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)
# un solo dato en especifico
# mycursor.execute("SELECT * FROM customers WHERE name = 'Kate'")
# rows = mycursor.fetchall()
# for row in rows:
#     print("Datos en la db cuyo name es Kate: ")
#     print(row)
# Datos que inicien o terminen con 'way'
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# Limitar el resultado a 5
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# Inicie en 3 y termine en 5
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# PREVENIR SQL INJECTION CON %s
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print("Customer with addres = ", x)


# ACTUALIZAR DATOS
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
print(mycursor.rowcount, "records updated")


# Borrar Datos
#mycursor.execute("DELETE FROM customers WHERE name = 'Kate'")
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
print(mycursor.rowcount, "records deleted")



# LO ANTERIOR CON UNA TABLA, AHORA CON DOS TABLAS =>
mycursor.execute("DROP TABLE IF EXISTS users")
mycursor.execute("DROP TABLE IF EXISTS products")


mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")
mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
  ('John', '1'),
  ('Peter', '1'),
  ('Hannah', '2'),
  ('Amy', ''),
  ('Michael', '')
]
mycursor.executemany(sql, val)
print(mycursor.rowcount, "records inserted.")

sql = "INSERT INTO products (name) VALUES ('Chocolate Heaven')"
mycursor.execute(sql)
sql = "INSERT INTO products (name) VALUES ('Tasty Lemons')"
mycursor.execute(sql)
sql = "INSERT INTO products (name) VALUES ('Vanilla Dreams')"
mycursor.execute(sql)
print("records inserted.")

# MOSTRAR LAS PERSONAS QUE TIENEN DULCES PREFERIDOS
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"
  
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)



# GUARDAR CAMBIOS Y CERRAR CONEXION
mydb.commit()#asegurarse que los cambios si se guarden dentro de la db
mydb.close()
