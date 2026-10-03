# Importamos Tkinter con el nombre corto tk para crear la ventana.
import tkinter as tk
# Importamos nuestra clase que construye los controles y organiza la carrera.
from interfaz import InterfazCarrera


# Esta función es el punto de inicio de la aplicación.
def main():
    # Creamos una única ventana principal.
    ventana = tk.Tk()
    # Construimos la interfaz dentro de esa ventana.
    aplicacion = InterfazCarrera(ventana)
    # Atendemos clics, dibujos y los diez temporizadores hasta cerrar la ventana.
    ventana.mainloop()


# Solo iniciamos el programa al ejecutar este archivo directamente.
if __name__ == "__main__":
    # Llamamos a la función que abre la aplicación.
    main()
