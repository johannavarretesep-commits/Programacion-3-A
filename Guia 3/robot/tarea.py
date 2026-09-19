import math


class Tarea:
    

    def __init__(self, nombre, tipo, tiempo_ejecucion):
        # Convertimos a string y eliminamos espacios laterales
        nombre = str(nombre).strip()
        if not nombre:
            raise ValueError("Escribe un nombre para la tarea.")
        if tipo not in ("Sensores", "Movimiento"):
            raise ValueError("El tipo debe ser Sensores o Movimiento.")
        if isinstance(tiempo_ejecucion, bool) or not isinstance(
            tiempo_ejecucion, (int, float)
        ):
            raise TypeError("El tiempo debe ser un número.")
        if not math.isfinite(tiempo_ejecucion) or tiempo_ejecucion <= 0:
            raise ValueError("El tiempo debe ser finito y mayor que cero.")

        self.nombre = nombre
        self.tipo = tipo
        self.tiempo_ejecucion = float(tiempo_ejecucion)

    def __str__(self):
        return f"{self.nombre} | {self.tipo} | {self.tiempo_ejecucion:g} s"
