from Estructuras.Arbol_B.PaginaB import PaginaB

class BTree:
    Raiz = PaginaB()
    codigo = 0
    nombre = ""
    obligario = ""
    prerequisitos = ""
    creditos = 0

    aux2 = paginaB()
    aux1 = False
    subeArriba= False
    estado = False
    comparador = False

    grafica = ""
    grafica2 = ""
    codigo1 = 0
    nombre1 = ""
    nodos = 0

    def Vacio(self,raiz):
        return (raiz ==null || raiz.cuenta == 0)

    def InsertarDatos(self, codigo, nombre, creditos,prerequisito,obligatorio):
            InsertarDatos2(self.Raiz, codigo, nombre, creditos, prerequisito,obligatorio)

    def InsertarDatos2(self, raiz,codigo, nombre, creditos, prerequisito,obligatorio):
        Empujar(raiz,codigo, nombre, creditos, prerequisito,obligatorio)
        if self.subeArriba:
            self.Raiz = PaginaB()
            self.Raiz.cuenta=1
            self.Raiz.codigo = self.codigo





