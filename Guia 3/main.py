# Importar COZAZ
# Cosas para crear las ventanas y se le pone el prefijo tk, se le pone tk como podria colocarse JabonJudio
import tkinter as tk

from interfaz_impresion import InterfazImpresion

# Funcion Principal main

def main():
    # Crear ventana
    ventana = tk.Tk()
    # Construimos nuestra interfaz dentro de esa ventana
    InterfazImpresion(ventana)
    # botones, teclado y temporizadores
    ventana.mainloop()

# Para que solo se inicie la aplicación desde el main colocamos:

if __name__ == "__main__":
    main()
