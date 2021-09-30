from Estructuras.Nodo_Mes import NodoMes
import os
class ListaM:

    def __init__(self):
        self.First = None
        self.Last = None
        self.conta = 0
        self.contador =0

    def getSize(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.Next

        return counter

    def buscar(self, mes):
        temp = self.First
        while(temp != None and temp.mes != mes):
            temp = temp.Next
        print("Se encontro el año: " + str(temp.mes))
        return  temp != None

    def buscarRetornar(self, mes):
        temp = self.First
        while(temp!=None and temp.mes!=mes):
            temp = temp.Next
        return temp


    def isEmpty(self):
        return self.First is None

    def getList(self):
        aux = self.First
        while aux is not None:
            print(aux.mes)
            aux = aux.Next

    def getListRev(self):
        aux = self.Last
        while aux is not None:
            print(aux.mes)
            aux = aux.Previous

    def insertValue(self, mes):
        new_node = NodoMes(mes)

        if self.isEmpty():
            self.Last = new_node
            self.First = self.Last
            self.contador +=1
        else:
            self.Last.Next = new_node
            new_node.Previous = self.Last
            self.Last = new_node
            self.contador += 1

    def eliminar(self, mes):
        actual = self.First
        eliminado = False

        if actual is None:
            eliminado = False
        elif actual.mes == mes:
            self.First = actual.Next
            self.First.Previous = None
            eliminado = True
        elif self.Last.mes ==mes:
            self.Last = self.Last.Previous
            self.Last.Next = None
            eliminado = True
        else:
            while actual:
                if actual.mes == mes:
                    actual.Previous.Next = actual.Next
                    actual.Next.Previous = actual.Previous
                    eliminado = True
                actual = actual.Next
        if eliminado:
            self.contador -=1

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
            info = "Mes: "+ str(aux.mes)
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
        f = open("mes"+str(self.conta)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica  Tareas *********  ")
        os.system("fdp -Tpng -o mesg"+str(self.conta)+".png mes"+str(self.conta)+".dot")
        self.conta +=1


    def orden(self):
        aux = self.First

        while aux.Next != None:
            aux2 = aux.Next
            while aux2 != None:
                if aux2.mes < aux.mes:
                    temp = aux.mes
                    aux.mes = aux2.mes
                    aux2.mes = temp

                aux2= aux2.Next

            aux = aux.Next