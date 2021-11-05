from Estructuras.Nodo_Sem import NodoSem
from Estructuras.Arbol_B.BTree import BTree
import os

class ListaSem:
    conta=1
    def __init__(self):
        self.first = None
        #self.Size = 0

    def getSize(self):
        aux = self.first
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.next
        return counter
    def isEmpty(self):
        return self.first is None


    def Insertar(self,carnet, año, semestre,codigo,nombre, creditos, prerequisito,obligatorio):
        #Nodo = NodoSem(semestre)
        if self.isEmpty():
            Nodo = NodoSem(carnet, año, semestre)
            self.first = Nodo
            if self.obtener(carnet) is not None:
                aux =self.obtener(carnet)
                aux.arbol.InsertarDatos(codigo, nombre, creditos, prerequisito, obligatorio)
        else:
                if self.buscar(carnet) is False:
                    Nodo = NodoSem(carnet,año,semestre)

                    current = self.first
                    while current.next != None:
                        current = current.next
                    current.next= Nodo

                    if self.obtener(carnet) is not None:
                        aux = self.obtener(carnet)
                        aux.arbol.InsertarDatos(codigo, nombre, creditos, prerequisito, obligatorio)
                else:

                    print("El carnet: "+ str(carnet)+" ya existe, entonces buscamos e insertamos los datos")
                    if self.obtener(carnet) is not None:
                        aux = self.obtener(carnet)
                        aux.arbol.InsertarDatos(codigo, nombre, creditos, prerequisito, obligatorio)


        #self.Size +=1

        #return Nodo

    def eliminar(self, semestre):
        aux = self.first
        prev = None
        found = False
        if self.getSize()!=0:
            if self.buscar(semestre):
                while aux != None and found ==False:
                    if aux.semestre == semestre:
                        if prev == None:
                            self.first = aux.next
                            aux.next = None

                        else:
                            prev.next = aux.next
                            aux.next=None
                        found = True
                        prev = aux
                    aux = aux.next
            else:
                print("Elemento: "+str(semestre)+" No encontrado")



    def getList(self):
        aux = self.first
        while aux is not None:
            print("Carnet: "+str(aux.carnet)+" Año :"+aux.año)
            aux = aux.next

    def graficarArbol(self,carnet):
        self.obtener(carnet).arbol.Graficar()


    def buscar(self, carnet):
        temp = self.first
        band = False
        while(temp != None and temp.carnet != carnet):
            if int(temp.carnet) == int(carnet):
                band = True
            temp = temp.next
            #return True
        if band ==True:
            print("Carnet encontrado metodo buscar: "+ str(carnet))
        else:
            print("Carnet no encontrado metodo buscar: " + str(carnet))

        return band

    def Modificar(self, semestre, semestre2):
        actual = self.first
        while actual!=None:
            if actual.semestre == semestre:
                if self.buscar(semestre2)==True:
                    print("El semestre: "+ str(semestre2)+ " ya existe ")
                else:
                    print("El semestre: " + str(semestre2) + " no existe y se reemplazara ")
                    actual.semestre = semestre2

            actual = actual.next

    def obtener(self, carnet):
        temp = self.first
        while temp != None:
            if int(temp.carnet) == int(carnet):
                print("Se encontro el carnet para retornar: " + str(temp.carnet))
                return temp
            temp = temp.next
        return temp


    def graficar(self, ngraf):
        grafo = "digraph\n{"
        #grafo += str("{\nnode[shape=record];\n")
        #grafo += str("graph[pencolor=transparent];\n")
        #grafo+=str("rankdir=LR\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")

        aux = self.first
        cont = 0

        while True:
            info = "Semestre: "+ str(aux.semestre)
            grafo += "\t nodo_"+str(cont)+ "[label = \"" + info + "\"];\n"
            aux = aux.next
            cont +=1
            if aux == None:
                break
        grafo += "\n"
        if self.getSize() == 1:
            grafo += "\t  \n"
        else:
            for i in range(1,self.getSize()):
                grafo += "\tnodo_"+str(i-1)+"-> nodo_"+ str(i)+"\n"




        grafo += str("}\n")
        tmp = self.conta
        f = open("semestre"+str(ngraf)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica de Semestres *********  " + str(ngraf))
        os.system("dot -Tsvg -o sem"+str(ngraf)+".svg semestre"+str(ngraf)+".dot")
        self.conta +=1