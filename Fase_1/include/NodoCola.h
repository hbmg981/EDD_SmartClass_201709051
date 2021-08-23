#include <string>
#include <iostream>

using namespace std;

class NodoCola {
private:
    string Descrip;
    string Tipo;
    int id, tip;
    NodoCola *Siguiente;
    NodoCola *Anterior;

public:
    //Constructores
    NodoCola();
    NodoCola(int id,string Descrip_,string Tipo_,int tip_, NodoCola *anterior_, NodoCola *siguiente_);

    //Getters
    string getDescrip();
    string getTipo();
    int getId();
    int getTip();
    NodoCola *getSiguiente();
    NodoCola *getAnterior();

    //Setters
    void setDescrip(string descrip);
    void setTipo(string Tipo);
    void setId(int Id);
    void setTip(int Tip);
    void setSiguiente(NodoCola *siguiente);
    void setAnterior(NodoCola *anterior);
};
