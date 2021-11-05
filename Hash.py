
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
                       373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,
                       509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,
                       659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,
                       823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,
                       983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069]

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
            nuevo = Nodo(posicion, int(carnet))
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
            nlist = NodoLista(titulo,contenido)
            nodoactual.lista.append(nlist)
            print("Insertando datos, carnet: "+ str(carnet) +" info: "+ titulo)
            nodoactual.contlista += 1







    def rehashing(self):
        siguiente = self.tamano
        factor = 0
        while (factor < 0.4):
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
                #print("Nueva posicion:", posicion, "Carnet:", i.carnet)
                i.indice = posicion
                temporal[posicion] = i

        self.vector = temporal

    def _funcion_hash(self, id):
        return int(id) % self.tamano

    def funcion_hash(self, id):

        posicion = int(id) % (self.tamano)
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

    def devolver_posicion(self, id):

        posicion = int(id) % (self.tamano)
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



    def buscarposicion(self, carnet):
        posicion = int(carnet) % int(self.tamano)
        print("Carnet:",carnet,"Tamaño:",self.tamano)
        print(posicion)

        if  int(self.vector[posicion].carnet) != int(carnet):
            print("El carnet no esta en esa posicion")
            contador =1
            k = posicion
            while self.vector[posicion].carnet!= None:
                while int(self.vector[posicion].carnet )!= int(carnet):
                    print("El carnet no esta en esa posicion entonces hay que buscarlo cuadraticamente")
                    posicion = self.linear(k,contador)
                    print("Nueva posicion:",posicion)
                    contador+=1
                return posicion
        else:
            print("Se encontro el carnet en esa posicion", posicion,"Carnet:",carnet)

        return posicion


    '''def buscar(self, carnet):
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

        return band'''



    def linear(self, k, i):
        return(k+ i*i) % self.tamano

    def print(self):
        contador = 0
        for i in self.vector:
            if i:
                print("indice:", i.indice,"carnet:", i.carnet)
                '''for x in i.lista:
                    print("titulo:",x.titulo,"Contenido",x.contenido)'''
            else:
                print("indice:", contador, "valor:", i)

            contador += 1

    def printapunte(self,carnet):
        contador = 1
        if self.buscar(carnet):
            car= self.retornar(carnet)
            for x in car.lista:
                print(contador,")","Titulo:",x.titulo,"Contenido:",x.contenido)
                contador+=1
        else:
            print("No se encontro el carnet")


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
        cont = 0
        grafo += " nodet [label = \"Carnet:"
        for i in self.vector:
            if i:
                # print("indice:", i.indice, "carnet:", i.carnet)
                grafo +=" |" +"<f"+str(i.carnet)+">"+"\\n "+str(i.carnet)+" \\n"+"\\n"

            else:
                grafo += "|"+ "<f" +str(cont)+ ">" +"\\n"+"\\n"+"\\n"
            cont += 1
            #height=10.5
        grafo+= "\" ]; \n"
        #grafo += "node [width = 3.5];\n"
        cont = 0
        for i in self.vector:
            if i:

                a = 0
                for x in i.lista:
                    # print("Apuntes: " + str(x.titulo) + " Contenido: " + x.contenido)
                    info = "Titulo: " + x.titulo + "\\n" + "Contenido:" + x.contenido
                           #+ x.contenido[51,100]+"\\n"
                    grafo += "\t node"  +str(i.carnet)+ "_" + str(a) + "[label = \"" + info + "\"];\n"
                    a += 1

            cont += 1

        contador = 0
        for i in self.vector:
            if i:
                # print("indice:", i.indice, "carnet:", i.carnet)
                grafo += "\t nodet:f" + str(i.carnet) + ""
                a = 0
                for x in i.lista:
                    grafo += "\t-> "+"node"+str(i.carnet)+ "_" + str(a) + ""+""
                    #print("Apuntes: " + str(x.titulo) + " Contenido: " + x.contenido)
                    a += 1
                grafo += "\n"
                #grafo += "point_"+str(i.carnet)


            contador += 1

        grafo += str("}\n")

        f = open("hash" + str(self.ngraf) + ".dot", 'w', encoding='utf-8')
        f.write(grafo)
        f.close()
        # print("********* Se realizo Grafica  AVL *********  " + str(self.ngraf))
        os.system("dot -Tsvg -o hashg" + str(self.ngraf) + ".svg hash" + str(self.ngraf) + ".dot")
        self.ngraf += 1






#tabla = Hash()
#tabla.graficarHash()
'''
tabla.insertar(0, "", "")
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
'''



#tabla.print()
#tabla.print2()
#print(tabla.buscar(365))
#tabla.graficarHash2()