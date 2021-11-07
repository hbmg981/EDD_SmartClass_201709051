key = None
f = None
import json
from flask import Flask, request, jsonify,render_template
from Estructuras.AVL import AVL
from Estructuras.Arbol_B.BTree import BTree
from Hash import Hash
import os
from Estructuras.ListaAdyacencia import ListaAdyacencia
from Estructuras.Lista_Sem import ListaSem
from cryptography.fernet import Fernet
from Estructuras.Nodo_AVL import Nodo


ls = ListaSem()
ad = ListaAdyacencia()
#ad.insert_node(101,"Mate Basica 1",1)
#ad.link_graph(101,103)
genera= bool

bt= BTree()
avl=AVL()
hash =Hash()
app=Flask(__name__)

@app.route('/')
def principal():
    return "Bienvenida a mi sitio web de python"

@app.route('/genClave')
def generar():
    nuevo = Nodo(0, 0, "Muestra", "", "", "", 0, 0)
    nuevo.generarClave()
    genera = True
    respuesta="Se ha generado la llave de encriptacion"
    return jsonify({"response": respuesta})


@app.route('/login')
def login():
    return "Aqui ira la pagina de inicio"
    #return  render_template('login.html')

@app.route('/carga', methods=['POST'])
def carga():
    try:
        data = request.get_json(force=True)
        tipo = data['tipo']
        path = data['path']
        texto = data['tx']
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
            respuesta = CargaCursosE(path)
            return jsonify({"response": respuesta})

        elif tipo =="curso_p":
            print("Mandamos a leer el archivo .json de cursos pensum")
            respuesta = CargaCursos(path)
            return jsonify({"response": respuesta})
    except:
        return jsonify({"response":"Ha ocurrido un error, verifique los datos"})


def CargaCursos(ruta):
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

                #print("Codigo:",codigo,"Nombre:",nombre,"Creditos",creditos,"Prerequisito",prerequisito,"Obligatorio:",obligatorio)

                ad.insert_node(codigo, nombre, creditos, prerequisito, str(obligatorio))
                if prerequisito == "":
                    print(" ")

                    # ad.link_graph(101,103)
                else:
                    #print("Hacer split")
                    arreglo = prerequisito.split(',')
                    for x in arreglo:
                        #print(x)
                        ad.link_graph(x,codigo )
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
                    titulo = apunte['Titulo']
                    contenido = apunte['Contenido']
                    print("Carnet:", carnet, "titulo:", titulo, "Contenido:", contenido)
                    hash.insertar(carnet,titulo,contenido)
        return "Carga de apuntes realizada correctamente"
    except:
        print("Ocurrio un error")
        return "Ha ocurrido un error, verifique los datos"


def CargaCursosE(ruta):
    #print(ruta)
    try:
        with open(ruta, 'r', encoding='utf8') as contenido:
            cursos = json.load(contenido)
            print(cursos)
            lista = cursos['Estudiantes']
            #print(lista)
            for elemento in lista:
                carnet = elemento['Carnet']
                lista_anio = elemento['Años']
                #print(lista_anio)
                for anio in lista_anio:
                    año = anio['Año']
                    lista_sem = anio['Semestres']
                    #print(lista_sem)
                    for sem in lista_sem:
                        semestre = sem['Semestre']
                        lista_curso = sem['Cursos']
                        #print(lista_curso)
                        for curso in lista_curso:
                            codigo = curso['Codigo']
                            nombre = curso['Nombre']
                            creditos = curso['Creditos']
                            prerequisito = curso['Prerequisitos']
                            obligatorio = curso['Obligatorio']
                            print("Carnet:",carnet,"Año:",año,"Semestre:",semestre,"Codigo:",codigo, "Nombre:"
                                  ,nombre,"Creditos",creditos,"Prerequisito:",prerequisito,"Obligatorio:",obligatorio)
                            ls.Insertar(carnet, año, semestre, codigo, nombre, creditos, prerequisito,obligatorio)
        return "Carga de cursos estudiante realizada correctamente"
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

