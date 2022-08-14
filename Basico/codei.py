f = open('prueba2', 'w+b')
letra = 'a'
numero = 20

letra2 = 'b'
numero2 = 5

binary_format = bytes(letra, 'utf-8')
f.write(binary_format)
binary_format = bytes([numero])
f.write(binary_format)

binary_format = bytes(letra2, 'utf-8')
f.write(binary_format)
binary_format = bytes([numero2])
f.write(binary_format)

f.close()

file = open("my_file", "rb")

bandera = True
byte = file.read(1)
while byte:
    if(bandera):
        print(byte)
        byte = file.read(1)
        bandera = False
    else:
        s = int(byte)
        print(s)
        byte = file.read(1)
        bandera = True