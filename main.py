import random

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
        
    condicion_fiscal_iva = int(input("Cual es su condicion fiscal frente al IVA? \n 1. Exento \n 2. Responsable inscripto \n 3. Consumidor final. \n"))
    
    while condicion_fiscal_iva < 1 or condicion_fiscal_iva > 3:
        condicion_fiscal_iva = int(input("Ingrese una condicion fiscal valida: \n 1. Exento \n 2. Responsable inscripto \n 3. Consumidor final. \n"))

    if condicion_fiscal_iva == 1 :
        condicion_fiscal_iva = "Exento"
    elif condicion_fiscal_iva == 2 :
        condicion_fiscal_iva = "Responsable inscripto"
    else:
        condicion_fiscal_iva = "Consumidor final"


    
    condicion_fiscal_iibb = int(input("Cual es su condicion fiscal frente a Ingresos Brutos? \n 1. Local \n 2. Multilateral \n 3. No inscripto. \n"))

    while condicion_fiscal_iibb < 1 or condicion_fiscal_iibb > 3:
        condicion_fiscal_iibb = int(input("Ingrese una condicion fiscal valida: \n 1. Local \n 2. Multilateral \n 3. No inscripto. \n"))
        
    if condicion_fiscal_iibb == 1 :
        condicion_fiscal_iibb = "Local"
    elif condicion_fiscal_iibb == 2 :
        condicion_fiscal_iibb = "Multilateral"
    else:
        condicion_fiscal_iibb = "No inscripto"
        
    
    provincia = int(input("Seleccione una provincia: \n"
      "1. Buenos Aires\n"
      "2. Catamarca\n"
      "3. Chaco\n"
      "4. Chubut\n"
      "5. Córdoba\n"
      "6. Corrientes\n"
      "7. Entre Ríos\n"
      "8. Formosa\n"
      "9. Jujuy\n"
      "10. La Pampa\n"
      "11. La Rioja\n"
      "12. Mendoza\n"
      "13. Misiones\n"
      "14. Neuquén\n"
      "15. Río Negro\n"
      "16. Salta\n"
      "17. San Juan\n"
      "18. San Luis\n"
      "19. Santa Cruz\n"
      "20. Santa Fe\n"
      "21. Santiago del Estero\n"
      "22. Tierra del Fuego\n"
      "23. Tucumán. \n"))

    
    while provincia < 1 or provincia > 23:
        provincia = int(input("Seleccione un número válido de provincia: \n"
                      "1. Buenos Aires\n"
                      "2. Catamarca\n"
                      "3. Chaco\n"
                      "4. Chubut\n"
                      "5. Córdoba\n"
                      "6. Corrientes\n"
                      "7. Entre Ríos\n"
                      "8. Formosa\n"
                      "9. Jujuy\n"
                      "10. La Pampa\n"
                      "11. La Rioja\n"
                      "12. Mendoza\n"
                      "13. Misiones\n"
                      "14. Neuquén\n"
                      "15. Río Negro\n"
                      "16. Salta\n"
                      "17. San Juan\n"
                      "18. San Luis\n"
                      "19. Santa Cruz\n"
                      "20. Santa Fe\n"
                      "21. Santiago del Estero\n"
                      "22. Tierra del Fuego\n"
                      "23. Tucumán. \n"))
        
    provincia_seleccionada = provincias_argentina[provincia]

    datos = {
        "monto": monto,
        "condicion_iva": condicion_fiscal_iva,
        "condicion_ibb": condicion_fiscal_iibb,
        "provincia": provincia_seleccionada
    }

    print(datos)
    
    return datos


        

## PROGRAMA PRINCIPAL
datos_transaccion = obtener_entrada()
# impuestos_aplicados = calcular_impuestos(datos_transaccion)
# imprimir_resumen(datos_transaccion, impuestos_aplicados)