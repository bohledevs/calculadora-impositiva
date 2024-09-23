

def calcular_impuestos(datos_transaccion):

    impuestos_aplicados = []
    impuestos_nacionales = calcular_nacionales(datos_transaccion)
    impuestos_provinciales = calcular_provinciales(datos_transaccion)
    impuestos_aplicados.append(calcular_nacionales)
    impuestos_aplicados.append(calcular_provinciales)
    return impuestos_aplicados

print("Hola mundo")
