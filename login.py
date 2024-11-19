import csv
import re

#Ruta del archivo CSV donde se guardaran los datos de los usuarios.
archivo_csv = "usuario.csv"

# Esta funcion verifica si el archivo CSV existe y, si no, lo crea.
def inicializar_archivo():
    try:
        #Intentamos abrir el archivo en modo lectura
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

# Esta funcion valida el nombre de usuario para que tenga entre 3 y 15 caracteres alfanuméricos.
def validar_nombre_usuario(nombre):
    # La expresión regular valida que el nombre tenga entre 3 y 15 caracteres
    # y que solo contenga letras (mayúsculas o minúsculas), sin números
    patron = r'^[a-zA-Z]{3,15}$'
    
    if re.match(patron, nombre):
        return True
    else:
        return False

# Esta funcion valida la contraseña para que cumpla con los requisitos de tener al menos 6 caracteres y contener al menos un número.
def validar_contrasena(contrasena):
    # La expresión regular valida que la contraseña tenga al menos 6 caracteres y contenga al menos un número
    patron = r'^(?=.*\d).{6,}$'
    
    if re.match(patron, contrasena):
        return True
    else:
        return False

#Funcion para registrar un nuevo usuario. Permite registrar un nombre de usuario, contraseña, pregunta de recuperación, respuesta de recuperación y domicilio.
def registrar():
    #Pedimos al usuario que ingrese su nombre y lo validamos
    nombre = input("Ingrese su nombre de usuario: ")
    while not validar_nombre_usuario(nombre):
        print("Nombre inválido. Debe tener entre 3 y 15 caracteres alfanúmericos.")
        nombre = input("Ingrese su nombre de usuario:")

    #Pedimos al usuario que ingrese su contraseña y la validamos
    contrasena = input("Ingrese su contraseña: ")
    while not validar_contrasena(contrasena):
        print("Contraseña inválida. Debe tener al menos 6 caracteres y contener al menos un número.")
        contrasena = input("Ingrese su contraseña: ")
    
    #Pedimos otros datos necesarios
    pregunta = input("Ingrese su pregunta de recuperación: ")
    respuesta = input("Ingrese su respuesta de recuperación: ")
    domicilio = input("Ingrese su domicilio: ")

    #Leer el archivo para determinar el proximo ID
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        ultimo_id = 0
        if len(lineas) > 1: #Si hay usuarios registrados
            ultimo_id = int(lineas[-1].split(',')[0]) #Obtenemos el ID del último usuario
    
    nuevo_id = ultimo_id + 1 #Asignamos el nuevo ID

    #Escribir los datos del nuevo usuario en el archivo
    with open(archivo_csv, 'a', encoding='utf-8') as archivo:
         archivo.write(f'{nuevo_id},{nombre},{contrasena},{pregunta},{respuesta},{domicilio}\n')

    print("Usuario registrado exitosamente.")

#Funcion para iniciar sesión. Permite a un usuario iniciar sesion en sistema.
def login():
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    usuario = None

    # Leer el archivo CSV y buscar las credenciales
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:  # Omitimos los encabezados
            datos = linea.strip().split(',')
            if datos[1] == nombre and datos[2] == contrasena:
                usuario = {
                    "nombre": datos[1],
                    "id": int(datos[0]),
                    "domicilio": datos[5]
                }
                print(f"Bienvenido, {usuario['nombre']}! ID: {usuario['id']}, Domicilio: {usuario['domicilio']}")
                return usuario
    print("Nombre de usuario o contraseña incorrectos.")
    return usuario


#Funcion para recuperar contraseña. Permite a un usuario recuperar su contraseña si responde correctamente a la pregunta de recuperación.
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
    usuario_autenticado = None
    
    while usuario_autenticado == None:
        print("\n--- Menú ---")
        print("1. Registrarse ")
        print("2. Login")
        print("3. Olvidé mi contraseña.")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar()
        elif opcion == '2':
            usuario = login() 
            return usuario
        elif opcion == '3':
            recuperar_contrasena()
        elif opcion == '4':
            print("Saliendo del programa...")
            return None
        else:
            print("Opción inválida.")
