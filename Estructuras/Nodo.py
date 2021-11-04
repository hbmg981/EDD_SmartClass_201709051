
class Nodo:
    def __init__(self, codigo):
        self.codigo = codigo
        self.Next = None
        self.Previous = None


class NodoG:
    def __init__(self, codigo,nombre,creditos,prerequisitos, obligatorio, lista):
        self.creditos = creditos
        self.nombre=nombre
        self.codigo = codigo
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio
        self.lista = lista
        self.Next = None
        self.Previous = None