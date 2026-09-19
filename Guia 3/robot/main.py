# Otra vez importando cosas
import tkinter as tk

from interfaz_robot import InterfazRobot


def main():
    ventana = tk.Tk()
    # Conservamos una referencia a la interfaz mientras funciona la aplicación.
    aplicacion = InterfazRobot(ventana)
    ventana.mainloop()

# Para que solo se abra cuando se ejecuta main
if __name__ == "__main__":
    main()
