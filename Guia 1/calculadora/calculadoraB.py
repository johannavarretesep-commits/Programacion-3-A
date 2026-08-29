# Esto simplemente llama librerias de python, en este caso una relacionada a operaciones matematicas
import math


# En esta siguiente linea creamos una clase llamada calculadorab, (la profe dijo que tenia que llamarse igual
# Que el archivo)
# La clase es algo general como decir computadores
class CALCULADORAB:

    
    # constructor, el constructor tiene atributos dentro que van en la calculadora 
    # (son como decir combustible, bateria, señal, etc)
    # El self luego se reemplaza por el objeto, por eso es que esta ahi

    def __init__(self, NUMERO1, NUMERO2, RESULTADO ):

    # Realmente no tengo idea de que y porque se hace lo de las siguientes lineas:
    # Solo recuerdo que no necesariamente lo que va despues del igual tiene que ser lo de arriba pero se pone
    # Por comodidad

        self.NUMERO1 = NUMERO1
        self.NUMERO2 = NUMERO2
        self.RESULTADO = RESULTADO

        # FUNCIONES, Estos son los Metodos, realmente son funciones en escencia pero ligadas a la clase

    def SUMA (self):
        self.RESULTADO = self.NUMERO1 + self.NUMERO2
    def RESTA (self):
        self.RESULTADO = self.NUMERO1 - self.NUMERO2
    def MULTIPLICACION (self):
        self.RESULTADO = self.NUMERO1 * self.NUMERO2 
    def DIVISION (self):
            self.RESULTADO = self.NUMERO1 / self.NUMERO2 
    
def OperacionesBasicas():

    print (" LA CALCULEISHON PARA HACER CALCULOS CALCULADOS CALCULADAMENTE")
    MICALCULADORA = CALCULADORAB (0,0,0)
    OPERACION =  int(input("""
    * 1. SUMA
    * 2. RESTA
    * 3. Multiplicación
    * 4. División
    """))

    if OPERACION == 1: 
        RESULTADO = 0
        MICALCULADORA.NUMERO1 = float (input("Número: "))
        MICALCULADORA.NUMERO2 = float (input("Número: "))
        MICALCULADORA.SUMA()
        RESULTADO = MICALCULADORA.RESULTADO
        print ("Resultado actual: ",RESULTADO)
        CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")

        while CONTINUAR != "=":

            MICALCULADORA.NUMERO1 = RESULTADO
            MICALCULADORA.NUMERO2 = float(CONTINUAR)

            MICALCULADORA.SUMA()

            RESULTADO = MICALCULADORA.RESULTADO

            print("Resultado actual:", RESULTADO)

            CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")

        print("Resultado Final:", RESULTADO)

    elif OPERACION == 2: 
            RESULTADO = 0
            MICALCULADORA.NUMERO1 = float (input("Número: "))
            MICALCULADORA.NUMERO2 = float (input("Número: "))
            MICALCULADORA.RESTA()
            RESULTADO = MICALCULADORA.RESULTADO
            print ("Resultado actual: ",RESULTADO)
            CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")
    
            while CONTINUAR != "=":
    
                MICALCULADORA.NUMERO1 = RESULTADO
                MICALCULADORA.NUMERO2 = float(CONTINUAR)
    
                MICALCULADORA.RESTA()
    
                RESULTADO = MICALCULADORA.RESULTADO
    
                print("Resultado actual:", RESULTADO)
    
                CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")
    
            print("Resultado Final:", RESULTADO)
    
    elif OPERACION == 3: 
                RESULTADO = 0
                MICALCULADORA.NUMERO1 = float (input("Número: "))
                MICALCULADORA.NUMERO2 = float (input("Número: "))
                MICALCULADORA.MULTIPLICACION()
                RESULTADO = MICALCULADORA.RESULTADO
                print ("Resultado actual: ",RESULTADO)
                CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")
        
                while CONTINUAR != "=":
        
                    MICALCULADORA.NUMERO1 = RESULTADO
                    MICALCULADORA.NUMERO2 = float(CONTINUAR)
        
                    MICALCULADORA.MULTIPLICACION()
        
                    RESULTADO = MICALCULADORA.RESULTADO
        
                    print("Resultado actual:", RESULTADO)
        
                    CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")
        
                print("Resultado Final:", RESULTADO)

    elif OPERACION == 4: 
                RESULTADO = 0
                MICALCULADORA.NUMERO1 = float (input("Número: "))
                MICALCULADORA.NUMERO2 = float (input("Número: "))
                MICALCULADORA.DIVISION()
                RESULTADO = MICALCULADORA.RESULTADO
                print ("Resultado actual: ",RESULTADO)
                CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")
        
                while CONTINUAR != "=":
        
                    MICALCULADORA.NUMERO1 = RESULTADO
                    MICALCULADORA.NUMERO2 = float(CONTINUAR)
        
                    MICALCULADORA.DIVISION()
        
                    RESULTADO = MICALCULADORA.RESULTADO
        
                    print("Resultado actual:", RESULTADO)
        
                    CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")
        
                print("Resultado Final:", RESULTADO)
    