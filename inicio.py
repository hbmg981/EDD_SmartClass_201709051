
import json
from flask import Flask, request, jsonify,render_template
from Estructuras.AVL import AVL
from Estructuras.Arbol_B.BTree import BTree
from Hash import Hash
import os

bt= BTree()
avl=AVL()
hash =Hash()
app=Flask(__name__)

@app.route('/')
def principal():
    return "Bienvenida a mi sitio web de python"

@app.route('/login')
def login():
    return "Aqui ira la pagina de inicio"
    #return  render_template('login.html')

@app.route('/carga', methods=['POST'])
def carga():
    data = request.get_json(force=True)
    tipo = data['tipo']
    path = data['path']
    print("el tipo es: ",tipo)
    print("el path es: ",path)
    if tipo == "estudiante":
        #print("Mandamos a llamar la carga de estudiantes")
        respuesta = CargaEstudiantes(path)
        return jsonify({"response": respuesta})
    elif tipo =="apunte":
        print("Mandamos a leer el archivo .json de apuntes")
        respuesta = CargaApuntes(path)
        return jsonify({"response": respuesta})

    elif tipo =="curso_e":
        print("Mandamos a leer el archivo .json de cursos estudiantes")

        return jsonify({"response": "Carga de Cursos de estudiantes realizada"})
    elif tipo =="curso_p":
        print("Mandamos a leer el archivo .json de cursos pensum")
        respuesta = CargaCursos(path)
        return jsonify({"response": respuesta})

    #return jsonify({"response":"informacion recibida"})


def CargaCursos(ruta):
    try:
        with open(ruta, 'r', encoding='utf8') as contenido:
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

                bt.InsertarDatos(codigo, nombre, creditos, prerequisito, obligatorio)
        return "Carga de cursos Pensum realizada correctamente"
    except:
        print("Ocurrio un error")
        return "Ha ocurrido un error, verifique los datos"


def CargaApuntes(ruta):
    #print(ruta)
    try:
        with open(ruta, 'r', encoding='utf8') as contenido:
            apuntes = json.load(contenido)
            print(apuntes)
            lista = apuntes['usuarios']
            print(lista)
            for elemento in lista:
                carnet = elemento['carnet']
                lista_apuntes = elemento['apuntes']
                for apunte in lista_apuntes:
                    titulo = apunte['Título']
                    contenido = apunte['Contenido']
                    print("Carnet:", carnet, "titulo:", titulo, "Contenido:", contenido)
                    hash.insertar(carnet,titulo,contenido)
        return "Carga de apuntes realizada correctamente"
    except:
        print("Ocurrio un error")
        return "Ha ocurrido un error, verifique los datos"








def CargaEstudiantes(ruta):
    try:
        with open(ruta, 'r', encoding='utf8') as contenido:
            cursos = json.load(contenido)
            print(cursos)
            lista = cursos['estudiantes']
            # print(lista)
            for elemento in lista:
                carnet= elemento['carnet']
                nombre = elemento['nombre']
                #creditos= elemento['Creditos']
                dpi= elemento['DPI']
                carrera= elemento['carrera']
                pasword= elemento['password']
                edad= elemento['edad']
                correo= elemento['correo']

                #insert(carnet,dpi,nombre,carrera,correo,password,edad,creditos=0):
                avl.insert(carnet,dpi,nombre,carrera,correo,pasword,edad)
        return "Carga de estudiantes realizada correctamente"
    except:
        print("Ocurrio un error")
        return "Ha ocurrido un error, verifique los datos"














if __name__ == '__main__':
    app.run("localhost", port=3000,debug=True)

