from llaves import *
import os

def imprimir_factura(resumen_transaccion):
    try:
        nombre_factura = obtener_nombre(resumen_transaccion)
        escribir_factura(resumen_transaccion, nombre_factura)
    except IOError:
        print("Hubo problemas con el filesystem al crear la factura.")
    except KeyError as ke:
        print(f"El resumen de transacción no contiene los campos mandatorios para la facturación. {ke}")
    except Exception as e:
        print(f"Error desconocido al crear la factura: {e}")
    else:
        print(f"La factura ha sido guardada bajo el nombre: {nombre_factura}")
    finally:
        print("Facturación finalizada.")
        
    return nombre_factura

def obtener_nombre(resumen_transaccion):
    usuario = resumen_transaccion[LLAVE_USUARIO][LLAVE_NOMBRE]
    fecha = resumen_transaccion[LLAVE_FECHA]
    nombre = f"transaccion_{usuario}_{fecha}.txt"
    nombre_formateado = nombre.replace(":", "-").replace("/", "-").replace(" ", "-")
    directorio = crear_directorios(usuario, fecha)
    file_path = f"{directorio}/{nombre_formateado}"
    return file_path

def escribir_factura(resumen_transaccion, filename):

    with open(filename, "w", encoding="UTF-8") as file:
        file.write("=" * 50 + "\n")
        file.write(" " * 15 + "FACTURA B" + "\n")
        file.write("=" * 50 + "\n")
        file.write(f"Nombre: {resumen_transaccion[LLAVE_USUARIO][LLAVE_NOMBRE]}\n")
        file.write(f"Domicilio: {resumen_transaccion[LLAVE_USUARIO][LLAVE_DOMICILIO]}\n")
        file.write(f"Condición IVA: {resumen_transaccion[LLAVE_CF_IVA]}\n")
        file.write(f"Fecha: {resumen_transaccion[LLAVE_FECHA]}\n")
        file.write("-" * 50 + "\n")
        file.write(f"{'Item':<20}{'Unidad (%)':<20}{'Monto ($)':<10}\n")
        file.write("-" * 50 + "\n")

        total_neto = resumen_transaccion[LLAVE_MONTO]
        total_impuesto = 0

        file.write(f"{'Venta':<20}{100:<20}{total_neto:<10.2f}\n")

        for impuesto in resumen_transaccion[IMPUESTOS_APLICADOS]:
            nombre = impuesto[LLAVE_TITULO]
            tasa = impuesto[LLAVE_TASA]
            monto = impuesto[LLAVE_IMPUESTO]
            total_impuesto += monto

            file.write(f"{nombre:<20}{tasa:<20}{-monto:<10.2f}\n")

        file.write("-" * 50 + "\n")
        file.write(f"{'Total Neto:':<40}${total_neto:<10.2f}\n")
        file.write(f"{'Impuestos:':<40}${total_impuesto:<10.2f}\n")
        file.write(f"{'Total a Pagar:':<40}${total_neto + total_impuesto:<10.2f}\n")
        file.write("=" * 50 + "\n")

def crear_directorios(nombre_usuario, fecha):
    fecha_str = str(fecha).split('T')[0]  # '19-11-2024'
    dia, mes, year = fecha_str.split('-')

    directory = f"{nombre_usuario}/{year}/{mes}"

    if not existe_directorio(nombre_usuario):
        os.makedirs(nombre_usuario)

    if not existe_directorio(f"{nombre_usuario}/{year}"):
        os.makedirs(f"{nombre_usuario}/{year}")

    if not existe_directorio(f"{nombre_usuario}/{year}/{mes}"):
        os.makedirs(f"{nombre_usuario}/{year}/{mes}")

    return f"{nombre_usuario}/{year}/{mes}"

def existe_directorio(path):
    # Check if the given path is a directory
    return os.path.isdir(path)

def buscar_factura(root_folder, filename):

    entries = os.listdir(root_folder)  # List all entries in the folder

    for entry in entries:
        full_path = os.path.join(root_folder, entry)
        if entry == filename:  # File is found
            return full_path
        elif os.path.isdir(full_path):  # If it's a directory, recurse
            found_file = buscar_factura(full_path, filename)
            if found_file:
                return found_file

    return None