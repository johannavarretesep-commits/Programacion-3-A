from tarea import Tarea


class PilaTareas:
    # Lista vacia
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, tarea):
        # usamos append
        self._tareas.append(tarea)

    def retirar_tarea(self):
        if self.esta_vacia():
            return None
        # pop() sin índice retira y devuelve el último elemento.
        return self._tareas.pop()
    # Ver cual esta arriba
    def ver_cima(self):
        if self.esta_vacia():
            return None
        # Primer elemento -1 osea el ultimo
        return self._tareas[-1]
    # Verificar si esta vacia
    def esta_vacia(self):
        return len(self._tareas) == 0
    # Verificar cantidad
    def cantidad(self):
        return len(self._tareas)
    
    def obtener_tareas(self):
        # Copia de la colección, de cima a base, para mostrarla en pantalla.
        # Los objetos Tarea que contiene siguen siendo los mismos.
        return list(reversed(self._tareas))
