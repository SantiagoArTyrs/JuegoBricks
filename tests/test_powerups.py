# tests/test_powerups.py
import pytest
from src.powerups import aplicar_powerup

def test_aplicar_velocidad():
    j = {"velocidad": 3, "escudo": False, "vidas": 2}
    r = aplicar_powerup(j, "velocidad")
    assert r["velocidad"] == 5

def test_aplicar_vida():
    j = {"velocidad": 3, "escudo": False, "vidas": 2}
    r = aplicar_powerup(j, "vida")
    assert r["vidas"] == 3

def test_powerup_invalido():
    j = {"velocidad": 3, "escudo": False, "vidas": 2}
    with pytest.raises(ValueError):
        aplicar_powerup(j, "invisibilidad")
