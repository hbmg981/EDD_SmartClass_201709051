#include "NodoTarea.h"

class ListaTarea{
private:
    NodoTarea *First;
    NodoTarea *Last;
    int id, tam;
    int archi;

public:
    //Construct
    ListaTarea();

    //Method
    int getSize();
    string obtenerListaGraphviz();
    bool isEmpty();

    void getList();
    void getListReverse();
    void BuscarTarea(int mes_, int dia_, int hora_);
    void insertList(string carnet_, string nombre_,string descrip_, string materia_, string fecha_,string hora, string estado_,int index_);
    void deleteValue(int index);
    void ModificarNodo(string id);
    bool validarFecha(const string&);
    void generaTarea();
    void generaTarea1();

};
