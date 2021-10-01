from Estructuras.Arbol_B.NodoDoble import NodoDoble

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def vacia(self):
        return self.primero is None

    def InsertarNodoD(self, codigo, nombre,creditos,prerequisito,obligatorio):
        NodoD = NodoDoble(codigo, nombre, creditos, prerequisito, obligatorio)
        if self.cuenta < 4:
            if self.vacia():
                self.primero = NodoD
                self.ultimo = self.primero
            else:
                self.ultimo.Siguiente = NodoD
                NodoD.Anterior = self.ultimo
                self.ultimo = NodoD
            self.cuenta += 1
        else:
            print("tamaño superado")


    def InsertarDato(self, codigo, posicion):
        Aux = self.primero
        while posicion!=0:
            posicion -=1
            Aux = Aux.Siguiente
        Aux.codigo = codigo

    def DevolverDato(self, posicion):
        Aux = self.primero
        while posicion!=0:
            posicion -=1
            Aux = Aux.Siguiente
        return Aux

    def MostrarDatos(self):
        Aux = self.primero
        while Aux!=None:
            print("dato: "+Aux.codigo)
            Aux = Aux.Siguiente




