# importando
import tkinter as tk
# Mostrar avisos y errores en ventanas emergentes, botones, etc
from tkinter import messagebox, ttk

from impresora import ColaImpresion
from Documento import Documento

# Creamos la clase para la interfaz de la aplicación
class InterfazImpresion:
    # Podemos meterle unos ajustes de estetica como el color
    COLOR_FONDO = "#f3f5f8"
    COLOR_PRINCIPAL = "#1f4e78"
    COLOR_SECUNDARIO = "#2e75b6"
    # Iniciamos el constructor
    def __init__(self, ventana):
        # Guardamos la ventana como atributo
        self.ventana = ventana
        # Creamos una cola vacia
        self.cola = ColaImpresion()

        # Variables de estado de la impresión:
        self.documento_actual = None
        self.pagina_actual = 0
        self.pagina_en_proceso = False
        self.simulacion_activa = False
        self.en_pausa = False
        self.id_after = None

        # Funciones que inicia el constructor (metodos)
        self._configurar_ventana()
        self._crear_estilos()
        self._crear_interfaz()
        self._actualizar_cola_visible()
        self._actualizar_estado("Sin documentos en impresión")

    # Configuramos la ventana de la aplicación
    def _configurar_ventana(self):
        # Titulo principal
        self.ventana.title("Guía 3 - Simulador de cola de impresión")
        # Resolución
        self.ventana.geometry("1920x1080")
        # Color del fondo
        self.ventana.configure(bg=self.COLOR_FONDO)
        # Cerrar la aplicación
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    # Vamos a crear una función para meterle el estilo a la aplicación
    def _crear_estilos(self):
        # Creamos objeto para configurar el estilo
        estilo = ttk.Style()
        # Asignamos tipo de letra, tamaño y en negrilla
        estilo.configure("Titulo.TLabel", font=("Segoe UI", 18, "bold"))
        estilo.configure("Subtitulo.TLabel", font=("Segoe UI", 11, "bold"))
        estilo.configure("Estado.TLabel", font=("Segoe UI", 11, "bold"))
        estilo.configure("Principal.TButton", font=("Segoe UI", 10, "bold"))
    # Ahora vamos a crear la interfaz de la aplicación (como se organiza en la pantalla)
    def _crear_interfaz(self):
        # Creamos contenedor donde guardaremos los botones y eso
        # En este caso va a estar en la ventana y tiene 18 de espacio
        contenedor = ttk.Frame(self.ventana, padding=18)
        # Ahora lo colocamos en la pantalla de la aplicación
        # expand es para que quede en el espacio disponible (el que esta en blanco)
        # El fill es para que se ajuste en el espacio que tiene disponible
        contenedor.pack(fill="both", expand=True)
        # Ahora tenemos que organizar los controles del contenedor en el espacio que tiene
        # El 0 configura la primera columna y se va agrandando a medida que entran más objetos
        contenedor.columnconfigure(0, weight=1)
        # Lo mismo pero con columnas, aunque se pone 4 porque aqui vamos a meter el documento
        # Y antes de eso tienen que mostrarse otras cosas como el titulo y eso
        contenedor.rowconfigure(4, weight=1)
        # Creación de un objeto digamos dentro del contenedor, en este caso es el titulo
        ttk.Label(
            contenedor,
            text="Simulador de cola de impresión",
            style="Titulo.TLabel",
            # Fila 1, columna 1 y empieza desde el west (osea izquierda)
        ).grid(row=0, column=0, sticky="w")

        ttk.Label(
            contenedor,
            text="Los documentos se procesan en orden FIFO: primero en entrar, primero en salir.",
            # El pady es para dejar espacio, primero se pone el de arriba y luego el de abajo
        ).grid(row=1, column=0, sticky="w", pady=(2, 14))
        # Aqui llamamos a las funciones (o metodos) que tambien toca mostrar en el interfaz
        self._crear_formulario(contenedor)
        self._crear_panel_control(contenedor)
        self._crear_paneles_informacion(contenedor)
    # Creamos una nueva función para crear los formularios, padre es el contenedor
    def _crear_formulario(self, padre):
        # Creamos el formulario que estara alojado en padre
        formulario = ttk.LabelFrame(padre, text="Nuevo documento", padding=12)
        # Ubicamos el formulario en su lugar de la cuadricula digamos
        formulario.grid(row=2, column=0, sticky="ew")
        # Vamos a repartir el espacio para que mas o menos se ajuste a la ventana
        # Si no se coloca eso queda feo
        # El nombre que es lo primero que aparece tiene el doble de espacio disponible digamos
        formulario.columnconfigure(1, weight=2)
        # luego van paginas y eso son números asi que le ponemos 1 porque no necesitan tanto espacio
        formulario.columnconfigure(3, weight=1)
        formulario.columnconfigure(5, weight=1)
        # Ahora colocamos el texto nombre en la ventana
        ttk.Label(formulario, text="Nombre:").grid(row=0, column=0, sticky="w")
        # Ponemos un espacio donde el usuario pueda escribir y asi digitar cual es el nombre
        # Del documento
        self.entrada_nombre = ttk.Entry(formulario)
        # Lo ubica en la fila 1, columna 2, ew es para que ocupe más espacio horizontal si necesita
        # Luego le deja espacio a la izquierda 6 y a la derecha 14
        self.entrada_nombre.grid(row=0, column=1, sticky="ew", padx=(6, 14))
        # Lo mismo de antes pero para que el usuario ingrese la cantidad de paginas
        ttk.Label(formulario, text="Páginas:").grid(row=0, column=2, sticky="w")
        self.entrada_paginas = ttk.Entry(formulario, width=10)
        self.entrada_paginas.grid(row=0, column=3, sticky="ew", padx=(6, 14))
        # Ahora con el tiempo que se tarda en imprimir cada pagina
        ttk.Label(formulario, text="Segundos/página:").grid(
            row=0, column=4, sticky="w"
        )
        self.entrada_tiempo = ttk.Entry(formulario, width=12)
        self.entrada_tiempo.grid(row=0, column=5, sticky="ew", padx=(6, 14))
        # Ahora insertamos un 1 en la casilla, para que quede como predeterminado 1 segundo
        self.entrada_tiempo.insert(0, "1")
        # Ahora creamos el boton para agregar el formulario
        ttk.Button(
            formulario,
            text="Agregar a la cola",
            # Se coloca sin el () para que no se ejecute apenas inicie el programa sino solo cuando
            # Se oprima el boton
            command=self.agregar_documento,
            style="Principal.TButton",
        ).grid(row=0, column=6, sticky="ew")
        # Para mayor comodidad, podemos ponerle que ejecute el comando si precionamos el enter
        # Esto lo aplicamos para todas las entradas
        self.entrada_nombre.bind("<Return>", lambda evento: self.agregar_documento())
        self.entrada_paginas.bind("<Return>", lambda evento: self.agregar_documento())
        self.entrada_tiempo.bind("<Return>", lambda evento: self.agregar_documento())
    # Hacemos lo mismo pero con el panel de control
    def _crear_panel_control(self, padre):
        control = ttk.Frame(padre, padding=(0, 12))
        control.grid(row=3, column=0, sticky="ew")
        control.columnconfigure(3, weight=1)
        # Creamos el boton de iniciar y luego el de pausar
        self.boton_iniciar = ttk.Button(
            control,
            text="Iniciar / Reanudar",
            command=self.iniciar_impresion,
            style="Principal.TButton",
        )
        self.boton_iniciar.grid(row=0, column=0, padx=(0, 8))

        self.boton_pausar = ttk.Button(
            control,
            text="Detener / Pausar",
            command=self.pausar_impresion,
        )
        self.boton_pausar.grid(row=0, column=1, padx=(0, 8))
        # Creamos el boton de limpiar el historial igual que los otros
        ttk.Button(control, text="Limpiar historial", command=self.limpiar_historial).grid(
            row=0, column=2
        )
        # Ahora vamos a crear el cartel que indique que anda haciendo la imprerosa, si esta pausada, vacia y eso
        self.etiqueta_estado = ttk.Label(control, style="Estado.TLabel")
        self.etiqueta_estado.grid(row=0, column=3, sticky="e")
    # Vamos con los paneles de información de la misma manera que las anteriores
    def _crear_paneles_informacion(self, padre):
        # Creamos contenedor llamado panel que a su vez esta en padre
        panel = ttk.Frame(padre)
        panel.grid(row=4, column=0, sticky="nsew")
        panel.columnconfigure(0, weight=2)
        panel.columnconfigure(1, weight=3)
        panel.rowconfigure(0, weight=1)
        # Crear el marco de los documentos pendientes
        marco_cola = ttk.LabelFrame(panel, text="Documentos pendientes", padding=10)
        marco_cola.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        marco_cola.columnconfigure(0, weight=1)
        marco_cola.rowconfigure(1, weight=1)

        self.etiqueta_cantidad = ttk.Label(marco_cola, text="0 documento(s)")
        self.etiqueta_cantidad.grid(row=0, column=0, sticky="w", pady=(0, 6))

        self.lista_cola = tk.Listbox(
            marco_cola,
            # Tipo y tamaño de letra
            font=("Consolas", 10),
            # Color de fondo y marca visual
            activestyle="none",
            selectbackground=self.COLOR_SECUNDARIO,
        )
        self.lista_cola.grid(row=1, column=0, sticky="nsew")
        # Ahora hacemos que la lista se pueda mover digamos, bueno, expandir hacia abajo
        desplazamiento_cola = ttk.Scrollbar(
            # Utilizamos el metodo de tkinder yview para poder subir y bajar en la lista_cola
            marco_cola, orient="vertical", command=self.lista_cola.yview
        )
        desplazamiento_cola.grid(row=1, column=1, sticky="ns")
        # Este es otro comando para que la la posición de la lista la barra se actualice y se vaya moviendo 
        # usamos el .set que tmb es metodo de tkinder
        self.lista_cola.configure(yscrollcommand=desplazamiento_cola.set)
        # Ahora hacemos lo mismo pero con el marco del proceso de impresión
        marco_proceso = ttk.LabelFrame(panel, text="Proceso de impresión", padding=10)
        marco_proceso.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        marco_proceso.columnconfigure(0, weight=1)
        marco_proceso.rowconfigure(3, weight=1)
        # Creamos el titulo del documento actual, al inicio como no hay nada se pone ninguno
        self.etiqueta_documento_actual = ttk.Label(
            marco_proceso,
            text="Documento actual: ninguno",
            style="Subtitulo.TLabel",
        )
        self.etiqueta_documento_actual.grid(row=0, column=0, sticky="w")
        # Texto de en que pagina va
        self.etiqueta_pagina = ttk.Label(marco_proceso, text="Página: -")
        self.etiqueta_pagina.grid(row=1, column=0, sticky="w", pady=(4, 4))
        # Vamos a hacer una barra de progreso
        self.barra_progreso = ttk.Progressbar(
            # La barra va dentro del marco de proceso, va horizontalemnte 
            # El mode determinante es para que podamos meterle donde va la barra
            marco_proceso, orient="horizontal", mode="determinate"
        )
        self.barra_progreso.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        # Ahora la sección del historial que va dentro del de procesos
        marco_historial = ttk.Frame(marco_proceso)
        # El nsew es para que ocupe todo el espacio que tenga disponible en la celda
        marco_historial.grid(row=3, column=0, sticky="nsew")
        marco_historial.columnconfigure(0, weight=1)
        marco_historial.rowconfigure(0, weight=1)
        # Ahora un texto que va dentro del marco historial que a su vez va en el de procesos
        self.texto_historial = tk.Text(
            marco_historial,
            # Ocupa el espacio disponible
            wrap="word",
            # Esto es para que no se edite el texto cuando el programa este corriendo
            state="disabled",
            # fuente y tamaño de letra
            font=("Consolas", 10),
            # color del fondo
            bg="#ffffff",
        )
        self.texto_historial.grid(row=0, column=0, sticky="nsew")
        # Ahora hacemos lo mismo de la lista que se puede mover 
        desplazamiento_texto = ttk.Scrollbar(
            marco_historial, orient="vertical", command=self.texto_historial.yview
        )
        desplazamiento_texto.grid(row=0, column=1, sticky="ns")
        self.texto_historial.configure(yscrollcommand=desplazamiento_texto.set)
    # Creamos el texto para agregar documentos
    def agregar_documento(self):
        # Le pedimos el nombre al usuario con el .get() y quita espacios en los extremos para que encaje 
        # El texto bien
        nombre = self.entrada_nombre.get().strip()

        try:
            # Pedimos paginas y tiempo
            texto_paginas = self.entrada_paginas.get().strip()
            texto_tiempo = self.entrada_tiempo.get().strip().replace(",", ".")
            # Hacemos lo mismo que pidiendo el documento en el archivo de Documento.py
            # Pero esta vez con las paginas y el tiempo, tambien manda carteles bien maquiavelicos

            if not texto_paginas:
                raise ValueError("Debe ingresar el número de páginas.")
            if not texto_tiempo:
                raise ValueError("Debe ingresar el tiempo por página.")

            try:
                # Preguntamos si el numero de paginas es un numero entero
                numero_paginas = int(texto_paginas)
            except ValueError as error:
                raise ValueError(
                    "El número de páginas debe ser un número entero."
                ) from error

            try:
                # Tiempo debe ser decimal
                tiempo_por_pagina = float(texto_tiempo)
            except ValueError as error:
                raise ValueError(
                    "El tiempo por página debe ser un número."
                ) from error
            # Creamos el documento
            documento = Documento(nombre, numero_paginas, tiempo_por_pagina)
            # Si alguna de las cosas de arriba sale mal mete un error y no agrega el documento
        except ValueError as error:
            messagebox.showerror("Datos inválidos", str(error))
            return

        self.cola.agregar_documento(documento)
        self._registrar(f"Documento agregado: {documento}")
        self._actualizar_cola_visible()

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_paginas.delete(0, tk.END)
        self.entrada_nombre.focus()
        #  textos y eso relacionados con iniciar impresión
    def iniciar_impresion(self):
        # Preguntamos si la simulación esta activa, en ese caso mete el cartel
        if self.simulacion_activa and not self.en_pausa:
            messagebox.showinfo("Impresión", "La simulación ya está en ejecución.")
            return
        # Si la cola esta vacia lo dice y no se pone a simular
        if self.documento_actual is None and self.cola.esta_vacia():
            messagebox.showwarning(
                "Cola vacía", "Primero debe agregar al menos un documento."
            )
            return

        if self.en_pausa:
            self.en_pausa = False
            self._registrar("Impresión reanudada.")
        else:
            self.simulacion_activa = True
            self._registrar("Simulación iniciada.")

        self.simulacion_activa = True
        # Si la simulación esta activa llamamos al siguiente metodo
        self._avanzar_simulacion()
        # Mismo de arriba pero con la impresión en pausa
    def pausar_impresion(self):
        if not self.simulacion_activa or self.en_pausa:
            messagebox.showinfo("Impresión", "No hay una impresión activa para pausar.")
            return

        self.en_pausa = True

        if self.id_after is not None:
            self.ventana.after_cancel(self.id_after)
            self.id_after = None

        self._actualizar_estado("Impresión pausada")
        self._registrar("Impresión pausada. Presione Iniciar / Reanudar para continuar.")

    def _avanzar_simulacion(self):
        # Si la simulación no esta activa o esta en pausa no hace nada
        if not self.simulacion_activa or self.en_pausa:
            return
        # Usamos uno de los metodos de documento.py para ir sacando los objetos de la cola
        # Ahi los agregamos a documento actual
        if self.documento_actual is None:
            self.documento_actual = self.cola.retirar_documento()
            # Cuando se terminen, saca la lista vacia y termina la simulación
            if self.documento_actual is None:
                self._finalizar_simulacion()
                return
            # Empieza el condator en 0 e inicia la impresion digamos
            self.pagina_actual = 0
            self.pagina_en_proceso = False
            self._registrar(
                f"Iniciando impresión de '{self.documento_actual.nombre}'."
            )
            # Luego de eso se actualiza la lista de la cola visible 
            # (osea la que tiene la barrita para subir y bajar)
            self._actualizar_cola_visible()
            self.barra_progreso.configure(
                maximum=self.documento_actual.numero_paginas, value=0
            )
        # Si ya esta en proceso va acumulando las paginas 
        if not self.pagina_en_proceso:
            self.pagina_actual += 1
            self.pagina_en_proceso = True
            self._registrar(
                f"Imprimiendo página {self.pagina_actual} de "
                f"{self.documento_actual.numero_paginas}: "
                f"{self.documento_actual.nombre}"
            )

        self._actualizar_panel_documento()

        milisegundos = max(
            1, round(self.documento_actual.tiempo_por_pagina * 1000)
        )
        self.id_after = self.ventana.after(milisegundos, self._terminar_pagina)

    def _terminar_pagina(self):
        # se indica que ya termino
        self.id_after = None
        # Comprobar si se puede continuar
        if not self.simulacion_activa or self.en_pausa:
            return

        self.pagina_en_proceso = False
        self.barra_progreso.configure(value=self.pagina_actual)

        if self.pagina_actual >= self.documento_actual.numero_paginas:
            self._registrar(
                f"Documento terminado: '{self.documento_actual.nombre}'."
            )
            self.documento_actual = None
            self.pagina_actual = 0

        self._avanzar_simulacion()

    def _finalizar_simulacion(self):
        self.simulacion_activa = False
        self.en_pausa = False
        self.documento_actual = None
        self.pagina_actual = 0
        self.pagina_en_proceso = False
        self.id_after = None
        self.barra_progreso.configure(value=0)
        self.etiqueta_documento_actual.configure(text="Documento actual: ninguno")
        self.etiqueta_pagina.configure(text="Página: -")
        self._actualizar_estado("Cola vacía - impresión finalizada")
        self._registrar("Todos los documentos fueron impresos.")

    def _actualizar_panel_documento(self):
        documento = self.documento_actual
        self.etiqueta_documento_actual.configure(
            text=f"Documento actual: {documento.nombre}"
        )
        self.etiqueta_pagina.configure(
            text=f"Página: {self.pagina_actual} de {documento.numero_paginas}"
        )
        self.barra_progreso.configure(value=max(0, self.pagina_actual - 1))
        self._actualizar_estado("Imprimiendo")

    def _actualizar_cola_visible(self):
        self.lista_cola.delete(0, tk.END)

        for posicion, documento in enumerate(
            self.cola.obtener_documentos(), start=1
        ):
            self.lista_cola.insert(tk.END, f"{posicion}. {documento}")

        cantidad = self.cola.cantidad()
        self.etiqueta_cantidad.configure(text=f"{cantidad} documento(s)")

    def _actualizar_estado(self, mensaje):
        self.etiqueta_estado.configure(text=f"Estado: {mensaje}")

    def _registrar(self, mensaje):
        self.texto_historial.configure(state="normal")
        self.texto_historial.insert(tk.END, f"• {mensaje}\n")
        self.texto_historial.see(tk.END)
        self.texto_historial.configure(state="disabled")

    def limpiar_historial(self):
        self.texto_historial.configure(state="normal")
        self.texto_historial.delete("1.0", tk.END)
        self.texto_historial.configure(state="disabled")

    def cerrar_aplicacion(self):
        if self.id_after is not None:
            self.ventana.after_cancel(self.id_after)
        self.ventana.destroy()
