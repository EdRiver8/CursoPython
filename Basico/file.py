#cuenta la cantidad de lineas que tiene un archivo y al final lo lee
fname = input("Ingrese el nombre del archivo para abrir: ")
try: 
    #fhand = open('prueba.txt')
    fhand = open (fname, "r")
except: 
    #print("El archivo ", fname, " no se puede abrir")
    #quit() #termina el programa 
    print("El archivo ", fname, "no se puede abrir o no existe, por defecto se tomara el ",
    "archivo \"prueba2.txt\"")
    fhand = open ("prueba2.txt", "r")

count = 0
for line in fhand:
    count = count + 1
    
print("Cantidad de lineas en el doc: " , count) 

for line in fhand:
    print(line)
print(fhand.read())

""" inp = fhand.read()
print(len(inp))
print(inp[:20]) """