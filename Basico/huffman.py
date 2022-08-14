#se aplica el algoritmo de comprension de Hoffman para codificar un archivo y enviarlo con su
#respectivo diccionario de datos en otro archivo terminacion .arq

#abre el documento con el que se va a trabajar o se toma el documento por default
fname = input("Ingrese el nombre del archivo a abrir: ")
try:
    fhand = open (fname, "r")
except:
    print("El archivo ", fname, "no se puede abrir o no existe, por defecto se tomara el ",
    "archivo \"prueba2.txt\"")
    fhand = open ("prueba2.txt", "r")

#if fhand.stat(fhand).st_size == 0:    print('File is empty')
#print("Contenido del documento:\n", fhand.read())



#se determina la frecuencia de cada simbolo dentro del archivo de texto (cuenta la cantidad de veces que se repite un simbolo en el documento)
def frecuenciaSimbolo(filehandle):
    contSim = dict() #contador de veces que se repite un simbolo
    tamOrigBit = 0  #variable que guarda el tamaño original en bits del archivo sin contar los espacios
    for line in filehandle:  
        #words = line.split() #cada linea del cocumento lo separa en palabras, eliminando espacios en blancos   
        for word in line:  #cada palabra la convierte en una lista de simbolos 
            simbolos = list(word)
            for simbolo in simbolos:    #cada lista de simbolos los recorre para contas las veces que se repiten
                contSim[simbolo] =  contSim.get(simbolo, 0) + 1 #guarda cada simbolo y su repeticion en el diccionario contador de letras
                tamOrigBit = tamOrigBit + len(simbolo) * 7 #cada letra se multiplica por 7(cantidad de bits que ocupa cada simbolo)
    #print("Letras y cantidad de repeticiones sin ordenar: ", contSim)
    #print("Tamaño original del archivo en bits:  ", tamOrigBit)
    return contSim, tamOrigBit



#ordenar el diccionario formado por el texto
def ordenar(dic):    
    orderDict = dict() #diccionario ordenado
    auxLst = list() #lista con la que se va a ordenanar el antiguo diccionario, guardando tuplas key, value
    for k,v in dic.items(): #para cada par clave valor en contador de letras
        tpl = (v, k) #se crea una nueva tupla asignando valor y clave, elementos invertidos para que al ordenar 
                    #la lista, lo haga por valores, de lo contrario la ordena alfabeticamente
        auxLst.append(tpl) #se agrega la tupla a la lista auxiliar
    auxLst = sorted(auxLst) #ordena la lista de menor a mayor repeticion del simbolo
    #print("Lista ordenada ascendentemente por valor", auxLst)
    #despues de ordenarla, se llevan los valores ordenados al nuevo diccionario
    for v,k in auxLst:  #recorre toda la lista de tuplas
        tpl = (k, v)    #crea una tupla par key, value
        orderDict[k] = v    #almacena en el directorio ordenado el key y le asigna su respectivo valor
    #print("Diccionario ordenado: ", orderDict)
    return orderDict


conteoSimbol, sizeOrigBit  = frecuenciaSimbolo(fhand) #guardan respectivamente los valores que retorna la funcion "frecuenciaSimbolo"
diccOrdenado = ordenar(conteoSimbol)    #Lleva el diccionario con el conteo y lo retorna ordenado
dicCopOrig = diccOrdenado.copy() #crea una copia del diccionario original
print("Diccionario ordenado: ", diccOrdenado)

#if "a" in diccOrdenado:  print("Yes, 'a' is one of the keys in the thisdict dictionary")
#diccOrdenado['a'] = 21 #cambia el valor de una clave
#valor = dicCopOrig.pop('a')
#print("Valor de la a eliminada: ", valor)
#print(dicCopOrig)


def agrupar(dic):
    cont = 0; valor = 0
    auxDic = dict()
    lista = list()
    for k,v in dic.items():        
        if cont <= 1:     
            lista.append(k)
            valor += dic[k]  #suma los valores de los 2 1ros simbolos 
        if cont == 1: #si es igual a uno, ya termino de crear los grupos de los primeros simbolos 
            lista.append(valor)
            lista.append(lista[0] + lista [1])
            auxDic[lista[3]] = lista  #se agrega la clave (suma de los dos simbolos) y su valor al diccionario      
        auxDic[k] = v
        cont += 1        
    #auxDic.pop(lista[1], 404)
    [auxDic.pop(key) for key in [lista[0], lista[1]]] #Eliminacion multiple del diccionario los datos que ya se encuentra agrupados en la lista
    return auxDic

aux = agrupar(diccOrdenado)  
print(aux)
#print("Agrupada: ", agrupar(aux))
  

