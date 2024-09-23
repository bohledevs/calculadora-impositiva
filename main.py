import json

print("Hola mundo")

jurisdicciones = {
    "jurisdiccion": "Argentina",
    "id": 99,
    "impuestos": ["IVA", "Ganancias"],
    "sub_jurisdicciones": [
        {"jurisdiccion": "Ciudad Autónoma de Buenos Aires", "id": 0, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Buenos Aires", "id": 1, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Catamarca", "id": 2, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Chaco", "id": 3, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Chubut", "id": 4, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Córdoba", "id": 5, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Corrientes", "id": 6, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Entre Ríos", "id": 7, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Formosa", "id": 8, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Jujuy", "id": 9, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "La Pampa", "id": 10, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "La Rioja", "id": 11, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Mendoza", "id": 12, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Misiones", "id": 13, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Neuquén", "id": 14, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Río Negro", "id": 15, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Salta", "id": 16, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "San Juan", "id": 17, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "San Luis", "id": 18, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Santa Cruz", "id": 19, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Santa Fe", "id": 20, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Santiago del Estero", "id": 21, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Tierra del Fuego", "id": 22, "impuestos": ["IIBB"], "sub_jurisdicciones": []},
        {"jurisdiccion": "Tucumán", "id": 23, "impuestos": ["IIBB"], "sub_jurisdicciones": []}
    ]
}

# Guardamos el diccionario en un archivo .json 
contenido = open("C:/Users/tomic/OneDrive/Escritorio/Python/jurisdicciones_argentina.json", "w")
json.dump(jurisdicciones, contenido, ensure_ascii=False)
contenido.close()

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