import os
import csv
import pytest
from login import inicializar_archivo, validar_nombre_usuario, validar_contrasena, registrar, login, recuperar_contrasena

# Ruta temporal para pruebas
archivo_csv_prueba = "usuario_prueba.csv"

@pytest.fixture(autouse=True)
def setup_teardown():
    """
    Fixture para inicializar y limpiar el entorno de pruebas.
    Crea un archivo CSV temporal antes de cada prueba y lo elimina después.
    """
    global archivo_csv
    archivo_csv = archivo_csv_prueba  # Reemplazamos la ruta original con la de prueba
    inicializar_archivo()  # Inicializamos el archivo CSV
    yield  # Ejecutamos las pruebas
    if os.path.exists(archivo_csv_prueba):
        os.remove(archivo_csv_prueba)

def test_inicializar_archivo():
    """
    Verifica que el archivo CSV se cree correctamente con los encabezados iniciales.
    """
    assert os.path.exists(archivo_csv_prueba)
    with open(archivo_csv_prueba, 'r', encoding='utf-8') as archivo:
        encabezados = archivo.readline().strip()
        assert encabezados == "id_usuario,nombre_de_usuario,contrasena,preg_recup,resp_recup"

def test_validar_nombre_usuario():
    """
    Pruebas para la función validar_nombre_usuario.
    """
    assert validar_nombre_usuario("Juan") == True  # Nombre válido
    assert validar_nombre_usuario("J") == False  # Nombre demasiado corto
    assert validar_nombre_usuario("JuanPerezMartinez") == False  # Nombre demasiado largo
    assert validar_nombre_usuario("Juan123") == False  # Nombre con números
    assert validar_nombre_usuario("Juan_Perez") == False  # Nombre con caracteres especiales

def test_validar_contrasena():
    """
    Pruebas para la función validar_contrasena.
    """
    assert validar_contrasena("abc123") == True  # Contraseña válida
    assert validar_contrasena("abcdef") == False  # Contraseña sin números
    assert validar_contrasena("12345") == False  # Contraseña demasiado corta
    assert validar_contrasena("a1") == False  # Contraseña corta y con números

def test_registrar(monkeypatch):
    """
    Prueba para la función registrar.
    Simula la entrada del usuario y verifica que los datos se registren correctamente.
    """
    inputs = iter(["TestUser", "Test123", "Pregunta", "Respuesta", "Domicilio Prueba"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    registrar()

    with open(archivo_csv_prueba, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        assert len(lineas) == 2  # Encabezado + 1 usuario registrado
        datos = lineas[1].strip().split(',')
        assert datos[1] == "TestUser"
        assert datos[2] == "Test123"
        assert datos[5] == "Domicilio Prueba"

def test_login(monkeypatch):
    """
    Prueba para la función login.
    Simula un inicio de sesión exitoso.
    """
    # Agregamos un usuario de prueba al archivo
    with open(archivo_csv_prueba, 'a', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([1, "testuser", "test123", "Pregunta", "Respuesta", "Domicilio Test"])

    # Simulamos entradas de usuario
    inputs = iter(["testuser", "test123"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    resultado = login()
    assert resultado == {"nombre": "testuser", "id": 1, "domicilio": "Domicilio Test"}

def test_recuperar_contrasena(monkeypatch, capsys):
    """
    Prueba para la función recuperar_contrasena.
    Simula la recuperación de contraseña con una respuesta correcta.
    """
    # Agregamos un usuario de prueba al archivo
    with open(archivo_csv_prueba, 'a', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([1, "testuser", "test123", "Pregunta", "Respuesta", "Domicilio Test"])

    # Simulamos entradas de usuario
    inputs = iter(["testuser", "Respuesta"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    recuperar_contrasena()
    captured = capsys.readouterr()
    assert "Su contraseña es: test123" in captured.out
