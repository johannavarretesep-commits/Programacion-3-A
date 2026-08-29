# Esto simplemente llama librerias de python, en este caso una relacionada a operaciones matematicas
import math


# En esta siguiente linea creamos una clase llamada calculadorab, (la profe dijo que tenia que llamarse igual
# Que el archivo)
# La clase es algo general como decir computadores
class CALCULADORAE:

    
    # constructor, el constructor tiene atributos dentro que van en la calculadora 
    # (son como decir combustible, bateria, señal, etc)
    # El self luego se reemplaza por el objeto, por eso es que esta ahi

    def __init__(self, NUMERO, NUMERO2, RESULTADO ):

    # Realmente no tengo idea de que y porque se hace lo de las siguientes lineas:
    # Solo recuerdo que no necesariamente lo que va despues del igual tiene que ser lo de arriba pero se pone
    # Por comodidad

        self.NUMERO = NUMERO
        self.NUMERO2 = NUMERO2
        self.RESULTADO = RESULTADO

        # FUNCIONES, Estos son los Metodos, realmente son funciones en escencia pero ligadas a la clase

    def RAIZ(self):
        self.RESULTADO = math.sqrt(self.NUMERO)
    def POTENCIA(self):
        self.RESULTADO = math.pow(self.NUMERO , self.NUMERO2)


    def FACTORIAL(self):
        self.RESULTADO = 1
        if self.NUMERO.is_integer():
            print ("Solo se aceptan números enteros para una operación factorial.")
        while (self.NUMERO>0):
            self.RESULTADO = self.RESULTADO * self.NUMERO
            self.NUMERO = self.NUMERO - 1
    def FIBONACCI(self):
        self.RESULTADO = 0
        if self.NUMERO.is_integer():
            print ("Solo se aceptan números enteros para una serie Fibonacci")
        b= 0
        c= 1
        i = 2
        while (i<=self.NUMERO):
            self.RESULTADO = b + c
            b = c
            c = self.RESULTADO
            i = i+1
        self.RESULTADO = c

    def MCD(self):

        RESULTADO  = 1
        if not self.NUMERO.is_integer() and not self.NUMERO2.is_integer():
            print ("Solo se aceptan números enteros para una operación de Máximo Común Divisor")
        while (RESULTADO > 0):
            if self.NUMERO== 0 and self.NUMERO2 == 0:
                RESULTADO = 0 
                print ("Error Matematico")
            elif self.NUMERO== 0 or self.NUMERO2 == 0:
                if self.NUMERO== 0:
                    self.RESULTADO = self.NUMERO2
                else:
                    self.RESULTADO = self.NUMERO
                RESULTADO = 0
            elif self.NUMERO > self.NUMERO2:
                RESULTADO = self.NUMERO % self.NUMERO2
                self.NUMERO = self.NUMERO2
                self.NUMERO2 = RESULTADO
                if RESULTADO > 0:
                    self.RESULTADO = RESULTADO
            elif self.NUMERO < self.NUMERO2:
                RESULTADO = self.NUMERO2 % self.NUMERO
                self.NUMERO2 = self.NUMERO
                self.NUMERO = RESULTADO
                if RESULTADO > 0:
                    self.RESULTADO = RESULTADO
            else:
                self.RESULTADO = self.NUMERO
                RESULTADO = 0
    def MCM(self):
        mcd = 0
        num_orig1 = abs(self.NUMERO)
        num_orig2 = abs(self.NUMERO2)

        RESULTADO  = 1
        if not self.NUMERO.is_integer() and not self.NUMERO2.is_integer():
            print ("Solo se aceptan números enteros para una operación de Máximo Común Divisor")
        while (RESULTADO > 0):
            if self.NUMERO== 0 and self.NUMERO2 == 0:
                RESULTADO = 0 
                print ("Error Matematico")
            elif self.NUMERO== 0 or self.NUMERO2 == 0:
                if self.NUMERO== 0:
                    self.RESULTADO = self.NUMERO2
                else:
                    self.RESULTADO = self.NUMERO
                RESULTADO = 0
            elif self.NUMERO > self.NUMERO2:
                RESULTADO = self.NUMERO % self.NUMERO2
                self.NUMERO = self.NUMERO2
                self.NUMERO2 = RESULTADO
                if RESULTADO > 0:
                    self.RESULTADO = RESULTADO
            elif self.NUMERO < self.NUMERO2:
                RESULTADO = self.NUMERO2 % self.NUMERO
                self.NUMERO2 = self.NUMERO
                self.NUMERO = RESULTADO
                if RESULTADO > 0:
                    self.RESULTADO = RESULTADO
            else:
                self.RESULTADO = self.NUMERO
                RESULTADO = 0
        if num_orig1 > 0 and num_orig2 > 0:
            mcd = self.RESULTADO
            self.RESULTADO = (num_orig1 * num_orig2) // mcd
        

    def IVA(self):
         self.RESULTADO = self.NUMERO * 0.19
    def ERROR():
         print ("Error")


