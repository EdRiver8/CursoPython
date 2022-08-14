"""
res = input("Ingrese un numero cualquiera: ")
try:
    num = int(res)
except:
    num = False

if num != False:    print("El dato ingresado es un numero!")
else:    print("El dato ingresado no es un numero!!!")
"""


#Eliminar multiples elementos
meal = {'fats': 10, 'proteins': 10, 'carbohydrates': 80}
[meal.pop(key) for key in ['fats', 'proteins']]
print(meal)

lista = [2, 4, 3]
print(sorted(lista))
if lista == list(): print ('si')