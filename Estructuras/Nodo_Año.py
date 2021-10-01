from Estructuras.Lista_Mes import ListaM
from Estructuras.Lista_Sem import ListaSem

class NodoA:
    def __init__(self, año):
        self.año = año
        self.Next = None
        self.Previous = None
        # Aca van las listas, los punteros hacia lista de semestres y meses
        #self.semestres
        self.mes = ListaM()
        self.semestre = ListaSem()


