class Matrices:

    def __init__(self, MATRIZA=None, MATRIZB=None, VECTOR=None):

        self.MATRIZA = MATRIZA
        self.MATRIZB = MATRIZB
        self.VECTOR = VECTOR
        self.RESULTADO = []


    # SUMA DE MATRICES
    def suma(self):

        self.RESULTADO = []

        # Para sumar, ambas matrices deben tener el mismo tamaño
        if len(self.MATRIZA) == len(self.MATRIZB) and len(self.MATRIZA[0]) == len(self.MATRIZB[0]):

            for i in range(len(self.MATRIZA)):

                FILA = []

                for j in range(len(self.MATRIZA[0])):

                    VALOR = self.MATRIZA[i][j] + self.MATRIZB[i][j]

                    FILA.append(VALOR)

                self.RESULTADO.append(FILA)

        else:
            self.RESULTADO = None


    # PRODUCTO DE MATRICES
    def producto(self):

        self.RESULTADO = []

        # Las columnas de A deben ser iguales a las filas de B
        if len(self.MATRIZA[0]) == len(self.MATRIZB):

            # Recorremos las filas de A
            for i in range(len(self.MATRIZA)):

                FILA = []

                # Recorremos las columnas de B
                for j in range(len(self.MATRIZB[0])):

                    SUMA = 0

                    # Multiplicamos fila de A por columna de B
                    for k in range(len(self.MATRIZB)):

                        SUMA = SUMA + self.MATRIZA[i][k] * self.MATRIZB[k][j]

                    FILA.append(SUMA)

                self.RESULTADO.append(FILA)

        else:
            self.RESULTADO = None


    # INVERSA DE UNA MATRIZ
    def inversa(self):

        self.RESULTADO = None

        N = len(self.MATRIZA)

        # Verificamos que sea una matriz cuadrada
        CUADRADA = True

        for FILA in self.MATRIZA:
            if len(FILA) != N:
                CUADRADA = False

        if CUADRADA and N > 0:

            # Creamos la matriz aumentada [A | I]
            AUMENTADA = []

            for i in range(N):

                FILA = self.MATRIZA[i].copy()

                # Agregamos la matriz identidad
                for j in range(N):

                    if i == j:
                        FILA.append(1.0)
                    else:
                        FILA.append(0.0)

                AUMENTADA.append(FILA)

            SINGULAR = False

            # Método de Gauss-Jordan
            for i in range(N):

                # Buscamos un pivote diferente de cero
                FILA_PIVOTE = i

                while FILA_PIVOTE < N and abs(AUMENTADA[FILA_PIVOTE][i]) < 0.000000000001:
                    FILA_PIVOTE = FILA_PIVOTE + 1

                # Si no encontramos pivote, no existe inversa
                if FILA_PIVOTE == N:
                    SINGULAR = True
                    break

                # Intercambiamos filas si es necesario
                if FILA_PIVOTE != i:

                    AUMENTADA[i], AUMENTADA[FILA_PIVOTE] = AUMENTADA[FILA_PIVOTE], AUMENTADA[i]

                # Convertimos el pivote en 1
                PIVOTE = AUMENTADA[i][i]

                for j in range(2 * N):
                    AUMENTADA[i][j] = AUMENTADA[i][j] / PIVOTE

                # Convertimos los demás elementos de la columna en 0
                for k in range(N):

                    if k != i:

                        FACTOR = AUMENTADA[k][i]

                        for j in range(2 * N):

                            AUMENTADA[k][j] = AUMENTADA[k][j] - FACTOR * AUMENTADA[i][j]

            # Extraemos la matriz inversa
            if SINGULAR == False:

                self.RESULTADO = []

                for i in range(N):

                    FILA = []

                    for j in range(N, 2 * N):

                        FILA.append(AUMENTADA[i][j])

                    self.RESULTADO.append(FILA)


    # PRODUCTO MATRIZ POR VECTOR
    def producto_vector(self):

        self.RESULTADO = []

        # El número de columnas debe ser igual
        # a la cantidad de elementos del vector
        if len(self.MATRIZA[0]) == len(self.VECTOR):

            # Recorremos las filas de la matriz
            for i in range(len(self.MATRIZA)):

                SUMA = 0

                # Multiplicamos cada elemento de la fila
                # por el correspondiente elemento del vector
                for j in range(len(self.VECTOR)):

                    SUMA = SUMA + self.MATRIZA[i][j] * self.VECTOR[j]

                self.RESULTADO.append(SUMA)

        else:
            self.RESULTADO = None


    # GET
    def get_resultado(self):

        return self.RESULTADO