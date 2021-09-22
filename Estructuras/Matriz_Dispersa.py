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
        while(temporalfila.indice!=nodo.y): 
            temporalfila = temporalfila.siguiente
        #temporalfila=temporalfila.derecha
        if temporalfila.derecha is None:
            nodo.derecha=temporalfila.derecha 
            temporalfila.derecha = nodo 
        elif temporalfila.derecha.x >= nodo.x: 
            nodo.derecha = temporalfila.derecha
            temporalfila.derecha = nodo 
        else : 
            current = temporalfila.derecha 
            while(current.derecha is not None and current.derecha.x < nodo.x): 
                current = current.derecha
            nodo.derecha = current.derecha
            current.derecha = nodo
    def insertar_nodo_col(self,nodo):
        temporalcol = self.NodoRaiz.NodoColumnas 
        while(temporalcol.indice!=nodo.x): 
            temporalcol= temporalcol.siguiente
        #temporalcol=temporalcol.abajo
        if temporalcol.abajo is None: 
            nodo.abajo = temporalcol.abajo
            temporalcol.abajo = nodo
        elif temporalcol.abajo.y >= nodo.y: 
            nodo.abajo = temporalcol.abajo
            temporalcol.abajo = nodo
        else : 
            current = temporalcol.abajo
            while(current.abajo is not None and current.abajo.y < nodo.y): 
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
                
    def insertar(self,x,y,informacion):
        nodoN = NodoMatriz(x=x,y=y,dato=informacion)
        if  self.NodoRaiz is None:
            self.NodoRaiz= NodoRaiz()
            self.NodoRaiz.NodoColumnas=NodoCabecera(tipo="Columna",indice=x) 
            self.NodoRaiz.NodoFilas=NodoCabecera(tipo="Fila",indice=y)
            self.NodoRaiz.NodoColumnas.siguiente =None   
            self.NodoRaiz.NodoFilas.siguiente =None
            self.NodoRaiz.NodoColumnas.abajo=nodoN
            self.NodoRaiz.NodoFilas.derecha=nodoN
        else:
            Nodotemporal=self.NodoRaiz
            self.insertar_cabercera(Nodotemporal.NodoFilas,y,"Fila")
            Nodotemporal=self.NodoRaiz
            self.insertar_cabercera(Nodotemporal.NodoColumnas,x,"Columna")
            self.insertar_nodo_fila(nodo=nodoN)
            self.insertar_nodo_col(nodo=nodoN)
    def buscar(self,x,y):
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                if nodo_temp.x ==x and nodo_temp.y==y:
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

        for y in range(1, 11):
            nodo_temp = nodo.derecha
            for x in range(1, 11):
                if (self.buscar(x, y)):
                    grafo += str(
                        "p" + str(x) + str(y) + "[label=\"{<data>" + "Dia: "+ str(x) + "\\n" +"Hora: "+ str(y) + "| info }\" pos=\"" + str(
                            x) + "," + str(10 - y) + "!\"];\n")
                    if (nodo_temp.derecha != None):
                        nodo_2 = nodo_temp
                        nodo_temp = nodo_temp.derecha
                        grafo += str("p" + str(nodo_2.x) + str(nodo_2.y) + "->" + "p" + str(nodo_temp.x) + str(
                            nodo_temp.y) + "[dir=both];\n")
                else:
                    pass
                if nodo.siguiente != None:
                    if nodo.siguiente.indice == y + 1:
                        nodo = nodo.siguiente
        nodo = self.NodoRaiz.NodoColumnas
        for x in range(1, 11):
            nodo_temp = nodo.abajo
            for y in range(1, 11):
                if (self.buscar(x, y)):
                    if (nodo_temp.abajo != None):
                        nodo_2 = nodo_temp
                        nodo_temp = nodo_temp.abajo
                        grafo += str("p" + str(nodo_2.x) + str(nodo_2.y) + "->" + "p" + str(nodo_temp.x) + str(nodo_temp.y) + "[dir=both];\n")
                else:
                    pass
                if nodo.siguiente != None:
                    if nodo.siguiente.indice == x + 1:
                        nodo = nodo.siguiente
        grafo += str("}\n")
        tmp = self.cont
        f = open("dispersa"+str(self.cont)+".dot", "w+")
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica *********  ")
        os.system("fdp -Tpng -o disp"+str(self.cont)+".png dispersa"+str(self.cont)+".dot")
        self.cont +=1






