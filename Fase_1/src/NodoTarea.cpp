#include "NodoTarea.h"

NodoTarea::NodoTarea(){
    this-> descrip= "";
    this-> nombre= "";
    this-> carnet= "";
    this-> fecha= "";
    this-> materia= "";
    this-> estado= "";
    this->id =1;
    this->index =0;
    this->Next = NULL;
    this->Previous = 0;
}

NodoTarea::NodoTarea(int id_,string carnet_,string nombre_, string descrip_, string materia_, string fecha_, string estado_,int index_,NodoTarea *next_, NodoTarea *previous_) {
    this-> id= id_;
    this-> index= index_;
    this-> descrip= descrip_;
    this-> nombre= nombre_;
    this-> carnet= carnet_;
    this-> fecha= fecha_;
    this-> materia= materia_;
    this-> estado= estado_;
    this->Next = next_;
    this->Previous = previous_;
}
int NodoTarea::getid() {
    return this->id;
}
int NodoTarea::getindex() {
    return this->index;
}
string NodoTarea::getcarnet() {
    return this->carnet;
}
string NodoTarea::getnombre() {
    return this->nombre;
}
string NodoTarea::getmateria() {
    return this->materia;
}
string NodoTarea::getdescrip() {
    return this->descrip;
}
string NodoTarea::getfecha() {
    return this->fecha;
}
string NodoTarea::getestado() {
    return this->estado;
}

NodoTarea *NodoTarea::getNext(){
    return this->Next;
}

NodoTarea *NodoTarea::getPrevious(){
    return this->Previous;
}

void NodoTarea::setcarnet(string carnet){
    this->carnet = carnet ;
}
void NodoTarea::setindex(int index){
    this->index = index;
}
void NodoTarea::setnombre(string nombre){
    this->nombre = nombre ;
}
void NodoTarea::setdescrip(string descrip){
    this->descrip = descrip ;
}
void NodoTarea::setmateria(string materia){
    this->materia=materia ;
}
void NodoTarea::setfecha(string fecha ){
    this->fecha=fecha ;
}
void NodoTarea::setestado(string estado){
    this->estado=estado ;
}
void NodoTarea::setNext(NodoTarea *next){
    this->Next = next;
}

void NodoTarea::setPrevious(NodoTarea *previous){
    this->Previous = previous;
}

