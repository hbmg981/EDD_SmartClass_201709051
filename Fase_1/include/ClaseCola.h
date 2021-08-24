#include "NodoCola.h"

class ClaseCola{
private:
    NodoCola *First;
    NodoCola *Last;
    int contador, archi, cont, tip;

public:
    //Constructor
    ClaseCola();

    //Metodos
    int getSize();
    bool isEmpty();

    void getList();
    void getListReverse();

    void insertList( string Descrip, string Tipo, int tip, int tipo2);
    void Desencolar();
    void generaError();
    bool ErrorUsuario();
    bool ErrorTarea2();
    bool ErrorTarea3();
    int TipoError();
};
