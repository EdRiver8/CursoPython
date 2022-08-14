import csv
import os # evita que se pierda la ruta abs dependiendo del pc

# ruta = "csv_vacio.csv"# sino existe lo crea, ruta relativa
# archivo_abierto = open(ruta, "w")# permisos para escribir
# writer = csv.writer(archivo_abierto, delimiter=",")# separador de columnas
# archivo_abierto.close()# cerrar conexion con el archivo

# ruta_abs = "D:\DrivePoli\Programacion Extra\Python\Basico\csv_vacio.csv" #la ruta puede cambiar dependiendo del pc en el que se esta

# ruta_abs_os = os.path.join(os.getcwd(), "csv_vacio.csv")
# print(ruta_abs)
# print(ruta_abs_os)

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Perez", 31],
    ["Emilia", "Clark", 29]
]

datos_dict = [
    {"nombre": "Paco", "apellido": "Botero" ,"edad": 26},
    {"nombre": "Javier", "apellido": "Perez" ,"edad": 31},
    {"nombre": "Emilia", "apellido": "Clark" ,"edad": 29}
]

# archivo = open("datos.csv", "w")
# writer = csv.writer(archivo, delimiter=",")
# archivo.close()
# Otra manera de abrirlo
with open("datos_personas.csv", "w", newline="") as archivo:# new line "" evita una linea vacia entre los datos
    # writer = csv.writer(archivo, delimiter=",")
    # writer.writerow(columnas)
    # writer.writerow(dato)
    # writer.writerows(datos_lista)
    # Para usar el diccionario =>
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dict)
    
# Leer los datos del archivo

with open("datos_personas.csv", "r", encoding="UTF-8") as archivo_lec:
    # reader = csv.reader(archivo_lec)
    # columnas = next(reader) #Evita leer la primera fila (encabezado)
    # print("Columnas: ", columnas)
    # for fila in reader:
    #     #print(fila)
    #     #print(fila[0])
    #Leyendo los datos como dict =>
    reader = csv.DictReader(archivo_lec)
    for fila in reader:
        #print(fila)
        print(fila["nombre"])
    
