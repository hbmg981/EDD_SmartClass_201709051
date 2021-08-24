#include "NodoU.h"

class ListaU{
private:
    NodoU *First;
    NodoU *Last;
    int id, tam;
    int archi;

public:
    //Construct
    ListaU();

    //Method
    int getSize();
    string obtenerListaGraphviz();
    bool isEmpty();
    bool buscarUsuarioDPI(string dpi);
    bool buscarUsuarioCarnet(string carnet);
    bool validarCarnet(const string&);
    bool validarDpi(const string&);
    bool validarCorreo(const string&);

    void getList();
    void ModificarDato(string dato);
    void getListReverse();

    void insertList(string carnet_,string dpi_,string nombre_,string carrera_,string correo_,string pass_,string creditos_,string edad_);
    void deleteValue(string carnet);
    void ModificarNodo(string DPI);
    void generaDot();
    void generatxt();
};
