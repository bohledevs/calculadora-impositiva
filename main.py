import random
print("Hola mundo")

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


crearMatrizAlicuotas()


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
        
    
        