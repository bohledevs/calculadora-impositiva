
import json
import random

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

# Llaves de la entrada
LLAVE_CF_IVA = "condicion_fiscal_iva"
LLAVE_CF_IIBB = "condicion_fiscal_iibb"
LLAVE_MONTO = "monto"
LLAVE_PROVINCIA = "provincia"


# Llaves de la salida
LLAVE_TASA = "tasa"
LLAVE_IMPUESTO = "impuesto"
LLAVE_TITULO = "titulo"


# El usuario ingresa los datos requeridos en la pantalla.
# La función encapsula los datos en un diccionario, y lo retorna.
def obtener_entrada():
    
    datos_transaccion = {}

    monto = int(input("Ingrese el monto: "))
    
    while monto < 1:
        monto = int(input("Ingrese un monto correcto: "))
        
    datos_transaccion[LLAVE_MONTO] = monto 

    condicion_fiscal_iva = int(input("Cual es su condicion fiscal frente al IVA? \n 1. Exento \n 2. Responsable inscripto \n 3. Consumidor final: \n Respuesta: "))
    
    while condicion_fiscal_iva < 1 or condicion_fiscal_iva > 3:
        condicion_fiscal_iva = int(input("Ingrese una condicion fiscal valida: \n 1. Exento \n 2. Responsable inscripto \n 3. Consumidor final \n Respuesta: "))

    if condicion_fiscal_iva == 1 :
        condicion_fiscal_iva = "Exento"
    elif condicion_fiscal_iva == 2 :
        condicion_fiscal_iva = "Responsable Inscripto"
    else:
        condicion_fiscal_iva = "Consumidor Final"
    
    datos_transaccion[LLAVE_CF_IVA] = condicion_fiscal_iva

    condicion_fiscal_iibb = int(input("Cual es su condicion fiscal frente a Ingresos Brutos? \n 1. Local \n 2. Multilateral \n 3. No inscripto \n Respuesta: "))

    while condicion_fiscal_iibb < 1 or condicion_fiscal_iibb > 3:
        condicion_fiscal_iibb = int(input("Ingrese una condicion fiscal valida: \n 1. Local \n 2. Multilateral \n 3. No inscripto \n Respuesta: "))
        
    if condicion_fiscal_iibb == 1 :
        condicion_fiscal_iibb = "Local"
    elif condicion_fiscal_iibb == 2 :
        condicion_fiscal_iibb = "Multilateral"
    else:
        condicion_fiscal_iibb = "No inscripto"
        
    datos_transaccion[LLAVE_CF_IIBB] = condicion_fiscal_iibb
    
    indice_provincia = int(input(f"Ingrese el número correspondiente a su provincia: \n {imprimir_tupla(provincias_argentina)} \n Respuesta: "))
    while indice_provincia < 1 or indice_provincia > 23:
        indice_provincia = int(input(f"Ingrese el número correspondiente a su provincia válido: \n {imprimir_tupla(provincias_argentina)} \n Respuesta: "))
    provincia = provincias_argentina[indice_provincia-1]

    datos_transaccion[LLAVE_PROVINCIA] = provincia

    return datos_transaccion
        

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



    datos_transaccion[LLAVE_CF_IIBB] = condicion_fiscal_iibb
    
    indice_provincia = int(input(f"Ingrese el número correspondiente a su provincia: \n{imprimir_tupla(provincias_argentina)} Nro. de Provincia \n Respuesta: "))
    while indice_provincia < 1 or indice_provincia > 23:
       indice_provincia = int(input(f"Ingrese un número válido: \n{imprimir_tupla(provincias_argentina)} Nro. de Provincia \n Respuesta: "))
    provincia = provincias_argentina[indice_provincia-1]

    datos_transaccion[LLAVE_PROVINCIA] = provincia
    
    return datos_transaccion


# Imprime tuplas, numeradas por su indice
def imprimir_tupla(tupla):
    resultado = ""
    for indice, elemento in enumerate(tupla):
        resultado += f"{indice + 1}. {elemento}\n"
    return resultado



# Tupla de provincias argentinas
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


condiciones_iibb = (
    "Local",
    "Multilateral",
    "No inscripto"
)

# Función para imprimir el diccionario completo en pantalla
def imprimir_jurisdicciones_simplificado(jurisdiccion, nivel=0):
    print(f"Jurisdicción: {jurisdiccion['jurisdiccion']}")
    print(f"ID: {jurisdiccion['id']}")
    print(f"Impuestos: {', '.join(jurisdiccion['impuestos'])}")
    if jurisdiccion['sub_jurisdicciones']:
        print("Sub-jurisdicciones:")
        for sub in jurisdiccion['sub_jurisdicciones']:
            imprimir_jurisdicciones_simplificado(sub, nivel + 1)

