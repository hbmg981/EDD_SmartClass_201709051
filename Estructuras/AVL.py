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

    def insert(self, carnet):
        self.Root = self.insert_inter(carnet, self.Root)

    def insert_inter(self, carnet, root):
        if root is None:
            return Nodo(carnet)
        else:
            if carnet < root.carnet:
                root.left = self.insert_inter(carnet, root.left)
                if self.height(root.right) - self.height(root.left) == -2:
                    if carnet < root.left.carnet:
                        root = self.RI(root)
                        print("Rotacion simple izquierda")
                    else:
                        root = self.RDI(root)
                        print("Rotacion doble izquierda")
            elif carnet > root.carnet :
                root.right = self.insert_inter(carnet, root.right)
                if self.height(root.right) - self.height(root.left) == 2:
                    if carnet > root.right.carnet:
                        root = self.RD(root)
                        print("Rotacion simple derecha")
                    else:
                        root = self.RID(root)
                        print("Rotacion doble derecha")
            else:
                root.carnet = carnet

        root.height = self.MAX(self.height(root.left), self.height(root.right)) + 1
        return root

    def RI(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        node.height = self.MAX(self.height(node.left), self.height(node.right)) + 1
        aux.height = self.MAX(self.height(aux.left), node.height) + 1
        return aux

    def RD(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        node.height = self.MAX(self.height(node.left), self.height(node.right)) + 1
        aux.height = self.MAX(self.height(aux.right), node.height) + 1
        return aux

    def RDI(self, node):
        node.left = self.RD(node.left)
        return self.RI(node)

    def RID(self, node):
        node.right = self.RI(node.right)
        return self.RD(node)

    def pre_orden(self):
        self.pre_orden_intern(self.Root)

    def pre_orden_intern(self, root):
        if root is not None:
            print(root.carnet)
            self.pre_orden_intern(root.left)
            self.pre_orden_intern(root.right)

