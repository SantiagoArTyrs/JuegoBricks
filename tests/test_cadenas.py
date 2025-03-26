# tests/test_cadenas.py

import pytest
from src.cadenas import convertir_mayusculas

def test_convertir_mayusculas_basico():
    assert convertir_mayusculas("python") == "PYTHON"
    assert convertir_mayusculas("Prueba") == "PRUEBA"

def test_convertir_mayusculas_numeros_y_simbolos():
    assert convertir_mayusculas("123") == "123"
    assert convertir_mayusculas("hello123!") == "HELLO123!"

def test_convertir_mayusculas_vacio():
    assert convertir_mayusculas("") == ""

def test_convertir_mayusculas_minusculas_exclusivas():
    entrada = "solo minusculas"
    esperado = "SOLO MINUSCULAS"
    assert convertir_mayusculas(entrada) == esperado

def test_convertir_mayusculas_mixto_con_espacios():
    entrada = "eSto Es Un tEsTo"
    esperado = "ESTO ES UN TESTO"
    assert convertir_mayusculas(entrada) == esperado
