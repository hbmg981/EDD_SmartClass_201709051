#include "NodoMatriz.h"

NodoMatriz::NodoMatriz(){
    this-> nombre= "";
    this-> descrip= "";
    this-> carnet= "";
    this-> fecha= "";
    this-> materia= "";
    this-> estado= "";

}

NodoMatriz::NodoMatriz( string carnet_,string nombre_, string descrip_, string materia_, string fecha_, string estado_) {
    this-> nombre= nombre_;
    this-> descrip= descrip_;
    this-> carnet= carnet_;
    this-> fecha= fecha_;
    this-> materia= materia_;
    this-> estado= estado_;
}



string NodoMatriz::getnombre() {
    return this->nombre;
}
string NodoMatriz::getcarnet() {
    return this->carnet;
}
string NodoMatriz::getmateria() {
    return this->materia;
}
string NodoMatriz::getdescrip() {
    return this->descrip;
}
string NodoMatriz::getfecha() {
    return this->fecha;
}
string NodoMatriz::getestado() {
    return this->estado;
}


void NodoMatriz::setnombre(string nombre ){
    this->nombre= nombre;
}
void NodoMatriz::setcarnet(string carnet){
    this->carnet = carnet ;
}
void NodoMatriz::setdescrip(string descrip){
    this->descrip = descrip ;
}
void NodoMatriz::setmateria(string materia){
    this->materia=materia ;
}
void NodoMatriz::setfecha(string fecha ){
    this->fecha=fecha ;
}
void NodoMatriz::setestado(string estado){
    this->estado=estado ;
}

