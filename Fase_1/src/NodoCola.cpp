#include "NodoCola.h"

NodoCola::NodoCola(){
    this->Descrip = "";
    this->Tipo = "";
    this->id = 1;
    this->Siguiente = NULL;
    this->Anterior = 0;
}

NodoCola::NodoCola(int id,string Descrip,string Tipo,  NodoCola *Siguiente_, NodoCola *Anterior_){
    this->Descrip =Descrip;
    this->Tipo = Tipo;
    this->id = id;
    this->Siguiente = Siguiente_;
    this->Anterior = Anterior_;
}

string NodoCola::getDescrip() {
    return this->Descrip;
}
string NodoCola::getTipo() {
    return this->Tipo;
}
int NodoCola::getId(){
    return this->id;
}

NodoCola *NodoCola::getSiguiente(){
    return this->Siguiente;
}

NodoCola *NodoCola::getAnterior(){
    return this->Anterior;
}
void NodoCola::setDescrip(string Descrip){
    this->Descrip = Descrip;
}
void NodoCola::setId(int id){
    this->id = id;
}

void NodoCola::setSiguiente(NodoCola *next){
    this->Siguiente = next;
}

void NodoCola::setAnterior(NodoCola *previous){
    this->Anterior = previous;
}
