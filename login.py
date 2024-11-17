import csv
import re 
import os

#Nombre del archivo csv
archivo_csv = "usuario.csv"

# Función para inicializar el archivo si no existe
def inicializar_archivo():
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            if not contenido.strip():
                # Escribimos los encabezados si el archivo está vacío
                with open(archivo_csv, 'w', encoding='utf-8') as archivo_w:
                    archivo_w.write('id_usuario,nombre_de_usuario,contrasena,preg_recup,resp_recup\n')
    except FileNotFoundError:
        # Crear archivo si no existe
        with open(archivo_csv, 'w', encoding='utf-8') as archivo:
            archivo.write('id_usuario,nombre_de_usuario,contrasena,preg_recup,resp_recup\n')

# Validación básica del nombre de usuario (manual)
def validar_nombre_usuario(nombre):
    if len(nombre) < 3 or len(nombre) > 15:
        return False
    for caracter in nombre:
        if not ('a' <= caracter <= 'z' or 'A' <= caracter <= 'Z' or '0' <= caracter <= '9'):
            return False
    return True 

# Validación básica de la contraseña (manual)
def validar_contrasena(contrasena):
    if len(contrasena) < 6:
        return False
    tiene_numero = False
    for caracter in contrasena:
        if '0' <= caracter <= '9':
            tiene_numero = True
            break
    return tiene_numero

#Funcion para registrar un nuevo usuario 
def registrar():
    nombre = input("Ingrese su nombre de usuario: ")
    while not validar_nombre_usuario(nombre):
        print("Nombre inválido. Debe tener entre 3 y 15 caracteres alfanúmericos.")
        nombre = input("Ingrese su nombre de usuario:")
    
    contrasena = input("Ingrese su contraseña: ")
    while not validar_contrasena(contrasena):
        print("Contraseña inválida. Debe tener al menos 6 caracteres y contener al menos un número.")
        contrasena = input("Ingrese su contraseña: ")
    
    pregunta = input("Ingrese su pregunta de recuperación: ")
    respuesta = input("Ingrese su respuesta de recuperación: ")

    #Leer el archivo para determinar el proximo ID
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        ultimo_id = 0
        if len(lineas) > 1:
            ultimo_id = int(lineas[-1].split(',')[0])
    
    nuevo_id = ultimo_id + 1

    #Escribir los datos del nuevo usuario en el archivo
    with open(archivo_csv, 'a', encoding='utf-8') as archivo:
         archivo.write(f'{nuevo_id},{nombre},{contrasena},{pregunta},{respuesta}\n')

    print("Usuario registrado exitosamente.")

#Funcion para iniciar sesión
def login():
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    #Leer el archivo y buscar las credenciales 
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]: #Omitimos los encabezado
            datos = linea.strip().split(',')
            if datos[1] == nombre and datos[2] == contrasena:
                print(f"Bienvenido, {nombre}!")
                return
    print("Nombre de usuario o contraseña incorrectos.")

#Funcion para recuperar contraseña
def recuperar_contrasena():
    nombre = input("Ingrese su nombre de usuario: ")

    #Leer el archivo y buscar el usuario
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]: #Omitimos los encabezados
            datos = linea.strip().split(',')
            if datos[1] == nombre:
                print(f"Pregunta de recuperación: {datos[3]}")
                respuestas = input("Respuestas: ")
                if respuestas.lower() == datos[4].lower():
                    print(f"Su contraseña es: {datos[2]}")
                    return
                else:
                    print("Respuesta Incorrecta")
                    return
    print("Usuario no encontrado.")

#Menu principal.
def menu():
    inicializar_archivo()
    while True:
        print("\n--- Menú ---")
        print("1. Registrarse ")
        print("2. Login")
        print("3. Olvidé mi contraseña.")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar()
        elif opcion == '2':
            login()
        elif opcion == '3':
            recuperar_contrasena()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

#Ejecutar el programa
menu()




# usuarios = {
#     "usuario1": "contraseña1",
#     "usuario2": "contraseña2"
# }

# def iniciar_sesion():
#     print("\n\t╔═════════════════════════════╗")
#     print("\t║       Iniciar Sesión        ║")
#     print("\t╚═════════════════════════════╝\n")

#     usuarioLogeado = False

#     while usuarioLogeado == False:

#         usuario = input("Ingrese su nombre de usuario: ")
#         contrasena = input("Ingrese su contraseña: ")

#         if usuario in usuarios:
#             if usuarios[usuario] == contrasena:
#                 print("\n\t╔═════════════════════════════╗")
#                 print("\t║  Inicio de sesión exitoso!  ║")
#                 print("\t╚═════════════════════════════╝\n")
#                 usuarioLogeado = True
#             else:
#                 print("\n\t╔═════════════════════════════╗")
#                 print("\t║   Contraseña incorrecta.    ║")
#                 print("\t╚═════════════════════════════╝\n")
#         else:
#             print("\n\t╔═════════════════════════════╗")
#             print("\t║  Usuario no encontrado.     ║")
#             print("\t╚═════════════════════════════╝\n")

