# tests/test_sonido.py
import pytest
from src.sonido import cargar_sonido

def test_cargar_sonido_valido():
    assert cargar_sonido("golpe.wav") == "Reproduciendo golpe.wav"

def test_cargar_sonido_invalido_extension():
    with pytest.raises(ValueError):
        cargar_sonido("error.mp3")
