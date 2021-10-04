from Estructuras.Nodo_Año import NodoA
import os
class ListaA:

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

    def buscar(self, año):
        temp = self.First
        while temp != None :
            if temp.año ==año:
                print("Se encontro el año en buscar: " + str(temp.año))
                return True
            temp = temp.Next

        return  temp != None

    def buscarRetornar(self, año):
        temp = self.First
        while temp!=None:
            if temp.año == año:
                print("Se encontro el año para retornar: " + str(temp.año))
                return temp
            temp = temp.Next
        return temp


    def isEmpty(self):
        return self.First is None

    def getList(self):
        #self.orden()
        aux = self.First
        while aux is not None:
            print("Año: "+ str(aux.año))
            aux = aux.Next

    def getListRev(self):
        aux = self.Last
        while aux is not None:
            print(aux.año)
            aux = aux.Previous

    def insertValue(self, año,semestre,mes,dia,hora,carnet, nombre, descrip, materia, fecha, estado):

        # Cuando hay datos en la lista
        if self.isEmpty():
            new_node = NodoA(año)
            self.Last = new_node
            self.First = self.Last
            self.contador +=1
            self.buscarRetornar(año).mes.insertValue(mes, dia, hora, carnet, nombre, descrip, materia, fecha, estado)
            self.buscarRetornar(año).semestre.Insertar(semestre)
        else:
            # Cuando ya hay datos en la lista pero el año no existe
            if self.buscar(año) == False:
                new_node = NodoA(año)
                self.Last.Next = new_node
                new_node.Previous = self.Last
                self.Last = new_node
                self.contador += 1
                self.buscarRetornar(año).mes.insertValue(mes, dia, hora, carnet, nombre, descrip, materia, fecha,
                                                         estado)
                self.buscarRetornar(año).semestre.Insertar(semestre)
            else:
                #Cuando el año ya existe, se manda a llenar el mes y el semestre
                self.buscarRetornar(año).mes.insertValue(mes,dia,hora,carnet, nombre, descrip, materia, fecha, estado)
                print("El año ya existia, insertando mes " + str(mes)+ " Y semestre "+ str(semestre))
                self.buscarRetornar(año).semestre.Insertar(semestre)

    def GraficarTareas(self, año, mes, dia, hora):
        if self.buscarRetornar(año) is not None:
            print("El año: " + str(año) + " Existe")
            if self.buscarRetornar(año).mes.buscarRetornar(mes) is not None:
                print("El mes: " + str(mes) + " Existe")
                if self.buscarRetornar(año).mes.buscarRetornar(mes).tareas.buscarRetornar(
                        dia, hora) is not None:
                    print("La matriz de dia: " + str(dia) + " Hora: " + str(hora) + " Existe")
                    # Graficar lista de tareas
                    self.buscarRetornar(año).mes.buscarRetornar(mes).tareas.graficarLista(dia,hora, self.conta)
                    self.conta += 1
                else:
                    print("La matriz de dia: " + str(dia) + " Hora: " + str(hora) + "  No Existe")
            else:
                print("El mes: " + str(mes) + " No se encontro")
        else:
            print("El año: " + str(año) + " No Se encontro")
            print("Mostrando lista de años: ")
           # self.buscarRetornar(carnet).lista.getList()



    def GraficarDispersa(self, año, mes):
        if self.buscarRetornar(año) is not None:
            print("El año: " + str(año) + " Existe")
            if self.buscarRetornar(año).mes.buscarRetornar(mes) is not None:
                print("El mes: " + str(mes) + " Existe")
                self.buscarRetornar(año).mes.buscarRetornar(mes).tareas.graficar_matriz(self.conta)
                self.conta+=1

            else:
                print("El mes: " + str(mes) + " No se encontro")
        else:
            print("El año: " + str(año) + " No Se encontro")
            print("Mostrando lista de años: ")
           # self.buscarRetornar(carnet).lista.getList()



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
        f = open("año"+str(self.conta)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica  Tareas *********  ")
        os.system("dot -Tsvg -o añog"+str(self.conta)+".svg año"+str(self.conta)+".dot")
        self.conta +=1





