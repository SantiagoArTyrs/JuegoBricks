# tests/test_calculadora.py

import pytest
from src.calculadora import sumar

def test_sumar_enteros():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(100, 200) == 300

def test_sumar_flotantes():
    assert sumar(1.5, 2.5) == 4.0
    assert sumar(-0.5, 0.5) == 0.0
    assert round(sumar(0.1, 0.2), 2) == 0.3  # por errores de punto flotante

def test_sumar_numeros_grandes():
    assert sumar(1e10, 1e10) == 2e10

def test_sumar_con_zero():
    assert sumar(42, 0) == 42
    assert sumar(0, -42) == -42
