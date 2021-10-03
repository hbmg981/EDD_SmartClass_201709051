from Estructuras.Lista_A import ListaA
class Nodo:
    def __init__(self, carnet,dpi,nombre,carrera,correo,password,creditos,edad):
        self.carnet = carnet
        self.left = None
        self.right = None
        self.height = 0
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.lista = ListaA()

    def textoGraf(self):
        if self.left is None and self.right is None:
            text="nodo_"+str(self.carnet)
            return text
        else:
            texto=""
            if self.left is not None:
                texto += "nodo_"+str(self.carnet) + "->" + ""+str(self.left.textoGraf())+ "\n"

            if self.right is not None:
                texto += "nodo_"+str(self.carnet) + "->" + ""+str(self.right.textoGraf()) + "\n"

            return texto


    def textoLabel(self):
        if self.left is None and self.right is None:
            info = "Carnet: "+ str(self.carnet) + "\\n Nombre: "+ self.nombre + "\\n Carrera: "+ self.carrera
            grafo = "\t nodo_"+str(self.carnet)+ "[label = \"" + info + "\"];\n"
            return grafo
        else:
            grafo=""
            if self.left is not None:

                info = " Carnet: " + str(self.carnet) + "\\n Nombre: " + self.nombre + "\\n Carrera: " + self.carrera
                grafo += "\t nodo_" + str(self.carnet) + "[label = \"" + info + "\"];\n" + self.left.textoLabel()


            if self.right is not None:
                info = " Carnet: " + str(self.carnet) + "\\n Nombre: " + self.nombre + "\\n Carrera: " + self.carrera
                grafo += "\t nodo_" + str(self.carnet) + "[label = \"" + info + "\"];\n" +self.right.textoLabel()

            return grafo
