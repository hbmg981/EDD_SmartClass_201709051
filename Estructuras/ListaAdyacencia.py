from Estructuras.Lista import Lista
from Estructuras.Nodo import NodoG
import os

class ListaAdyacencia:
    def __init__(self):
        self.First = None
        self.Last = None
        self.ngraf =0
        self.listaaux =[]
        self.previos = []
        self.textoaux = ""
        self.textolabel = ""

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


    def retornar(self, codigo):
        aux = self.First
        while aux is not None:
            if aux.codigo == codigo:
                return aux
            aux = aux.Next
        return aux


    def insert_node(self, codigo, nombre, creditos, prerequisito,obligatorio):
        if not self.exists(codigo):
            new_list = Lista()
            lista_post = Lista()
            new_node = NodoG(codigo,nombre,creditos,prerequisito,obligatorio, new_list, lista_post)

            if self.is_empty():
                self.Last = new_node
                self.First = self.Last
            else:
                self.Last.Next = new_node
                new_node.Previous = self.Last
                self.Last=new_node
        else:
            #------ Ya existe un curso con ese codigo ---------
            print("El valor ya existe")




    def link_graph(self, codigo1, codigo2):
        aux = self.First
        while aux is not None:
            if aux.codigo == codigo1:
                #Lista de cursos posteriores
                aux.lista_post.insertValue(codigo2)
                #print("Insertando valor: ",codigo2, "en:", codigo1)
                break
            aux = aux.Next

        aux2 = self.First
        while aux2 is not None :
            if aux2.codigo == codigo2:
                #Lista de cursos anteriores
                aux2.lista.insertValue(codigo1)
                break
            aux2 = aux2.Next


    def link_graph2(self, codigo1, codigo2):
        aux = self.First
        while aux is not None:
            if aux.codigo == codigo1:
                aux.lista.insertValue(codigo2)
                #print("Insertando valor: ",codigo2, "en:", codigo1)
                break
            aux = aux.Next

    def get_list_post(self):
        aux = self.First
        counter =0
        adjacency_list = ""
        while aux is not None:
            if not aux.lista_post.isEmpty():
                aux2 = aux.lista_post.First
                while aux2 is not None:
                    #print("El codigo deberia estar aqui",aux2.codigo)
                    adjacency_list += "--"+str(aux.creditos)+"->" + str(aux2.codigo)
                    aux2=aux2.Next
            print(str(counter)+")"+str(aux.codigo)+" Nombre: "+aux.nombre+" Creditos: " + str(aux.creditos)
                   + " Prerequisitos: "+aux.prerequisitos+" Obligatorio: "+aux.obligatorio + adjacency_list)
            adjacency_list = ""
            counter+=1
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
            print(str(counter)+")"+str(aux.codigo)+" Nombre: "+aux.nombre+" Creditos: " + str(aux.creditos)
                   + " Prerequisitos: "+aux.prerequisitos+" Obligatorio: "+aux.obligatorio + adjacency_list)
            adjacency_list = ""
            counter+=1
            aux = aux.Next

    def get_list2(self, codigo):
        if self.exists(codigo):
            aux = self.retornar(codigo)
        else:
            print("No existe curso con ese codigo")
        counter =0
        # recorre la lista principal de nodosg
        if aux is not None:
            self.buscar_pre(aux, counter)
            counter+=1
            aux = aux.Next

    def buscar_pre(self, aux, counter):

        if not aux.lista.isEmpty():
            aux2 = aux.lista.First
            adjacency_list = []
            cont = 0
            while aux2 is not None:
                #
                adjacency_list.append(aux2.codigo)
                cont += 1
                aux2 = aux2.Next

            if adjacency_list is not None:
                print(
                    str(counter) + ")" + str(aux.codigo) + " Nombre: " + aux.nombre + " Creditos: " + str(aux.creditos)
                    + " Prerequisitos: " + aux.prerequisitos + " Obligatorio: " + aux.obligatorio)
                for x in adjacency_list:
                    print("El curso anterior a:",aux.codigo,"es:",x)
                    print("->",x)
                    if self.exists(x):
                        self.buscar_pre(self.retornar(x),counter)
                    else:
                        print("No se encontro el curso con codigo",x)
                    # print(self.exists(x))
                    # aux =self.retornar(x).lista.First
                del adjacency_list
        else:
            #print("Cuando no hay elementos anteriores, es el ultimo nodo")
            print(
                str(counter) + ")" + str(aux.codigo) + " Nombre: " + aux.nombre + " Creditos: " + str(aux.creditos)
                + " Prerequisitos: " + aux.prerequisitos + " Obligatorio: " + aux.obligatorio)



    def graf(self, codigo):
        if self.exists(codigo):
            aux = self.retornar(codigo)
            texto = ""
            self.graf2(aux)

        else:
            print("No existe curso con ese codigo")
        #return texto

    def buscarenlista(self, codigo):
        for x in self.listaaux:
            if int(x) == int(codigo):
                print("Se encontro en la lista")
                return True
        return False

    def buscarenlista2(self, infox):
        for x in self.previos:
            if x ==infox:
                print("Se encontro en la lista que hay previos repetidos")
                return True
        return False

    def llenarlabel(self):
        for x in self.listaaux:
            if self.exists(x):
                aux = self.retornar(x)
                info = "Codigo: "+ str(aux.codigo)\
                    +"\\nNombre: " + aux.nombre + "\\nCreditos: " + str(aux.creditos)\
                       + " \\nPrerequisitos: " + aux.prerequisitos + " \\nObligatorio: " + aux.obligatorio
                self.textolabel += "nodo_"+str(aux.codigo)+"[label = \" "+ info+ "  \"]"+"\n"

    def llenarprevios(self):
        for x in self.previos:
            self.textoaux += x +"\n"


    def graf2(self, aux):
        if self.buscarenlista(aux.codigo) is False:
            self.listaaux.append(aux.codigo)
            print("No se encontro el codigo:", aux.codigo)
        else:
            print("Ya existe el codigo:", aux.codigo)
        if not aux.lista.isEmpty():

            aux2 = aux.lista.First
            adjacency_list = []
            cont = 0
            while aux2 is not None:
                #
                adjacency_list.append(aux2.codigo)
                cont += 1
                aux2 = aux2.Next

            if adjacency_list is not None:


                print(str(aux.codigo) + " Nombre: " + aux.nombre + " Creditos: " + str(aux.creditos)
                    + " Prerequisitos: " + aux.prerequisitos + " Obligatorio: " + aux.obligatorio)
                for x in adjacency_list:
                    print("El curso anterior a:", aux.codigo, "es:", x)

                    print(x,"->", aux.codigo)
                    if self.exists(x):
                        aux2 = self.retornar(x)
                        infox= "nodo_" + str(x) + "-> nodo_" + str(aux.codigo)+ "[label=\"" + str(aux2.creditos) + "\"]"
                        if self.buscarenlista2(infox) is False:
                            self.previos.append(infox)
                            print("no se encontro el texto igual")
                        self.graf2(aux2)

                    else:
                        print("No se encontro el curso con codigo", x)
                    # print(self.exists(x))
                    # aux =self.retornar(x).lista.First
                del adjacency_list
        else:
            # print("Cuando no hay elementos anteriores, es el ultimo nodo")
            print( str(aux.codigo) + " Nombre: " + aux.nombre + " Creditos: " + str(aux.creditos)
                + " Prerequisitos: " + aux.prerequisitos + " Obligatorio: " + aux.obligatorio)

    def printlistaaux(self):
        for element in self.listaaux:
            print(element)


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
            if not aux.lista_post.isEmpty():
                aux2 = aux.lista_post.First
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


    def graficar2(self, codigo):
        grafo = "digraph\n"
        grafo += str("{\nnode[shape=component];\n")
        # grafo += str("graph[pencolor=transparent];\n")
        grafo+=str("rankdir=LR\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")

        self.graf(codigo)
        self.llenarlabel()

        self.llenarprevios()
        grafo+=self.textolabel
        grafo+=self.textoaux


        grafo += "\n"

        aux = self.First
        counter = 0
        adjacency_list = ""



        grafo += str("}\n")
        tmp = self.ngraf
        f = open("grafo" + str(tmp) + ".dot", "w+", encoding='utf-8')
        f.write(grafo)
        f.close()
        self.previos.clear()
        self.listaaux.clear()
        self.textolabel = ""
        self.textoaux = ""
        os.system("dot -Tsvg -o graf" + str(tmp) + ".svg grafo" + str(tmp) + ".dot")
        print("********* Se realizo Grafica  *********  " + str(tmp))
        self.ngraf += 1