def OperacionesEspeciales():

    print (" LA CALCULEISHON PARA HACER CALCULOS CALCULADOS CALCULADAMENTE")
    MICALCULADORA = CALCULADORAE (0,0,0)
    OPERACION =  int(input("""
    * 1. Raíz
    * 2. Potencia
    * 3. Factorial
    * 4. Fibonacci
    * 5. Maximo Comun Divisor
    * 6. Minimo Comun Multiplo
    * 7. IVA
    """))

    if OPERACION == 1: 
            RESULTADO = 0
            TERMINAR = False
            while TERMINAR == False:
                   
                MICALCULADORA.NUMERO = input("Número (o = para terminar) ")
                if MICALCULADORA.NUMERO == "=":
                                       TERMINAR = True
                else:
                    MICALCULADORA.NUMERO = float (MICALCULADORA.NUMERO)
                    MICALCULADORA.RAIZ()
                    RESULTADO = MICALCULADORA.RESULTADO
                    print("Resultado Actual", RESULTADO)
            print("Resultado Final:", RESULTADO)
    elif OPERACION == 2: 
                RESULTADO = 0
                TERMINAR = False
                while TERMINAR == False:
                       
                    MICALCULADORA.NUMERO = input("Número (o = para terminar) ")
                    
                    if MICALCULADORA.NUMERO == "=":
                                           TERMINAR = True
                    else:
                        MICALCULADORA.NUMERO = float (MICALCULADORA.NUMERO)
                        MICALCULADORA.NUMERO2 = float(input("Ingrese Exponente: "))
                        MICALCULADORA.POTENCIA()
                        RESULTADO = MICALCULADORA.RESULTADO
                        print("Resultado Actual", RESULTADO)
                print("Resultado Final:", RESULTADO)

    elif OPERACION == 3: 
                RESULTADO = 0
                TERMINAR = False
                while TERMINAR == False:
                       
                    MICALCULADORA.NUMERO = input("Número (o = para terminar) ")
                    if MICALCULADORA.NUMERO == "=":
                                           TERMINAR = True
                    else:
                        MICALCULADORA.NUMERO = float (MICALCULADORA.NUMERO)
                        MICALCULADORA.FACTORIAL()
                        RESULTADO = MICALCULADORA.RESULTADO
                        print("Resultado Actual", RESULTADO)
                print("Resultado Final:", RESULTADO)

    elif OPERACION == 4: 
                RESULTADO = 0
                TERMINAR = False
                while TERMINAR == False:
                       
                    MICALCULADORA.NUMERO = input("Número (o = para terminar) ")
                    if MICALCULADORA.NUMERO == "=":
                                           TERMINAR = True
                    else:
                        MICALCULADORA.NUMERO = float (MICALCULADORA.NUMERO)
                        MICALCULADORA.FIBONACCI()
                        RESULTADO = MICALCULADORA.RESULTADO
                        print("Resultado Actual", RESULTADO)
                print("Resultado Final:", RESULTADO)

    elif OPERACION == 5: 
                RESULTADO = 0
                TERMINAR = False
                while TERMINAR == False:
                       
                    MICALCULADORA.NUMERO = input("Número (o = para terminar) ")
                    
                    if MICALCULADORA.NUMERO == "=":
                                           TERMINAR = True
                    else:
                        MICALCULADORA.NUMERO = float (MICALCULADORA.NUMERO)
                        MICALCULADORA.NUMERO2 = float(input("Ingrese el segundo Número: "))
                        MICALCULADORA.MCD()
                        RESULTADO = MICALCULADORA.RESULTADO
                        print("Resultado Actual", RESULTADO)
                print("Resultado Final:", RESULTADO)

    elif OPERACION == 6: 
                RESULTADO = 0
                TERMINAR = False
                while TERMINAR == False:
                       
                    MICALCULADORA.NUMERO = input("Número (o = para terminar) ")
                    
                    if MICALCULADORA.NUMERO == "=":
                                           TERMINAR = True
                    else:
                        MICALCULADORA.NUMERO = float (MICALCULADORA.NUMERO)
                        MICALCULADORA.NUMERO2 = float(input("Ingrese el segundo Número: "))
                        MICALCULADORA.MCM()
                        RESULTADO = MICALCULADORA.RESULTADO
                        print("Resultado Actual", RESULTADO)
                print("Resultado Final:", RESULTADO)

    if OPERACION == 7: 
            RESULTADO = 0
            TERMINAR = False
            while TERMINAR == False:
                   
                MICALCULADORA.NUMERO = input("Monto (o = para terminar):  ")
                if MICALCULADORA.NUMERO == "=":
                                       TERMINAR = True
                else:
                    MICALCULADORA.NUMERO = float (MICALCULADORA.NUMERO)
                    MICALCULADORA.IVA()
                    RESULTADO = MICALCULADORA.RESULTADO
                    print("Resultado Actual", RESULTADO)
            print("Resultado Final:", RESULTADO)
