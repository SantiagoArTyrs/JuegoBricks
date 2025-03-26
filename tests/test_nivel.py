# tests/test_nivel.py
import pytest
from src.nivel import cargar_nivel

def test_cargar_nivel_completo():
    config = {"ladrillos": 20, "velocidad_bola": 5, "fondo": "nivel1.png"}
    nivel = cargar_nivel(config)
    assert nivel["ladrillos"] == 20
    assert nivel["velocidad_bola"] == 5
    assert nivel["fondo"] == "nivel1.png"

def test_cargar_nivel_sin_fondo():
    config = {"ladrillos": 10, "velocidad_bola": 3}
    nivel = cargar_nivel(config)
    assert nivel["fondo"] == "default.png"

def test_falta_dato_esencial():
    config = {"ladrillos": 10}
    with pytest.raises(ValueError):
        cargar_nivel(config)
