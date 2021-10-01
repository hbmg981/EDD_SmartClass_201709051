
from analyzers.Lex import tokens
from Structures_Ply.List import List
from Structures_Ply.Node import Node
from Estructuras.AVL import AVL
from Estructuras.Lista_A import ListaA
from Estructuras.Lista_Mes import ListaM
from Estructuras.Matriz_Dispersa import Matriz_dispersa

hora = 0
dia = 0
mes = 0
año = 0
semestre = 0


# Lists for save the information about users and tasks
user_list = List()
task_list = List()
avl = AVL()
listaAños = ListaA()
Dispersa = Matriz_dispersa()
# This node allows to store information about one user or task
element_node = Node()

# dictionary of names
names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """
    # t[0] = t[1]
    # if len(t) == 2:
    #     t[0] = [t[1]]
    # else:
    #     t[0] = t[1]
    #     t[0].append(t[2])

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'



    if element_node.Fecha !="":
        fechan = element_node.Fecha.split("/")
        dia = fechan[0]
        mes =fechan[1]
        año = fechan[2]

        if int(mes) >= 7:
            semestre = 2
        else:
            semestre = 1

        #print(fechan)
        #print("Mes: "+fechan[1])
   #       print("Listado de dias")


    if element_node.Hora != "":
        horan = element_node.Hora.split(":")
        hora= horan[0]
        #print("hora: "+hora)


    if t[3] == "user":


        avl.insert(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Correo, element_node.Password, element_node.Creditos, element_node.Edad)
        '''user_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              element_node.Creditos, element_node.Edad, element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, hora, element_node.Estado)'''
    else:
        #nueva_matriz.insertar(1, 5, 20210859, "nombre", "descripcion", "Materia", "Fecha", "estado")
        listaAños.insertValue(int(año),int(semestre), int(mes), dia, hora,element_node.Carnet,element_node.Nombre,element_node.Descripcion, element_node.Materia,element_node.Fecha, element_node.Estado )
        task_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              element_node.Creditos, element_node.Edad, element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, hora, element_node.Estado)
    element_node.clean_values()

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    t[0] = t[3].replace('"', '').replace(' ', '')


def p_items(t):
    """items : items item
    """
    t[0] = t[2]

def p_items_2(t):
    """items : item
    """
    t[0] = t[1]

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    if t[3].lower() == "carnet":
        element_node.Carnet = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "dpi":
        element_node.DPI = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "nombre":
        element_node.Nombre = t[5].replace('"', '')
    elif t[3].lower() == "carrera":
        element_node.Carrera = t[5].replace('"', '')
    elif t[3].lower() == "password":
        element_node.Password = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "creditos":
        element_node.Creditos = t[5]
    elif t[3].lower() == "edad":
        element_node.Edad = t[5]
    elif t[3].lower() == "correo":
        element_node.Correo = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "descripcion":
        element_node.Descripcion = t[5].replace('"', '')
    elif t[3].lower() == "materia":
        element_node.Materia = t[5].replace('"', '')
    elif t[3].lower() == "fecha":
        element_node.Fecha = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "hora":
        element_node.Hora = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "estado":
        element_node.Estado = t[5].replace('"', '').replace(' ', '')

    t[0] = element_node

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                | TCORREO
                """
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()