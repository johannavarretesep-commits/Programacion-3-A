# importar librerias
import time
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText

from pila_tareas import PilaTareas
from tarea import Tarea


class InterfazRobot:
    """Construye la ventana y coordina una tarea a la vez usando after()."""

    def __init__(self, ventana):
        self.ventana = ventana
        self.pila = PilaTareas()
        self.tarea_actual = None
        self.simulacion_activa = False
        self.en_pausa = False
        self.id_after = None
        self.tiempo_restante = 0.0
        self.instante_fin = 0.0

        self.ventana.title("Guía 3 - Robot explorador | Pila LIFO")
        self.ventana.geometry("900x680")
        self.ventana.minsize(760, 580)
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        self._crear_interfaz()
        self._actualizar_pila_visible()

    def _crear_interfaz(self):
        principal = ttk.Frame(self.ventana, padding=16)
        principal.pack(fill="both", expand=True)
        principal.columnconfigure(0, weight=1)
        principal.rowconfigure(5, weight=1)

        ttk.Label(principal, text="Robot explorador", font=("Segoe UI", 18, "bold")).grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(
            principal,
            text="LIFO: la última tarea agregada será la siguiente. La actual termina primero.",
            wraplength=700,
        ).grid(row=1, column=0, sticky="w", pady=(4, 12))

        formulario = ttk.LabelFrame(principal, text="Nueva tarea", padding=10)
        formulario.grid(row=2, column=0, sticky="ew")
        formulario.columnconfigure(0, weight=3)
        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(2, weight=1)

        for columna, titulo in enumerate(("Nombre", "Tipo", "Tiempo de ejecución (s)")):
            ttk.Label(formulario, text=titulo).grid(row=0, column=columna, sticky="w")

        self.entrada_nombre = ttk.Entry(formulario)
        self.entrada_nombre.grid(row=1, column=0, sticky="ew", padx=(0, 8))
        # readonly permite seleccionar únicamente los dos tipos requeridos.
        self.selector_tipo = ttk.Combobox(
            formulario, values=("Sensores", "Movimiento"), state="readonly", width=15
        )
        self.selector_tipo.current(0)
        self.selector_tipo.grid(row=1, column=1, sticky="ew", padx=(0, 8))
        self.entrada_tiempo = ttk.Entry(formulario, width=12)
        self.entrada_tiempo.insert(0, "3")
        self.entrada_tiempo.grid(row=1, column=2, sticky="ew")
        ttk.Button(formulario, text="Agregar a la pila", command=self.agregar_tarea).grid(
            row=2, column=0, sticky="w", pady=(10, 0)
        )
        for entrada in (self.entrada_nombre, self.entrada_tiempo):
            entrada.bind("<Return>", lambda evento: self.agregar_tarea())

        botones = ttk.Frame(principal)
        botones.grid(row=3, column=0, sticky="ew", pady=12)
        ttk.Button(botones, text="Iniciar / Reanudar", command=self.iniciar_simulacion).pack(
            side="left", padx=(0, 8)
        )
        ttk.Button(botones, text="Detener / Pausar", command=self.pausar_simulacion).pack(
            side="left"
        )
        self.etiqueta_estado = ttk.Label(principal, text="Estado: sin tareas pendientes")
        self.etiqueta_estado.grid(row=4, column=0, sticky="w", pady=(0, 8))

        paneles = ttk.Frame(principal)
        paneles.grid(row=5, column=0, sticky="nsew")
        paneles.columnconfigure(0, weight=1, uniform="panel")
        paneles.columnconfigure(1, weight=1, uniform="panel")
        paneles.rowconfigure(0, weight=1)

        pendientes = ttk.LabelFrame(paneles, text="Pila pendiente · cima arriba", padding=8)
        pendientes.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        pendientes.columnconfigure(0, weight=1)
        pendientes.rowconfigure(1, weight=1)
        self.etiqueta_cantidad = ttk.Label(pendientes)
        self.etiqueta_cantidad.grid(row=0, column=0, sticky="w")
        self.lista_pila = tk.Listbox(pendientes, width=25, font=("Consolas", 10))
        self.lista_pila.grid(row=1, column=0, sticky="nsew", pady=(6, 0))
        barra = ttk.Scrollbar(pendientes, orient="vertical", command=self.lista_pila.yview)
        barra.grid(row=1, column=1, sticky="ns")
        self.lista_pila.configure(yscrollcommand=barra.set)
        barra_horizontal = ttk.Scrollbar(
            pendientes, orient="horizontal", command=self.lista_pila.xview
        )
        barra_horizontal.grid(row=2, column=0, sticky="ew")
        self.lista_pila.configure(xscrollcommand=barra_horizontal.set)

        proceso = ttk.LabelFrame(paneles, text="Ejecución e historial", padding=8)
        proceso.grid(row=0, column=1, sticky="nsew", padx=(6, 0))
        proceso.columnconfigure(0, weight=1)
        proceso.rowconfigure(3, weight=1)
        self.etiqueta_actual = ttk.Label(proceso, text="Tarea actual: ninguna", wraplength=310)
        self.etiqueta_actual.grid(row=0, column=0, sticky="w")
        self.etiqueta_tiempo = ttk.Label(proceso, text="Tiempo restante: -")
        self.etiqueta_tiempo.grid(row=1, column=0, sticky="w", pady=6)
        self.progreso = ttk.Progressbar(proceso, maximum=100, mode="determinate")
        self.progreso.grid(row=2, column=0, sticky="ew", pady=(0, 8))
        self.historial = ScrolledText(
            proceso, width=30, height=10, wrap="word", state="disabled", font=("Consolas", 10)
        )
        self.historial.grid(row=3, column=0, sticky="nsew")
        self.entrada_nombre.focus()

    def agregar_tarea(self):
        try:
            # Las entradas entregan texto: convertimos los segundos a float.
            tiempo = float(self.entrada_tiempo.get().strip().replace(",", "."))
        except ValueError:
            messagebox.showerror("Dato inválido", "Escribe un tiempo numérico, por ejemplo 2 o 0,5.")
            return
        try:
            tarea = Tarea(self.entrada_nombre.get(), self.selector_tipo.get(), tiempo)
        except (ValueError, TypeError) as error:
            messagebox.showerror("Dato inválido", str(error))
            return

        self.pila.agregar_tarea(tarea)
        self._registrar(f"Agregada: {tarea}")
        self._actualizar_pila_visible()
        if not self.simulacion_activa:
            self.etiqueta_estado.configure(text="Estado: tareas listas; presiona Iniciar")
        # No retiramos la tarea actual ni reiniciamos su temporizador al agregar otra.
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_nombre.focus()

    def iniciar_simulacion(self):
        # Evita crear temporizadores duplicados al pulsar Iniciar varias veces.
        if self.simulacion_activa and not self.en_pausa:
            return
        if self.tarea_actual is None and self.pila.esta_vacia():
            messagebox.showinfo("Pila vacía", "Agrega al menos una tarea antes de iniciar.")
            return
        self.simulacion_activa = True
        if self.en_pausa:
            self.en_pausa = False
            # Reanudamos solo el tiempo que faltaba, sin contar la pausa.
            self.instante_fin = time.monotonic() + self.tiempo_restante
            self.etiqueta_estado.configure(text="Estado: ejecutando")
            self._registrar("Simulación reanudada.")
            self._actualizar_ejecucion()
        else:
            self._registrar("Simulación iniciada.")
            self._iniciar_siguiente()

    def _iniciar_siguiente(self):
        self.tarea_actual = self.pila.retirar_tarea()
        self._actualizar_pila_visible()
        if self.tarea_actual is None:
            self.simulacion_activa = False
            self.en_pausa = False
            self.tiempo_restante = 0.0
            self.etiqueta_estado.configure(text="Estado: sin tareas pendientes")
            self.etiqueta_actual.configure(text="Tarea actual: ninguna")
            self.etiqueta_tiempo.configure(text="Tiempo restante: -")
            self.progreso.configure(value=0)
            self._registrar("Simulación finalizada: no quedan tareas en la pila.")
            return
        self.tiempo_restante = self.tarea_actual.tiempo_ejecucion
        # monotonic mide tiempo transcurrido sin depender de cambios del reloj del PC.
        self.instante_fin = time.monotonic() + self.tiempo_restante
        self.etiqueta_actual.configure(text=f"Tarea actual: {self.tarea_actual}")
        self.etiqueta_estado.configure(text="Estado: ejecutando")
        self._registrar(f"Ejecutando: {self.tarea_actual}")
        self._actualizar_ejecucion()

    def _actualizar_ejecucion(self):
        self.id_after = None
        if not self.simulacion_activa or self.en_pausa:
            return
        self.tiempo_restante = max(0.0, self.instante_fin - time.monotonic())
        self._mostrar_progreso()
        if self.tiempo_restante <= 0:
            self._registrar(f"Terminada: {self.tarea_actual.nombre}")
            self.tarea_actual = None
            self._iniciar_siguiente()
            return
        # Revisamos el tiempo sin bloquear la ventana ni usar time.sleep().
        self.id_after = self.ventana.after(50, self._actualizar_ejecucion)

    def pausar_simulacion(self):
        if not self.simulacion_activa or self.en_pausa:
            return
        self.en_pausa = True
        self.tiempo_restante = max(0.0, self.instante_fin - time.monotonic())
        if self.id_after is not None:
            self.ventana.after_cancel(self.id_after)
            self.id_after = None
        self._mostrar_progreso()
        self.etiqueta_estado.configure(text="Estado: pausado")
        self._registrar("Pausa: se conservan la tarea actual, el tiempo restante y la pila.")

    def _mostrar_progreso(self):
        self.etiqueta_tiempo.configure(text=f"Tiempo restante: {self.tiempo_restante:.2f} s")
        porcentaje = 100 * (1 - self.tiempo_restante / self.tarea_actual.tiempo_ejecucion)
        self.progreso.configure(value=max(0, min(100, porcentaje)))

    def _actualizar_pila_visible(self):
        self.lista_pila.delete(0, tk.END)
        for posicion, tarea in enumerate(self.pila.obtener_tareas(), start=1):
            marca = "CIMA" if posicion == 1 else str(posicion)
            self.lista_pila.insert(tk.END, f"{marca}: {tarea}")
        self.etiqueta_cantidad.configure(text=f"{self.pila.cantidad()} tarea(s) pendientes")

    def _registrar(self, mensaje):
        self.historial.configure(state="normal")
        self.historial.insert(tk.END, mensaje + "\n")
        self.historial.see(tk.END)
        self.historial.configure(state="disabled")

    def cerrar_aplicacion(self):
        self.simulacion_activa = False
        if self.id_after is not None:
            self.ventana.after_cancel(self.id_after)
            self.id_after = None
        self.ventana.destroy()
