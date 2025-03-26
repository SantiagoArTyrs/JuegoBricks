# src/nivel.py
def cargar_nivel(config):
    if "ladrillos" not in config or "velocidad_bola" not in config:
        raise ValueError("Faltan datos esenciales del nivel")
    return {
        "ladrillos": config["ladrillos"],
        "velocidad_bola": config["velocidad_bola"],
        "fondo": config.get("fondo", "default.png")
    }
