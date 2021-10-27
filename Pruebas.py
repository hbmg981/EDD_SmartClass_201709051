


#--------------PROBANDO DATOS DEL AVL-----------
from Estructuras.AVL import AVL
avl = AVL()
avl.insert(120,123,"HEIDY", "SISTEMAS", "CORREO@GMAIL", "1234", 120, 15)
avl.insert(105,123,"BEATRIZ", "SISTEMAS", "CORREO@GMAIL", "1234", 120, 15)
avl.insert(185,123,"MIRANDA", "SISTEMAS", "CORREO@GMAIL", "1234", 120, 15)
avl.insert(100,123,"GAMEZ", "SISTEMAS", "CORREO@GMAIL", "1234", 120, 15)
avl.insert(95,123,"LOPEZ", "SISTEMAS", "CORREO@GMAIL", "1234", 120, 15)
avl.insert(115,123,"ANDREA", "SISTEMAS", "CORREO@GMAIL", "1234", 120, 15)
avl.pre_orden()
print("------- DESPUES DE ELIMINAR -----------")
avl.eliminar(115)
avl.insert(103,123,"ANDREA", "SISTEMAS", "CORREO@GMAIL", "1234", 120, 15)
avl.pre_orden()
avl.graficar()

#-------------Probando el arbol B -----------------------
from Estructuras.Arbol_B.BTree import BTree
btree = BTree()
btree.InsertarDatos(120,"Heidy",250,"Io2","No")
btree.InsertarDatos(100,"Miranda",20,"Analisis","si")
btree.InsertarDatos(170,"Miranda",20,"Analisis","si")
btree.InsertarDatos(125,"Heidy",250,"Io2","No")
btree.InsertarDatos(80,"Miranda",20,"Analisis","si")
btree.InsertarDatos(160,"Beatriz",240,"Io1","No")
btree.InsertarDatos(130,"Beatriz",240,"Io1","No")
btree.InsertarDatos(110,"Beatriz",240,"Io1","No")
btree.InsertarDatos(150,"Beatriz",240,"Io1","No")
btree.Preorden()
btree.Graficar(1)