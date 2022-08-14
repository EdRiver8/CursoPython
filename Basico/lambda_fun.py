# Son funciones de una sola expresion (una linea), tambien conocidas como funciones anonimas
# lambda x: x 
# lambda -> sentencia que invoca la funcion
# Primera x -> variable dependiente, argumentos de la func
# Segunda x -> cuerpo de la funcion

print((lambda num: num * 2)(5,)) # evalua inmediatamente la funcion
resul = lambda num: num ** 2
print('Potencia de 5 =',resul(5))

print()

calcular_cuadrado = lambda lado: lado**2
print(calcular_cuadrado(2))
print(calcular_cuadrado(3))
print(calcular_cuadrado(4))

print()

lista = [1,2,3,4,5,6,7,8]
# lista_pares = lambda numero: numero % 2 == 0
# print(lista_pares(2))
# print(lista_pares(3))
lista_pares = list(filter(lambda numero: numero % 2 == 0, lista))# se pasa la lista por el filtro que es lambda
print(f'Numeros pares de la lista: {lista_pares}')

nueva = list(map(lambda numero: numero * 10, lista))
print(f'Resultado Multip = {nueva}')
