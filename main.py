from Estructuras.Matriz_Dispersa import Matriz_dispersa
from Estructuras.AVL import AVL
from Estructuras.Lista_simple import ListaSimple
import os

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

