from Estructuras.Matriz_Dispersa import Matriz_dispersa
from Estructuras.AVL import AVL
from Estructuras.Lista_simple import ListaSimple
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list, avl
from Estructuras.Lista_A import ListaA
from Estructuras.Lista_Mes import ListaM
from Estructuras.Arbol_B.BTree import BTree
import os
'''


listaaño = ListaA()
listaaño.insertValue(2020)
listaaño.insertValue(2021)
listaaño.insertValue(2019)
listaaño.insertValue(2022)
listaaño.buscar(2021)
print(str(listaaño.buscarRetornar(2021).año) + " Año actual")


listaaño.getList()
listaaño.getListRev()

btree = BTree()
btree.InsertarDatos(200,"Heidy",250,"Io2","No")
btree.InsertarDatos(100,"Miranda",20,"Analisis","si")
btree.InsertarDatos(400,"Beatriz",240,"Io1","No")


#--------------PROBANDO DATOS DEL AVL-----------
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

#-----------------Metodo para llamar al analizador-------------
f = open('repo.txt', "r", encoding="utf-8")
mensaje = f.read()
print(mensaje)
f.close()
parser.parse('¿ Elements ? ¿Element type = "task"?  ¿item Carnet = "201901425" $? ¿$Element? ¿ $Elements ?')
parser.parse(mensaje)

#user_list.getList()
avl.pre_orden()
print("------------------------")
task_list.getList()


#--------------PROBANDO DATOS LISTA SIMPLE DE TAREAS QUE VA EN LA MATRIZ-----------
simple = ListaSimple()
simple.InsertarTarea(2047,"nombre","descrip","materia", "fecha","hora","estado")
simple.InsertarTarea(2067,"heidy","tarea1","mate", "12/12/45","7:00","pendiente")
simple.InsertarTarea(2087,"bea","tarea2","progra", "62/12/45","8:00","cumplido")
simple.InsertarTarea(2060,"mira","tarea5","orga", "12/10/80","9:00","realizado")
simple.getList()
simple.eliminar(2047)
simple.Modificar(2060,2080,"elisa","tarea7","orga2", "10/10/80","9:00","realizado")
print("\n *** Lista Final *** : ")
simple.getList()
simple.obtener(2067)
simple.graficar()




#---------LISTA De MESES -------------
listaaño = ListaM()
listaaño.insertValue(12)
listaaño.insertValue(8)
listaaño.insertValue(1)
listaaño.insertValue(2)
listaaño.getList()
listaaño.eliminar(2)
print("Despues de eliminar")
listaaño.orden()
listaaño.getList()
listaaño.graficar()
#listaaño.getListRev()

#---------LISTA DE AÑOS -------------
listaaño = ListaA()
listaaño.insertValue(2020)
listaaño.insertValue(2021)
listaaño.insertValue(2019)
listaaño.insertValue(2022)
listaaño.getList()
listaaño.eliminar(2021)
print("Despues de eliminar")
listaaño.orden()
listaaño.getList()
listaaño.graficar()



'''
#----------- MATRIZ DISPERSA -----------------
nueva_matriz = Matriz_dispersa()
nueva_matriz.insertar(1, 5, " taarea")
nueva_matriz.insertar(1, 1, " nodo")
nueva_matriz.insertar(2, 4, "nuevo")
nueva_matriz.insertar(22, 9, "ro")
nueva_matriz.insertar(3, 7, "nh")
nueva_matriz.insertar(3, 1, "nur")
nueva_matriz.insertar(3, 8, "nyo")
nueva_matriz.insertar(3, 9, "nwero")
nueva_matriz.insertar(6, 6, "nfddo")
nueva_matriz.insertar(3, 19, "nwero")
nueva_matriz.insertar(6, 6, "nfddo")
nueva_matriz.insertar(6, 1, "asdfdo")
nueva_matriz.insertar(6, 5, "bla")
nueva_matriz.insertar(16, 5, "repetido")
nueva_matriz.insertar(9, 9, "as")
nueva_matriz.graficar_matriz()

















