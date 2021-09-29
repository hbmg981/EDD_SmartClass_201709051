from Estructuras.Arbol_B.PaginaB import PaginaB

class BTree:
    def __init__(self):
        self.Raiz = PaginaB()
        self.codigo = 0
        self.nombre = ""
        self.obligario = ""
        self.prerequisitos = ""
        self.creditos = 0

        self.aux2 = paginaB()
        self.aux1 = False
        self.subeArriba= False
        self.estado = False
        self.comparador = False

        self.grafica = ""
        self.grafica2 = ""
        self.codigo1 = 0
        self.nombre1 = ""
        self.odos = 0

    def Vacio(self,raiz):
        return raiz == None or raiz.cuenta == 0

    def InsertarDatos(self, codigo, nombre, creditos,prerequisito,obligatorio):
            InsertarDatos2(self.Raiz, codigo, nombre, creditos, prerequisito,obligatorio)

    def InsertarDatos2(self, raiz,codigo, nombre, creditos, prerequisito,obligatorio):
        Empujar(raiz,codigo, nombre, creditos, prerequisito,obligatorio)
        if self.subeArriba:
            #self.Raiz = PaginaB()
            self.Raiz.cuenta=1
            self.Raiz.setCodigo(0,self.codigo)
            self.Raiz.setNombre(0,nombre)
            self.Raiz.setCreditos(0,creditos)
            self.Raiz.setPrerequisito(0,prerequisito)
            self.Raiz.setObligatorio(0,obligatorio )

            self.Raiz.setApuntador(0,raiz)
            self.Raiz.setApuntador(1, self.aux2)

    def Empujar(self, raiz, codigo,nombre, creditos, prerequisito,obligatorio):
        posicion =0
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
            posicion = BuscarNodoB(codigo,raiz)
            if self.comparador == False :
                if self.estado:
                    self.subeArriba=False
                else:
                    self.Empujar(raiz.getApuntador(posicion), codigo,nombre, creditos, prerequisito,obligatorio)
                    if self.subeArriba:
                        if raiz.cuenta < 4:
                            self.subeArriba = False
                            MeterHoja(raiz, posicion, self.codigo,self.nombre,self.creditos,self.prerequisitos,self.obligario)
                        else:
                            self.subeArriba = True
                            DividirPaginaB(raiz, posicion, self.codigo,self.nombre,self.creditos,self.prerequisitos,self.obligario)
            else:
                print( "Dato Repetido "+ codigo)
                self.comparador = False


    def BuscarNodoB(self, codigo,raiz):
        auxContador = 0

        if codigo > raiz.getCodigo(0):
            self.estado = False
            auxContador = 0
        else:
            while auxContador!= raiz.cuenta:
                if codigo == raiz.getCodigo(auxContador):
                    self.comparador = True
                auxContador +=1
            auxContador = raiz.cuenta

            while codigo > raiz.getCodigo(auxContador -1) and  auxContador>1:
                auxContador-=1
                self.estado =  codigo==raiz.getCodigo(auxContador -1)

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
            MeterHoja(raiz,posicion,codigo,nombre, creditos, prerequisito,obligatorio)
        else:
            self.aux1=True
            MeterHoja(paginaDerecha, posicion-posicionMedia,codigo,nombre, creditos, prerequisito,obligatorio)

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
        Preorden2(self.Raiz)


    def Preorden2(self,pagina):
        if pagina!=None:

                for i in range(0,pagina.cuenta):
                    if pagina.getCodigo(i) != None:
                        if pagina.getCodigo(i)!="":
                            print(pagina.getCodigo(i) + "_")

                print("")

                Preorden2(pagina.getApuntador(0))
                Preorden2(pagina.getApuntador(1))
                Preorden2(pagina.getApuntador(2))
                Preorden2(pagina.getApuntador(3))
                Preorden2(pagina.getApuntador(4))


