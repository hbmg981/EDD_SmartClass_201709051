#from Estructuras.Lista_A import ListaA
from cryptography.fernet import Fernet
#from inicio import f,key
key = Fernet.generate_key()
f = Fernet(key)

class Nodo:

    #key = None
    #f = None
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
        self.key = None
        self.f = None

        #self.lista = ListaA()

    def generarClave(self):
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)

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
        nombre = str(f.decrypt(self.nombre).decode())
        dpi = str(f.decrypt(self.dpi).decode())
        correo = str(f.decrypt(self.correo).decode())
        password = str(f.decrypt(self.password).decode())
        edad = str(f.decrypt(self.edad).decode())
        if self.left is None and self.right is None:
            info = "Carnet: "+ str(self.carnet) + "\\n Nombre: "+  f.decrypt(self.nombre).decode() + "\\n Carrera: "+ self.carrera\
                   + "\\n DPI: " + dpi+ "\\n Correo: " + correo+ "\\n Password: " + password[0:15]\
                   + "\\n Edad: " + edad+ "\\n Creditos: " + "Calificacion"

            grafo = "\t nodo_"+str(self.carnet)+ "[label = \"" + info + "\"];\n"
            return grafo
        else:
            grafo=""
            if self.left is not None:

                #carrera =str(f.decrypt(self.carrera).decode())
                info = " Carnet: " + str(self.carnet) + "\\n Nombre: " + nombre+ "\\n Carrera: " + self.carrera\
                       + "\\n DPI: " + dpi+ "\\n Correo: " + correo+ "\\n Password: " + password[0:15]\
                       + "\\n Edad: " + edad+ "\\n Creditos: " + str(self.creditos)

                grafo += "\t nodo_" + str(self.carnet) + "[label = \"" + info + "\"];\n" + self.left.textoLabel()


            if self.right is not None:
                info = " Carnet: " + str(self.carnet) + "\\n Nombre: " + f.decrypt(self.nombre).decode() + "\\n Carrera: " + self.carrera\
                       + "\\n DPI: " + dpi + "\\n Correo: " + correo + "\\n Password: " + password[0:15] \
                       + "\\n Edad: " + edad + "\\n Creditos: " + str(self.creditos)

                grafo += "\t nodo_" + str(self.carnet) + "[label = \"" + info + "\"];\n" +self.right.textoLabel()

            return grafo








    def _textoLabel(self):
        if self.left is None and self.right is None:
            carnet = f.encrypt(str(self.carnet).encode())
            info = "Carnet: "+ str(carnet)[0:6] + "\\nNombre: "+  str(self.nombre)[0:6] + "\\nCarrera: "+ self.carrera+ "\\n DPI: "+  str(self.dpi)[0:6]\
                   + "\\nCorreo: " + str(self.correo)[0:6] + "\\nPassword: " + str(self.password)[0:6]\
                   + "\\nEdad: " + str(self.edad)[0:6]+ "\\nCreditos: " + str(self.creditos)
            grafo = "\t nodo_"+str(self.carnet)+ "[label = \"" + info + "\"];\n"
            return grafo
        else:
            grafo=""
            if self.left is not None:
                carnet = f.encrypt(str(self.carnet).encode())
                #carrera =f.decrypt(self.carrera).decode()
                info = " Carnet: " + str(carnet)[0:6] + "\\n Nombre: " + str(self.nombre)[0:6]+ "\\n Carrera: " + self.carrera+ "\\n DPI: "\
                       +str(self.dpi)[0:6]+ "\\nCorreo: " + str(self.correo)[0:6] + "\\nPassword: " + str(self.password)[0:6]\
                       + "\\nEdad: " + str(self.edad)[0:6]+ "\\nCreditos: " + str(self.creditos)
                grafo += "\t nodo_" + str(self.carnet) + "[label = \"" + info + "\"];\n" + self.left._textoLabel()


            if self.right is not None:
                carnet = f.encrypt(str(self.carnet).encode())
                info = " Carnet: " + str(carnet)[0:6] + "\\n Nombre: " + str(self.nombre)[0:6] + "\\n Carrera: " + self.carrera+ "\\n DPI: "+  str(self.dpi)[0:6]\
                       + "\\nCorreo: " + str(self.correo)[0:6] + "\\nPassword: " + str(self.password)[0:6]\
                       + "\\nEdad: " + str(self.edad)[0:6]+ "\\nCreditos: " + str(self.creditos)
                grafo += "\t nodo_" + str(self.carnet) + "[label = \"" + info + "\"];\n" +self.right._textoLabel()

            return grafo

    def _textoGraf(self):
        if self.left is None and self.right is None:
            text="nodo_"+str(self.carnet)
            return text
        else:
            texto=""
            if self.left is not None:
                texto += "nodo_"+str(self.carnet) + "->" + ""+str(self.left._textoGraf())+ "\n"

            if self.right is not None:
                texto += "nodo_"+str(self.carnet) + "->" + ""+str(self.right._textoGraf()) + "\n"

            return texto


