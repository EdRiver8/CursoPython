import json

persona = {
    "nombre": "kt",
    "apellido": "River",
    "edad": 24
}
objeto_json = json.dumps(persona, indent=2)# dos espacios de indentacion
with open("persona.json", "w") as archivo_json:
    archivo_json.write(objeto_json)

archivo_json.close()
    
# Leer el json =>
with open("persona.json", "r") as datos_json:
    datos = json.load(datos_json)

print(type(datos))
print(datos)
print(f"Nombre: {datos['nombre']}")