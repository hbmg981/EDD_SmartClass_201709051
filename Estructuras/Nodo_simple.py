class NodoTarea:
    def __init__(self, carnet, nombre, descrip, materia, fecha,hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.descrip = descrip
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.next = None
        self.prev = None
        self.up = None
        self.down = None




