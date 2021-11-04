from Estructuras.Nodo import Nodo
import os
class Lista:

    def __init__(self):
        self.First = None
        self.Last = None
        self.contador = 0
        self.conta = 1

    def getSize(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.Next

        return counter

    def isEmpty(self):
        return self.First is None

    def getList(self):
        #self.orden()
        aux = self.First
        result_list = []
        while aux is not None:
            result_list.append(aux.codigo)
            aux = aux.Next
        return  result_list



    def insertValue(self, codigo):
        # Cuando no hay datos en la lista
        new_node = Nodo(codigo)
        if self.isEmpty():
            self.Last = new_node
            self.First = self.Last
        else:
            self.Last.Next = new_node
            new_node.Previous = self.Last
            self.Last = new_node





    def eliminar(self, año):
        actual = self.First
        eliminado = False

        if actual is None:
            eliminado = False
        elif actual.año == año:
            self.First = actual.Next
            self.First.Previous = None
            eliminado = True
        elif self.Last.año ==año:
            self.Last = self.Last.Previous
            self.Last.Next = None
            eliminado = True
        else:
            while actual:
                if actual.año == año:
                    actual.Previous.Next = actual.Next
                    actual.Next.Previous = actual.Previous
                    eliminado = True
                actual = actual.Next
        if eliminado:
            self.contador -=1


    def ordenar(self):
        ayuda = self.First
        while ayuda != None:
            ini = ayuda.Next
            if ayuda.año > ini.año:
                aux = ayuda.año
                ayuda.año = ini.año
                ini.año = aux

            ini = ini.Next

        ayuda = ayuda.Next

        #self.getList()

    def buscar(self, codigo):
        temp = self.First
        while temp != None :
            if temp.codigo ==codigo:
                print("Se encontro el año en buscar: " + str(temp.codigo))
                return True
            temp = temp.Next

        return  temp != None

    def buscarRetornar(self, codigo):
        temp = self.First
        while temp!=None:
            if temp.codigo == codigo:
                print("Se encontro el año para retornar: " + str(temp.codigo))
                return temp
            temp = temp.Next
        return temp


    def orden(self):
        aux = self.First

        while aux.Next != None:
            aux2 = aux.Next
            while aux2 != None:
                if aux2.año < aux.año:
                    temp = aux.año
                    aux.año = aux2.año
                    aux2.año = temp

                aux2= aux2.Next

            aux = aux.Next

    def graficar(self):
        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        grafo+=str("rankdir=LR;\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")

        self.orden()
        aux = self.First
        cont = 0

        while True:
            info = "Mes: "+ str(aux.año)
            grafo += "\t nodo_"+str(cont)+ "[label = \"" + info + "\"];\n"
            aux = aux.Next
            cont +=1
            if aux == None:
                break
        grafo += "\n"
        if self.getSize() == 1:
            grafo += "\t nodo_0 -> nodo_0 \n"
        else:
            for i in range(1,self.getSize()):
                grafo += "\tnodo_"+str(i-1)+"-> nodo_"+ str(i)+"\n"
                grafo += "\tnodo_" + str(i ) + "-> nodo_" + str(i-1) + "\n"



        grafo += str("}\n")
        tmp = self.conta
        f = open("curso"+str(self.conta)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica Cursos *********  ")
        os.system("dot -Tsvg -o cursog"+str(self.conta)+".svg curso"+str(self.conta)+".dot")
        self.conta +=1