#funcion buscar_impuesto
def obtener_impuestos_provincia(jurisdicciones, provincia):
    data = jurisdicciones.get("sub_jurisdicciones")

    for i in range(len(data)):

        if data[i].get("jurisdiccion") == provincia:
            impuestos = data[i].get("impuestos")
            return impuestos

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


# Recibe los datos del usuario y retorna los impuestos aplicados
def calcular_impuestos(datos_transaccion):
    return calcular_nacionales(datos_transaccion) + calcular_provinciales(datos_transaccion)


def calcular_nacionales(datos_transaccion):
    condicion_fiscal_iva = datos_transaccion.get(LLAVE_CF_IVA)
    monto = datos_transaccion.get(LLAVE_MONTO)
    return [calcular_iva(monto, condicion_fiscal_iva), calcular_ganancias(monto, condicion_fiscal_iva)]

# Funcion para calcular IVA
def calcular_iva(monto, cf):
    
    resumen = {}

    tasa = 0
    if (cf == "Responsable Inscripto"):
        tasa = 10.5
    elif (cf == "Consumidor Final"):
        tasa = 21.0
    resumen[LLAVE_TASA] = tasa

    impuesto_aplicado = monto * (tasa/100)
    resumen[LLAVE_IMPUESTO] = impuesto_aplicado
    resumen[LLAVE_TITULO] = "IVA"

    return resumen

# Funcion para calcular IVA
def calcular_ganancias(monto, cf):
    
    resumen = {}
    resumen[LLAVE_TITULO] = "Ganancias"

    tasa = 0
    if (cf == "Responsable Inscripto"):
        tasa = 0.5
    elif (cf == "Consumidor Final"):
        tasa = 2.0
    resumen[LLAVE_TASA] = tasa

    impuesto_aplicado = monto * (tasa/100)
    resumen[LLAVE_IMPUESTO] = impuesto_aplicado

    return resumen


def calcular_provinciales(datos_transaccion):
    condicion_fiscal_iibb = datos_transaccion.get(LLAVE_CF_IIBB)
    monto = datos_transaccion.get(LLAVE_MONTO)
    provincia = datos_transaccion.get(LLAVE_PROVINCIA)
    return [calcular_iibb(monto, condicion_fiscal_iibb, provincia)]


def calcular_iibb(monto, cf, provincia):

    resumen = {}
    resumen[LLAVE_TITULO] = "IIBB"

    matriz = crearMatrizAlicuotas()
    indice_jurisdiccion = provincias_argentina.index(provincia)
    indice_cf = condiciones_iibb.index(cf)
    
    tasa = matriz[indice_jurisdiccion][indice_cf]
    resumen[LLAVE_TASA] = tasa

    impuesto_aplicado = monto * (tasa/100)
    resumen[LLAVE_IMPUESTO] = impuesto_aplicado

    return resumen


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
    return matriz

# Funcion para generar valores de alicuotas ficticios
def generarValoresAlicoutas():

    alicouta = round(random.uniform(0.2, 7), 1)

    return alicouta

# Funcion para imprimir matriz - (A cambiar para que quede mejor visualmente)
def imprimirMatriz(matriz):
    print("Matriz de Alicuotas:")
    print("-" * 30)
    print("{:<10} {:<10} {:<10}".format("No inscripto", "Local", "Multilateral"))
    print("-" * 30)
    
    for fila in matriz:
        print("{:<10.1f} {:<10.1f} {:<10.1f}".format(fila[0], fila[1], fila[2]))


def imprimir_resumen(datos_transaccion, impuestos_aplicados):
    # Extraemos los datos de la transacción
    monto = datos_transaccion['monto']
    condicion_iva = datos_transaccion['condicion_fiscal_iva']
    condicion_iibb = datos_transaccion['condicion_fiscal_iibb']
    provincia = datos_transaccion['provincia']

    # Título principal
    print("==== Resumen de la Transacción ====\n")
    
    # Detalles de la transacción
    print(f"Provincia: {provincia}")
    print(f"Monto: ${monto:.2f}")
    print(f"Condición Fiscal IVA: {condicion_iva}")
    print(f"Condición Fiscal IIBB: {condicion_iibb}\n")
    
    # Título para los impuestos
    print("==== Impuestos Aplicados ====\n")

    # Detalles de los impuestos aplicados
    for impuesto in impuestos_aplicados:
        titulo = impuesto['titulo']
        tasa = impuesto['tasa']
        monto_impuesto = impuesto['impuesto']
        print(f"{titulo}:")
        print(f"  - Tasa: {tasa}%")
        print(f"  - Monto del impuesto: ${monto_impuesto:.2f}\n")
   

## PROGRAMA PRINCIPAL
datos_transaccion = obtener_entrada()
impuestos_aplicados = calcular_impuestos(datos_transaccion)
# print(datos_transaccion)
# print(impuestos_aplicados)
imprimir_resumen(datos_transaccion, impuestos_aplicados)

 

