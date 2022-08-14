def calcular_area_cuadrado(lado):
    """Calcular el area de un cuadrado"""
    area = lado * lado
    return area

area_cuadrado = calcular_area_cuadrado(lado=5)
print('Area del cuadrado', area_cuadrado)

# '*args' recibe todo los parametros en forma de tupla
def calcular_perimetro(*args):
    """Calcular el area de un cuadrado"""
    perimetro = 0
    #print(args)
    for lado in args:
        perimetro += lado
    return perimetro

print(f'Perimetro Cuadrado = {calcular_perimetro(1,2,3,4)}')
print(f'Perimetro Triangulo = {calcular_perimetro(1,2,3,4)}')

# enviando kwargs, clave valor o dict
def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f'Llave: {llave}, Valor: {valor}')
    print(kwargs["nombre"], kwargs["apellido"])

funcion_kwargs(nombre="Ed", apellido="River")

# # Genera error =>
# def parametros_desordenados(nombre, apellido, **kwargs, *args):
#     pass

# usando los tres tipos de parametros respetando el orden
def parametros_ordenados(nombre, apellido, *args, **kwargs):
    pass

