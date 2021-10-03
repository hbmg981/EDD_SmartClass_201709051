from Estructuras.Nodo_simple import NodoTarea
import os

class ListaSimple:
    conta=1
    def __init__(self):
        self.first = None
        self.Size = 0

    def InsertarTarea(self, carnet, nombre, descrip, materia, fecha,hora, estado):
        Nodo = NodoTarea(carnet, nombre, descrip, materia, fecha,hora, estado)
        if self.Size ==0:
            self.first = Nodo
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next= Nodo

        self.Size +=1

        return Nodo

    def eliminar(self, carnet):
        aux = self.first
        prev = None
        found = False
        if self.Size!=0:
            if self.buscar(carnet):
                while aux != None and found ==False:
                    if aux.carnet == carnet:
                        if prev == None:
                            self.first = aux.next
                            aux.next = None

                        else:
                            prev.next = aux.next
                            aux.next=None
                        found = True
                        self.Size -=1
                    prev = aux
                    aux = aux.next
            else:
                print("Elemento: "+str(carnet)+" No encontrado")



    def getList(self):
        aux = self.first
        while aux is not None:
            print(str(aux.carnet) + " - " + aux.nombre + "-" + aux.descrip + "-" + aux.materia + "-" + aux.fecha + "-" + aux.hora + "-" + aux.estado)
            aux = aux.next


    def buscar(self, carnet):
        temp = self.first
        while(temp != None and temp.carnet != carnet):
            temp = temp.next
        return  temp != None

    def Modificar(self, carnet,carnet2, nombre, descrip, materia, fecha,hora, estado):
        actual = self.first
        while actual!=None:
            if actual.carnet == carnet:
                actual.carnet = carnet2
                actual.nombre = nombre
                actual.descrip = descrip
                actual.materia = materia
                actual.fecha = fecha
                actual.hora = hora
                actual.estado = estado

            actual = actual.next

    def obtener(self, carnet):
        actual = self.first
        if self.buscar(carnet):
            while actual != None:
                if actual.carnet == carnet:
                    print("Estudiante encontrado")
                    print("Carnet: "+str(actual.carnet)+" Nombre: "+ actual.nombre +" Descripcion: "+ actual.descrip)

                actual = actual.next
        else:
            print("Estudiante NO encontrado")

    def graficar(self, ngraf):
        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        grafo+=str("rankdir=LR\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")

        aux = self.first
        cont = 0

        while True:
            info = "Carnet: "+ str(aux.carnet) + "\\nNombre:"+ aux.nombre+ "\\nDescripcion:"+ aux.descrip
            grafo += "\t nodo_"+str(cont)+ "[label = \"" + info + "\"];\n"
            aux = aux.next
            cont +=1
            if aux == None:
                break
        grafo += "\n"
        if self.Size == 1:
            grafo += "\t  \n"
        else:
            for i in range(1,self.Size):
                grafo += "\tnodo_"+str(i-1)+"-> nodo_"+ str(i)+"\n"




        grafo += str("}\n")
        tmp = self.conta
        f = open("tarea"+str(ngraf)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica  Tareas *********  ")
        os.system("dot -Tsvg -o tare"+str(ngraf)+".svg tarea"+str(ngraf)+".dot")
        self.conta +=1