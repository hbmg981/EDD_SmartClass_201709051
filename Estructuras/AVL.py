from Estructuras.Nodo_AVL import Nodo

class AVL:
    def __init__(self):
        self.Root = None

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

    def insert(self, carnet,dpi,nombre,carrera,correo,password,creditos,edad):
        self.Root = self.insert_inter(carnet,dpi,nombre,carrera,correo,password,creditos,edad, self.Root)

    def insert_inter(self, carnet,dpi,nombre,carrera,correo,password,creditos,edad ,root):
        if root is None:
            # cuando no hay datos en el avl
            return Nodo(carnet,dpi,nombre,carrera,correo,password,creditos,edad)
        else:
            if carnet < root.carnet:
                root.left = self.insert_inter(carnet,dpi,nombre,carrera,correo,password,creditos,edad, root.left)
                if self.height(root.right) - self.height(root.left) == -2:
                    if carnet < root.left.carnet:
                        root = self.RD(root)
                        print("Rotacion simple derecha")
                    else:
                        root = self.RID(root)
                        print("Rotacion doble derecha")
            elif carnet > root.carnet :
                root.right = self.insert_inter(carnet,dpi,nombre,carrera,correo,password,creditos,edad, root.right)
                if self.height(root.right) - self.height(root.left) == 2:
                    if carnet > root.right.carnet:
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

    def pre_orden(self):
        self.pre_orden_intern(self.Root)

    def pre_orden_intern(self, root):
        if root is not None:
            print("CARNET: "+ str(root.carnet) + " NOMBRE: "+ root.nombre)
            self.pre_orden_intern(root.left)
            self.pre_orden_intern(root.right)

    def eliminar(self, carnet):
        self.Root = self.eliminarAVL(self.Root, carnet)

    def eliminarAVL(self,nodoActual, carnet):
        if nodoActual == None:
            return nodoActual
        if carnet < nodoActual.carnet:
            nodoActual.left = self.eliminarAVL(nodoActual.left,carnet)
        elif carnet> nodoActual.carnet:
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

    def buscarDato(self, raiz, carnet):
        if raiz is None:
            return False
        elif raiz.carnet == carnet:
            return True
        elif carnet < raiz.carnet:
            return self.buscarDato(raiz.izquierda, carnet)
        else:
            return self.buscarDato(raiz.izquierda,carnet)

    def buscarRetornar(self, raiz, carnet):
        if raiz is None:
            return raiz
        elif raiz.carnet == carnet:
            return raiz
        elif carnet < raiz.carnet:
            return self.buscarDato(raiz.izquierda, carnet)
        else:
            return self.buscarDato(raiz.izquierda,carnet)


    #def graficarListaTareas(self, carnet, año, mes, dia, hora):
        #if self.buscarDato(self.Root, carnet):
            #self.buscarRetornar(self.Root, carnet).lista.



