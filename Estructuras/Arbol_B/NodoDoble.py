

class NodoDoble:
    def __init__(self, codigo, nombre,creditos,prerequisito,obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.prerequisito = prerequisito
        self.obligatorio = obligatorio
        self.Siguiente = None
        self.Anterior = None