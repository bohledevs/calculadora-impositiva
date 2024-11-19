import pytest
import os

# Funciones del código a probar (deben estar importadas si están en otro archivo)
from login import validar_nombre_usuario, validar_contrasena, inicializar_archivo, registrar, login

# Test para validar nombre de usuario
def test_validar_nombre_usuario():
    # Casos de prueba para el nombre de usuario
    assert validar_nombre_usuario("Juan") == True, "El nombre 'Juan' debería ser válido."
    assert validar_nombre_usuario("a") == False, "El nombre 'a' debería ser inválido (menos de 3 caracteres)."
    assert validar_nombre_usuario("Juan123") == False, "El nombre 'Juan123' debería ser inválido (contiene números)."
    assert validar_nombre_usuario("JuanMiguelLopez") == False, "El nombre 'JuanMiguelLopez' debería ser inválido (más de 15 caracteres)."

# Test para validar la contraseña
def test_validar_contrasena():
    # Casos de prueba para la contraseña
    assert validar_contrasena("abc123") == True, "La contraseña 'abc123' debería ser válida."
    assert validar_contrasena("abc") == False, "La contraseña 'abc' debería ser inválida (menos de 6 caracteres)."
    assert validar_contrasena("123456") == True, "La contraseña '123456' debería ser válida."
    assert validar_contrasena("abcdef") == False, "La contraseña 'abcdef' debería ser inválida (no contiene números)."

# Test para inicializar el archivo (crea un archivo vacío si no existe)
def test_inicializar_archivo():
    # Asegurarnos de que el archivo sea inicializado correctamente
    if os.path.exists("usuario.csv"):
        os.remove("usuario.csv")  # Borrar archivo previo si existe

    inicializar_archivo()  # Llamamos a la función para crear el archivo
    assert os.path.exists("usuario.csv") == True, "El archivo no fue creado correctamente."

    # Verificamos si tiene la cabecera correcta
    with open("usuario.csv", 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        assert contenido.startswith('id_usuario,nombre_de_usuario,contrasena,preg_recup,resp_recup'), \
            "El archivo no contiene los encabezados correctos."

# Test para login correcto (simple ejemplo)
def test_login_correcto():
    # Preparamos un archivo con un usuario ficticio
    if os.path.exists("usuario.csv"):
        os.remove("usuario.csv")  # Asegurarnos de que el archivo está limpio
    
    inicializar_archivo()  # Crear archivo
    # Agregamos un usuario ficticio para probar login
    with open("usuario.csv", 'a', encoding='utf-8') as archivo:
        archivo.write("1,Juan,abc123,¿Tu color favorito?,Rojo,Calle Falsa 123\n")

    # Simulamos el login
    datos_usuario = login()  # Asumimos que `login` pedirá las credenciales correctamente desde la consola
    assert datos_usuario is not None, "El login debería haber sido exitoso."
    assert datos_usuario["nombre"] == "Juan", "El nombre del usuario no coincide."

# Test para login fallido (nombre incorrecto)
def test_login_incorrecto():
    # Preparamos un archivo con un usuario ficticio
    if os.path.exists("usuario.csv"):
        os.remove("usuario.csv")  # Asegurarnos de que el archivo está limpio
    
    inicializar_archivo()  # Crear archivo
    # Agregamos un usuario ficticio para probar login
    with open("usuario.csv", 'a', encoding='utf-8') as archivo:
        archivo.write("1,Juan,abc123,¿Tu color favorito?,Rojo,Calle Falsa 123\n")

    # Intentamos hacer login con un nombre incorrecto
    datos_usuario = login()  # Asumimos que `login` pedirá las credenciales correctamente desde la consola
    assert datos_usuario is None, "El login debería haber fallado con credenciales incorrectas."

# Ejecutar los tests
if __name__ == "__main__":
    pytest.main()
