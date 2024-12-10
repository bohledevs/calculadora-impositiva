from llaves import *
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import chardet
from PyPDF2 import PdfReader

def detectar_codificacion(ruta_archivo):
    with open(ruta_archivo, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def imprimir_factura(resumen_transaccion):
    try:
        nombre_factura = obtener_nombre(resumen_transaccion)
        crear_pdf_facturas(resumen_transaccion)
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
    nombre = f"transaccion_{usuario}.txt"
    nombre_formateado = nombre.replace(":", "-").replace("/", "-").replace(" ", "-")
    directorio = crear_directorios(usuario, fecha)
    file_path = f"{directorio}/{nombre_formateado}"
    return file_path

def crear_carpeta_facturas(carpeta_usuario):
    if not os.path.exists(carpeta_usuario):
        os.makedirs(carpeta_usuario)


def buscar_ruta():
    filename = input("Ingrese el nombre del archivo:")
    ruta = buscar_factura(".", filename)
    if ruta:
        print(f"Su factura se encuentra en: {ruta}")
        try:
            # Leer contenido del PDF
            reader = PdfReader(ruta)
            for i, page in enumerate(reader.pages):
                print(f"--- Página {i + 1} ---")
                print(page.extract_text())
        except Exception as e:
            print(f"Error al leer el PDF: {e}")
    else:
        print("No se encontró su factura.")

def buscar_factura(root_folder, filename):
    entries = os.listdir(root_folder)
    for entry in entries:
        full_path = os.path.join(root_folder, entry)
        if entry == filename:
            return full_path
        elif os.path.isdir(full_path):
            found_file = buscar_factura(full_path, filename)
            if found_file:
                return found_file
    return None


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

    fecha_str = str(fecha).split('_')[0]  # '19-11-2024'
    dia, mes, year = fecha_str.split('-')

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

def mostrar_banner(titulo):
    print("=" * 50)
    print(" " * 10 + titulo)
    print("=" * 50)

def imprimir_tupla(tupla):
    resultado = ""
    for indice, elemento in enumerate(tupla):
        resultado += f"{indice + 1}. {elemento}\n"
    return resultado

def mostrar_menu_facturas():

    opciones = (
    "Buscar una factura",
    "Salir"
    )

    mostrar_banner("FACTURACIÓN")
    print(imprimir_tupla(opciones))
    print("=" * 50)
    op = int(input("Ingrese su opción: "))

    if (op == 1):
        buscar_ruta()
    elif (op == 2):
        print("Finalizando Búsqueda")
    else:
        raise IndexError(f"Opción ingresada inválida: {op}")

def crear_pdf_facturas(resumen_transaccion):
    nombre_carpeta = "facturas"
    contador = 1
    nombre_usuario = resumen_transaccion[LLAVE_USUARIO][LLAVE_NOMBRE]
    carpeta_usuario = os.path.join(nombre_carpeta, nombre_usuario)

    crear_carpeta_facturas(carpeta_usuario)
    

    # Buscar un nombre de archivo único
    while True:
        nombre_pdf = f"factura_{contador:02d}.pdf"
        ruta_archivo = os.path.join(carpeta_usuario, nombre_pdf)
        
        if not os.path.exists(ruta_archivo):
            break  # Si el archivo no existe, usamos este nombre
        contador += 1
    
    try:
        c = canvas.Canvas(ruta_archivo)
        ancho, alto = 595, 842  # Tamaño A4 en puntos (ancho x alto)

        # Coordenadas iniciales
        x = 72  # Margen izquierdo
        y = alto - 72  # Margen superior

        # Configurar título
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x, y, "=" * 50)
        y -= 20  # Ajustar línea
        c.drawString(x, y, " " * 15 + "FACTURA B")
        y -= 20
        c.drawString(x, y, "=" * 50)
        y -= 30

        # Información general
        c.setFont("Helvetica", 12)
        c.drawString(x, y, f"Nombre: {resumen_transaccion[LLAVE_USUARIO][LLAVE_NOMBRE]}")
        y -= 20
        c.drawString(x, y, f"Domicilio: {resumen_transaccion[LLAVE_USUARIO][LLAVE_DOMICILIO]}")
        y -= 20
        c.drawString(x, y, f"Condición IVA: {resumen_transaccion[LLAVE_CF_IVA]}")
        y -= 20
        c.drawString(x, y, f"Fecha: {resumen_transaccion[LLAVE_FECHA]}")
        y -= 30

        # Tabla de items
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, f"{'Item':<20}{'Unidad (%)':<20}{'Monto ($)':<10}")
        y -= 20
        c.drawString(x, y, "-" * 50)
        y -= 20

        total_neto = resumen_transaccion[LLAVE_MONTO]
        total_impuesto = 0

        c.setFont("Helvetica", 12)
        c.drawString(x, y, f"{'Venta':<20}{100:<20}{total_neto:<10.2f}")
        y -= 20

        for impuesto in resumen_transaccion[IMPUESTOS_APLICADOS]:
            nombre = impuesto[LLAVE_TITULO]
            tasa = impuesto[LLAVE_TASA]
            monto = impuesto[LLAVE_IMPUESTO]
            total_impuesto += monto
            c.drawString(x, y, f"{nombre:<20}{tasa:<20}{monto:<10.2f}")
            y -= 20

        # Totales
        y -= 20
        c.drawString(x, y, "-" * 50)
        y -= 20
        c.drawString(x, y, f"{'Total Neto:':<40}${total_neto:<10.2f}")
        y -= 20
        c.drawString(x, y, f"{'Impuestos:':<40}${total_impuesto:<10.2f}")
        y -= 20
        c.drawString(x, y, f"{'Total a Pagar:':<40}${total_neto + total_impuesto:<10.2f}")
        y -= 30
        c.drawString(x, y, "=" * 50)

        c.save()
        print(f"PDF guardado en {ruta_archivo}")
    except IOError as e:
        print(f"Error al escribir el archivo PDF: {e}")
    except Exception as e:
        print(f"Error inesperado al crear el PDF: {e}")

def buscar_ruta():
    filename = input("Ingrese el nombre del archivo:")
    ruta = buscar_factura(".", filename)
    if ruta:
        print(f"Su factura se encuentra en: {ruta}")
        try:
            # Leer contenido del PDF
            reader = PdfReader(ruta)
            for i, page in enumerate(reader.pages):
                print(f"--- Página {i + 1} ---")
                print(page.extract_text())
        except Exception as e:
            print(f"Error al leer el PDF: {e}")
    else:
        print("No se encontró su factura.")

def buscar_factura(root_folder, filename):
    entries = os.listdir(root_folder)
    for entry in entries:
        full_path = os.path.join(root_folder, entry)
        if entry == filename:
            return full_path
        elif os.path.isdir(full_path):
            found_file = buscar_factura(full_path, filename)
            if found_file:
                return found_file
    return None