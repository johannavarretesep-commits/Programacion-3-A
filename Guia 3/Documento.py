# Primero importamos las librerias
import math

# Creamos la clase Documento para poder crear los objetos
class Documento:
    # Cada documento tiene nombre, número de paginas y tiempo de impresión por pagina
    def __init__(self, nombre, numero_paginas, tiempo_por_pagina):
        # Convertimos la variable a texto y le quitamos espacios del inicio y final si es que hay
        # (No quita los que estan entre las palabras si algo)
        nombre = str(nombre).strip()

        # Esta linea nos permite saber si esta vacio y se le coloca not para que lance true y ejecute
        if not nombre:
            # raise sirve para lanzar un cartel de error en el programa
            # ValueError() es para mostrar que queremos que aparezca en el mensaje de error
            raise ValueError("El nombre del documento no puede estar vacío.")
        # Comprobamos que el número de paginas sea entero y no sea un true o false
        if isinstance(numero_paginas, bool) or not isinstance(numero_paginas, int):
            raise TypeError("El número de páginas debe ser un entero.")
        # Comprobamos que el número de paginas no sea cero
        if numero_paginas <= 0:
            raise ValueError("El número de páginas debe ser mayor que cero.")
        # Comprobar que el tiempo sea un float (o un int tmb)
        if isinstance(tiempo_por_pagina, bool) or not isinstance(tiempo_por_pagina, (int, float)):
            raise TypeError("El tiempo por página debe ser un número.")
        # Comprobar que el número es finito y positivo (para el tiempo de impresión)
        if not math.isfinite(tiempo_por_pagina) or tiempo_por_pagina <= 0:
            raise ValueError("El tiempo por página debe ser mayor que cero.")
        # Creación de atributos
        self.nombre = nombre
        self.numero_paginas = numero_paginas
        self.tiempo_por_pagina = float(tiempo_por_pagina)

    # Creamos una funcion que nos permita mostrar el nombre, número de paginas y tiempo en la pantalla
    def __str__(self):
        return (
            f"{self.nombre} - {self.numero_paginas} página(s) - "
            f"{self.tiempo_por_pagina:g} s/página"
        )