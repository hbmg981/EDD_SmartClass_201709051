from Estructuras.Matriz_Dispersa import Matriz_dispersa
from Estructuras.AVL import AVL
from Estructuras.Lista_simple import ListaSimple
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list, avl, listaAños
from Estructuras.Lista_A import ListaA
from Estructuras.Lista_Mes import ListaM
from Estructuras.Arbol_B.BTree import BTree
from Estructuras.Lista_Sem import ListaSem
import os
import json
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

#----------- MATRIZ DISPERSA -----------------
nueva_matriz = Matriz_dispersa()
#insertar(self,dia,hora,carnet, nombre, descrip, materia, fecha,horas, estado)
nueva_matriz.insertar(1, 5,20210859, "nombre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(1, 1,20210860, "nosfe","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(2, 4,20210859, "nfdse","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(22, 9,20210259, "sdfbre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(3, 7, 20268859, "dfmbre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(3, 1,2011159, "nwwbre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(3, 8, 2022259, "nomdfe","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(3, 9, 20213359, "nwbre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(6, 6, 244459, "nooure","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(3, 19,20266859, "asdfombre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(6, 6, 20277569, "tembre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(6, 1, 20210359, "fgsdmbre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(6, 5, 20210859, "sdfbre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(16, 5, 20210859, "nsdfbre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.insertar(9, 9, 20210279, "nooytre","descripcion", "Materia", "Fecha", "estado")
nueva_matriz.graficarLista(6,6)
nueva_matriz.graficarLista(9,9)
nueva_matriz.graficar_matriz()


#--------------PROBANDO DATOS LISTA SIMPLE DE SEMESTRES QUE VA EN LA MATRIZ-----------
simple = ListaSem()
simple.Insertar(1)
simple.Insertar(2)
simple.Insertar(2087)
print("Lista de semestres .....")
simple.getList()
#simple.eliminar(2047)
print("Modificar el semestre 2 por el 1")
simple.Modificar(2,1)
print("\n *** Lista Final *** : ")
simple.getList()
simple.obtener(1)
simple.graficar(1)


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


btree = BTree()
btree.InsertarDatos(200,"Heidy",250,"Io2","No")
btree.InsertarDatos(100,"Miranda",20,"Analisis","si")
btree.InsertarDatos(400,"Beatriz",240,"Io1","No")
btree.InsertarDatos(300,"Beatriz",240,"Io1","No")
btree.InsertarDatos(500,"Beatriz",240,"Io1","No")

btree.Preorden()
btree.Graficar(1)



#-----------------Metodo para llamar al analizador-------------
f = open('repo.txt', "r", encoding="utf-8")
mensaje = f.read()
print(mensaje)
f.close()
#¿Elements? ¿element type="user"?  ¿item Carnet="201700886" $?
parser.parse('¿ Elements ? ¿element type = "user"?  ¿item Carnet = "201700886" $? ¿$element? ¿ $Elements ?')
parser.parse(mensaje)

user_list.getList()
print("Preorden del AVL:")
avl.pre_orden()
print("------------------------")
task_list.getList()
avl.buscarDato(2015000)
print(avl.buscarDato(201501785))
listaAños.GraficarPrueba(2021,7,1,8)
listaAños.GraficarPrueba(2021,7,14,10)
listaAños.GraficarPrueba(2021,7,14,16)
listaAños.buscarRetornar(2021).mes.buscarRetornar(7).tareas.graficar_matriz(10)

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
avl.graficar(1)

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



listaAños.buscarRetornar(2021).mes.buscarRetornar(7).tareas.graficarLista(1,8,10)
listaAños.buscarRetornar(2021).mes.buscarRetornar(7).tareas.graficarLista(1,11,2)
listaAños.buscarRetornar(2021).mes.buscarRetornar(7).tareas.graficarLista(14,10,3)
listaAños.buscarRetornar(2021).mes.buscarRetornar(7).tareas.graficarLista(14,16,4)
listaAños.buscarRetornar(2021).mes.buscarRetornar(10).tareas.graficarLista(21,8,5)
listaAños.buscarRetornar(2021).mes.buscarRetornar(10).tareas.graficarLista(21,13,6)


simple = ListaSimple()
simple.InsertarTarea(2047,"nombre","descrip","materia", "fecha","hora","estado")
simple.InsertarTarea(2067,"heidy","tarea1","mate", "12/12/45","7:00","pendiente")
simple.InsertarTarea(2087,"bea","tarea2","progra", "62/12/45","8:00","cumplido")
simple.InsertarTarea(2060,"mira","tarea5","orga", "12/10/80","9:00","realizado")
simple.getList()

simple.Modificar(2060,2080,"elisa","tarea7","orga2", "10/10/80","9:00","realizado")
print("\n *** Lista Final *** : ")
simple.getList()
simple.obtener(2067)
simple.graficar(30)

#-----------------Metodo para llamar al analizador-------------

avl.buscarDato(2015000)
print(avl.buscarDato(201501786))
avl.graficar()
avl.eliminar(201501786)
avl.graficar()


listaAños.GraficarPrueba(2021,7,1,8)
listaAños.GraficarPrueba(2021,7,14,10)
listaAños.GraficarPrueba(2021,7,14,16)
listaAños.buscarRetornar(2021).mes.buscarRetornar(7).tareas.graficar_matriz(10)



f = open('repo.txt', "r", encoding="utf-8")
mensaje = f.read()
print(mensaje)
f.close()
parser.parse(mensaje)

user_list.getList()
print("Preorden del AVL:")
avl.pre_orden()
avl.eliminar(201502186)
print("------------------------")
avl.pre_orden()
task_list.getList()

listaAños.GraficarDispersa(2021,10)

'''












def CargaCursos(ruta):
    with open(ruta) as contenido:
        cursos = json.load(contenido)
        print(cursos)
        lista= cursos['Cursos']
        print(lista)
        for elemento in lista:
            codigo= elemento['Codigo']
            nombre = elemento['Nombre']
            creditos= elemento['Creditos']
            prerequisito= elemento['Prerequisitos']
            obligatorio= elemento['Obligatorio']
            print(elemento)
            print(codigo)
            print(nombre)
            print(creditos)
            print(prerequisito)
            print(obligatorio)





ruta="CursosPensum.json"
CargaCursos(ruta)


