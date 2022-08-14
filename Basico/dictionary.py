dicc = dict()
dicc = {
    "p": "2",
    "x": "1",
    "y": "3",
}
print(dicc)

cars = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(cars)
x = cars.keys()
print(x)
cars["colors"] = "white" #reemplaza toda la tupla por un solo valor
print(x)
print(cars)
print(cars.values())
if "electric" in cars:
  print("Yes, 'electric' is one of the keys in the thisdict dictionary")




#Diccionarios Anidados
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)



#guarda nombres y edades en un diccionario
import re

cont = 0
nombres = dict()
finish = ""
buscar = "[Nn]" 
print("Ingrese los nombres y edades que va a guardar, cuando termiene, ingrese \"N\".")
while True:
    if cont != 0: 
        print("Desea agregar una nueva persona?\t" )
        finish = input("Y = Si, N = No... ")        
        if re.search(buscar, finish) is None: print("Mostrando Datos Ingresados: ")
    nombre = input("Ingrese nombre: ")
    edad = input("Ingrese edad: ")    
    cont = cont + 1
    nombres[nombre] = edad

print(nombres)


#Eliminar multiples elementos
meal = {'fats': 10, 'proteins': 10, 'carbohydrates': 80}
[meal.pop(key) for key in ['fats', 'proteins']]
print(meal)




#guarda nombres en un diccionario, asignando una clave sucesiva ascendente a cada uno de ellos 
"""cont = 0
nombres = dict()
print("Ingrese los nombres que va a guardar, cuando termiene, ingrese \"exit\".")
while True:
    res = input("Ingrese nombre: ")
    if res == 'exit': break
    cont = cont + 1
    nombres[res] = cont

res = input("Ingrese un nombre que desea saber si esta en el diccionario: ")
if res in nombres: print(res, " hace parte del diccionario")
else: print(res, " como nombre no existe")

print("El diccionario de nombres con claves es: ")
print(nombres)"""

"""
#divide una frase en palabras y luego cuenta las veces que se repiten las palabras
counts = dict()
print("Ingrese un texto cualquiera: ")
line = input('')
#lista de palabras words
words = line.split()
print('Words:', words)
print('Contando...')
for word in words:
    if(word in counts):#si ya esta en la lista al value le suma 1
        counts[word] = counts.get(word) + 1 #retorna value y le suma uno
        print ("Palabra: ", word, " Clave: ", counts[word])
    else: #sino al value lo hace igual a uno
        counts[word] = 1
        print ("Palabra: ", word, " Clave: ", counts[word])
    #Version corta =>
    #counts[word] = counts.get(word, 0) + 1 #obten el valor actual del word o cero y sumale 1
print('Cuenta: ', counts)
"""

"""
#dividir una frase en letras
contLet = dict()
cadena = input("Ingrese una frase: ")
simbolos = list(cadena)
print(simbolos)#imprimi todos los simbolos de la frase en forma de lista (vector)
for simbolo in simbolos:
    contLet[simbolo] = contLet.get(simbolo, 0) + 1
print(contLet)
"""


"""
#lee un documento, cuenta la cantidad de veces que se repite una palabra y retorna la de mayor repeticiones
fname = input("Ingrese el nombre del archivo a abrir: ")
try:
    fhand = open (fname, "r")
except:
    print("El archivo ", fname, " no se puede abrir o no existe, por defecto se tomara el ",
    "archivo \"words.txt\"")
    fhand = open ("words.txt", "r")
#if len(fname) < 1: fname = "words.txt" #abrir archivo default
#cuenta las veces que se repite cada palabra en el documento, eliminando los espacios con split
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] =  counts.get(word, 0) + 1
#muestra la palabra que se repite mas veces
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
"""

