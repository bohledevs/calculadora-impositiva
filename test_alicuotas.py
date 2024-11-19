import pytest
from main import calcular_iva, calcular_ganancias, calcular_iibb, provincias_argentina, condiciones_iva, condiciones_iibb

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
    