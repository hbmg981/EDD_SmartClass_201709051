#include <string>
#include <iostream>

using namespace std;

class NodoTarea {
private:
    string mes, dia, hora, carnet, descrip,materia,fecha,estado, nombre;
    int id, index;
    NodoTarea *Next;
    NodoTarea *Previous;

public:
    //Constructs
    NodoTarea();
    NodoTarea(int id,string carnet,string nombre, string descrip, string materia, string fecha, string estado,int index, NodoTarea *next_, NodoTarea *previous_);

    //Getters
    int getid();
    int getindex();
    string getnombre();
    string getcarnet();
    string getdescrip();
    string getmateria();
    string getfecha();
    string getestado();
    NodoTarea *getNext();
    NodoTarea *getPrevious();


    //Setters
    void setcarnet(string carnet);
    void setindex(int index);
    void setnombre(string nombre);
    void setdescrip(string descrip );
    void setmateria(string materia);
    void setfecha(string fecha);
    void setestado(string estado);
    void setNext(NodoTarea *next);
    void setPrevious(NodoTarea *previous);

};
