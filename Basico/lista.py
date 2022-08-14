"""print("Ingresa numeros, cuando desees terminar, digita \"done\"")
total = 0
count = 0
while True:
    inp = input("Ingresa un numero: ")
    if inp == 'done': break
    val = float(inp)
    total = total + val
    count = count + 1

average = total/count
print ("Average = ", average)"""

#otra manera usando listas =>
print("Ingresa numeros, cuando desees terminar, digita \"done\"")
numlist = list()
while True:
    inp = input("Ingresa un numero: ")
    if inp == 'done': break
    val = float(inp)
    numlist.append(val)

average = sum(numlist)/len(numlist)
print ("Average = ", average)

 