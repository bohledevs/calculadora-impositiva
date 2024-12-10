from llaves import *  # Importa constantes o llaves desde un módulo externo llamado "llaves".
import os  # Importa el módulo para trabajar con el sistema de archivos.

# Esta función genera y guarda una factura a partir de un resumen de transacción.
def imprimir_factura(resumen_transaccion):
    try:
        # Obtiene el nombre y la ubicación del archivo de factura.
        nombre_factura = obtener_nombre(resumen_transaccion)
        # Escribe la factura en el archivo.
        escribir_factura(resumen_transaccion, nombre_factura)
    except IOError:
        # Maneja errores relacionados con el sistema de archivos.
        print("Hubo problemas con el filesystem al crear la factura.")
    except KeyError as ke:
        # Maneja casos donde faltan datos obligatorios en el resumen.
        print(f"El resumen de transacción no contiene los campos mandatorios para la facturación. {ke}")
    except Exception as e:
        # Captura cualquier otro tipo de error.
        print(f"Error desconocido al crear la factura: {e}")
    else:
        # Mensaje exitoso si no hubo errores.
        print(f"La factura ha sido guardada bajo el nombre: {nombre_factura}")
    finally:
        # Siempre imprime que el proceso ha finalizado.
        print("Facturación finalizada.")
        
    return nombre_factura  # Devuelve el nombre del archivo de factura.

# Crea un nombre de archivo único para la factura y su ruta.
def obtener_nombre(resumen_transaccion):
    # Extrae el usuario y la fecha del resumen de transacción.
    usuario = resumen_transaccion[LLAVE_USUARIO][LLAVE_NOMBRE]
    fecha = resumen_transaccion[LLAVE_FECHA]
    # Construye el nombre del archivo usando usuario y fecha.
    nombre = f"transaccion_{usuario}_{fecha}.txt"
    # Formatea el nombre para evitar caracteres no válidos.
    nombre_formateado = nombre.replace(":", "-").replace("/", "-").replace(" ", "-")
    # Crea los directorios necesarios.
    directorio = crear_directorios(usuario, fecha)
    # Combina el directorio con el nombre del archivo.
    file_path = f"{directorio}/{nombre_formateado}"
    return file_path

# Escribe los detalles de la factura en un archivo de texto.
def escribir_factura(resumen_transaccion, filename):
    with open(filename, "w", encoding="UTF-8") as file:
        # Encabezado de la factura.
        file.write("=" * 50 + "\n")
        file.write(" " * 15 + "FACTURA B" + "\n")
        file.write("=" * 50 + "\n")
        # Datos del usuario y transacción.
        file.write(f"Nombre: {resumen_transaccion[LLAVE_USUARIO][LLAVE_NOMBRE]}\n")
        file.write(f"Domicilio: {resumen_transaccion[LLAVE_USUARIO][LLAVE_DOMICILIO]}\n")
        file.write(f"Condición IVA: {resumen_transaccion[LLAVE_CF_IVA]}\n")
        file.write(f"Fecha: {resumen_transaccion[LLAVE_FECHA]}\n")
        file.write("-" * 50 + "\n")
        # Tabla de items e impuestos.
        file.write(f"{'Item':<20}{'Unidad (%)':<20}{'Monto ($)':<10}\n")
        file.write("-" * 50 + "\n")

        total_neto = resumen_transaccion[LLAVE_MONTO]
        total_impuesto = 0

        # Detalle del total neto.
        file.write(f"{'Venta':<20}{100:<20}{total_neto:<10.2f}\n")

        # Detalle de cada impuesto aplicado.
        for impuesto in resumen_transaccion[IMPUESTOS_APLICADOS]:
            nombre = impuesto[LLAVE_TITULO]
            tasa = impuesto[LLAVE_TASA]
            monto = impuesto[LLAVE_IMPUESTO]
            total_impuesto += monto

            file.write(f"{nombre:<20}{tasa:<20}{-monto:<10.2f}\n")

        # Totales finales.
        file.write("-" * 50 + "\n")
        file.write(f"{'Total Neto:':<40}${total_neto:<10.2f}\n")
        file.write(f"{'Impuestos:':<40}${total_impuesto:<10.2f}\n")
        file.write(f"{'Total a Pagar:':<40}${total_neto + total_impuesto:<10.2f}\n")
        file.write("=" * 50 + "\n")

# Crea los directorios necesarios para guardar la factura.
def crear_directorios(nombre_usuario, fecha):
    # Extrae la fecha en formato "día-mes-año".
    fecha_str = str(fecha).split('T')[0]
    dia, mes, year = fecha_str.split('-')

    # Define la estructura del directorio.
    directory = f"{nombre_usuario}/{year}/{mes}"

    # Crea los directorios si no existen.
    if not existe_directorio(nombre_usuario):
        os.makedirs(nombre_usuario)
    if not existe_directorio(f"{nombre_usuario}/{year}"):
        os.makedirs(f"{nombre_usuario}/{year}")
    if not existe_directorio(f"{nombre_usuario}/{year}/{mes}"):
        os.makedirs(f"{nombre_usuario}/{year}/{mes}")

    return f"{nombre_usuario}/{year}/{mes}"

# Verifica si un directorio existe.
def existe_directorio(path):
    return os.path.isdir(path)

# Muestra un banner decorativo con un título.
def mostrar_banner(titulo):
    print("=" * 50)
    print(" " * 10 + titulo)
    print("=" * 50)

# Convierte una tupla en una lista enumerada para mostrar opciones.
def imprimir_tupla(tupla):
    resultado = ""
    for indice, elemento in enumerate(tupla):
        resultado += f"{indice + 1}. {elemento}\n"
    return resultado

# Muestra un menú relacionado con las facturas.
def mostrar_menu_facturas():
    opciones = (
        "Ver mis facturas",
        "Buscar una factura",
        "Salir"
    )

    mostrar_banner("Menú de Facturas")
    print(imprimir_tupla(opciones))
    print("=" * 50)
    op = int(input("Ingrese su opción: "))

    # Procesa la opción seleccionada.
    if op == 1:
        print("WIP")  # Work in Progress.
    elif op == 2:
        buscar_ruta()
    elif op == 3:
        print("Finalizando Búsqueda")
    else:
        raise IndexError(f"Opción ingresada inválida: {op}")

# Solicita un archivo de factura al usuario y busca su ruta.
def buscar_ruta():
    filename = input("Ingrese el nombre del archivo:")
    ruta = buscar_factura(".", filename)
    if ruta != None:
        print(f"Su factura se encuentra en: {ruta}")

        with open(ruta, "r", encoding="UTF-8") as file:
            contenido = file.read()

            lineas = contenido.split("\n")
            for linea in lineas:
                print(linea)
    else:
        print("No se encontró su factura.")

# Busca una factura en un directorio y sus subdirectorios.
def buscar_factura(root_folder, filename):
    entries = os.listdir(root_folder)  # Lista todas las entradas en el directorio.

    for entry in entries:
        full_path = os.path.join(root_folder, entry)
        if entry == filename:  # Si encuentra el archivo, devuelve la ruta.
            return full_path
        elif os.path.isdir(full_path):  # Si es un directorio, busca recursivamente.
            found_file = buscar_factura(full_path, filename)
            if found_file:
                return found_file

    return None  # Si no encuentra nada, devuelve None.
