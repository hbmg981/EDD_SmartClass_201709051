
#import SolovayStrassen as ss
import os
class Nodo:

    def __init__(self, indice, carnet):
        self.indice = indice
        self.carnet = carnet
        self.lista = []
        self.contlista =0

class NodoLista:

    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido



class Hash:
    def __init__(self, valor=7):
        self.primos = [7,11,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97101,103,
                       107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,
                       233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,
                       373,379,383,389,397,401,409]
        self.contadordeprimos=1
        self.vector = []
        self.elementos = 0
        self.factorCarga = 0
        self.tamano = valor
        self.ngraf =1

        for i in range(valor):
            self.vector.append(None)

    def buscar(self, carnet):
        encontrado = False
        for i in self.vector:
            if i:
                if int(i.carnet) == int(carnet):
                    #print("Se encontro el carnet")
                    encontrado=True
                #else:
                    #print("No se encontro nada")
        return encontrado

    def retornar(self, carnet):
        aux = None
        for i in self.vector:
            if i:
                if int(i.carnet) == int(carnet):
                    #print("Se encontro el carnet")
                    aux = i
                #else:
                    #print("No se encontro nada")
        return aux


    def insertar(self, carnet, titulo, contenido):
        if self.buscar(carnet)==False:
            posicion = self.funcion_hash(carnet)
            nuevo = Nodo(posicion, carnet)
            self.vector[posicion] = nuevo
            self.elementos += 1
            self.factorCarga = self.elementos / self.tamano
            nlist = NodoLista(titulo, contenido)
            nuevo.lista.append(nlist)


            if self.factorCarga > 0.5:
                self.rehashing()
                #print("Haciendo el rehashing de: " + str(carnet))

            #nodoactual = self.retornar(carnet)
            #nodoactual.lista.append(valor)
            #nodoactual.contlista += 1
            #print("Insertando datos, carnet: " + str(carnet) + " info: " + nodoactual.lista[nodoactual.contlista])

        else:
            print("El carnet ya existe: ")
            nodoactual = self.retornar(carnet)
            nlist = NodoLista(titulo,"contenido")
            nodoactual.lista.append(nlist)
            print("Insertando datos, carnet: "+ str(carnet) +" info: "+ titulo)
            nodoactual.contlista += 1







    def rehashing(self):
        siguiente = self.tamano
        factor = 0
        while (factor < 0.5):
            factor = self.elementos / siguiente
            siguiente = self.primos[self.contadordeprimos]
            self.contadordeprimos+=1

        temporal = []

        for i in range(siguiente):
            temporal.append(None)
        aux_vector = self.vector

        self.vector = temporal
        self.tamano = siguiente

        #print("Nuevo tamano", siguiente, "Tamano:", len(temporal))
        for i in aux_vector:
            if i:
                posicion = self.funcion_hash(i.carnet)
                #posicion = self.funcion_hash(i.indice)
                #print("Nueva posicion:", posicion)
                i.indice = posicion
                temporal[posicion] = i

        self.vector = temporal

    def _funcion_hash(self, id):
        return id % self.tamano

    def funcion_hash(self, id):

        posicion = id % (self.tamano)
        #print("El tamano actual es: "+ str(self.tamano)+ " La posicion es: "+ str(posicion))

        k= posicion
        conti =1
        while (self.vector[posicion] != None):

            posicion = self.linear(k, conti)
            conti += 1
            #print(posicion)
            #if posicion > self.tamano:
               # posicion = posicion - self.tamano
        return posicion

    def linear(self, k, i):
        return(k+ i*i) % self.tamano

    def print(self):
        contador = 0
        for i in self.vector:
            if i:
                print("indice:", i.indice,"carnet:", i.carnet)
            else:
                print("indice:", contador, "valor:", i)

            contador += 1


    def print2(self):
        print ("Imprimiendo valores de la lista")
        contador = 0
        for i in self.vector:
            if i:
                print("indice:", i.indice, "carnet:", i.carnet)
                for x in  i.lista:
                    print("Apuntes: "+ str(x.titulo)+ " Contenido: "+ x.contenido)
            else:
                print("indice:", contador, "carnet:", i)

            contador += 1

    def graficarHash(self):

        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        grafo += str("rankdir=LR;\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")



        cont =0
        for i in self.vector:
            if i:

                a=0
                for x in i.lista:
                    #print("Apuntes: " + str(x.titulo) + " Contenido: " + x.contenido)
                    info = "Titulo: " + x.titulo+ "\\n" + "Contenido:" + x.contenido
                    grafo += "\t nodo_" + str(i.indice)+"_"+str(a) + "[label = \"" + info + "\"];\n"
                    a+=1

            cont += 1

        contador = 0
        for i in self.vector:
            if i:
                #print("indice:", i.indice, "carnet:", i.carnet)
                grafo += "\t nodo_" + str(i.indice) + "-> " + "\n"
                a=0
                for x in i.lista:
                    grafo += "\t nodo_" + str(i.indice) + "_" + str(a) +" \n"
                    #print("Apuntes: " + str(x.titulo) + " Contenido: " + x.contenido)
                    a+=1

            else:
                print("indice:", contador, "carnet:", i)

            contador += 1

        grafo += str("}\n")

        f = open("hash" + str(self.ngraf) + ".dot", 'w', encoding='utf-8')
        f.write(grafo)
        f.close()
        # print("********* Se realizo Grafica  AVL *********  " + str(self.ngraf))
        os.system("dot -Tsvg -o hashg" + str(self.ngraf) + ".svg hash" + str(self.ngraf) + ".dot")
        self.ngraf += 1

    def graficarHash2(self):

        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        grafo += str("rankdir=LR;\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")
        grafo += str("node [shape=record,width=.1,height=.1];\n")
        #

        cont = 0

        grafo += " nodet [label = \""
        for i in self.vector:
            if i:
                # print("indice:", i.indice, "carnet:", i.carnet)
                grafo += "<f"+str(i.carnet)+">"+"\\n"+str(i.carnet)+"\\n"+"\\n"+" |"

            else:
                grafo += "<f" +str(cont)+ ">" +"\\n"+"\\n"+"\\n"+ "|"

            cont += 1
        grafo+= "\",height=10.5]; \n"
        grafo += "node [width = 2.5];\n"
        cont = 0
        for i in self.vector:
            if i:

                a = 0
                for x in i.lista:
                    # print("Apuntes: " + str(x.titulo) + " Contenido: " + x.contenido)
                    info = "Titulo: " + x.titulo + "\\n" + "Contenido:" + x.contenido
                    grafo += "\t node" +str(i.carnet)+ "_" + str(a) + "[label = \"" + info + "\"];\n"
                    a += 1

            cont += 1

        contador = 0
        for i in self.vector:
            if i:
                # print("indice:", i.indice, "carnet:", i.carnet)
                grafo += "\t nodet:f" + str(i.carnet) + ""
                a = 0
                for x in i.lista:
                    grafo += "-> "+"\t node"+str(i.carnet)+ "_" + str(a) + ""+"   \n"
                    # print("Apuntes: " + str(x.titulo) + " Contenido: " + x.contenido)
                    a += 1
                #grafo += "point_"+str(i.carnet)
            else:
                print("indice:", contador, "carnet:", i)

            contador += 1

        grafo += str("}\n")

        f = open("hash" + str(self.ngraf) + ".dot", 'w', encoding='utf-8')
        f.write(grafo)
        f.close()
        # print("********* Se realizo Grafica  AVL *********  " + str(self.ngraf))
        os.system("dot -Tsvg -o hashg" + str(self.ngraf) + ".svg hash" + str(self.ngraf) + ".dot")
        self.ngraf += 1






tabla = Hash()
#tabla.graficarHash()
tabla.insertar(0, "primera clase", "realizar tarea")
tabla.insertar(15,  "segundo valor 15", "realizar tarea")
tabla.insertar(29,  "tercer valor 29", "realizar tarea")
tabla.insertar(44,  "4to valor 44", "realizar tarea")
tabla.insertar(58,  "5to valor 58", "realizar tarea")
tabla.insertar(73,  "6to valor 73", "realizar tarea")
tabla.insertar(87,  "7mo valor 87", "realizar tarea")
tabla.insertar(116,  "8o valor 116", "realizar tarea")
tabla.insertar(145,  "9 valor 145", "realizar tarea")
tabla.insertar(174,  "10 valor 174", "realizar tarea")
tabla.insertar(203,  "11 valor 203", "realizar tarea")
tabla.insertar(232,  "12 valor 232", "realizar tarea")
tabla.insertar(203,  "13 valor 203", "realizar tarea")

#tabla.print()
#tabla.print2()
#print(tabla.buscar(365))
tabla.graficarHash2()