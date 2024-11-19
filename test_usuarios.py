import os
import pytest
import csv
from login import (
    inicializar_archivo,
    validar_nombre_usuario,
    validar_contrasena,
    registrar,
    login,
    recuperar_contrasena,
    archivo_csv
)
def test_inicializar_archivo():
    # Verificar que el archivo existe después de inicializarlo
    assert os.path.exists(archivo_csv)
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        encabezados = archivo.readline().strip()
        assert encabezados == "id_usuario,nombre_de_usuario,contrasena,preg_recup,resp_recup"
def test_validar_nombre_usuario():
    assert validar_nombre_usuario("Juan") is True
    assert validar_nombre_usuario("J") is False
    assert validar_nombre_usuario("Juan123") is False
    assert validar_nombre_usuario("JuanPedroSantos") is True
    assert validar_nombre_usuario("12345") is False
def test_validar_contrasena():
    assert validar_contrasena("abc123") is True
    assert validar_contrasena("abcdef") is False
    assert validar_contrasena("123") is False
    assert validar_contrasena("password123") is True