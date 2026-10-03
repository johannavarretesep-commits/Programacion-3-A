# Tkinter aporta la ventana, el lienzo, el deslizador y sus variables.
import tkinter as tk
# ttk aporta controles con tema; messagebox muestra mensajes de error.
from tkinter import messagebox, ttk
# Importamos el reloj común que permite acelerar el tiempo del juego.
from reloj import RelojCarrera
# Importamos los vehículos, cada uno con su temporizador independiente.
from vehiculo import Vehiculo


# Esta clase construye la ventana y coordina la carrera.
class InterfazCarrera:
    # Una tupla con diez colores para distinguir los vehículos.
    COLORES = ("#dc3545", "#1976d2", "#26834a", "#ed8b23", "#804ab8",
               "#138c91", "#c24386", "#7a5840", "#636b73", "#c19b16")

    # Recibimos la ventana principal creada en main.py.
    def __init__(self, ventana):
        # Guardamos la ventana para crear controles y temporizadores.
        self.ventana = ventana
        # La lista estará vacía hasta iniciar los diez vehículos.
        self.vehiculos = []
        # Creamos un cronómetro del juego, inicialmente a velocidad normal.
        self.reloj = RelojCarrera()
        # Aquí guardaremos pares número de carro: tiempo final.
        self.resultados = {}
        # Indicamos que aún no hay una carrera en curso.
        self.activa = False
        # Definimos el texto de la barra superior de la ventana.
        self.ventana.title("Guía 4 - Carrera con diez temporizadores")
        # Solicitamos un tamaño inicial; el usuario puede agrandarlo.
        self.ventana.geometry("1000x740")
        # Evitamos reducir la ventana hasta ocultar los carriles.
        self.ventana.minsize(960, 720)
        # La X llama a cerrar para cancelar los timers antes de salir.
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar)
        # Creamos campos, botones, pista y tabla.
        self._crear_controles()
        # Dibujamos los diez carros en su posición inicial.
        self._dibujar_pista()

    # Construimos todos los controles de la aplicación.
    def _crear_controles(self):
        # Frame agrupa controles; padding=10 deja un margen interno.
        base = ttk.Frame(self.ventana, padding=10)
        # fill y expand permiten que el marco ocupe el espacio disponible.
        base.pack(fill="both", expand=True)
        # Label muestra un título; font indica familia, tamaño y negrita.
        ttk.Label(base, text="Carrera con temporizadores",
                  font=("Arial", 17, "bold")).pack()
        # Creamos un marco para colocar los campos y botones en una fila.
        controles = ttk.Frame(base)
        # fill=x lo extiende horizontalmente; pady deja espacio vertical.
        controles.pack(fill="x", pady=6)
        # side=left coloca cada control a continuación del anterior.
        ttk.Label(controles, text="Rondas (ida y vuelta):").pack(side="left")
        # Entry recibe texto; width=5 indica un ancho aproximado en caracteres.
        self.rondas = ttk.Entry(controles, width=5)
        # Insertamos el valor inicial en la posición cero del campo.
        self.rondas.insert(0, "2")
        # padx separa horizontalmente este campo de los demás controles.
        self.rondas.pack(side="left", padx=6)
        # Mostramos la etiqueta de selección del carro apostado.
        ttk.Label(controles, text="Apuesto por el carro:").pack(side="left")
        # range(1,11) genera 1 a 10; readonly permite elegir sin escribir otro valor.
        self.apuesta = ttk.Combobox(controles, values=list(range(1, 11)),
                                    state="readonly", width=5)
        # Elegimos la opción de índice cero, que corresponde al carro 1.
        self.apuesta.current(0)
        # Colocamos el selector después de su etiqueta.
        self.apuesta.pack(side="left", padx=6)
        # command recibe el método sin ejecutarlo; el clic lo ejecutará.
        self.iniciar_boton = ttk.Button(controles, text="Iniciar", command=self.iniciar)
        # Colocamos el botón con espacio a sus lados.
        self.iniciar_boton.pack(side="left", padx=6)
        # Reiniciar cancela la carrera, limpia y permite elegir una nueva apuesta.
        self.reiniciar_boton = ttk.Button(controles, text="Reiniciar", command=self.reiniciar)
        # Colocamos este botón al lado de Iniciar.
        self.reiniciar_boton.pack(side="left")
        # DoubleVar vincula un número decimal con el deslizador; empieza en 1x.
        self.factor = tk.DoubleVar(value=1.0)
        # Creamos el slider horizontal de 0.25x a 4x, en pasos de 0.25.
        # variable guarda su valor; command recibe el nuevo valor al moverlo.
        self.deslizador = tk.Scale(base, from_=0.25, to=4.0, resolution=0.25,
            orient="horizontal", variable=self.factor, command=self._cambiar_factor,
            label="Rapidez del juego: 1 = normal; 0.25 = lenta; 4 = rápida")
        # El slider ocupa todo el ancho del marco principal.
        self.deslizador.pack(fill="x")
        # Esta etiqueta informa preparación, carrera y resultado de la apuesta.
        self.estado = ttk.Label(base, text="Elige las rondas y tu carro; luego pulsa Iniciar.")
        # Añadimos un pequeño espacio vertical alrededor del mensaje.
        self.estado.pack(pady=4)
        # Canvas es el lienzo; width/height son píxeles; bg es el color del fondo.
        self.pista = tk.Canvas(base, width=940, height=340,
                               bg="#eef2f5", highlightthickness=0)
        # Colocamos el lienzo debajo de los controles.
        self.pista.pack()
        # Agrupamos tabla y barra de desplazamiento en un marco aparte.
        marco_tabla = ttk.Frame(base)
        # La tabla aprovecha el espacio sobrante si se agranda la ventana.
        marco_tabla.pack(fill="both", expand=True, pady=6)
        # Definimos los identificadores internos de las columnas.
        columnas = ("puesto", "carro", "tiempo")
        # headings muestra encabezados; height=10 solicita diez filas visibles.
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=10)
        # Asociamos cada identificador con el título que verá el usuario.
        for columna, titulo in zip(columnas, ("Puesto", "Vehículo", "Tiempo del juego (s)")):
            # Definimos el texto de este encabezado.
            self.tabla.heading(columna, text=titulo)
            # Centramos los valores y asignamos ancho inicial en píxeles.
            self.tabla.column(columna, width=220, anchor="center")
        # La tabla se expande, dejando a su derecha sitio para la barra.
        self.tabla.pack(side="left", fill="both", expand=True)
        # yview permite que la barra desplace verticalmente la tabla.
        barra = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla.yview)
        # La barra ocupa la altura disponible a la derecha de la tabla.
        barra.pack(side="right", fill="y")
        # La tabla también informa a la barra qué parte del contenido se ve.
        self.tabla.configure(yscrollcommand=barra.set)

    # Dibujamos la pista y los diez vehículos desde cero.
    def _dibujar_pista(self):
        # Quitamos los dibujos de cualquier carrera anterior.
        self.pista.delete("all")
        # Guardaremos la coordenada horizontal de cada carro.
        self.posiciones = {}
        # Guardaremos el identificador del texto informativo de cada carril.
        self.textos = {}
        # La carrera empieza y termina en el extremo izquierdo.
        self.pista.create_text(65, 15, text="Salida / Meta")
        # El extremo derecho marca dónde comienza la vuelta.
        self.pista.create_text(765, 15, text="Retorno")
        # Construimos los carros identificados del 1 al 10.
        for numero in range(1, 11):
            # Separamos verticalmente los carriles 30 píxeles.
            y = 45 + (numero - 1) * 30
            # Dibujamos una línea divisoria debajo del vehículo.
            self.pista.create_line(40, y + 14, 800, y + 14, fill="#b6c2cc")
            # Mostramos el número del carro al lado de su carril.
            self.pista.create_text(20, y, text=str(numero))
            # Todas las piezas del mismo carro compartirán esta etiqueta.
            etiqueta = f"carro{numero}"
            # Restamos uno porque los índices de la tupla comienzan en cero.
            color = self.COLORES[numero - 1]
            # Rectángulo de carrocería: dos esquinas, color y etiqueta de grupo.
            self.pista.create_rectangle(45, y - 8, 85, y + 8, fill=color, tags=etiqueta)
            # Dibujamos una cabina clara dentro de la carrocería.
            self.pista.create_rectangle(56, y - 5, 74, y + 5,
                                        fill="#d9efff", tags=etiqueta)
            # Elegimos dos posiciones horizontales para las ruedas.
            for x in (49, 73):
                # En cada posición habrá una rueda arriba y otra abajo.
                for dy in (-11, 7):
                    # Dibujamos las cuatro ruedas con la misma etiqueta del carro.
                    self.pista.create_rectangle(x, y + dy, x + 7, y + dy + 4,
                                                fill="#222222", tags=etiqueta)
            # El centro inicial del carro está en x=65.
            self.posiciones[numero] = 65.0
            # Creamos el texto de estado y conservamos su identificador.
            self.textos[numero] = self.pista.create_text(865, y, text="Listo")

    # Validamos datos y ponemos en marcha los diez temporizadores.
    def iniciar(self):
        # Evitamos iniciar dos carreras simultáneamente.
        if self.activa:
            return
        # Intentamos convertir a entero el texto escrito en el campo.
        try:
            # get lee el campo; int convierte ese texto en un número entero.
            rondas = int(self.rondas.get())
            # Limitamos las rondas para que la demostración sea manejable.
            if not 1 <= rondas <= 20:
                # Provocamos un error que atenderá el bloque except.
                raise ValueError("Cantidad de rondas fuera del intervalo.")
        # Atendemos tanto texto no numérico como valores fuera del intervalo.
        except ValueError:
            # Mostramos qué debe corregir el usuario.
            messagebox.showerror("Rondas inválidas", "Escribe un entero entre 1 y 20.")
            # Salimos sin crear ni iniciar temporizadores.
            return
        # Conservamos el número de rondas de esta carrera.
        self.rondas_carrera = rondas
        # Fijamos la apuesta antes de iniciar los vehículos.
        self.apuesta_carrera = int(self.apuesta.get())
        # Vaciamos el registro de tiempos de la carrera anterior.
        self.resultados = {}
        # get_children devuelve los identificadores de las filas de la tabla.
        for fila in self.tabla.get_children():
            # Eliminamos cada fila de resultados anterior.
            self.tabla.delete(fila)
        # Creamos el reloj con la rapidez que tiene actualmente el slider.
        self.reloj = RelojCarrera(self.factor.get())
        # Creamos diez objetos; cada uno guardará su propio id_after.
        # _actualizar_vehiculo es la función que llamarán para informar su avance.
        self.vehiculos = [Vehiculo(self.ventana, n, rondas, self.reloj,
                                    self._actualizar_vehiculo) for n in range(1, 11)]
        # Devolvemos todos los dibujos a la salida.
        self._dibujar_pista()
        # Marcamos que la carrera está en curso.
        self.activa = True
        # Deshabilitamos Iniciar para evitar duplicar temporizadores.
        self.iniciar_boton.configure(state="disabled")
        # Las rondas no pueden cambiar durante la carrera.
        self.rondas.configure(state="disabled")
        # La apuesta tampoco puede cambiar después de la salida.
        self.apuesta.configure(state="disabled")
        # Establecemos una referencia de tiempo común para todos.
        self.reloj.iniciar()
        # Recorremos los diez vehículos recién creados.
        for vehiculo in self.vehiculos:
            # Cada objeto programa su propio temporizador after.
            vehiculo.iniciar()
        # Mostramos el carro elegido antes de la salida.
        self.estado.configure(text=f"Carrera en curso. Tu apuesta: carro {self.apuesta_carrera}.")

    # Tkinter llama a este método al mover el deslizador.
    def _cambiar_factor(self, valor):
        # El slider entrega texto; float permite usarlo como número decimal.
        self.reloj.cambiar_factor(float(valor))
        # Ajustamos las esperas pendientes de los diez carros.
        for vehiculo in self.vehiculos:
            # Cada carro conserva su avance y recalcula su próximo vencimiento real.
            vehiculo.reprogramar()

    # Un vehículo llama a este método desde su temporizador para informar cambios.
    def _actualizar_vehiculo(self, vehiculo):
        # Consultamos qué carro debemos actualizar.
        numero = vehiculo.numero
        # Una ronda mide 200 m; el resto da la posición dentro de esa ronda.
        # Ejemplo: 250 % 200 = 50; lleva 50 m de la siguiente ronda.
        fase = vehiculo.distancia % (2 * Vehiculo.LONGITUD)
        # En ida la posición crece; en vuelta disminuye hasta regresar a cero.
        posicion = fase if fase <= Vehiculo.LONGITUD else 2 * Vehiculo.LONGITUD - fase
        # Convertimos los metros de posición a píxeles entre x=65 y x=765.
        x = 65 + posicion / Vehiculo.LONGITUD * 700
        # Movemos todas las piezas del carro por la diferencia con su x anterior.
        self.pista.move(f"carro{numero}", x - self.posiciones[numero], 0)
        # Conservamos la posición nueva para la siguiente actualización.
        self.posiciones[numero] = x
        # La división entera cuenta idas y vueltas completas.
        completas = vehiculo.distancia // (2 * Vehiculo.LONGITUD)
        # Avanzamos 1 m por intervalo: velocidad = 1 / intervalo.
        texto = f"{completas}/{vehiculo.rondas} | {1 / vehiculo.intervalo:.1f} m/s"
        # Si este carro ya completó todas sus rondas, registramos su tiempo final.
        if vehiculo.terminado:
            # Usamos el número como clave para guardar un solo resultado por carro.
            self.resultados[numero] = vehiculo.tiempo
            # Mostramos su llegada; .3f limita la presentación a tres decimales.
            texto = f"Meta | {vehiculo.tiempo:.3f} s"
        # Cambiamos el texto del carril sin crear otro objeto gráfico.
        self.pista.itemconfigure(self.textos[numero], text=texto)
        # Solo clasificamos cuando llegaron los diez participantes.
        if len(self.resultados) == 10:
            # Ordenamos tiempos, mostramos la tabla y anunciamos la apuesta.
            self._clasificar()

    # Construimos la clasificación final de menor a mayor tiempo.
    def _clasificar(self):
        # items produce pares (número, tiempo); ordenamos por tiempo y luego número.
        # El segundo criterio resuelve un empate exacto por menor número de carro.
        # lambda recibe cada par y devuelve (tiempo, número) como clave de orden.
        orden = sorted(self.resultados.items(), key=lambda par: (par[1], par[0]))
        # enumerate numera los puestos desde 1 y desempaquetamos cada resultado.
        for puesto, (numero, tiempo) in enumerate(orden, start=1):
            # Insertamos al final una fila; .6f muestra seis decimales del tiempo.
            self.tabla.insert("", "end", values=(puesto, f"Carro {numero}", f"{tiempo:.6f}"))
        # El primer par contiene el carro con el menor tiempo.
        ganador = orden[0][0]
        # Comparamos al ganador con la apuesta fijada antes de iniciar.
        acierto = "¡Acertaste!" if ganador == self.apuesta_carrera else "No acertaste."
        # Habilitamos una nueva carrera e informamos el resultado.
        self._habilitar(f"Ganador: carro {ganador}. Apostaste por {self.apuesta_carrera}. {acierto}")

    # Dejamos los campos disponibles al terminar o reiniciar una carrera.
    def _habilitar(self, texto):
        # Ya no hay una carrera en curso.
        self.activa = False
        # Mostramos el mensaje recibido como argumento.
        self.estado.configure(text=texto)
        # Volvemos a permitir iniciar.
        self.iniciar_boton.configure(state="normal")
        # Volvemos a permitir escribir el número de rondas.
        self.rondas.configure(state="normal")
        # Permitimos seleccionar una apuesta entre las diez opciones.
        self.apuesta.configure(state="readonly")

    # Reiniciamos sin cerrar la ventana; el usuario puede elegir y pulsar Iniciar.
    def reiniciar(self):
        # Recorremos también los carros ya terminados; detener es seguro para ellos.
        for vehiculo in self.vehiculos:
            # Cancelamos cualquier after pendiente antes de borrar los dibujos.
            vehiculo.detener()
        # Quitamos las referencias a los carros anteriores.
        self.vehiculos = []
        # Borramos los tiempos anteriores.
        self.resultados = {}
        # Recorremos las filas existentes en la tabla.
        for fila in self.tabla.get_children():
            # Eliminamos cada resultado mostrado.
            self.tabla.delete(fila)
        # Devolvemos el reloj a cero, conservando la rapidez elegida.
        self.reloj.iniciar()
        # Volvemos a dibujar diez carros en la salida.
        self._dibujar_pista()
        # Habilitamos rondas, apuesta e inicio; no anunciamos un ganador al cancelar.
        self._habilitar("Carrera reiniciada. Elige tu apuesta y pulsa Iniciar.")

    # Atendemos el cierre de la ventana principal.
    def cerrar(self):
        # Recorremos los vehículos que existen en esta carrera.
        for vehiculo in self.vehiculos:
            # Cancelamos todos los temporizadores antes de destruir los controles.
            vehiculo.detener()
        # Cerramos la ventana y finaliza mainloop.
        self.ventana.destroy()
