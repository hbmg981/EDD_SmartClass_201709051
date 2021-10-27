from Estructuras.Arbol_B.ListaPuntero import ListaPuntero
from Estructuras.Arbol_B.ListaDoble import ListaDoble

class PaginaB:

    def __init__(self):
        self.cuenta = 0
        self.maxClaves = 0
        self.punteros = ListaPuntero()
        self.datos = ListaDoble()

        for i in range(0,5):
            if i!=4:
                 self.datos.InsertarNodoD(0,"",0,"","")

            self.punteros.InsertarPuntero(None)
        self.maxClaves = 5

    def paginaLlena(self):
        return self.cuenta == self.maxClaves - 1

    def paginaCasiLlena(self):
        return self.cuenta == self.maxClaves/2

    def getCodigo(self, posicion):
        return self.datos.DevolverDato(posicion).codigo

    def setCodigo(self, posicion, codigo):
        self.datos.InsertarDato(codigo,posicion)

    def getNombre(self, posicion):
        return self.datos.DevolverDato(posicion).nombre

    def setNombre(self, posicion, nombre):
        self.datos.DevolverDato(posicion).nombre = nombre

    def getCreditos(self, posicion):
        return self.datos.DevolverDato(posicion).creditos

    def setCreditos(self, posicion, creditos):
        self.datos.DevolverDato(posicion).creditos = creditos

    def getPrerequisito(self, posicion):
        return self.datos.DevolverDato(posicion).prerequisito

    def setPrerequisito(self, posicion,prerequisito ):
        self.datos.DevolverDato(posicion).prerequisito = prerequisito

    def getObligatorio(self, posicion):
        return self.datos.DevolverDato(posicion).obligatorio

    def setObligatorio(self, posicion,obligatorio ):
        self.datos.DevolverDato(posicion).obligatorio = obligatorio

    def getApuntador(self, posicion):
        return self.punteros.DevolverPuntero(posicion).puntero

    def setApuntador(self, posicion,puntero):
        self.punteros.InsertarPunteroP(puntero,posicion)

