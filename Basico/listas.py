# las listas son ordenadas, mantienen el orden en que son declarados
lenguajes = ["python", "java", "golang"]
lista = [1, 2.0, True, "python",1]
print(lenguajes[0])
print(len(lenguajes))
print(lenguajes[2])# ultima pos
print(lenguajes[-1])# ultima pos
print(lenguajes[-2])# primera pos
print(lenguajes[0:2])
programacion = [lenguajes, "dedicacion", "practica"]
print(programacion)
print(programacion[0][0])
lenguajes[0] = "java"
print(lenguajes[0])
lenguajes.append("python")
print(lenguajes[-1])
otros_lenguajes = ["c", "c++"]
lenguajes.extend(otros_lenguajes)
print(lenguajes)
lenguajes.append(otros_lenguajes)
print(lenguajes)