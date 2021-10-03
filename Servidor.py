import json

from flask import Flask, request, jsonify
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

bt= BTree()


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
    elif int(tipo) ==1:
        print("----- Mandar a graficar MATRIZ con Carnet, Año, Mes... ----- ")
        listaAños.GraficarDispersa(año,mes)
    elif int(tipo) ==2:
        print("----- Mandar a graficar Lista Tareas con Carnet, Año, Mes, Dia, Hora... ----- ")
        listaAños.GraficarPrueba(año, mes, dia, hora)
    elif int(tipo) ==3:
        print("----- Mandar a graficar Arbol B de cursos... ----- ")
        bt.Graficar(0)
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
    data = request.get_json(force=True)
    carnet = data['carnet']

    if avl.buscarRetornar(carnet) is not None:
        avl.eliminar(carnet)
        cadena= "Estudiante eliminado"
    else:
        cadena= "No se encontro el estudiante"
    return jsonify({cadena})


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




def CargaMasiva(ruta):
    f = open(ruta, "r", encoding="utf-8")
    mensaje = f.read()
    #print(mensaje)
    f.close()
    parser.parse(mensaje)
    user_list.getList()
    print("Preorden del AVL:")
    avl.pre_orden()
    print("------------------------")
    task_list.getList()

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

            bt.InsertarDatos(codigo,nombre,creditos,prerequisito,obligatorio)








if __name__ == "__main__":
    app.run("localhost", port=3000)
   # matriz_dispersa()
    ruta="CursosPensum.json"
    CargaCursos(ruta)


