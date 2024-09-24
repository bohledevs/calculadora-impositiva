import json

# Cargamos el archivo JSON con la información de las jurisdicciones
jurisdicciones = None
# Abre el archivo JSON en modo lectura y carga los datos en la variable "jurisdicciones"
with open("jurisdicciones_argentina.json", "r") as file:
    jurisdicciones = json.load(file)

file.close()

# Función para imprimir el diccionario completo en pantalla, mostrando las jurisdicciones, IDs e impuestos
def imprimir_jurisdicciones_simplificado(jurisdiccion, nivel=0):
    print(f"Jurisdicción: {jurisdiccion['jurisdiccion']}")  # Imprime el nombre de la jurisdicción
    print(f"ID: {jurisdiccion['id']}")  # Imprime el ID de la jurisdicción
    print(f"Impuestos: {', '.join(jurisdiccion['impuestos'])}")  # Imprime los impuestos aplicables en la jurisdicción
    if jurisdiccion['sub_jurisdicciones']:  # Si hay sub-jurisdicciones, las imprime
        print("Sub-jurisdicciones:")
        for sub in jurisdiccion['sub_jurisdicciones']:  # Itera sobre cada sub-jurisdicción
            imprimir_jurisdicciones_simplificado(sub, nivel + 1)

# Función para imprimir el resumen de una transacción y sus impuestos
def imprimir_resumen(transaccion, saldo):
    fecha = transaccion.get('fecha', 'Sin Fecha')  # Obtiene la fecha de la transacción, o un valor por defecto
    descripcion = transaccion.get('descripcion', 'Sin Descripcion')  # Obtiene la descripción de la transacción
    monto = transaccion.get('monto', 0.0)  # Obtiene el monto de la transacción
    cliente = transaccion.get('cliente', 'Sin Cliente')  # Obtiene el cliente de la transacción
    IVA = transaccion.get('IVA', 0.0)  # Obtiene el IVA de la transacción
    ganacias = transaccion.get('ganancias', 0.0)  # Obtiene el valor de Ganancias
    iibb = transaccion.get('iibb', 0.0)  # Obtiene el valor de IIBB

    # Resumen general de la transacción
    print(f"Resumen de la Transacción:")
    print(f'Fecha: {fecha}')
    print(f'Descripcion: {descripcion}')
    print(f'Cliente: {cliente}')
    print(f"Monto total de la transacción: {monto}")

    # Detalles sobre los impuestos aplicados a la transacción
    print("\nDetalles Impositivos:")
    print(f"IVA: {IVA}")
    print(f"Ganancias: {ganacias}")
    print(f"IIBB: {iibb}")
    
    # Cálculo y muestra del total de impuestos
    total_impuestos = IVA + ganacias + iibb
    print(f"Total de Impuestos: {total_impuestos}")

    # Cálculo y muestra del monto final de la transacción incluyendo los impuestos
    monto_final = monto + total_impuestos
    print(f"Monto Final: {monto_final}")

# Función para obtener los impuestos de una provincia específica
def obtener_impuestos_provincia(jurisdicciones, provincia):
    data = jurisdicciones.get("sub_jurisdicciones")  # Obtiene las sub-jurisdicciones del diccionario principal

    # Itera sobre las sub-jurisdicciones y busca la provincia solicitada
    for i in range(len(data)):
        if data[i].get("jurisdiccion") == provincia:  # Compara el nombre de la provincia
            impuestos = data[i].get("impuestos")  # Obtiene los impuestos de la provincia
            return impuestos  # Retorna los impuestos encontrados

# Llamada a la función para obtener los impuestos de la "Ciudad Autonoma de Buenos Aires"
print(obtener_impuestos_provincia(jurisdicciones, "Ciudad Autonoma de Buenos Aires"))
