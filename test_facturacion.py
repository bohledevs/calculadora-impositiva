from facturacion import imprimir_factura
from facturacion import obtener_nombre
import os

def test_imprimir_factura():
    
    resumen_transaccion = {
        "usuario": {"nombre": "Juan Perez"},
        "fecha": "19-11-2024T15-30-00",
        "condicion_fiscal_iva": "Responsable Inscripto",
        "monto": 3150,
        "impuestos_aplicados": [
              {
                "titulo": "IVA",
                "tasa": 10.5,
                "impuesto": 300.0
              },
              {
                "titulo": "IIBB",
                "tasa": 0.7,
                "impuesto": 32.0
              }
        ]
    }
    
    nombre_factura = imprimir_factura(resumen_transaccion)

    try:
            file = open(nombre_factura, "r", encoding="UTF-8")
            content = file.readlines()
            num_lineas = len(content)
            assert num_lineas == 18
            file.close()
            os.remove(nombre_factura)
    except FileNotFoundError:
            assert False, "No se creo el archivo de la factura."
    
    print("test_facturacion ejecutado con exito.")
    
def test_obtener_nombre():
    resumen_transaccion = {
        "usuario": {"nombre": "Juan Perez"},
        "fecha": "19-11-2024"
    }
    resultado = obtener_nombre(resumen_transaccion)
    assert resultado == "transaccion_Juan-Perez_19-11-2024.txt"
