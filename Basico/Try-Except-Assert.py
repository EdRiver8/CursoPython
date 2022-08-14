def calcular_promedio(lista):
    assert len(lista)>0, "La lista esta vacia!"
    return sum(lista)/len(lista)

# try:
#     promedio = calcular_promedio(lista=[])
#     print(promedio)
# except:
#     print("La funcion no puede calcular el promedio")

    
# try:
#     promedio = calcular_promedio(lista=[])
#     print(promedio)
# except Exception as e:
#     print("La funcion no puede calcular el promedio")
#     print(e)
    
    
# try:
#     promedio = calcular_promedio(lista=[])
#     print(promedio)
# except AssertionError as assert_error:
#     print(assert_error)
# except Exception as e:
#     print("La funcion no puede calcular el promedio")
#     print(e)
    
    
# try:
#     promedio = calcular_promedio(lista=["Texto"])
#     print(promedio)
# except AssertionError as assert_error:
#     print(assert_error)
# except Exception as e:
#     print("La funcion no puede calcular el promedio")
#     print(e)


try:
    promedio = calcular_promedio(lista=[1,2,3,4,5])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("La funcion no puede calcular el promedio")
    print(e)