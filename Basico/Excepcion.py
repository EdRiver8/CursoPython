# Se intenta abrir un archivo y se genera la captura de la excepción
try:
    with open('archivo.txt') as file:
        read_data = file.read()
# Capturamos la excepción 
except OSError:
    print('OSError. No se pudo abrir') 
