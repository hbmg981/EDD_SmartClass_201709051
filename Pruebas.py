from Estructuras.ListaAdyacencia import ListaAdyacencia
from Estructuras.Arbol_B import BTree
import json
ad = ListaAdyacencia()

ad.insert_node(101,"Mate Basica 1",1,"a","si")
ad.insert_node(103,"Mate Basica 2",2,"b","no")
ad.insert_node(107,"Mate intermedia 1",3,"c","no")
ad.insert_node(770,"Introduccion a la programacion",4,"d","si")
ad.insert_node(771,"Intro a la Progra2", 5,"e","si")
ad.insert_node(795,"Logica de sistemas",6,"f","si")
ad.insert_node(960,"Mate Computo 1",6,"g","si")

ad.link_graph(101,103)
ad.link_graph(103,107)
ad.link_graph(103,770)
ad.link_graph(103,795)
ad.link_graph(103,960)
ad.link_graph(795,771)
ad.link_graph(107,771)
ad.link_graph(770,771)
ad.link_graph(960,771)


ad.get_list2(771)
ad.graf(771)
#ad.graficar2(771)
















'''







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
btree.Graficar()

#--------------PROBANDO DATOS DEL AVL-----------
from Estructuras.AVL import AVL
avl = AVL()
avl.insert(120,123,"HEIDY", "SISTEMAS", "CORREO@GMAIL", "devnami", 25, 150)
avl.insert(105,123,"BEATRIZ", "SISTEMAS", "CORREO@GMAIL", "12340", 20, 105)
avl.insert(185,123,"MIRANDA", "SISTEMAS", "CORREO@GMAIL", "12341", 12, 125)
avl.insert(100,123,"GAMEZ", "SISTEMAS", "CORREO@GMAIL", "12342", 16, 155)
avl.insert(95,123,"LOPEZ", "SISTEMAS", "CORREO@GMAIL", "12343", 19, 175)
avl.insert(115,123,"ANDREA", "SISTEMAS", "CORREO@GMAIL", "12344", 22, 195)
avl.pre_orden()
print("------- DESPUES DE ELIMINAR -----------")
#avl.eliminar(115)
avl.insert(103,123,"ANDREA", "SISTEMAS", "CORREO@GMAIL", "51234", 23, 135)
avl._pre_orden()
avl._graficar()
avl.graficar()






import json

from flask import Flask, request, jsonify
from Estructuras.AVL import AVL
from Estructuras.Arbol_B.BTree import BTree
import os

bt= BTree()
avl=AVL()


app = Flask(__name__)

@app.route('/bienvenido', methods=['GET'])
def hello_world():
    cadena="Welcome to SmartClass "
    return jsonify({"response":cadena})



@app.route('/reporte', methods=['GET'])
def reporte():
    data = request.get_json(force=True)
    tipo = data['tipo']
    carnet = data['carnet']
    año= data['año']
    semestre= data['semestre']
    mes= data['mes']
    dia= data['dia']
    hora= data['hora']

    print("el tipo es: ",tipo)
    print("el carnet es: ", carnet)
    print("año es: ",año)
    print("el semestre es: ",semestre)
    print("el mes es: ",mes )
    print("el dia es: ",dia)
    print("la hora es:",hora )
    if int(tipo) ==0:
        print("----- Mandar a graficar el arbol AVL... ----- ")
        avl.graficar()
        return jsonify({"response": "Arbol AVL graficado"})
    elif int(tipo) ==1:
        print("----- Mandar a graficar MATRIZ con Carnet, Año:" + str(año)+ ", Mes: "+str(mes)+" ----- ")
        listaAños.GraficarDispersa(año,mes)
    elif int(tipo) ==2:
        print("----- Mandar a graficar Lista Tareas con Carnet, Año, Mes, Dia, Hora... ----- ")
        listaAños.GraficarTareas(año, mes, dia, hora)

    elif int(tipo) ==3:
        print("----- Mandar a graficar Arbol B de cursos... ----- ")
        bt.Graficar(0)
        return jsonify({"response": "Graficando Arbol B de Cursos Pensum"})
    elif int(tipo) ==4:
        print("----- Mandar a graficar Arbol B de cursos de estudiante con Carnet, Año y Semestre... ----- ")


    return jsonify({"response":"informacion recibida"})

@app.route('/estudiante', methods=['POST'])
def CrearEstudiante():
    data = request.get_json(force=True)
    DPI = data['DPI']
    carnet = data['carnet']
    nombre= data['nombre']
    carrera= data['carrera']
    correo= data['correo']
    password= data['password']
    creditos= data['creditos']
    edad= data['edad']

    avl.insert(carnet,DPI,nombre,carrera,correo,password,creditos,edad)
    return jsonify({"Estudiante Insertado la AVL"})

@app.route('/recordatorios', methods=['POST'])
def CrearRecordatorio():
    data = request.get_json(force=True)
    descripcion = data['descripcion']
    carnet = data['carnet']
    nombre= data['nombre']
    materia= data['materia']
    fecha= data['fecha']
    hora= data['hora']
    estado= data['estado']

    fechan = fecha.split("/")
    dia = fechan[0]
    mes = fechan[1]
    año = fechan[2]
    horan = hora.split(":")
    hora = horan[0]

    if int(mes) >= 7:
        semestre = 2
    else:
        semestre = 1

    print(semestre)


    listaAños.insertValue(año,semestre,mes,dia,hora,carnet,nombre,descripcion,materia,fecha,estado)
    print(listaAños.buscarRetornar(año).mes.buscarRetornar(mes))
    return jsonify({"Recordatorio Insertado"})



@app.route('/estudiante', methods=['PUT'])
def ModificarEstudiante():
    data = request.get_json(force=True)
    DPI = data['DPI']
    carnet = data['carnet']
    nombre= data['nombre']
    carrera= data['carrera']
    correo= data['correo']
    password= data['password']
    creditos= data['creditos']
    edad= data['edad']

    avl.Modificar(carnet,DPI,nombre,carrera,correo,password,creditos,edad)
    return jsonify({"Estudiante Modificado AVL"})

@app.route('/estudiante', methods=['DELETE'])
def EliminarEstudiante():
    try:
        data = request.get_json(force=True)
        carnet = data['carnet']

        if avl.buscarDato(carnet):
            avl.eliminar(carnet)
            return jsonify({"Estudiante eliminado"})
        else:
            cadena= "No se encontro el estudiante"
            return jsonify({"Estudiante no eliminado"})
    except:
        return jsonify({"Verifique los datos"})


@app.route('/estudiante', methods=['GET'])
def ObtenerEstudiante():
    data = request.get_json(force=True)
    carnet = data['carnet']

    #print(avl.buscarRetornar(carnet).carnet)
    DPI = avl.buscarRetornar(carnet).dpi
    carnet2 = avl.buscarRetornar(carnet).carnet
    nombre = avl.buscarRetornar(carnet).nombre
    carrera = avl.buscarRetornar(carnet).carrera
    correo = avl.buscarRetornar(carnet).correo
    password = avl.buscarRetornar(carnet).password
    creditos = avl.buscarRetornar(carnet).creditos
    edad = avl.buscarRetornar(carnet).edad
    return jsonify({"Carnet":carnet2,"Nombre":nombre, "DPI":DPI,"Carrera":carrera,"Correo":correo,"Password":password,"Creditos":creditos,"Edad":edad})

@app.route('/cursosPensum', methods=['POST'])
def CrearCurso():
    data = request.get_json(force=True)
    CargaCursosServer(data)
    return jsonify({"Cursos insertados"})


def CargaMasiva(ruta):
    f = open(ruta, "r", encoding="utf-8")
    mensaje = f.read()
    #print(mensaje)
    f.close()
    parser.parse(mensaje)
    user_list.getList()
    LlenarAVL()
    LlenarTarea()
    print("Preorden del AVL:")
    avl.pre_orden()
    print("------------------------")
    task_list.getList()

def CargaCursos(ruta):
    with open(ruta) as contenido:
        cursos = json.load(contenido)
        print(cursos)
        lista= cursos['Cursos']
        #print(lista)
        for elemento in lista:
            codigo= elemento['Codigo']
            nombre = elemento['Nombre']
            creditos= elemento['Creditos']
            prerequisito= elemento['Prerequisitos']
            obligatorio= elemento['Obligatorio']


            bt.InsertarDatos(codigo,nombre,creditos,prerequisito,obligatorio)

def CargaCursosServer(contenido):
        cursos = contenido
        #print(cursos)
        lista= cursos['Cursos']
        #print(lista)
        for elemento in lista:
            codigo= elemento['Codigo']
            nombre = elemento['Nombre']
            creditos= elemento['Creditos']
            prerequisito= elemento['Prerequisitos']
            obligatorio= elemento['Obligatorio']


            bt.InsertarDatos(codigo,nombre,creditos,prerequisito,obligatorio)

def LlenarAVL():
    aux = user_list.First
    while aux is not None:
       # print( aux.Carnet + " - " + aux.Nombre + "-" + aux.DPI + "-" + aux.Carrera + "-" + aux.Correo + "-" + aux.Edad)
        avl.insert(aux.Carnet, aux.DPI, aux.Nombre, aux.Carrera,
                   aux.Correo, aux.Password, aux.Creditos, aux.Edad)
        aux = aux.Next


def LlenarTarea():
    aux = task_list.First
    while aux is not None:

        fechan = aux.Fecha.split("/")
        dia = fechan[0]
        mes = fechan[1]
        año = fechan[2]
        horan = aux.Hora.split(":")
        hora = horan[0]


        if int(mes) >= 7:
            semestre = 2
        else:
            semestre = 1

        print(
            aux.Carnet + " - " + aux.Nombre + "-" + aux.Descripcion + "-" + aux.Materia + "-" + aux.Fecha + "-" + aux.Estado)
        listaAños.insertValue(int(año), int(semestre), int(mes), int(dia), int(hora), aux.Carnet,
                              aux.Nombre, aux.Descripcion, aux.Materia, aux.Fecha,
                              aux.Estado)
        aux = aux.Next




if __name__ == "__main__":
    app.run("localhost", port=3000)
   # matriz_dispersa()
    ruta="CursosPensum.json"
    CargaCursos(ruta)
    #LlenarAVL()
    
    
    
    def CargaCursos(ruta):
    ad = ListaAdyacencia()
    bt = BTree()
    try:
        with open(ruta, 'r', encoding='utf-8') as contenido:
            cursos = json.load(contenido)
            print(cursos)
            lista = cursos['Cursos']
            # print(lista)
            for elemento in lista:
                codigo = elemento['Codigo']
                nombre = elemento['Nombre']
                creditos = elemento['Creditos']
                prerequisito = elemento['Prerequisitos']
                obligatorio = elemento['Obligatorio']

                ad.insert_node(codigo, nombre, creditos, prerequisito, obligatorio)
                if prerequisito == "":
                    print(" No tiene prerequisitos, solo se inserta")

                    # ad.link_graph(101,103)
                else:
                    print("Hacer split")
                    arreglo = prerequisito.split(',')
                    for x in arreglo:
                        #print(x)
                        ad.link_graph(codigo,x )
                bt.InsertarDatos(codigo, nombre, creditos, prerequisito, obligatorio)

        return "Carga de cursos Pensum realizada correctamente"
    except:
        print("Ocurrio un error")
        return "Ha ocurrido un error, verifique los datos"


path = "C:\\Users\\Compu Fire\\Downloads\\CursosPensum.json"
respuesta=CargaCursos(path)
print(respuesta)

    
    
    '''

