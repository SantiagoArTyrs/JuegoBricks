# src/powerups.py
def aplicar_powerup(jugador, tipo):
    if tipo == "velocidad":
        jugador["velocidad"] += 2
    elif tipo == "escudo":
        jugador["escudo"] = True
    elif tipo == "vida":
        jugador["vidas"] += 1
    else:
        raise ValueError("Power-up no reconocido")
    return jugador
