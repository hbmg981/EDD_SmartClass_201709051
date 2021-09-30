from Estructuras.Matriz_Dispersa import Matriz_dispersa

class NodoMes:
    def __init__(self, mes):
        self.mes = mes
        self.Next = None
        self.Previous = None
        # Aca van las listas, los punteros hacia la matriz de tareas
        self.tareas = Matriz_dispersa()