# Importamos librerias
import math
import random

class Ordenamientos:

    def __init__(self, LISTA):

        self.LISTA = LISTA

    def burbuja(self):
        # CICLO BURBUJA
        
            # Primer for que hace LISTA veces el recorrido por la lista
            for j in range(len(self.LISTA) - 1):
                # Segundo ciclo que realiza Lista veces comparación e intercambio
                for i in range(len(self.LISTA) - 1):
                    # Comparamos si el valor de la izquierda es mayor al de la derecha
                    if self.LISTA[i] > self.LISTA[i + 1]:
                        # En caso de serlo, se intercambian
                        # A la izquierda del igual, se toman los valores originales que comparamos
                        # Esos valores se asignan de forma contraria a la derecha del igual
                        # De esa forma: (2,3) --> (3,2)
                        self.LISTA[i], self.LISTA[i + 1] = self.LISTA[i + 1], self.LISTA[i]

    def seleccion(self):
        # METODO DE SELECCIÓN
        
            # Empezamos con un ciclo para actualizar el valor minimo (empieza en la posición 0)
            for i in range(len(self.LISTA) - 1):
                # Inicialmente asumimos que el menor es el que esta en la posición 0
                MENOR = i
                # Ciclo de comparación para actualizar el valor menor, empezamos comparando desde la posición 1
                for j in range(i + 1, len(self.LISTA)):
                    # Preguntamos si la posición 1 es menor que la posición 0 inicialmente
                    # En segunda vuelta, preguntamos si la posición 2 es menor al valor actualizado de MENOR
                    if self.LISTA[j] < self.LISTA[MENOR]:
                        # En caso de ser cierta, actualizamos el valor MENOR con el nuevo número
                        MENOR = j
                # De la misma manera que en el ciclo burbuja intercambiamos los valores
                self.LISTA[i], self.LISTA[MENOR] = self.LISTA[MENOR], self.LISTA[i]
            

    def insercion(self):
        # METODO DE INSERCIÓN
        
            # Empezamos con un ciclo que va desde 1 hasta el número de elementos que tiene la lista
            for i in range(1, len(self.LISTA)):
                # Primero asumimos que el el valor de la posición 0 es el menor
                ORDENAR = self.LISTA[i]
                # Para comparar, j es la posición a la izquierda de i (inicialmente posición 1)
                j = i - 1
                # Iniciamos un ciclo while preguntando si el número en la posición j es mayor al valor en posición 0
                while j >= 0 and self.LISTA[j] > ORDENAR:
                    # En caso de serlo, el valor de la posición j se desplaza a la derecha
                    self.LISTA[j + 1] = self.LISTA[j]
                    j = j - 1
                # Insertamos el valor en la posición que le corresponde
                self.LISTA[j + 1] = ORDENAR


    def merge_sort(self):
        # METODO Merge Sort
        
            # Iniciamos una funcion para poder aplicar recursividad
            def merge_sort(LISTA):
                # En caso de que las listas tengan mas de un elemento
                if len(LISTA) > 1:
                    # La parte a la mitad
                    MITAD = len(LISTA) // 2
                    # Crea dos nuevas listas con la mitad derecha e izquierda
                    IZQUIERDA = LISTA[:MITAD]
                    DERECHA = LISTA[MITAD:]
                    # Aqui llega la recursividad, se ejecuta nuevamente la función pero con las 2 mitades de la lista original
                    merge_sort(IZQUIERDA)
                    merge_sort(DERECHA)
        
                    # Ahora se une y ordena
        
                    i = 0
                    j = 0
                    k = 0
        
                    while i < len(IZQUIERDA) and j < len(DERECHA):
        
                        if IZQUIERDA[i] <= DERECHA[j]:
                            LISTA[k] = IZQUIERDA[i]
                            i = i + 1
                        else:
                            LISTA[k] = DERECHA[j]
                            j = j + 1
        
                        k = k + 1
                    # Si quedaron elementos en la lista izquierda
                    while i < len(IZQUIERDA):
                        LISTA[k] = IZQUIERDA[i]
                        i = i + 1
                        k = k + 1
        
                    # Si quedaron elementos en la lista derecha
                    while j < len(DERECHA):
                        LISTA[k] = DERECHA[j]
                        j = j + 1
                        k = k + 1
            # Llamamos la función
            merge_sort(self.LISTA)


    def python_sort(self):
        self.LISTA.sort()

    def get_resultado(self):
        return self.LISTA

    