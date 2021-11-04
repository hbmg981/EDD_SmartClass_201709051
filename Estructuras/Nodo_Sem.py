from Estructuras.Arbol_B import BTree
class NodoSem:
    def __init__(self, carnet,año,semestre):
        self.carnet = carnet
        self.año = año
        self.semestre = semestre
        self.next = None
        self.prev = None
        #self.cursos = arbolB
