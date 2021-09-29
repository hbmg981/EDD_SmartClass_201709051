from Estructuras.Nodo_Año import NodoA

class ListaA:

    def __init__(self):
        self.First = None
        self.Last = None

    def getSize(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.Next()

        return counter

    def buscar(self, año):
        temp = self.First
        while(temp != None and temp.año != año):
            temp = temp.Next
        print("Se encontro el año: " + str(temp.año))
        return  temp != None

    def buscarRetornar(self, año):
        temp = self.First
        while(temp!=None and temp.año!=año):
            temp = temp.Next
        return temp


    def isEmpty(self):
        return self.First is None

    def getList(self):
        aux = self.First
        while aux is not None:
            print(aux.año)
            aux = aux.Next

    def getListRev(self):
        aux = self.Last
        while aux is not None:
            print(aux.año)
            aux = aux.Previous

    def insertValue(self, año):
        new_node = NodoA(año)

        if self.isEmpty():
            self.Last = new_node
            self.First = self.Last
        else:
            self.Last.Next = new_node
            new_node.Previous = self.Last
            self.Last = new_node
