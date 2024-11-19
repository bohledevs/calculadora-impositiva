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
    return nombre_formateado

def escribir_factura(resumen_transaccion, filename):
    nombre_usuario = resumen_transaccion["usuario"]["nombre"]
    fecha = resumen_transaccion["fecha"]
    directorio = crear_directorios(nombre_usuario, fecha)

    file_path = f"{directorio}/{filename}"

    with open(file_path, "w", encoding="UTF-8") as file:
        file.write("=" * 50 + "\n")
        file.write(" " * 15 + "FACTURA B" + "\n")
        file.write("=" * 50 + "\n")
        file.write(f"Nombre: {resumen_transaccion['usuario']['nombre']}\n")
        file.write(f"Domicilio: {resumen_transaccion['usuario']['domicilio']}\n")
        file.write(f"Condición IVA: {resumen_transaccion['condicion_fiscal_iva']}\n")
        file.write(f"Fecha: {resumen_transaccion['fecha']}\n")
        file.write("-" * 50 + "\n")
        file.write(f"{'Item':<20}{'Unidad (%)':<20}{'Monto ($)':<10}\n")
        file.write("-" * 50 + "\n")

        total_neto = resumen_transaccion["monto"]
        total_impuesto = 0

        file.write(f"{'Venta':<20}{100:<20}{total_neto:<10.2f}\n")

        for impuesto in resumen_transaccion["impuestos_aplicados"]:
            nombre = impuesto["titulo"]
            tasa = impuesto["tasa"]
            monto = impuesto["impuesto"]
            total_impuesto += monto

            file.write(f"{nombre:<20}{tasa:<20}{-monto:<10.2f}\n")

        file.write("-" * 50 + "\n")
        file.write(f"{'Total Neto:':<40}${total_neto:<10.2f}\n")
        file.write(f"{'Impuestos:':<40}${total_impuesto:<10.2f}\n")
        file.write(f"{'Total a Pagar:':<40}${total_neto + total_impuesto:<10.2f}\n")
        file.write("=" * 50 + "\n")

    return file_path

def crear_directorios(nombre_usuario, fecha):
    fecha_str = str(fecha).split('T')[0]  # '19-11-2024'
    day, month, year = fecha_str.split('-')

    # Create the directory structure as a string: usuario/year/month/
    directory = f"{nombre_usuario}/{year}/{month}"

    # Create directories if they don't exist
    if not is_directory_exists(nombre_usuario):
        os.makedirs(nombre_usuario)

    if not is_directory_exists(f"{nombre_usuario}/{year}"):
        os.makedirs(f"{nombre_usuario}/{year}")

    if not is_directory_exists(f"{nombre_usuario}/{year}/{month}"):
        os.makedirs(f"{nombre_usuario}/{year}/{month}")

    return f"{nombre_usuario}/{year}/{month}"

def is_directory_exists(path):
    # Check if the given path is a directory
    return os.path.isdir(path)
