
import json
import random

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

# Recibe los datos del usuario y retorna los impuestos aplicados
def calcular_impuestos(datos_transaccion):
    impuestos_aplicados = []
    impuestos_nacionales = calcular_nacionales(datos_transaccion)
    impuestos_provinciales = calcular_provinciales(datos_transaccion)
    impuestos_aplicados.append(calcular_nacionales)
    impuestos_aplicados.append(calcular_provinciales)
    return impuestos_aplicados

#funcion que pida al usuario los datos y los retorne al diccionario
def obtener_datos_usuario():
    # Crear el diccionario
    datos = {}
    
    # Pedir datos al usuario
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    email = input("Ingrese su correo electrónico: ")
    
    # Almacenar los datos en el diccionario
    datos["Nombre"] = nombre
    datos["edad"] = edad
    datos["email"] = email
    
    return datos

#tupla de provincias arg
provincias_argentina = (
    "Buenos Aires",
    "Catamarca",
    "Chaco",
    "Chubut",
    "Córdoba",
    "Corrientes",
    "Entre Ríos",
    "Formosa",
    "Jujuy",
    "La Pampa",
    "La Rioja",
    "Mendoza",
    "Misiones",
    "Neuquén",
    "Río Negro",
    "Salta",
    "San Juan",
    "San Luis",
    "Santa Cruz",
    "Santa Fe",
    "Santiago del Estero",
    "Tierra del Fuego",
    "Tucumán"
)

def crearMatrizAlicuotas():

    matriz = []
    filas = 23
    columnas = 3

    for i in range (filas):
        fila = []
        for j in range(columnas):
            # Generar valores de alicoutas random y ordenarlos de mayor a menos
            valores = [generarValoresAlicoutas() for _ in range(3)]
            valores.sort()

            #  Agregar los valores a la fila
            fila = [valores[2], valores[1], valores[0]] 

        matriz.append(fila)
        
    
    imprimirMatriz(matriz)


# Funcion para generar valores de alicuotas ficticios
def generarValoresAlicoutas():

    alicouta = round(random.uniform(0.2, 7), 1)

    return alicouta


# Funcion para calcular IVA
def calcularIva(monto, IVA):
    
    impuesto_iva = (monto * IVA) / 100

    return impuesto_iva

# Funcion para calcular impuesto a las ganancias

def  calcularGanancias(monto, ganancias):
    
    impuesto_ganancias = (monto * ganancias) / 100

    return impuesto_ganancias

# Funcion para imprimir matriz - (A cambiar para que quede mejor visualmente)
def imprimirMatriz(matriz):
    print("Matriz de Alicuotas:")
    print("-" * 30)
    print("{:<10} {:<10} {:<10}".format("No inscripto", "Local", "Multilateral"))
    print("-" * 30)
    
    for fila in matriz:
        print("{:<10.1f} {:<10.1f} {:<10.1f}".format(fila[0], fila[1], fila[2]))

# Ingreso de datos del usuario
def obtener_entrada():
    
    monto = int(input("Ingrese el monto: "))
    
    while monto < 1:
        monto = int(input("Ingrese un monto correcto: "))
        
    condicion_fiscal_iva = int(input("Cual es su condicion fiscal frente al IVA? \n 1. Exento \n 2. Responsable inscripto \n 3. Consumidor final"))
    
    while condicion_fiscal_iva < 1 and condicion_fiscal_iva > 3:
        condicion_fiscal_iva = int(input("Ingrese una condicion fiscal valida: \n 1. Exento \n 2. Responsable inscripto \n 3. Consumidor final"))

    if condicion_fiscal_iva == 1 :
        condicion_fiscal_iva = "Exento"
    elif condicion_fiscal_iva == 2 :
        condicion_fiscal_iva = "Responsable inscripto"
    else:
        condicion_fiscal_iva = "Consumidor final"


    
    condicion_fiscal_iibb = int(input("Cual es su condicion fiscal frente a Ingresos Brutos? \n 1. Local \n 2. Multilateral \n 3. No inscripto"))

    while condicion_fiscal_iibb < 1 and condicion_fiscal_iibb > 3:
        condicion_fiscal_iibb = int(input("Ingrese una condicion fiscal valida: \n 1. Local \n 2. Multilateral \n 3. No inscripto"))
        
    if condicion_fiscal_iibb == 1 :
        condicion_fiscal_iibb = "Local"
    elif condicion_fiscal_iibb == 2 :
        condicion_fiscal_iibb = "Multilateral"
    else:
        condicion_fiscal_iibb = "No inscripto"
        

## PROGRAMA PRINCIPAL
datos_transaccion = obtener_entrada()
impuestos_aplicados = calcular_impuestos(datos_transaccion)
imprimir_resumen(datos_transaccion, impuestos_aplicados)
