#include <string>
#include <iostream>

using namespace std;

class NodoCola {
private:
    string Descrip;
    string Tipo;
    int id, tip,tipo2;
    NodoCola *Siguiente;
    NodoCola *Anterior;

public:
    //Constructores
    NodoCola();
    NodoCola(int id,string Descrip_,string Tipo_,int tip_,int tipo2_, NodoCola *anterior_, NodoCola *siguiente_);

    //Getters
    string getDescrip();
    string getTipo();
    int getId();
    int getTip();
    int getTipo2();
    NodoCola *getSiguiente();
    NodoCola *getAnterior();

    //Setters
    void setDescrip(string descrip);
    void setTipo(string Tipo);
    void setId(int Id);
    void setTip(int Tip);
    void setTipo2(int Tipo2);
    void setSiguiente(NodoCola *siguiente);
    void setAnterior(NodoCola *anterior);
};
