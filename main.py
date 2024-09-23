import json

jurisdicciones = None
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
# imprimir_jurisdicciones_simplificado(jurisdicciones)

#funcion imprirmir_resumen
def imprimir_resumen(transaccion, saldo):
    fecha = transaccion.get('fecha', 'Sin Fecha')
    descripcion = transaccion.get('descripcion', 'Sin Descripcion')
    monto = transaccion.get('monto', 0.0)
    cliente = transaccion.get('cliente', 'Sin Cliente')
    IVA = transaccion.get('IVA', 0.0)
    ganacias = transaccion.get('ganancias', 0.0)
    iibb = transaccion.get('iibb', 0.0)

    #Resumen de la Transacción
    print(f"Resumen de la Transacción:")
    print(f'Fecha: {fecha}')
    print(f'Descripcion: {descripcion}')
    print(f'Cliente: {cliente}')
    print(f"Monto total de la transacción: {monto}")

    #Detalles Impositivos
    print("\nDetalles Impositivos:")
    print(f"IVA: {IVA}")
    print(f"Ganancias: {ganacias}")
    print(f"IIBB: {iibb}")
    
    #Total de impuestos
    total_impuestos = IVA + ganacias + iibb
    print(f"Total de Impuestos: {total_impuestos}")

    #Monto Final
    monto_final = monto + total_impuestos
    print(f"Monto Final: {monto_final}")

 #funcion buscar_impuesto
def obtener_impuestos_provincia(jurisdicciones, provincia):
    data = jurisdicciones.get("sub_jurisdicciones")

    for i in range(len(data)):

        if data[i].get("jurisdiccion") == provincia:
            impuestos = data[i].get("impuestos")
            return impuestos


    
print(obtener_impuestos_provincia(jurisdicciones, "Ciudad Autonoma de Buenos Aires"))
