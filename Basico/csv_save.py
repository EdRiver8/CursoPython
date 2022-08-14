import csv
# doc = open("archivo.csv", "w")

# doc_csv_w = csv.writer(doc)
# lista = ["Pedro", 88989]
# doc_csv_w.writerow(lista)
# doc.close()

# doc_csv_w = csv.writer(doc)
# lista = [["Pedro", 88989],["Juan", 1000],["Luis", 7],["Anacreta", 19],["Bertilia", 23]]
# doc_csv_w.writerows(lista)
# doc.close()

# doc_csv_w = csv.writer(doc)
# lista = [["Perriana", 88989],["Juan", 1000],["Luis", 7],["Anacreta", 19],["Bertilia", 23]]
# doc_csv_w.writerows(lista)
# for x in lista:
#     doc_csv_w.writerow(x)#permiso dengado = archivo abierto en el pc
# doc.close()

# LEER EL ARCHIVO
doc = open("archivo.csv", "r")
doc_csv = csv.reader(doc)
# for nombre, numero in doc_csv: #deberia funcionar asi pero no lo hace
#     print(nombre, numero)   
for linea in doc_csv:
    #print(linea)   
    for palabra in linea:
        print(palabra)
doc.close()