@app.route('/reporte', methods=['GET'])
def reporte():
    try:
        data = request.get_json(force=True)
        tipo = data['tipo']
        codigo=data['codigo']
        carnet = data['carnet']
        carnex = data['a']
        año= data['b']
        semestre= data['c']
        mes= data['d']
        dia= data['dia']
        hora= data['hora']

        '''print("el tipo es: ",tipo)
        print("el carnet es: ", carnet)
        print("año es: ",año)
        print("el semestre es: ",semestre)
        print("el mes es: ",mes )
        print("el dia es: ",dia)
        print("la hora es:",hora )'''
        if int(tipo) ==0:
            #print("----- Mandar a graficar el arbol AVL... ----- ")
            try:
                avl.graficar()
                return jsonify({"response": "Arbol AVL graficado"})
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
        elif int(tipo) ==3:
            try:
                bt.Graficar()
                return jsonify({"response": "Arbol B graficado"})
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
        elif int(tipo) ==2:
            try:
                hash.graficarHash2()
                return jsonify({"response": "Tabla de apuntes graficada"})
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})

        elif int(tipo) ==1:
            try:
                if genera:
                    avl._graficar()
                    return jsonify({"response": "Arbol AVL Cifrado graficado"})
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
        elif int(tipo) ==4:
            try:
                #ad.get_list()
                ad.graficar()
                return jsonify({"response": "Grafo de Cursos graficado"})
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
        elif int(tipo) ==5:
            try:
                #ad.get_list()
                ad.graficar2(codigo)
                return jsonify({"response": "Grafo de Cursos graficado"})
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
        elif int(tipo) ==8:
            try:
                #ad.get_list()
                print("Carnet encontrado en posicion:", hash.buscarposicion(carnet))
                info = "Carnet encontrado en posicion:  "+ str(hash.buscarposicion(carnet))
                return jsonify({"response: ":info })
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
        elif int(tipo) ==7:
            try:
                #ad.get_list()

                info = ""
                ls.graficarArbol(carnet)
                info = "Se grafico el arbol"
                return jsonify({"response":info })
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
        elif int(tipo) ==6:
            try:
                info2 = ""
                info ="--- Lista de Apuntes -----"
                contador = 1
                if hash.buscar(carnet):
                    car = hash.retornar(carnet)
                    for x in car.lista:
                        info+= "\n"+str(contador)+") "+"\n\t{\n\t" +" \"Titulo \" :" +x.titulo +"\n\t\"Contenido\" : \t"+ x.contenido+"\n\t}"
                        print(contador, ")", "Titulo:", x.titulo, "Contenido:", x.contenido)
                        #info2 += jsonify({"Titulo": x.titulo,"Contenido":x.contenido})
                        contador += 1

                else:
                    print("No se encontro el carnet")
                return info
            except:
                return jsonify({"response": "Ha ocurrido un error, verifique los datos"})

        else:
            return jsonify({"response": "Tipo fuera de rango"})
    except:
        return jsonify({"response": "Ha ocurrido un error, verifique los datos"})
    #print("Carnet encontrado en posicion:",tabla.buscarposicion(0))

    #

@app.route('/registro', methods=['POST'])
def CrearEstudiante():
    data = request.get_json(force=True)
    respuesta = CrearEstudianteServer(data)
    return jsonify({"response": respuesta})

def CrearEstudianteServer(data):
    try:
        DPI = data['DPI']
        carnet = data['carnet']
        nombre= data['nombre']
        carrera= data['carrera']
        correo= data['correo']
        password= data['password']
        creditos= data['creditos']
        edad= data['edad']

        avl.insert(carnet,DPI,nombre,carrera,correo,password,edad,creditos)
        return "Estudiante Insertado al AVL"
    except:
        return "Hubo un error al intentar insertar los datos"

@app.route('/asignarCursos', methods=['POST'])
def asignarCurso():
    data = request.get_json(force=True)
    respuesta = asignarCursoServer(data)
    return jsonify({"response": respuesta})


def asignarCursoServer(data):
    try:
        #contenido=data
        cursos = data
        print(cursos)
        lista = cursos['Estudiantes']
        print(lista)
        for elemento in lista:
            carnet = elemento['Carnet']
            lista_anio = elemento['Años']
            #print(lista_anio)
            for anio in lista_anio:
                año = anio['Año']
                lista_sem = anio['Semestres']
                #print(lista_sem)
                for sem in lista_sem:
                    semestre = sem['Semestre']
                    lista_curso = sem['Cursos']
                    #print(lista_curso)
                    for curso in lista_curso:
                        codigo = curso['Codigo']
                        nombre = curso['Nombre']
                        creditos = curso['Creditos']
                        prerequisito = curso['Prerequisitos']
                        obligatorio = curso['Obligatorio']
                        print("Carnet:",carnet,"Año:",año,"Semestre:",semestre,"Codigo:",codigo, "Nombre:"
                              ,nombre,"Creditos",creditos,"Prerequisito:",prerequisito,"Obligatorio:",obligatorio)
                        ls.Insertar(carnet, año, semestre, codigo, nombre, creditos, prerequisito,obligatorio)
        return "Carga de cursos estudiante realizada correctamente"
    except:
        print("Ocurrio un error")
        return "Ha ocurrido un error, verifique los datos"


@app.route('/crearApunte', methods=['POST'])
def CrearApunte():
    data = request.get_json(force=True)
    respuesta = CrearApunteServer(data)
    return jsonify({"response": respuesta})

def CrearApunteServer(data):
    try:
        apuntes = data
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
                hash.insertar(carnet, titulo, contenido)
        return "Apunte Insertado en la tabla"
    except:
        return "Hubo un error al intentar insertar los datos"

@app.route('/cursosPensum', methods=['POST'])
def CrearCurso():
    data = request.get_json(force=True)
    respuesta = CargaCursosServer(data)
    return jsonify({"response": respuesta})


def CargaCursosServer(contenido):
    try:
        cursos = contenido
        # print(cursos)
        lista = cursos['Cursos']
        # print(lista)
        for elemento in lista:
            codigo = elemento['Codigo']
            nombre = elemento['Nombre']
            creditos = elemento['Creditos']
            prerequisito = elemento['Prerequisitos']
            obligatorio = elemento['Obligatorio']

            ad.insert_node(codigo, nombre, creditos, prerequisito, str(obligatorio))
            if prerequisito == "":
                print(" ")

                # ad.link_graph(101,103)
            else:
                # print("Hacer split")
                arreglo = prerequisito.split(',')
                for x in arreglo:
                    # print(x)
                    ad.link_graph(x, codigo)

            bt.InsertarDatos(codigo, nombre, creditos, prerequisito, obligatorio)
        return "Elementos insertados"
    except:
        print()
        return "Ocurrio un error, revise los datos"




if __name__ == '__main__':
    app.run("localhost", port=3000,debug=True)

#class ini:
