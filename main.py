
import json
<<<<<<< HEAD
import csv


# # Cargamos el archivo JSON con la información de las jurisdicciones
# jurisdicciones = None
# # Abre el archivo JSON en modo lectura y carga los datos en la variable "jurisdicciones"
# with open("jurisdicciones_argentina.json", "r") as file:
#     jurisdicciones = json.load(file)
=======
import random
>>>>>>> 5baaffbfd01f072ba98df96bc5fc93427372be63

# file.close()

# # Función para imprimir el diccionario completo en pantalla, mostrando las jurisdicciones, IDs e impuestos
# # Qué hace?: Esta función imprime la información simplificada de una jurisdicción, mostrando su nombre, ID e impuestos aplicables. Si tiene sub-jurisdicciones, también las imprime recursivamente.
# # Qué ingresa?: Ingresa un diccionario que representa una jurisdicción, y opcionalmente un nivel de profundidad (nivel), utilizado para estructurar la impresión de sub-jurisdicciones.
# # Qué sale?: No devuelve ningún valor, simplemente imprime la información.
# def imprimir_jurisdicciones_simplificado(jurisdiccion, nivel=0):
#     print(f"Jurisdicción: {jurisdiccion['jurisdiccion']}")  # Imprime el nombre de la jurisdicción
#     print(f"ID: {jurisdiccion['id']}")  # Imprime el ID de la jurisdicción
#     print(f"Impuestos: {', '.join(jurisdiccion['impuestos'])}")  # Imprime los impuestos aplicables en la jurisdicción
#     if jurisdiccion['sub_jurisdicciones']:  # Si hay sub-jurisdicciones, las imprime
#         print("Sub-jurisdicciones:")
#         for sub in jurisdiccion['sub_jurisdicciones']:  # Itera sobre cada sub-jurisdicción
#             imprimir_jurisdicciones_simplificado(sub, nivel + 1)

# # Función para imprimir el resumen de una transacción y sus impuestos
# # Qué hace?: Esta función imprime un resumen detallado de una transacción, mostrando la fecha, descripción, cliente, monto, y los impuestos aplicados (IVA, Ganancias, IIBB). También calcula y muestra el total de impuestos y el monto final de la transacción.
# # Qué ingresa?: Ingresa un diccionario que representa la transacción (con claves como 'fecha', 'descripcion', 'monto', etc.) y un saldo que no se utiliza en la función actual.
# # Qué sale?: No devuelve ningún valor, simplemente imprime el resumen de la transacción.
# def imprimir_resumen(transaccion, saldo):
#     fecha = transaccion.get('fecha', 'Sin Fecha')  # Obtiene la fecha de la transacción, o un valor por defecto
#     descripcion = transaccion.get('descripcion', 'Sin Descripcion')  # Obtiene la descripción de la transacción
#     monto = transaccion.get('monto', 0.0)  # Obtiene el monto de la transacción
#     cliente = transaccion.get('cliente', 'Sin Cliente')  # Obtiene el cliente de la transacción
#     IVA = transaccion.get('IVA', 0.0)  # Obtiene el IVA de la transacción
#     ganacias = transaccion.get('ganancias', 0.0)  # Obtiene el valor de Ganancias
#     iibb = transaccion.get('iibb', 0.0)  # Obtiene el valor de IIBB

#     # Resumen general de la transacción
#     print(f"Resumen de la Transacción:")
#     print(f'Fecha: {fecha}')
#     print(f'Descripcion: {descripcion}')
#     print(f'Cliente: {cliente}')
#     print(f"Monto total de la transacción: {monto}")

#     # Detalles sobre los impuestos aplicados a la transacción
#     print("\nDetalles Impositivos:")
#     print(f"IVA: {IVA}")
#     print(f"Ganancias: {ganacias}")
#     print(f"IIBB: {iibb}")
    
#     # Cálculo y muestra del total de impuestos
#     total_impuestos = IVA + ganacias + iibb
#     print(f"Total de Impuestos: {total_impuestos}")

#     # Cálculo y muestra del monto final de la transacción incluyendo los impuestos
#     monto_final = monto + total_impuestos
#     print(f"Monto Final: {monto_final}")

# # Función para obtener los impuestos de una provincia específica
# # Qué hace?: Esta función busca dentro de las sub-jurisdicciones de Argentina y devuelve los impuestos aplicables a una provincia específica.
# # Qué ingresa?: Ingresa el diccionario de jurisdicciones (de Argentina) y el nombre de la provincia como una cadena de texto.
# # Qué sale?: Retorna una lista de impuestos aplicables a la provincia encontrada. Si la provincia no existe, retorna None.
# def obtener_impuestos_provincia(jurisdicciones, provincia):
#     data = jurisdicciones.get("sub_jurisdicciones")  # Obtiene las sub-jurisdicciones del diccionario principal

#     # Itera sobre las sub-jurisdicciones y busca la provincia solicitada
#     for i in range(len(data)):
#         if data[i].get("jurisdiccion") == provincia:  # Compara el nombre de la provincia
#             impuestos = data[i].get("impuestos")  # Obtiene los impuestos de la provincia
#             return impuestos  # Retorna los impuestos encontrados

# # Llamada a la función para obtener los impuestos de la "Ciudad Autonoma de Buenos Aires"
# print(obtener_impuestos_provincia(jurisdicciones, "Ciudad Autonoma de Buenos Aires"))

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


<<<<<<< HEAD
#Login
#Ruta donde se almacenan los usuarios
archivo_csv = 'usuarios.csv'

#Funcion para validar el inicio de sesion
def login():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    with open(archivo_csv, mode='r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == usuario and fila[1] == contraseña:
                print("Inicio de sesion exitoso")
                return True
    print("Usuario o contraseña incorrectos")
    return False

def recuperar_contraseña():
    usuario = input("Ingrese el nombre de usuario: ")
    correo = input("Ingrese el correo electrónico asociado:")

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == usuario and fila[2] == correo:
                print("Recuperacion exitosa.")
                print("Su contraseña es:", fila[1])
                return
    print("Usuario o correo incorrectos.")

def menu():
    while True:
        print("\n1. Registrar.\n2. Iniciar Sesión.\n3. Recuperar contraseña.\n4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            login()
        elif opcion == '3':
            recuperar_contraseña()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

#Ejecutar menu
menu()
=======
    
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
>>>>>>> 5baaffbfd01f072ba98df96bc5fc93427372be63
