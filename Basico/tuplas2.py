fhand = open('romeo.txt')
counts = dict()
for line in fhand:#divide el documento en lineas
    words = line.split()
    for word in words:#divide las lineas en palabras
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():#cada par clave y valor lo guarda como nueva tupla y lo agg al final de la lista
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)#ordena la lista descendentemente por clave

for val, key in lst[:10]:#imprime los elementos de 0 a 10 par valor clave de la lista
    print(key, val)

#forma corta de hacer lo anterior
c = {'a':10, 'b':3, 'c': 22}
print(sorted([
    (v,k) for k,v in c.items()
]))