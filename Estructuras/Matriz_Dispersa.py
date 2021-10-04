from Estructuras.Nodo_dispersa import NodoMatriz
from Estructuras.Nodo_dispersa import NodoCabecera
from Estructuras.Nodo_dispersa import NodoRaiz
import os


class Matriz_dispersa:
    cont =1;

    def __init__(self):
        self.NodoRaiz=None
        self.contTarea = 1
        self.ngraf =1
        
    def insertar_nodo_fila(self,nodo):
        temporalfila = self.NodoRaiz.NodoFilas 
        while(temporalfila.indice!=nodo.hora):
            temporalfila = temporalfila.siguiente
        #temporalfila=temporalfila.derecha
        if temporalfila.derecha is None:
            nodo.derecha=temporalfila.derecha 
            temporalfila.derecha = nodo 
        elif temporalfila.derecha.dia >= nodo.dia:
            nodo.derecha = temporalfila.derecha
            temporalfila.derecha = nodo 
        else : 
            current = temporalfila.derecha 
            while(current.derecha is not None and current.derecha.dia < nodo.dia):
                current = current.derecha
            nodo.derecha = current.derecha
            current.derecha = nodo
    def insertar_nodo_col(self,nodo):
        temporalcol = self.NodoRaiz.NodoColumnas 
        while(temporalcol.indice!=nodo.dia):
            temporalcol= temporalcol.siguiente
        #temporalcol=temporalcol.abajo
        if temporalcol.abajo is None: 
            nodo.abajo = temporalcol.abajo
            temporalcol.abajo = nodo
        elif temporalcol.abajo.hora >= nodo.hora:
            nodo.abajo = temporalcol.abajo
            temporalcol.abajo = nodo
        else : 
            current = temporalcol.abajo
            while(current.abajo is not None and current.abajo.hora < nodo.hora):
                current = current.abajo
            nodo.abajo = current.abajo
            current.abajo = nodo    
    def insertar_cabercera(self,nodo,indice,tipo):
        temporalfila=nodo
        if temporalfila.indice > indice: 
            nuevaCabecera=NodoCabecera(tipo=tipo,indice=indice)
            nuevaCabecera.siguiente = self.NodoRaiz.NodoFilas 
            self.NodoRaiz.NodoFilas = nuevaCabecera 
        else : 
            current = temporalfila 
            while(current.siguiente is not None and current.siguiente.indice <= indice): 
                current = current.siguiente
            if current.indice != indice:
                nuevaCabecera=NodoCabecera(tipo=tipo,indice=indice)
                nuevaCabecera.siguiente = current.siguiente
                current.siguiente = nuevaCabecera
                
    def insertar(self,dia,hora,carnet, nombre, descrip, materia, fecha, estado):


        # Cuando no existe ningun valor en la matriz
        if  self.NodoRaiz is None:
            nodoN = NodoMatriz(dia=dia, hora=hora, ntareas=self.contTarea)
            nodoN.lista.InsertarTarea(carnet, nombre, descrip, materia, fecha, hora, estado)
            print("Insertando datos cuando no hay datos:  dia: " + str(dia) + " hora: " + str(hora))
            self.NodoRaiz = NodoRaiz()
            self.NodoRaiz.NodoColumnas=NodoCabecera(tipo="Columna",indice=dia)
            self.NodoRaiz.NodoFilas=NodoCabecera(tipo="Fila",indice=hora)
            self.NodoRaiz.NodoColumnas.siguiente =None
            self.NodoRaiz.NodoFilas.siguiente =None
            self.NodoRaiz.NodoColumnas.abajo=nodoN
            self.NodoRaiz.NodoFilas.derecha=nodoN
            nodoN.lista.InsertarTarea(carnet, nombre, descrip, materia, fecha, hora, estado)
            print("Insertando datos cuando no hay datos:  dia: " + str(dia) + " hora: " + str(hora))
        # Cuando ya hay elementos en la matriz
        else:
            #Cuando no existe nodo con ese dia y hora, se crea uno
            nodoN = NodoMatriz(dia=dia, hora=hora, ntareas=self.contTarea)
            Nodotemporal = self.NodoRaiz
            self.insertar_cabercera(Nodotemporal.NodoFilas, hora, "Fila")
            Nodotemporal = self.NodoRaiz
            self.insertar_cabercera(Nodotemporal.NodoColumnas, dia, "Columna")
            self.insertar_nodo_fila(nodo=nodoN)
            self.insertar_nodo_col(nodo=nodoN)

            if self.buscar(dia,hora) ==False:
                nodoN.lista.InsertarTarea(carnet, nombre, descrip, materia, fecha, hora, estado)
                print("Insertando datos cuando ya hay datos:  dia: " + str(dia) + " hora: " + str(hora))
            else:
                # implementar un metodo buscar y retornar el nodo repetido para acceder a su lista
                print("el dato ya existia  dia: " + str(dia) + " hora: " + str(hora))
                self.buscarRetornar(dia,hora).cont += 1
                self.buscarRetornar(dia, hora).lista.InsertarTarea(carnet, nombre, descrip, materia, fecha, hora, estado)
                print("Elemento duplicado")
                print("Dato en el nodo: "+  str(self.buscarRetornar(dia,hora).ntareas))
                #self.buscarRetornar(dia,hora)



   # def insertarTarea(self):


    def buscar(self,dia,hora):
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                if nodo_temp.dia ==dia and nodo_temp.hora==hora:
                    return True
                nodo_temp=nodo_temp.derecha
            nodo=nodo.siguiente
        return False

    def buscarRetornar(self,dia,hora):
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                if nodo_temp.dia ==dia and nodo_temp.hora==hora:
                    return nodo_temp
                nodo_temp=nodo_temp.derecha
            nodo=nodo.siguiente
        return nodo

    def graficarLista(self, dia, hora, n):
        if self.buscarRetornar(dia,hora) is not None:
            self.buscarRetornar(dia,hora).lista.graficar(n)
            self.ngraf +=1
        else:
            print("No se encontro la matriz del dia: "+ str(dia)+" Hora: "+str(hora))


    def graficar_matriz(self, ngraf):
        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        # grafo+=str("rankdir=LR;\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")
        nodo = self.NodoRaiz.NodoFilas

        for hora in range(1, 24):
            nodo_temp = nodo.derecha
            for dia in range(1, 31):
                if (self.buscar(dia, hora)):
                    grafo += str(
                        "p" + str(dia) +"_"+ str(hora) + "[label=\"{<data>" + "Dia: "+ str(dia) + "\\n" +"Hora: "+ str(hora) + "| "+ str(nodo_temp.cont) +" }\" pos=\"" + str(
                            dia) + "," + str(10 - hora) + "!\"];\n")
                    if (nodo_temp.derecha != None):
                        nodo_2 = nodo_temp
                        nodo_temp = nodo_temp.derecha
                        grafo += str("p" + str(nodo_2.dia) +"_"+ str(nodo_2.hora) + "->" + "p" + str(nodo_temp.dia) +"_"+ str(
                            nodo_temp.hora) + "[dir=both];\n")
                else:
                    pass
                if nodo.siguiente != None:
                    if nodo.siguiente.indice == hora + 1:
                        nodo = nodo.siguiente
        nodo = self.NodoRaiz.NodoColumnas
        for dia in range(1, 31):
            nodo_temp = nodo.abajo
            for hora in range(1, 24):
                if (self.buscar(dia, hora)):
                    if (nodo_temp.abajo != None):
                        nodo_2 = nodo_temp
                        nodo_temp = nodo_temp.abajo
                        grafo += str("p" + str(nodo_2.dia)+"_" + str(nodo_2.hora) + "->" + "p" + str(nodo_temp.dia) +"_"+ str(nodo_temp.hora) + "[dir=both];\n")
                else:
                    pass
                if nodo.siguiente != None:
                    if nodo.siguiente.indice == dia + 1:
                        nodo = nodo.siguiente
        grafo += str("}\n")
        tmp = self.cont
        f = open("dispersa"+str(ngraf)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica MAtriz Dispersa *********  ")
        os.system("fdp -Tsvg -o disp"+str(ngraf)+".svg dispersa"+str(ngraf)+".dot")
        self.cont +=1






