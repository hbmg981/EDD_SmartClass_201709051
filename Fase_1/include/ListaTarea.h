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

    void insertList(string carnet_, string nombre_,string descrip_, string materia_, string fecha_, string estado_,int index_);
    void deleteValue(string id);
    void ModificarNodo(string id);
    void generaTarea();
    void generaTarea1();
};
