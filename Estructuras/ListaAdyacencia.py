from Estructuras.Lista import Lista
from Estructuras.Nodo import NodoG
import os

class ListaAdyacencia:
    def __init__(self):
        self.First = None
        self.Last = None
        self.ngraf =0

    def get_size(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter +=1
            aux = aux.Next
        return counter

    def is_empty(self):
        return self.First is None



    def exists(self, codigo):
        aux = self.First
        while aux is not None:
            if aux.codigo == codigo:
                return True
            aux = aux.Next
        return False


    def insert_node(self, codigo, nombre, creditos, prerequisito,obligatorio):
        if not self.exists(codigo):
            new_list = Lista()
            new_node = NodoG(codigo,nombre,creditos,prerequisito,obligatorio, new_list)

            if self.is_empty():
                self.Last = new_node
                self.First = self.Last
            else:
                self.Last.Next = new_node
                new_node.Previous = self.Last
                self.Last=new_node
        else:
            print("El valor ya existe")

    def link_graph(self, codigo1, codigo2):
        aux = self.First
        '''while aux is not None:
            if aux.codigo == codigo1:
                aux.lista.insertValue(codigo2)
                #print("Insertando valor: ",codigo2, "en:", codigo1)
                break
            aux = aux.Next'''

        while aux is not None :
            if aux.codigo == codigo2:
                aux.lista.insertValue(codigo1)
                break
            aux = aux.Next


    def get_list(self):
        aux = self.First
        counter =0
        adjacency_list = ""
        while aux is not None:
            if not aux.lista.isEmpty():
                aux2 = aux.lista.First
                while aux2 is not None:
                    #print("El codigo deberia estar aqui",aux2.codigo)
                    adjacency_list += "--"+str(aux.creditos)+"->" + str(aux2.codigo)
                    aux2=aux2.Next
            print(str(counter)+")"+str(aux.codigo)+" Nombre:"+aux.nombre+"Creditos: " + str(aux.creditos)
                   + "Prerequisitos"+aux.prerequisitos+"Obligatorio"+aux.obligatorio)
            adjacency_list = ""
            counter+=1
            aux = aux.Next

    def graficar(self):
        grafo = "digraph\n"
        grafo += str("{\nnode[shape=component];\n")
        # grafo += str("graph[pencolor=transparent];\n")
        grafo+=str("rankdir=LR\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")

        aux = self.First
        cont = 0

        while True:
            info = "" + str(aux.codigo)+ "\\n"+ aux.nombre\
                   +"\\nCreditos: "+ str(aux.creditos)+ "\\n"+ "Prerequisitos: "+aux.prerequisitos\
                   + "\\n"+ "Obligatorio: "+aux.obligatorio
            grafo += "\t nodo_" +str(aux.codigo) + "[label = \"" + info + "\"];\n"
            aux = aux.Next
            cont += 1
            if aux == None:
                break
        grafo += "\n"

        aux = self.First
        counter = 0
        adjacency_list = ""
        while aux is not None:
            if not aux.lista.isEmpty():
                aux2 = aux.lista.First
                grafo += ""
                while aux2 is not None:
                    grafo+="nodo_" + str(aux.codigo)+ "->" +"nodo_"+ str(aux2.codigo)\
                           +"[label = \" "+ str(aux.creditos)+ "  \"]"+"\n"

                    aux2 = aux2.Next
            counter += 1
            aux = aux.Next



        grafo += str("}\n")
        tmp = self.ngraf
        f = open("grafo" + str(tmp) + ".dot", "w+", encoding='utf-8')
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica  *********  " + str(tmp))
        os.system("dot -Tsvg -o graf" + str(tmp) + ".svg grafo" + str(tmp) + ".dot")
        self.ngraf += 1
