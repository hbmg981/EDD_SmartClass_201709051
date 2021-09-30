from Estructuras.Nodo_dispersa import NodoMatriz
from Estructuras.Nodo_dispersa import NodoCabecera
from Estructuras.Nodo_dispersa import NodoRaiz
import os


class Matriz_dispersa:
    cont =1;
    def __init__(self):
        self.NodoRaiz=None
        
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
                
    def insertar(self,dia,hora,ntareas):
        #if self.buscar(x,y):

        nodoN = NodoMatriz(dia=dia,hora=hora,ntareas=ntareas)
        if  self.NodoRaiz is None:
            self.NodoRaiz = NodoRaiz()
            self.NodoRaiz.NodoColumnas=NodoCabecera(tipo="Columna",indice=dia)
            self.NodoRaiz.NodoFilas=NodoCabecera(tipo="Fila",indice=hora)
            self.NodoRaiz.NodoColumnas.siguiente =None   
            self.NodoRaiz.NodoFilas.siguiente =None
            self.NodoRaiz.NodoColumnas.abajo=nodoN
            self.NodoRaiz.NodoFilas.derecha=nodoN
        else:
            Nodotemporal=self.NodoRaiz
            self.insertar_cabercera(Nodotemporal.NodoFilas,hora,"Fila")
            Nodotemporal=self.NodoRaiz
            self.insertar_cabercera(Nodotemporal.NodoColumnas,dia,"Columna")
            self.insertar_nodo_fila(nodo=nodoN)
            self.insertar_nodo_col(nodo=nodoN)


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

    def graficar_matriz(self):
        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        # grafo+=str("rankdir=LR;\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")
        nodo = self.NodoRaiz.NodoFilas

        for hora in range(1, 11):
            nodo_temp = nodo.derecha
            for dia in range(1, 11):
                if (self.buscar(dia, hora)):
                    grafo += str(
                        "p" + str(dia) +"_"+ str(hora) + "[label=\"{<data>" + "Dia: "+ str(dia) + "\\n" +"Hora: "+ str(hora) + "| info }\" pos=\"" + str(
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
        for dia in range(1, 11):
            nodo_temp = nodo.abajo
            for hora in range(1, 11):
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
        f = open("dispersa"+str(self.cont)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica *********  ")
        os.system("fdp -Tpng -o disp"+str(self.cont)+".png dispersa"+str(self.cont)+".dot")
        self.cont +=1






