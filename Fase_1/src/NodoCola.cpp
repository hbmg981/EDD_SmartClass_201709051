#include "NodoCola.h"

NodoCola::NodoCola(){
    this->Descrip = "";
    this->Tipo = "";
    this->id = 1;
    this->tip = 0;
    this->Siguiente = NULL;
    this->Anterior = 0;
}

NodoCola::NodoCola(int id,string Descrip,string Tipo,int tip_,  NodoCola *Siguiente_, NodoCola *Anterior_){
    this->Descrip =Descrip;
    this->Tipo = Tipo;
    this->id = id;
    this->tip = tip_;
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
int NodoCola::getTip(){
    return this->tip;
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
void NodoCola::setTip(int tip){
    this->tip = tip;
}

void NodoCola::setSiguiente(NodoCola *next){
    this->Siguiente = next;
}

void NodoCola::setAnterior(NodoCola *previous){
    this->Anterior = previous;
}
