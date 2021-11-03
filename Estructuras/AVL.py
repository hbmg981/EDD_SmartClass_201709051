from Estructuras.Nodo_AVL import Nodo,f
import  os
#from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#f = Fernet(key)
import hashlib

class AVL:
    def __init__(self):
        self.Root = None
        self.ngraf =1

    def MAX(self, carnet1,carnet2):
        if carnet1 > carnet2:
            return carnet1
        else:
            return carnet2



    def height(self, node):
        if node is not None:
            return node.height
        else:
            return -1

    def insert(self, carnet,dpi,nombre,carrera,correo,password,edad,creditos=0):
        dpi_ = f.encrypt(str(dpi).encode())
        nombre_ = f.encrypt(nombre.encode())
        correo_ = f.encrypt(correo.encode())
        paw = bytes(password,"ascii")
        passw = hashlib.sha256(paw)
        passw_hex = passw.hexdigest()
        #print(passw_hex)
        password_ = f.encrypt(passw_hex.encode())
        edad_ = f.encrypt(str(edad).encode())
        self.Root = self.insert_inter(carnet,dpi_,nombre_,carrera,correo_,password_,creditos,edad_, self.Root)

    def insert_inter(self, carnet,dpi,nombre,carrera,correo,password,creditos,edad ,root):
        if root is None:
            # cuando no hay datos en el avl
            #carnet_ = f.encrypt(str(carnet).encode())
            return Nodo(carnet,dpi,nombre,carrera,correo,password,creditos,edad)
        else:
            if int(carnet) < int(root.carnet):
                root.left = self.insert_inter(carnet,dpi,nombre,carrera,correo,password,creditos,edad, root.left)
                if self.height(root.right) - self.height(root.left) == -2:
                    if int(carnet) < int(root.left.carnet):
                        root = self.RD(root)
                        print("Rotacion simple derecha")
                    else:
                        root = self.RID(root)
                        print("Rotacion doble derecha")
            elif int(carnet) > int(root.carnet) :
                root.right = self.insert_inter(carnet,dpi,nombre,carrera,correo,password,creditos,edad, root.right)
                if self.height(root.right) - self.height(root.left) == 2:
                    if int(carnet) > int(root.right.carnet):
                        root = self.RI(root)
                        print("Rotacion simple izquierda")
                    else:
                        root = self.RDI(root)
                        print("Rotacion doble izquierda")
            else:
                root.carnet = carnet

        root.height = self.MAX(self.height(root.left), self.height(root.right)) + 1
        return root



    def RD(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        node.height = self.MAX(self.height(node.left), self.height(node.right)) + 1
        aux.height = self.MAX(self.height(aux.left), node.height) + 1
        return aux

    def RI(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        node.height = self.MAX(self.height(node.left), self.height(node.right)) + 1
        aux.height = self.MAX(self.height(aux.right), node.height) + 1
        return aux

    def RID(self, node):
        node.left = self.RI(node.left)
        return self.RD(node)

    def RDI(self, node):
        node.right = self.RD(node.right)
        return self.RI(node)



    def eliminar(self, carnet):
        self.Root = self.eliminarAVL(self.Root, carnet)

    def eliminarAVL(self,nodoActual, carnet):
        if nodoActual == None:
            return nodoActual
        if int(carnet) < int (nodoActual.carnet):
            nodoActual.left = self.eliminarAVL(nodoActual.left,carnet)
        elif int(carnet) > int(nodoActual.carnet):
            nodoActual.right = self.eliminarAVL(nodoActual.right, carnet)
        else:
            if nodoActual.left ==None or nodoActual.right:
                temp = None
                if temp == nodoActual.left:
                    temp = nodoActual.right
                else:
                    temp = nodoActual.left

                if temp == None:
                    nodoActual = None
                else:
                    nodoActual = temp

            else:

                temp = self.getNodoConValorMaximo(nodoActual.left)

                nodoActual.carnet = temp.carnet

                nodoActual.left = self.eliminarAVL(nodoActual.left, temp.carnet)

        if nodoActual==None:
            return nodoActual

        nodoActual.height = self.MAX(self.height(nodoActual.left), self.height(nodoActual.right))+1

        fe= self.getFactorEquilibrio(nodoActual)

        if fe>1 and self.getFactorEquilibrio(nodoActual.left)>=0:
            return self.RD(nodoActual)

        if fe < -1 and self.getFactorEquilibrio(nodoActual.right)<=0:
            return self.RI(nodoActual)

        if fe >1 and self.getFactorEquilibrio(nodoActual.left)<0:
            nodoActual.left = self.RI(nodoActual.left)
            return self.RD(nodoActual)

        if fe<-1 and self.getFactorEquilibrio(nodoActual.right)>0:
            nodoActual.right = self.RD(nodoActual.right)
            return self.RI(nodoActual)

        return nodoActual

    def getFactorEquilibrio(self,nodoActual):
        if nodoActual== None:
            return 0
        return self.height(nodoActual.left) - self.height(nodoActual.right)



    def getNodoConValorMaximo(self, node):
        current = node
        while current.right != None:
            current = current.right

        return current


    def buscarDato(self, carnet):
        raiz = self.Root
        while int(raiz.carnet) != carnet:
            if int(carnet) < int(raiz.carnet):
                raiz = raiz.left
            else:
                raiz = raiz.right
            if raiz is None:
                return False

        return True

    def pre_orden(self):
        self.pre_orden_intern(self.Root)

    def pre_orden_intern(self, root):
        if root is not None:
            #f.decrypt(root.nombre).decode()
            print("CARNET: "+ str(root.carnet) + " NOMBRE: "+ f.decrypt(root.nombre).decode())
            #root.lista.getList()
            self.pre_orden_intern(root.left)
            self.pre_orden_intern(root.right)


    def _pre_orden(self):
        self._pre_orden_intern(self.Root)

    def _pre_orden_intern(self, root):
        if root is not None:
            #f.decrypt(root.nombre).decode()
            carnet = f.encrypt(str(root.carnet).encode())
            print("CARNET: "+ str(carnet)[0:20] + " NOMBRE: "+ str(root.nombre)[0:20])
            #root.lista.getList()
            self._pre_orden_intern(root.left)
            self._pre_orden_intern(root.right)


    def buscarRetornar(self, carnet):
        raiz = self.Root
        while int(raiz.carnet) != carnet:
            if int(carnet) < int(raiz.carnet):
                raiz = raiz.left
            else:
                raiz = raiz.right
            if raiz is None:
                return raiz

        return raiz


    def graficarListaTareas(self, carnet, año, mes, dia, hora):
        if self.buscarDato( carnet):
            print("El carnet: "+str(carnet)+ " Existe")

        else:
            print("No se encontro el carnet: "+ str(carnet))

    def graficar(self):
        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        grafo+=str("rankdir=TB;\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")


        aux = self.Root
        cont = 0

        if self.Root is not None:

            grafo+=self.Root.textoLabel()
            grafo+=self.Root.textoGraf()


        grafo += str("}\n")

        f = open("avldot"+str(self.ngraf)+".dot", 'w',encoding='utf-8')
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica  AVL *********  " + str(self.ngraf))
        os.system("dot -Tsvg -o avlg"+str(self.ngraf)+".svg avldot"+str(self.ngraf)+".dot")
        self.ngraf +=1

    def Modificar(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad):
        self.buscarRetornar(carnet).dpi = dpi
        self.buscarRetornar(carnet).nombre = nombre
        self.buscarRetornar(carnet).carrera =carrera
        self.buscarRetornar(carnet).coreo = correo
        self.buscarRetornar(carnet).password =password
        self.buscarRetornar(carnet).creditos = creditos
        self.buscarRetornar(carnet).edad = edad

    def _graficar(self):
        grafo = "digraph"
        grafo += str("{\nnode[shape=record];\n")
        grafo += str("graph[pencolor=transparent];\n")
        grafo+=str("rankdir=TB;\n")
        grafo += str("node [style=filled,fillcolor=thistle1];\n")


        aux = self.Root
        cont = 0

        if self.Root is not None:

            grafo+=self.Root._textoLabel()
            grafo+=self.Root._textoGraf()


        grafo += str("}\n")

        f = open("avldot"+str(self.ngraf)+".dot", 'w',encoding='utf-8')
        f.write(grafo)
        f.close()
        print("********* Se realizo Grafica  AVL *********  " + str(self.ngraf))
        os.system("dot -Tsvg -o avlg"+str(self.ngraf)+".svg avldot"+str(self.ngraf)+".dot")
        self.ngraf +=1







