from Estructuras.Arbol_B.PaginaB import PaginaB
import  os
class BTree:
    def __init__(self):
        self.Raiz = None
        self.codigo = 0
        self.nombre = ""
        self.obligario = ""
        self.prerequisitos = ""
        self.creditos = 0
        self.ngraf =0

        self.aux2 = None
        self.aux1 = False
        self.subeArriba= False
        self.estado = False
        self.comparador = False

        self.grafica = ""
        self.grafica2 = ""
        self.codigo1 = 0
        self.nombre1 = ""
        self.nodos = 0

    def Vacio(self,raiz):
        return raiz is None or raiz.cuenta == 0

    def InsertarDatos(self, codigo, nombre, creditos,prerequisito,obligatorio):
            self.InsertarDatos2(self.Raiz, codigo, nombre, creditos, prerequisito,obligatorio)

    def InsertarDatos2(self, raiz,codigo, nombre, creditos, prerequisito,obligatorio):
        self.Empujar(raiz,codigo, nombre, creditos, prerequisito,obligatorio)
        if self.subeArriba:
            self.Raiz = PaginaB()
            self.Raiz.cuenta=1
            self.Raiz.setCodigo(0,self.codigo)
            self.Raiz.setNombre(0,nombre)
            self.Raiz.setCreditos(0,creditos)
            self.Raiz.setPrerequisito(0,prerequisito)
            self.Raiz.setObligatorio(0,obligatorio )

            self.Raiz.setApuntador(0,raiz)
            self.Raiz.setApuntador(1, self.aux2)

    def Empujar(self, raiz, codigo,nombre, creditos, prerequisito,obligatorio):
        posicion = 0
        self.estado = False

        if self.Vacio(raiz) and self.comparador ==False:
            self.subeArriba = True
            self.codigo = codigo
            self.nombre = nombre
            self.creditos = creditos
            self.prerequisitos = prerequisito
            self.obligario = obligatorio
            self.aux2 = None
        else:
            posicion = self.BuscarNodoB(codigo,raiz)
            if self.comparador == False :
                if self.estado:
                    self.subeArriba=False
                else:
                    self.Empujar(raiz.getApuntador(posicion), codigo,nombre, creditos, prerequisito,obligatorio)
                    if self.subeArriba:
                        if raiz.cuenta < 4:
                            self.subeArriba = False
                            self.MeterHoja(raiz, posicion, self.codigo,self.nombre,self.creditos,self.prerequisitos,self.obligario)
                        else:
                            self.subeArriba = True
                            self.DividirPaginaB(raiz, posicion, self.codigo,self.nombre,self.creditos,self.prerequisitos,self.obligario)
            else:
                print( "Dato Repetido "+ codigo)
                self.comparador = False


    def _BuscarNodoB(self, codigo,raiz):
        auxContador = 0
        codigomenor = False
        codigomenorcont = False

        if codigo<raiz.getCodigo(0):
            codigomenor = True

        if codigomenor:
            self.estado = False
            print("El codigo es menor al de la raiz")
            auxContador = 0
        else:
            while auxContador!= raiz.cuenta:

                if codigo == raiz.getCodigo(auxContador):
                    self.comparador = True
                auxContador +=1
            auxContador = raiz.cuenta
            if codigo < raiz.getCodigo(auxContador - 1):
                codigomenorcont = True
            while codigomenorcont and  auxContador>1:
                auxContador-=1
                self.estado =  codigo==raiz.getCodigo(auxContador -1)

        return auxContador

    def BuscarNodoB(self,codigo,raiz):
        auxContador = 0

        if codigo < raiz.getCodigo(0):
            self.estado = False
            auxContador = 0
        else:
            while auxContador!= raiz.cuenta:
                if codigo==raiz.getCodigo(auxContador):
                    self.comparador = True
                auxContador+=1

            auxContador = raiz.cuenta

            while codigo < raiz.getCodigo(auxContador-1) and auxContador>1:
                auxContador-=1

                self.estado = codigo==raiz.getCodigo(auxContador-1)

        return auxContador





    def MeterHoja(self, raiz,posicion, codigo,nombre, creditos, prerequisito,obligatorio):
        auxC = raiz.cuenta

        while auxC!=posicion:
            if auxC!=0:
                raiz.setCodigo(auxC, raiz.getCodigo(auxC-1))
                raiz.setNombre(auxC, raiz.getNombre(auxC - 1))
                raiz.setCreditos(auxC, raiz.getCreditos(auxC - 1))
                raiz.setPrerequisito(auxC, raiz.getPrerequisito(auxC - 1))
                raiz.setObligatorio(auxC, raiz.getObligatorio(auxC - 1))
                raiz.setApuntador(auxC+1, raiz.getApuntador(auxC))
            auxC -=1

        raiz.setCodigo(posicion,codigo)
        raiz.setNombre(posicion,nombre )
        raiz.setCreditos(posicion,creditos )
        raiz.setPrerequisito(posicion, prerequisito )
        raiz.setObligatorio(posicion,obligatorio )
        raiz.setApuntador(posicion+1, self.aux2)
        raiz.cuenta = raiz.cuenta + 1

    def DividirPaginaB(self,raiz,posicion, codigo,nombre, creditos, prerequisito,obligatorio ):
        posicion2 = 0
        posicionMedia = 0
        if posicion<=2:
            posicionMedia=2
        else:
            posicionMedia=3

        paginaDerecha = PaginaB()
        posicion2=posicionMedia+1

        while posicion2!=5:
            if posicion2 - posicionMedia !=0:
                paginaDerecha.setCodigo(posicion2-posicionMedia-1, raiz.getCodigo(posicion2-1))
                paginaDerecha.setNombre(posicion2 - posicionMedia - 1, raiz.getNombre(posicion2 - 1))
                paginaDerecha.setCreditos(posicion2 - posicionMedia - 1, raiz.getCreditos(posicion2 - 1))
                paginaDerecha.setPrerequisito(posicion2 - posicionMedia - 1, raiz.getPrerequisito(posicion2 - 1))
                paginaDerecha.setObligatorio(posicion2 - posicionMedia - 1, raiz.getObligatorio(posicion2 - 1))
                paginaDerecha.setApuntador(posicion2-posicionMedia-1, raiz.getApuntador(posicion2))
            posicion2+=1

        paginaDerecha.cuenta = 4- posicionMedia
        raiz.cuenta = posicionMedia

        if posicion<=2:
            self.aux1 = True
            self.MeterHoja(raiz,posicion,codigo,nombre, creditos, prerequisito,obligatorio)
        else:
            self.aux1=True
            self.MeterHoja(paginaDerecha, posicion-posicionMedia,codigo,nombre, creditos, prerequisito,obligatorio)

        self.codigo = raiz.getCodigo(raiz.cuenta -1)
        self.nombre = raiz.getNombre(raiz.cuenta -1)
        self.creditos = raiz.getCreditos(raiz.cuenta - 1)
        self.prerequisitos = raiz.getPrerequisito(raiz.cuenta - 1)
        self.obligario = raiz.getObligatorio(raiz.cuenta - 1)

        paginaDerecha.setApuntador(0, raiz.getApuntador(raiz.cuenta))

        raiz.cuenta = raiz.cuenta -1
        self.aux2= paginaDerecha

        if self.aux1:
            raiz.setCodigo(3,"")
            raiz.setNombre(3,"")
            raiz.setCreditos(3,"")
            raiz.setPrerequisito(3, "")
            raiz.setObligatorio(3, "")
            raiz.setApuntador(4, None)

            raiz.setCodigo(2, "")
            raiz.setNombre(2, "")
            raiz.setCreditos(2, "")
            raiz.setPrerequisito(2, "")
            raiz.setObligatorio(2, "")
            raiz.setApuntador(3, None)


    def Preorden(self):
        self.Preorden2(self.Raiz)


    def Preorden2(self,pagina):
        if pagina!=None:

                for i in range(0,pagina.cuenta):
                    if pagina.getCodigo(i) != None:
                        if pagina.getCodigo(i)!="":
                            print( str(pagina.getCodigo(i)) + "_")

                print("")

                self.Preorden2(pagina.getApuntador(0))
                self.Preorden2(pagina.getApuntador(1))
                self.Preorden2(pagina.getApuntador(2))
                self.Preorden2(pagina.getApuntador(3))
                self.Preorden2(pagina.getApuntador(4))


    def Graficar(self):
        self.ngraf+=1
        self.grafica = "digraph ArbolB { \n"
        self.grafica+= "\n\trankdir= TB;\n"
        self.grafica+= "node [color=\"mediumvioletred\", style = \"rounded,filled\",fillcolor=thistle1, shape=record];\n"

        self.Graficar2(self.Raiz)
        self.Graficar3(self.Raiz)

        self.grafica+="\n}\n"

        #mandar a graficar

        f = open("ArbolB" + str(self.ngraf) + ".dot", "w+", encoding='utf8')
        f.write(self.grafica)
        f.close()
        print("********* Se realizo Grafica de Arbol B *********  ")
        os.system("dot -Tsvg -o Arbol" + str(self.ngraf) + ".svg ArbolB" + str(self.ngraf) + ".dot")


    def Graficar2(self, pagina):
        contador = 0
        if pagina is not None:
            self.nodos =0
            for i in range(0, pagina.cuenta):
                if pagina.getCodigo(i) is not None:
                    if pagina.getCodigo(i) != "":
                        self.nodos +=1
                        if i !=0:
                            self.grafica += "|"

                        if self.nodos ==1:
                            self.grafica += "\nNodo"+str(pagina.getCodigo(i))+"[label=\"<f0> |"

                        if i==0:
                            self.grafica += "<f" + str(i+1) + ">" + str(pagina.getCodigo(i)) + "\\n" + pagina.getNombre(i) + "|<f" + str(i + 2) + "> "
                            contador = 3
                        else:
                            self.grafica += "<f" + str(contador) + ">" + str(pagina.getCodigo(i)) + "\\n" + pagina.getNombre(i) + "|<f" + str(contador + 1) + "> "
                            contador += 2

                        if i == pagina.cuenta -1:
                            contador = 0
                            self.grafica += " \",group=0];\n"

            self.Graficar2(pagina.getApuntador(0))
            self.Graficar2(pagina.getApuntador(1))
            self.Graficar2(pagina.getApuntador(2))
            self.Graficar2(pagina.getApuntador(3))
            self.Graficar2(pagina.getApuntador(4))


    def Graficar3(self, pagina):
        if pagina is not None:
            if pagina.getCodigo(0 ) is not None:
                if pagina.getCodigo(0) != "":
                    if pagina.getApuntador(0) is not None and pagina.getApuntador(0).getCodigo(0) is not None:
                        self.grafica += "\nNodo"+str(pagina.getCodigo(0))+":f0->"+"Nodo"+ str(pagina.getApuntador(0).getCodigo(0))

                    if pagina.getApuntador(1) is not None and pagina.getApuntador(1).getCodigo(0) is not None:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0)) + ":f2->" + "Nodo" + str(pagina.getApuntador(1).getCodigo(0))

                    if pagina.getApuntador(2) is not None and pagina.getApuntador(2).getCodigo(0) is not None:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0)) + ":f4->" + "Nodo" + str(pagina.getApuntador(2).getCodigo(0))

                    if pagina.getApuntador(3) is not None and pagina.getApuntador(3).getCodigo(0) is not None:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0)) + ":f6->" + "Nodo" + str(pagina.getApuntador(3).getCodigo(0))

                    if pagina.getApuntador(4) is not None and pagina.getApuntador(4).getCodigo(0) is not None:
                        self.grafica += "\nNodo" + str(pagina.getCodigo(0))+ ":f8->" + "Nodo" + str(pagina.getApuntador(4).getCodigo(0))

            self.Graficar3(pagina.getApuntador(0))
            self.Graficar3(pagina.getApuntador(1))
            self.Graficar3(pagina.getApuntador(2))
            self.Graficar3(pagina.getApuntador(3))
            self.Graficar3(pagina.getApuntador(4))


