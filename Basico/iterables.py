# range(inicio, fin, paso)
serie1 = range(5)# 0 - 5
print(serie1)
print(list(serie1))

serie2 = range(5, 10)
print(list(serie2))

serie3 = range(3, 10, 2)
print(list(serie3))

for element in serie3:
    print(element)
    
print()

nombres = ['Ed', 'Mile', 'Lili']
apellidos = ['River', 'Bol', 'Perez']

# zip crea la cantidad de tuplas de la menor lista
nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo)

nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)
    
print()

# enumerate(iterable, start=0) crea indices y se puede indicar desde donde comenzar
nombres = ['Ed', 'Mile', 'Lili']
nombres_enumerados = enumerate(nombres)
print(list(nombres_enumerados))
nombres_enumerados = enumerate(nombres, start=5)
print(list(nombres_enumerados))
for indice, element in enumerate(nombres):
    print(indice, element)
    
print()
nombres = ['Ed', 'Alex', 'Kate']
for nombre in nombres:
    print(nombre)
else:
    print("Ciclo Terminado!")
    
print()


# def calcular_cuadrado(num):
#     return num ** 2
cuadrado = lambda num: num ** 2
lista = [1,2,3,4,5,6,7]
lista_cuadrados = []

# for nume in lista:
#     lista_cuadrados.append(cuadrado(nume))
    
# print(f'Cuadrados = {lista_cuadrados}')

map_cuadrados = map(cuadrado, lista)
print(f'Cuadrados = {list(map_cuadrados)}')

print()

# LIST COMPREHENSION
# lista = [expresion(elemento) for elemento in obj_iterable]
# lista_comprehension = [num ** 2 for num in lista]
lista_comprehension = [cuadrado(num) for num in lista]
print(f'Cuadrados por Lista Comprehension = {lista_comprehension}')

print()

def es_par(num):
    return num % 2 == 0

lista_cuadrados_pares = [cuadrado(num) for num in lista if es_par(num)]
print(f'Lista de cuadrados pares = {lista_cuadrados_pares}')

# Lo mismo pero usando walrus :=
pares_walrus = [cuadra for num in lista if(cuadra := cuadrado(num)) %2 == 0]
print(f'Lista de cuadrados por Walrus = {pares_walrus}')

# si es par se agrega el cuadrado, sino, se agrega un 0
lista_resultados = [cuadrado(num) if es_par(num) else 0 for num in lista]
print(f'Lista de cuadrados = {lista_resultados}')


print()

#clave vocal en minus, valor vocal mayus
vocales = 'aeiou'
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)


    