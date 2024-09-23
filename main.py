import json

# Guardamos el diccionario en un archivo .json 
with open("jurisdicciones_argentina.json", "r") as file:
    jurisdicciones = json.load(file)

file.close()

# Función para imprimir el diccionario completo en pantalla
def imprimir_jurisdicciones_simplificado(jurisdiccion, nivel=0):
    print(f"Jurisdicción: {jurisdiccion['jurisdiccion']}")
    print(f"ID: {jurisdiccion['id']}")
    print(f"Impuestos: {', '.join(jurisdiccion['impuestos'])}")
    if jurisdiccion['sub_jurisdicciones']:
        print("Sub-jurisdicciones:")
        for sub in jurisdiccion['sub_jurisdicciones']:
            imprimir_jurisdicciones_simplificado(sub, nivel + 1)

# Llamamos a la función para imprimir el diccionario en pantalla
imprimir_jurisdicciones_simplificado(jurisdicciones)