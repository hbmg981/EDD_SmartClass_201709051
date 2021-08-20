#include <string>
#include <iostream>

using namespace std;

class NodoU {
private:
    int id;
    string carnet;
    string dpi;
    string nombre;
    string carrera;
    string correo;
    string pass;
    string creditos;
    string edad;
    NodoU *Next;
    NodoU *Previous;

public:
    //Constructs
    NodoU();
    NodoU(int id,string carnet,string dpi,string nombre,string carrera,string correo,string pass,string creditos,string edad, NodoU *next_, NodoU *previous_);

    //Getters
    int getid();
    string getcarnet();
    string getdpi();
    string getnombre();
    string getcarrera();
    string getcorreo();
    string getpass();
    string getcreditos();
    string getedad();
    NodoU *getNext();
    NodoU *getPrevious();

    //Setters
    void setid(int id);
    void setnombre(string nombre);
    void setcarrera(string carrera);
    void setcorreo(string correo);
    void setpass(string pass);
    void setcreditos(string edad);
    void setcarnet(string edad);
    void setdpi(string edad);
    void setedad(string edad);
    void setNext(NodoU *next);
    void setPrevious(NodoU *previous);
};
