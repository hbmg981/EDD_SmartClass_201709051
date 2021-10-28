
#import SolovayStrassen as ss
class Nodo:

    def __init__(self, indice, carnet, valor):
        self.indice = indice
        self.carnet = carnet
        self.valor = valor
        self.lista = []
        self.contlista =0


class Hash:
    def __init__(self, valor=7):
        self.primos = [7,11,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97101,103,
                       107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,
                       233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,
                       373,379,383,389,397,401,409]
        self.contadordeprimos=1
        self.vector = []
        self.elementos = 0
        self.factorCarga = 0
        self.tamano = valor

        for i in range(valor):
            self.vector.append(None)

    def buscar(self, carnet):
        encontrado = False
        for i in self.vector:
            if i:
                if int(i.carnet) == int(carnet):
                    #print("Se encontro el carnet")
                    encontrado=True
                #else:
                    #print("No se encontro nada")
        return encontrado


    def insertar(self, carnet, valor):
        if self.buscar(carnet)==False:
            posicion = self.funcion_hash(carnet)
            nuevo = Nodo(posicion, carnet, valor)
            self.vector[posicion] = nuevo
            self.elementos += 1
            self.factorCarga = self.elementos / self.tamano

        else:
            print("El carnet ya existe: ")

        if self.factorCarga > 0.5:
            self.rehashing()
            print("Haciendo el rehashing de: "+ str(carnet))

    def rehashing(self):
        siguiente = self.tamano
        factor = 0
        while (factor < 0.5):
            factor = self.elementos / siguiente
            siguiente = self.primos[self.contadordeprimos]
            self.contadordeprimos+=1

        temporal = []

        for i in range(siguiente):
            temporal.append(None)
        aux_vector = self.vector

        self.vector = temporal
        self.tamano = siguiente

        print("Nuevo tamano", siguiente, "Tamano:", len(temporal))
        for i in aux_vector:
            if i:
                posicion = self.funcion_hash(i.carnet)
                #posicion = self.funcion_hash(i.indice)
                print("Nueva posicion:", posicion)
                i.indice = posicion
                temporal[posicion] = i

        self.vector = temporal

    def _funcion_hash(self, id):
        return id % self.tamano

    def funcion_hash(self, id):

        posicion = id % (self.tamano)
        print("El tamano actual es: "+ str(self.tamano)+ " La posicion es: "+ str(posicion))

        k= posicion
        conti =1
        while (self.vector[posicion] != None):

            posicion = self.linear(k, conti)
            conti += 1
            print(posicion)
            #if posicion > self.tamano:
               # posicion = posicion - self.tamano
        return posicion

    def linear(self, k, i):
        return(k+ i*i) % self.tamano

    def print(self):
        contador = 0
        for i in self.vector:
            if i:
                print("indice:", i.indice, "valor:", i.valor, "carnet:", i.carnet)
            else:
                print("indice:", contador, "valor:", i)

            contador += 1

    def get_next_prime(self, tamano):
        return ss.next_prime(tamano)


def toASCII(cadena):
    result = 0
    for char in cadena:
        result += ord(char)
    return result


tabla = Hash()
tabla.insertar(0, "primer valor 0")
tabla.insertar(15,  "segundo valor 15")
tabla.insertar(29,  "tercer valor 29")
tabla.insertar(44,  "4to valor 44")
#tabla.print()
tabla.insertar(58,  "5to valor 58")
tabla.insertar(73,  "6to valor 73")
tabla.insertar(87,  "7mo valor 87")
tabla.insertar(116,  "8o valor 116")
tabla.insertar(145,  "9 valor 145")
tabla.insertar(174,  "10 valor 174")
tabla.insertar(203,  "11 valor 203")
tabla.insertar(232,  "12 valor 232")
#tabla.insertar(232,  "13 valor 232")

tabla.print()
print(tabla.buscar(365))