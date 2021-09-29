from Estructuras.Lista_simple import ListaSimple

class NodoMatriz:
    def __init__(self, dia=None, hora = None, ntareas= None,arriba=None,abajo=None,izquierda=None,derecha=None):
        self.dia=dia
        self.hora=hora
        self.ntareas=ntareas
        self.arriba=arriba
        self.abajo=abajo
        self.izquierda= izquierda
        self.derecha = derecha
        self.lista = ListaSimple()
        self.cont = 0

class NodoCabecera:
    def __init__(self,tipo=None,indice=None,siguiente=None,derecha=None,abajo=None):
        self.tipo=tipo
        self.indice=indice
        self.siguiente=siguiente
        self.derecha=derecha
        self.abajo=abajo
class NodoRaiz:
    def __init__(self):
        self.NodoFilas=None
        self.NodoColumnas=None
