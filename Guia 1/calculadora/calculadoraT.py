# Esto simplemente llama librerias de python, en este caso una relacionada a operaciones matematicas
import math


# En esta siguiente linea creamos una clase llamada calculadorab, (la profe dijo que tenia que llamarse igual
# Que el archivo)
# La clase es algo general como decir computadores
class CALCULADORAT:

    
    # constructor, el constructor tiene atributos dentro que van en la calculadora 
    # (son como decir combustible, bateria, señal, etc)
    # El self luego se reemplaza por el objeto, por eso es que esta ahi

    def __init__(self, ANGULO, RESULTADO ):

    # Realmente no tengo idea de que y porque se hace lo de las siguientes lineas:
    # Solo recuerdo que no necesariamente lo que va despues del igual tiene que ser lo de arriba pero se pone
    # Por comodidad

        self.ANGULO = ANGULO
        self.RESULTADO = RESULTADO

        # FUNCIONES, Estos son los Metodos, realmente son funciones en escencia pero ligadas a la clase

    def SENO (self):
            self.RESULTADO = math.sin(self.ANGULO)
            print (self.RESULTADO)
    def COSENO (self):
                self.RESULTADO = math.cos(self.ANGULO)
                print (self.RESULTADO)
    def TANGENTE (self):
                self.RESULTADO = math.tan(self.ANGULO)
                print (self.RESULTADO)

def OperacionesTrigonometricas():

    print (" LA CALCULEISHON PARA HACER CALCULOS CALCULADOS CALCULADAMENTE")
    MICALCULADORA = CALCULADORAT (0,0)
    OPERACION =  int(input("""
    * 1. SENO
    * 2. COSENO
    * 3. TANGENTE
    """))

    if OPERACION == 1: 
            RESULTADO = 0
            TERMINAR = False
            while TERMINAR == False:
                   
                MICALCULADORA.ANGULO = input("Número (o = para terminar) ")
                if MICALCULADORA.ANGULO == "=":
                                       TERMINAR = True
                else:
                    MICALCULADORA.ANGULO = float (MICALCULADORA.ANGULO)
                    MICALCULADORA.SENO()
                    RESULTADO = MICALCULADORA.RESULTADO
                    print("Resultado Actual", RESULTADO)
            print("Resultado Final:", RESULTADO)

    elif OPERACION == 2: 
            RESULTADO = 0
            TERMINAR = False
            while TERMINAR == False:
                   
                MICALCULADORA.ANGULO = input("Número (o = para terminar) ")
                if MICALCULADORA.ANGULO == "=":
                                       TERMINAR = True
                else:
                    MICALCULADORA.ANGULO = float (MICALCULADORA.ANGULO)
                    MICALCULADORA.COSENO()
                    RESULTADO = MICALCULADORA.RESULTADO
                    print("Resultado Actual", RESULTADO)
            print("Resultado Final:", RESULTADO)
    
    elif OPERACION == 3: 
            RESULTADO = 0
            TERMINAR = False
            while TERMINAR == False:
                   
                MICALCULADORA.ANGULO = input("Número (o = para terminar) ")
                if MICALCULADORA.ANGULO == "=":
                                       TERMINAR = True
                else:
                    MICALCULADORA.ANGULO = float (MICALCULADORA.ANGULO)
                    MICALCULADORA.TANGENTE()
                    RESULTADO = MICALCULADORA.RESULTADO
                    print("Resultado Actual", RESULTADO)
            print("Resultado Final:", RESULTADO)

