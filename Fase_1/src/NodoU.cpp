#include "NodoU.h"

NodoU::NodoU(){
    this->id = 1;
    this->carnet= "";
    this->dpi="";
    this->nombre= "";
    this->carrera= "";
    this->correo= "";
    this->pass= "";
    this->creditos= "";
    this->edad= "";
    this->Next = NULL;
    this->Previous = 0;
}

NodoU::NodoU(int id_,string carnet_,string dpi_,string nombre_,string carrera_,string correo_,string pass_,string creditos_,string edad_, NodoU *next_, NodoU *previous_){
    this->id= id_;
    this->carnet= carnet_;
    this->dpi= dpi_;
    this->nombre= nombre_;
    this->carrera= carrera_;
    this->correo= correo_;
    this->pass= pass_;
    this->creditos= creditos_;
    this->edad= edad_;
    this->Next = next_;
    this->Previous = previous_;
}
int NodoU::getid(){
    return this->id;
}
string NodoU::getcarnet(){
    return this->carnet;
}
string NodoU::getdpi(){
    return this->dpi;
}
string NodoU::getnombre() {
    return this->nombre;
}
string NodoU::getcarrera() {
    return this->carrera;
}
string NodoU::getcorreo() {
    return this->correo;
}
string NodoU::getpass() {
    return this->pass;
}

string NodoU::getedad(){
    return this->edad;
}
string NodoU::getcreditos(){
    return this->creditos;
}

NodoU *NodoU::getNext(){
    return this->Next;
}

NodoU *NodoU::getPrevious(){
    return this->Previous;
}
void NodoU::setid(int id){
    this->id = id;
}
void NodoU::setnombre(string nombre){
    this->nombre = nombre;
}
void NodoU::setcarrera(string carrera){
    this->carrera = carrera;
}
void NodoU::setcorreo(string correo){
    this->correo = correo;
}
void NodoU::setpass(string pass){
    this->pass = pass;
}
void NodoU::setedad(string edad){
    this->edad = edad;
}
void NodoU::setdpi(string dpi){
    this->dpi = dpi;
}
void NodoU::setcarnet(string carnet){
    this->carnet = carnet;
}
void NodoU::setcreditos(string creditos){
    this->creditos = creditos;
}
void NodoU::setNext(NodoU *next){
    this->Next = next;
}

void NodoU::setPrevious(NodoU *previous){
    this->Previous = previous;
}
