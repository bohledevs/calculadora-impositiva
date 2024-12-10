from llaves import *

condiciones_iva = (
    "Exento",
    "Responsable Inscripto",
    "Consumidor Final"
)

condiciones_iibb = (
    "Local",
    "Multilateral",
    "No inscripto"
)

def calcular_iva(monto, cf):
    
    resumen = {}

    tasa = 0
    if (cf == condiciones_iva[1]):
        tasa = 10.5
    elif (cf == condiciones_iva[2]):
        tasa = 21.0
    resumen[LLAVE_TASA] = tasa

    impuesto_aplicado = monto * (tasa/100)
    resumen[LLAVE_IMPUESTO] = impuesto_aplicado
    resumen[LLAVE_TITULO] = "IVA"

    return resumen

# Funcion para calcular IVA
#Ingresa el monto de la transacción y la condición fiscal del cliente y retorna un diccionario con el impuesto aplicado
def calcular_ganancias(monto, cf):
    
    resumen = {}
    resumen[LLAVE_TITULO] = "Ganancias"

    tasa = 0
    if (cf == condiciones_iva[1]):
        tasa = 0.5
    elif (cf == condiciones_iva[2]):
        tasa = 2.0
    resumen[LLAVE_TASA] = tasa

    impuesto_aplicado = monto * (tasa/100)
    resumen[LLAVE_IMPUESTO] = impuesto_aplicado

    return resumen

def test_calcular_iva():
    # Caso con condición 'Responsable Inscripto'
    monto = 1000
    cf = "Responsable Inscripto"
    resultado = calcular_iva(monto, cf)
    assert resultado['tasa'] == 10.5
    assert resultado['impuesto'] == 105.0

    # Caso con condición 'Consumidor Final'
    cf = "Consumidor Final"
    resultado = calcular_iva(monto, cf)
    assert resultado['tasa'] == 21.0
    assert resultado['impuesto'] == 210.0

# Test para calcular el impuesto de Ganancias
def test_calcular_ganancias():
    # Caso con condición 'Responsable Inscripto'
    monto = 1000
    cf = "Responsable Inscripto"
    resultado = calcular_ganancias(monto, cf)
    assert resultado['tasa'] == 0.5
    assert resultado['impuesto'] == 5.0

    # Caso con condición 'Consumidor Final'
    cf = "Consumidor Final"
    resultado = calcular_ganancias(monto, cf)
    assert resultado['tasa'] == 2.0
    assert resultado['impuesto'] == 20.0
    