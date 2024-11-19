
from functools import reduce
 
def agregar_monto(datos):
 
	#Se filtran elementos donde "impuesto" sea igual a 0
	resultados_filtrados = list(filter(lambda x: x["impuesto"] == 0, datos))
 
	#Usamos map para extraer solo el valor de "impuesto" de los resultados filtrados
	impuestos_filtrados = list(map(lambda x: x["impuesto"], resultados_filtrados))
 
	#Usamos reduce para sumar todos los valores del campo "impuesto" en la lista original
	total_impuestos = reduce(lambda acc, x: acc + x["impuesto"], datos, 0)
 
	return total_impuestos
