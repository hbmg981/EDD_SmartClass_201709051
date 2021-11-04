
class Nodo:
    def __init__(self, codigo):
        self.codigo = codigo
        self.Next = None
        self.Previous = None


class NodoG:
    def __init__(self, codigo,nombre,creditos, lista):
        self.creditos = creditos
        self.nombre=nombre
        self.codigo = codigo
        self.lista = lista
        self.Next = None
        self.Previous = None