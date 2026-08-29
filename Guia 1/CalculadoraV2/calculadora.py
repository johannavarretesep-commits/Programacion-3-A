# Esto simplemente llama librerias de python, en este caso una relacionada a operaciones matematicas
import math


# En esta siguiente linea creamos una clase llamada calculadorab, (la profe dijo que tenia que llamarse igual
# Que el archivo)
# La clase es algo general como decir computadores
class CALCULADORA:

    
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
    def SENO(self,ang):
        self.RESULTADO = math.sin(ang)
    def COSENO(self,ang):
        self.RESULTADO = math.cos(ang)
    def TANGENTE(self,ang):
        self.RESULTADO = math.tan(ang)
    def RAIZ(self, a):
        self.RESULTADO = math.sqrt(a)
    def POTENCIA(self, a):
        self.RESULTADO = math.pow(a)


    def FACTORIAL(self,a):
        self.RESULTADO = 1
        if self.NUMERO1.is_integer() and self.NUMERO2.is_integer():
            print ("Solo se aceptan números enteros para una operación factorial.")
        while (a>0):
            self.RESULTADO = self.RESULTADO * a
            a = a - 1
    def FIBONACCI(self,a):
        self.RESULTADO = 0
        if self.NUMERO1.is_integer() and self.NUMERO2.is_integer():
            print ("Solo se aceptan números enteros para una serie Fibonacci")
        b= 0
        c= 1
        i = 2
        while (i<=a):
            self.RESULTADO = b + c
            b = c
            c = self.RESULTADO
            i = i+1
        self.RESULTADO = c

    def MCD(self):

        RESULTADO  = 1
        if self.NUMERO1.is_integer() and self.NUMERO2.is_integer():
            print ("Solo se aceptan números enteros para una operación de Máximo Común Divisor")
        while (RESULTADO > 0):
            if self.NUMERO1== 0 and self.NUMERO2 == 0:
                RESULTADO = 0 
                print ("Error Matematico")
            elif self.NUMERO1== 0 or self.NUMERO2 == 0:
                if self.NUMERO1== 0:
                    self.RESULTADO = self.NUMERO2
                else:
                    self.RESULTADO = self.NUMERO1
                RESULTADO = 0
            elif self.NUMERO1 > self.NUMERO2:
                RESULTADO = self.NUMERO1 % self.NUMERO2
                self.NUMERO1 = self.NUMERO2
                self.NUMERO2 = RESULTADO
                if RESULTADO > 0:
                    self.RESULTADO = RESULTADO
            elif self.NUMERO1 < self.NUMERO2:
                RESULTADO = self.NUMERO2 % self.NUMERO1
                self.NUMERO2 = self.NUMERO1
                self.NUMERO1 = RESULTADO
                if RESULTADO > 0:
                    self.RESULTADO = RESULTADO
            else:
                self.RESULTADO = self.NUMERO1
                RESULTADO = 0
    def MCM(self):
        if self.NUMERO1.is_integer() and self.NUMERO2.is_integer():
                    print ("Solo se aceptan números enteros para una operación de Máximo Común Divisor")

    def IVA():
    def ERROR():
    
    
def OperacionesBasicas():

    print (" LA CALCULEISHON PARA HACER CALCULOS CALCULADOS CALCULADAMENTE")
    MICALCULADORA = CALCULADORA (0,0,0)

    PrimerNumero = input("Ingrese el primer numero: ")
    CONTINUAR = input("""Ingrese siguiente número y la operación que desea realizar:
                ° + (suma)
                ° - (resta)
                ° * (multiplicación)
                ° / (división)
                

       """)
    
    while CONTINUAR != "+":
    
        MICALCULADORA.NUMERO1 = PrimerNumero
        MICALCULADORA.NUMERO2 = float(CONTINUAR)
    
        MICALCULADORA.SUMA()
    
        RESULTADO = MICALCULADORA.RESULTADO
    
        print("Resultado actual:", RESULTADO)
    
        CONTINUAR = input("Ingrese siguiente número (o = para terminar): ")
    
    print("Resultado Final:", RESULTADO)


OperacionesBasicas()

    