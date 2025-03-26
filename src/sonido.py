# src/sonido.py
def cargar_sonido(nombre_archivo):
    if not nombre_archivo.endswith(".wav"):
        raise ValueError("Solo se permiten archivos .wav")
    return f"Reproduciendo {nombre_archivo}"
