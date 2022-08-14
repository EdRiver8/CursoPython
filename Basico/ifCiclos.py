
res = input("ingrese un numero: ")
res
x = int(res)
if x > 2 :
    print("Mas grande que 2")
print("Terminamos con el mayor que 2")

print("veamos si dio en uno de los numeros del sistema")
arr = [10,2,3,5,6,7,15]
print("tamanio arreglo",len(arr))
for val in arr:
    print(val)
    if val == x: 
        print(x, " es un numero del sistema")
        break     
print("Todo terminado")

print("Ingresa numeros, cuando desees terminar, digita \"done\"")
total = 0
count = 0
while True:
    inp = input("Ingresa un numero: ")
    if inp == 'done': break
    val = float(inp)
    total = total + val
    count = count + 1

average = total/count
print ("Average = ", average)