# Importamos time para medir el tiempo real con perf_counter.
import time


# Esta clase convierte segundos reales en segundos del juego.
class RelojCarrera:
    # factor=1.0 significa velocidad normal al crear el reloj.
    def __init__(self, factor=1.0):
        # Guardamos cuánto se acelera o desacelera el tiempo.
        self.factor = factor
        # El juego empieza con cero segundos acumulados.
        self._acumulado = 0.0
        # Guardamos una referencia del reloj real del computador.
        self._anterior = time.perf_counter()

    # Ponemos el cronómetro en cero al comenzar una carrera.
    def iniciar(self):
        # Borramos el tiempo acumulado de la carrera anterior.
        self._acumulado = 0.0
        # La nueva referencia real corresponde a la nueva salida.
        self._anterior = time.perf_counter()

    # Calculamos y devolvemos el tiempo actual del juego.
    def leer(self):
        # Consultamos un contador de tiempo, no la hora del día.
        ahora = time.perf_counter()
        # Sumamos tiempo real transcurrido multiplicado por el factor.
        # += suma al valor que ya había: 0.5 s reales a 2x añaden 1 s del juego.
        self._acumulado += (ahora - self._anterior) * self.factor
        # Guardamos la lectura para no volver a sumar el mismo intervalo.
        self._anterior = ahora
        # Devolvemos los segundos simulados desde la salida.
        return self._acumulado

    # Recibimos la nueva rapidez elegida con el deslizador.
    def cambiar_factor(self, factor):
        # Permitimos desde un cuarto hasta cuatro veces la rapidez normal.
        if not 0.25 <= factor <= 4.0:
            # Avisamos si se intenta usar un valor fuera del intervalo.
            raise ValueError("El factor debe estar entre 0.25 y 4.")
        # Primero acumulamos el tiempo pasado usando el factor anterior.
        self.leer()
        # El factor nuevo se aplica únicamente al tiempo que pase después.
        self.factor = factor
