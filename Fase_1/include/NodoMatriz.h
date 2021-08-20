#include <string>
#include <iostream>

using namespace std;

class NodoMatriz {
private:
    string nombre, carnet, descrip,materia,fecha,estado;
    //int edad;

public:
    //Constructs
    NodoMatriz();
    NodoMatriz(string carnet, string nombre_, string descrip, string materia, string fecha, string estado );

    //Getters

    string getnombre();
    string getcarnet();
    string getdescrip();
    string getmateria();
    string getfecha();
    string getestado();


    //Setters
    void setnombre(string nombre);
    void setcarnet(string carnet);
    void setdescrip(string descrip );
    void setmateria(string materia);
    void setfecha(string fecha);
    void setestado(string estado);

};
