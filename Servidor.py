import json

from flask import Flask, request, jsonify
from Estructuras.Matriz_Dispersa import Matriz_dispersa
from Estructuras.AVL import AVL
from Estructuras.Lista_simple import ListaSimple
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list, listaAños
from Estructuras.Lista_A import ListaA
from Estructuras.Lista_Mes import ListaM
from Estructuras.Arbol_B.BTree import BTree
from Estructuras.Lista_Sem import ListaSem
import os

bt= BTree()
avl=AVL()


app = Flask(__name__)

@app.route('/bienvenido', methods=['GET'])
def hello_world():
    cadena="Welcome to SmartClass "
    return jsonify({"response":cadena})

@app.route('/carga', methods=['POST'])
def carga():
    data = request.get_json(force=True)
    tipo = data['tipo']
    path = data['path']
    print("el tipo es: ",tipo)
    print("el path es: ",path)
    if tipo == "estudiante" or tipo=="recordatorio":
        print("Mandamos a llamar al analizador con la ruta")
        CargaMasiva(path)
    elif tipo =="curso":
        print("Mandamos a leer el archivo .json")
        CargaCursos(path)

    return jsonify({"response":"informacion recibida"})

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

    #avl.insert(carnet,DPI,nombre,carrera,correo,password,creditos,edad)
    return jsonify({"Estudiante Insertado la AVL"})

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


