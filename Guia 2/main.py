# Importamos librerias
import math
import random
# Importamos otros archivos
from ordenamientos import Ordenamientos
from matrices import Matrices

# Crear funcion principal
def main():
    # Mensaje de Bienvenida
    print("Iniciando Calculadora de matrices...")
    print("Bienvenido Usuari@")

    OPERACION = 0
    while OPERACION != 3:

        OPERACION = int(input("""
        ¿Qué tipo de operación desea realizar?

        1. Operaciones con matrices
        2. Algoritmos de ordenamiento
        3. Salir
        """))

        if OPERACION == 1:
            METODO_MATRIZ = 0

            while METODO_MATRIZ != 5:

                METODO_MATRIZ = int(input("""
            ----- OPERACIONES CON MATRICES -----

            1. Suma de matrices
            2. Producto de matrices
            3. Inversa de una matriz
            4. Producto matriz por vector
            5. Volver

            Seleccione una opción: """))

                if METODO_MATRIZ == 1:

                    print("\n----- SUMA DE MATRICES -----")

                    FILAS = int(input("Digite el número de filas: "))
                    COLUMNAS = int(input("Digite el número de columnas: "))
                    print("\nIngrese los elementos de la matriz A:")

                    MATRIZA = []

                    for i in range(FILAS):

                        FILA = []

                        for j in range(COLUMNAS):

                            NUMERO = float(input(f"Digite A[{i}][{j}]: "))
                            FILA.append(NUMERO)

                        MATRIZA.append(FILA)
                    print("\nIngrese los elementos de la matriz B:")
                    MATRIZB = []

                    for i in range(FILAS):
                        FILA = []
                        for j in range(COLUMNAS):
                            NUMERO = float(input(f"Digite B[{i}][{j}]: "))
                            FILA.append(NUMERO)
                        MATRIZB.append(FILA)
                    # Creamos el objeto
                    SUMA = Matrices(MATRIZA, MATRIZB)
                    # Ejecutamos el método
                    SUMA.suma()
                    # Obtenemos el resultado mediante el get
                    RESULTADO = SUMA.get_resultado()

                    print("\nMatriz A:")
                    print(MATRIZA)
                    print("\nMatriz B:")
                    print(MATRIZB)
                    print("\nResultado de la suma:")
                    print(RESULTADO)
                elif METODO_MATRIZ == 2:

                    print("\n----- PRODUCTO DE MATRICES -----")

                    # Dimensiones de A
                    FILASA = int(input("Digite el número de filas de A: "))
                    COLUMNASA = int(input("Digite el número de columnas de A: "))

                    # Dimensiones de B
                    FILASB = int(input("Digite el número de filas de B: "))
                    COLUMNASB = int(input("Digite el número de columnas de B: "))

                    # MATRIZ A
                    MATRIZA = []

                    print("\nIngrese los elementos de la matriz A:")

                    for i in range(FILASA):

                        FILA = []

                        for j in range(COLUMNASA):

                            NUMERO = float(input(f"Digite A[{i}][{j}]: "))
                            FILA.append(NUMERO)

                        MATRIZA.append(FILA)

                    # MATRIZ B
                    MATRIZB = []

                    print("\nIngrese los elementos de la matriz B:")

                    for i in range(FILASB):

                        FILA = []

                        for j in range(COLUMNASB):

                            NUMERO = float(input(f"Digite B[{i}][{j}]: "))
                            FILA.append(NUMERO)

                        MATRIZB.append(FILA)

                    # Creamos objeto
                    PRODUCTO = Matrices(MATRIZA, MATRIZB)

                    # Ejecutamos operación
                    PRODUCTO.producto()

                    RESULTADO = PRODUCTO.get_resultado()

                    if RESULTADO == None:

                        print("\nNo se pueden multiplicar las matrices.")
                        print("Las columnas de A deben ser iguales a las filas de B.")

                    else:

                        print("\nResultado del producto:")
                        print(RESULTADO)
                elif METODO_MATRIZ == 3:

                    print("\n----- INVERSA DE UNA MATRIZ -----")

                    N = int(input("Digite el tamaño de la matriz cuadrada: "))

                    MATRIZA = []

                    print("\nIngrese los elementos de la matriz:")

                    for i in range(N):

                        FILA = []

                        for j in range(N):

                            NUMERO = float(input(f"Digite A[{i}][{j}]: "))
                            FILA.append(NUMERO)

                        MATRIZA.append(FILA)

                    # Para inversa solamente necesitamos MATRIZA
                    INVERSA = Matrices(MATRIZA)

                    INVERSA.inversa()

                    RESULTADO = INVERSA.get_resultado()

                    if RESULTADO == None:

                        print("\nLa matriz no tiene inversa.")

                    else:

                        print("\nMatriz inversa:")
                        print(RESULTADO)
                elif METODO_MATRIZ == 4:

                    print("\n----- PRODUCTO MATRIZ POR VECTOR -----")

                    FILAS = int(input("Digite el número de filas de la matriz: "))
                    COLUMNAS = int(input("Digite el número de columnas de la matriz: "))

                    # MATRIZ
                    MATRIZA = []

                    print("\nIngrese los elementos de la matriz:")

                    for i in range(FILAS):

                        FILA = []

                        for j in range(COLUMNAS):

                            NUMERO = float(input(f"Digite A[{i}][{j}]: "))
                            FILA.append(NUMERO)

                        MATRIZA.append(FILA)

                    # VECTOR
                    VECTOR = []

                    print("\nIngrese los elementos del vector:")

                    # El vector debe tener tantos elementos
                    # como columnas tenga la matriz
                    for i in range(COLUMNAS):

                        NUMERO = float(input(f"Digite VECTOR[{i}]: "))
                        VECTOR.append(NUMERO)

                    # Creamos objeto
                    PRODUCTO_VECTOR = Matrices(MATRIZA, None, VECTOR)

                    PRODUCTO_VECTOR.producto_vector()

                    RESULTADO = PRODUCTO_VECTOR.get_resultado()

                    if RESULTADO == None:

                        print("\nNo es posible realizar el producto.")

                    else:

                        print("\nResultado matriz por vector:")
                        print(RESULTADO)

           
        elif OPERACION ==2:
            CANTIDAD = int(input ("Digite la cantidad de números que desea en la lista: "))

            # CREACIÓN DE LA LISTA

            # Creando lista vacia
            LISTA =[]
            # Ciclo que repite CANTIDAD veces lo que esta dentro del for (contando de 0 a CANTIDAD-1)
            for i in range(CANTIDAD):
                # Agregamos en la ultima posición de la lista un número aleatorio entre 1.0 y 100000.0 (incluyendolos a ellos)
                LISTA.append(random.uniform(1.0,100000.0))
            # imprimimos la lista generada por el ciclo
            print("Lista generada:",LISTA)
            # Creamos un objeto por cada metodo de ordenamiento y se le asigna una copia original de la lista
            BURBUJA = Ordenamientos(LISTA.copy())
            SELECCION = Ordenamientos(LISTA.copy())
            INSERCION = Ordenamientos(LISTA.copy())
            MERGE_SORT = Ordenamientos(LISTA.copy())
            SORT_PYTHON = Ordenamientos(LISTA.copy())
        

            METODO = 0
            while METODO != 6:
                METODO = int(input ("""----- ALGORITMOS DE ORDENAMIENTO -----
                        Seleccione el algoritmo de ordenamiento que desea utilizar:

                        1. Método burbuja
                        2. Método selección
                        3. Método inserción
                        4. Merge Sort
                        5. Sort de Python
                        6. Terminar

        """))
                if METODO == 1:
                    BURBUJA.burbuja()
                    print(BURBUJA.get_resultado())

                elif METODO == 2:
                    SELECCION.seleccion()
                    print(SELECCION.get_resultado())
                elif METODO == 3:
                    INSERCION.insercion()
                    print(INSERCION.get_resultado())
                elif METODO == 4:
                    MERGE_SORT.merge_sort()
                    print(MERGE_SORT.get_resultado())
                elif METODO == 5:
                    SORT_PYTHON.python_sort()
                    print(SORT_PYTHON.get_resultado())
        
main()

