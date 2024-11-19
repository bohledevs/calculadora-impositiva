#FUNCION MONTO AGREGADO
from functools import reduce

# Lista de entrada
datos = [
    {
        "titulo": "IVA",
        "impuesto": 2010.5,
        "tasa": 21
    },
    {
        "titulo": "Ganancias",
        "impuesto": 200.5,
        "tasa": 0.2
    },
    {
        "titulo": "Sin Impuesto",
        "impuesto": 0,
        "tasa": 10
    }
]

#Se filtran elementos donde "impuesto" sea igual a 0
resultados_filtrados = list(filter(lambda x: x["impuesto"] == 0, datos))

#Usamos map para extraer solo el valor de "impuesto" de los resultados filtrados
impuestos_filtrados = list(map(lambda x: x["impuesto"], resultados_filtrados))

#Usamos reduce para sumar todos los valores del campo "impuesto" en la lista original
total_impuestos = reduce(lambda acc, x: acc + x["impuesto"], datos, 0)

# Imprimir resultados
print("Impuestos filtrados (impuesto == 0):", impuestos_filtrados)
print("Suma total de impuestos:", total_impuestos)