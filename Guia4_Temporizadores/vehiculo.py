# ceil redondea hacia arriba los milisegundos del temporizador.
import math
# random permite elegir un intervalo distinto para cada trayecto.
import random


# Cada objeto tiene su propio temporizador de Tkinter; no hereda de Thread.
class Vehiculo:
    # Un trayecto de ida o de vuelta mide 100 metros simulados.
    LONGITUD = 100

    # Recibimos ventana, identidad, rondas, reloj y función de actualización.
    def __init__(self, ventana, numero, rondas, reloj, actualizar):
        # La ventana permite usar after y after_cancel.
        self.ventana = ventana
        # Identificamos el carro con un número del 1 al 10.
        self.numero = numero
        # Guardamos cuántas idas y vueltas debe realizar.
        self.rondas = rondas
        # Todos consultan el mismo tiempo del juego.
        self.reloj = reloj
        # Guardamos una función de la interfaz para avisar de los cambios.
        self.actualizar = actualizar
        # Creamos un generador aleatorio propio para este carro.
        self.azar = random.Random()
        # Este identificador pertenece SOLO al temporizador de este carro.
        self.id_after = None
        # Al crear el carro todavía no está compitiendo.
        self.activo = False
        # La distancia acumulada empieza en cero y siempre aumenta.
        self.distancia = 0
        # Guardaremos aquí el instante de llegada, en segundos del juego.
        self.tiempo = 0.0
        # Indicamos si ya llegó a la meta después de todas las rondas.
        self.terminado = False
        # Inicializamos el intervalo; al salir elegiremos uno aleatorio.
        self.intervalo = 0.0
        # Instante del juego en el que corresponde avanzar el próximo metro.
        self.proximo_paso = 0.0

    # Ponemos en marcha el temporizador independiente del vehículo.
    def iniciar(self):
        # Evitamos programar dos temporizadores si se llama dos veces.
        if self.activo or self.terminado:
            return
        # Activamos el movimiento del carro.
        self.activo = True
        # Sorteamos la duración de cada paso de un metro, en segundos.
        self._sortear_intervalo()
        # La primera actualización corresponde a ese intervalo desde cero.
        self.proximo_paso = self.intervalo
        # Programamos la primera llamada futura con after.
        self._programar()

    # Elegimos una rapidez nueva al salir o llegar a un extremo.
    def _sortear_intervalo(self):
        # Entre 0.020 y 0.050 s por metro: entre 50 y 20 m/s simulados.
        self.intervalo = self.azar.uniform(0.020, 0.050)

    # Programamos una sola llamada futura para este carro.
    def _programar(self):
        # Calculamos cuántos segundos del juego faltan para el próximo paso.
        restante = max(0.0, self.proximo_paso - self.reloj.leer())
        # Pasamos a milisegundos reales y ajustamos la rapidez del juego.
        # Ejemplo: 0.03 s pendientes a 2x requieren 0.03 * 1000 / 2 = 15 ms.
        # ceil redondea hacia arriba; max exige al menos 1 ms de espera.
        milisegundos = max(1, math.ceil(restante * 1000 / self.reloj.factor))
        # Guardamos el identificador para poder cancelar o reprogramar.
        # Pasamos el método sin paréntesis: Tkinter lo llamará más adelante.
        self.id_after = self.ventana.after(milisegundos, self._avanzar)

    # Tkinter ejecuta este método cuando vence el temporizador del carro.
    def _avanzar(self):
        # La llamada pendiente ya se está ejecutando; dejó de estar pendiente.
        self.id_after = None
        # Si se canceló la carrera, no movemos ni reprogramamos el carro.
        if not self.activo:
            return
        # Consultamos el tiempo simulado actual.
        ahora = self.reloj.leer()
        # Cada ronda equivale a dos trayectos de LONGITUD metros.
        meta = 2 * self.rondas * self.LONGITUD
        # Recuperamos los pasos vencidos si Tkinter atendió el timer tarde.
        # En cada iteración aumenta proximo_paso; aquí no esperamos tiempo.
        # and exige las dos condiciones: ya venció el paso y falta terminar.
        # Usamos while porque podrían haber vencido varios pasos entre llamadas.
        while ahora >= self.proximo_paso and not self.terminado:
            # Cada vencimiento representa un metro recorrido.
            self.distancia += 1
            # Guardamos el instante previsto del paso, sin sumar retrasos de dibujo.
            self.tiempo = self.proximo_paso
            # Revisamos si completó toda la distancia de la carrera.
            self.terminado = self.distancia == meta
            # Al llegar a la meta dejamos de programar movimiento.
            if self.terminado:
                self.activo = False
            # Si llegó a un extremo y aún falta carrera, cambiamos la velocidad.
            # % devuelve el resto: en 100, 200, 300... metros el resto es cero.
            elif self.distancia % self.LONGITUD == 0:
                self._sortear_intervalo()
            # Calculamos cuándo corresponde el siguiente paso de un metro.
            self.proximo_paso += self.intervalo
        # Entregamos este objeto a la interfaz para dibujarlo y revisar su llegada.
        self.actualizar(self)
        # after es de una sola ejecución; lo repetimos mientras siga compitiendo.
        if self.activo:
            self._programar()

    # Ajustamos una espera pendiente cuando el usuario cambia el deslizador.
    def reprogramar(self):
        # Los carros detenidos o finalizados no necesitan otro temporizador.
        if self.activo:
            # Quitamos la llamada calculada con la rapidez anterior.
            self._cancelar_timer()
            # Conservamos el próximo paso y recalculamos el tiempo real restante.
            self._programar()

    # Cancelamos la llamada pendiente de este carro, si existe.
    def _cancelar_timer(self):
        # None significa que no hay una llamada pendiente para cancelar.
        if self.id_after is not None:
            # Cancelamos únicamente el identificador de este vehículo.
            self.ventana.after_cancel(self.id_after)
            # Borramos el identificador que ya no sirve.
            self.id_after = None

    # Detenemos el vehículo cuando se reinicia o se cierra la ventana.
    def detener(self):
        # Impedimos que vuelva a programarse movimiento.
        self.activo = False
        # Eliminamos su llamada pendiente para evitar movimientos antiguos.
        self._cancelar_timer()
