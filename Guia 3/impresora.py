
# Esto sirve para quitar y colocar cosas en los extremos
from collections import deque
from Documento import Documento


    # Ahora creamos la clase ColaImpresion, esta servira para ordenarlos y eso
class ColaImpresion:


    def __init__(self):
        # Creamos una cola vacia
        self._documentos = deque()
    # Funcion para agregar un documento
    def agregar_documento(self, documento):
        # Verificar si el objeto si es un documento
        if not isinstance(documento, Documento):
            raise TypeError("Solo se pueden agregar objetos de tipo Documento.")
        # Agrega el documento a la lista
        self._documentos.append(documento)
    # Lo mismo que la de antes pero para quitar documentos en vez de ponerlos
    # Retira el primero que entro a la lista, cosa importante
    def retirar_documento(self):
        # Primero preguntamos si la lista esta vacia, en ese caso no se quita nada ps porq no hay nada
        if self.esta_vacia():
            return None
        # Ahora si quitamos el ultimo documento con el .popleft()
        return self._documentos.popleft()
    # Ahora creamos una nueva función para poder consultar cual es el primer documento en la lista
    def ver_primero(self):
        # Otra vez lo de la lista vacia
        if self.esta_vacia():
            return None
        # Ahora si mostramos el documento que esta de primeras
        return self._documentos[0]
    # Nueva para ver si esta vacia la lista
    def esta_vacia(self):
        return len(self._documentos) == 0
    # Cantidad de documentos en cola
    def cantidad(self):
        return len(self._documentos)

    def obtener_documentos(self):
        # Devuelve una copia para evitar modificar la cola desde la interfaz.
        return list(self._documentos)
