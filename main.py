from Estructuras.Matriz_Dispersa import Matriz_dispersa
from Estructuras.AVL import AVL
from Estructuras.Lista_simple import ListaSimple
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list
from Estructuras.Lista_A import ListaA
import os
'''
nueva_matriz = Matriz_dispersa()

nueva_matriz.insertar(1, 5, "nuevo nodo")
nueva_matriz.insertar(1, 1, "nuevo nodo")
nueva_matriz.insertar(2, 4, "nuevo nodo")
nueva_matriz.insertar(2, 9, "nuevo nodo")
nueva_matriz.insertar(3, 7, "nuevo nodo")
nueva_matriz.insertar(3, 1, "nuevo nodo")
nueva_matriz.insertar(3, 8, "nuevo nodo")
nueva_matriz.insertar(3, 9, "nuevo nodo")
nueva_matriz.insertar(6, 6, "nuevo nodo")
nueva_matriz.insertar(6, 1, "nuevo nodo")
nueva_matriz.insertar(6, 5, "nuevo nodo")
nueva_matriz.insertar(9, 9, "nuevo nodo")

#nodo = nueva_matriz.NodoRaiz.NodoColumnas
#nodo = nueva_matriz.NodoRaiz.NodoFilas

#nueva_matriz.graficar_matriz()

avl = AVL()
avl.insert(120)
avl.insert(105)
avl.insert(80)
avl.insert(130)
avl.insert(90)
avl.insert(85)
avl.insert(135)
avl.insert(15)
avl.insert(195)

avl.pre_orden()

simple = ListaSimple()

simple.InsertarTarea(2047,"nombre","descrip","materia", "fecha","hora","estado")
simple.InsertarTarea(2067,"heidy","tarea1","mate", "12/12/45","7:00","pendiente")
simple.InsertarTarea(2087,"bea","tarea2","progra", "62/12/45","8:00","cumplido")
simple.InsertarTarea(2060,"mira","tarea5","orga", "12/10/80","9:00","realizado")
simple.getList()
simple.Remove(2047)
simple.Modificar(2060,2080,"elisa","tarea7","orga2", "10/10/80","9:00","realizado")
print("\n *** Lista Final *** : ")
simple.getList()
simple.obtener(2067)
simple.graficar()

f = open('repo.txt', "r", encoding="utf-8")
mensaje = f.read()
print(mensaje)
f.close()
parser.parse('¿ Elements ? ¿Element type = "task"?  ¿item Carnet = "201901425" $? ¿$Element? ¿ $Elements ?')
parser.parse(mensaje)

user_list.getList()
print("------------------------")
task_list.getList()

fecha= "12/05/2021"
lista =fecha.split("/")
print(lista)
print (lista[0])
print (lista[1])



listaaño = ListaA()
listaaño.insertValue(2020)
listaaño.insertValue(2021)
listaaño.insertValue(2019)
listaaño.insertValue(2022)
listaaño.buscar(2021)
print(str(listaaño.buscarRetornar(2021).año) + " Año actual")


listaaño.getList()
listaaño.getListRev()

'''