from Estructuras.Matriz_Dispersa import Matriz_dispersa
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

nodo = nueva_matriz.NodoRaiz.NodoColumnas

nodo = nueva_matriz.NodoRaiz.NodoFilas




nueva_matriz.graficar_matriz()
