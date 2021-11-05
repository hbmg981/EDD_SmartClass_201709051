from Estructuras.Arbol_B.BTree import BTree
class NodoSem:
    def __init__(self, carnet,año,semestre):
        self.carnet = carnet
        self.año = año
        self.semestre = semestre
        self.bt= BTree()
        self.next = None
        self.prev = None
        self.arbol = BTree()
        #self.cursos = arbolB
