#include "ClaseCola.h"
#include <string>
#include <sstream>
#include <fstream>
ClaseCola::ClaseCola(){
    this->First = NULL;
    this->Last = 0;
    this->contador =0; // contador para graficar
    this->cont=1;// Contador para ID
    this->archi = 1;

}

int ClaseCola::getSize(){
    NodoCola *aux = First;
    int counter = 0;

    while(aux != NULL){
        counter++;
        aux = aux->getSiguiente();
    }
    delete aux;
    return counter;
}

bool ClaseCola::isEmpty(){
    return this->First == NULL;
}

int  ClaseCola::TipoError(){
    if (this->isEmpty()!=true){
    NodoCola* actual = new NodoCola();
    actual = this->First;
    do{
        if (actual->getTip() ==1 && actual->getTipo2() == 1){
                return 11;
        }else if (actual->getTip() ==1 && actual->getTipo2() == 2){
                return 12;
        }else if (actual->getTip() ==1 && actual->getTipo2() == 3){
                return 13;
        }else if (actual->getTip() ==2 && actual->getTipo2() == 1){
                return 21;
        }else if (actual->getTip() ==2 && actual->getTipo2() == 2){
                return 22;
        }else if (actual->getTip() ==3){
                return 3;
        }
        actual = actual->getSiguiente();
    }while(actual!=NULL);
    }
    return -1;

}

bool ClaseCola::ErrorUsuario(){
    if (this->isEmpty()!=true){
    NodoCola* actual = new NodoCola();
    actual = this->First;
    do{
        if (actual->getTip() ==1){
                return true;
        }
        actual = actual->getSiguiente();
    }while(actual!=NULL);
    }
    return false;
}

bool ClaseCola::ErrorTarea2(){
    if (this->isEmpty()!=true){
    NodoCola* actual = new NodoCola();
    actual = this->First;
    do{
        if (actual->getTip() ==2){
                return true;
        }
        actual = actual->getSiguiente();
    }while(actual!=NULL);
    }
    return false;
}
bool ClaseCola::ErrorTarea3(){
    if (this->isEmpty()!=true){
    NodoCola* actual = new NodoCola();
    actual = this->First;
    do{
        if (actual->getTip() ==3){
                return true;
        }
        actual = actual->getSiguiente();
    }while(actual!=NULL);
    }
    return false;
}

void ClaseCola::getList(){
    NodoCola *aux = First;

    if (aux == NULL){
    cout<<" La lista esta vacia!\n "<<endl;
    }
    else{
    while(aux != NULL){
        cout<< " ID: "<<aux->getId()<<" Descripcion: "<<aux->getDescrip()<<" Tipo: "<<aux->getTipo()<<endl;
        aux = aux->getSiguiente();
    }
    }


    delete aux;
}

void ClaseCola::getListReverse(){
    NodoCola *aux = this->Last;

    while(aux != NULL){
        cout<<aux->getDescrip()<<" - "<<aux->getId()<<endl;
        aux = aux->getAnterior();
    }
    delete aux;
}

void ClaseCola::insertList(string Descrip,string Tipo, int tip_, int tipo2){

    NodoCola *newNode = new NodoCola(this->cont,Descrip,Tipo,tip_,tipo2, NULL, NULL);
    this->contador++;
    this->cont++;
    if(isEmpty()){
        this->First = newNode;
        this->Last = this->First;
    }
    else {
        this->Last->setSiguiente(newNode);
        newNode->setAnterior(this->Last);
        this->Last = newNode;
    }
}

void ClaseCola :: Desencolar(){
    NodoCola *aux = this->First;
    while(this->First != NULL){

            if(aux == this->First){
                aux = this->First->getSiguiente();
                aux->setAnterior(NULL);
                this->contador--;
                this->cont--;
                break;
            }
            this->First = this->First->getSiguiente();
    }
    this->First = aux;


}
void ClaseCola :: generaError(){

        int tam = this->contador;
        string generar = "dot -Tpng error.dot -o error"+to_string(this->archi)+".png";
        string abrir = "start error"+to_string(this->archi)+".png ";
        // verificando que la lista este vacia
        if (isEmpty()){
            cout<<"\n La lista esta vacia!\n "<<endl;
        }else{
            ofstream archivo;
            archivo.open("error.dot",ios::out);
            //iniciando comandos para el grafo
            archivo<<"digraph D { \n";
            archivo<<"\t rankdir =LR \n";
            archivo<<"\t graph [dpi=300]; \n";
            archivo<<"\t node [shape = record, color=blue , style=filled,fillcolor=moccasin]; \n";
            //archivo<<"\t nodo_inicio [shape = point]; \n";

            NodoCola *aux = First;
            int contador=0;
            do{
                    string info= "ID: "+to_string(aux->getId())
                    +"\\n Descripcion: "+ aux->getDescrip()
                    +"\\n Tipo : "+aux->getTipo();
            archivo<<"\t nodo_"<<contador<<"[shape=box, label= \"";
            archivo<<info;
            archivo<<"\"];\n";

            aux = aux->getSiguiente();
            contador++;

            }while(aux != NULL);
            archivo<<"\n";

            if (aux==Last){
            archivo <<"\t nodo_"+to_string(tam)+" \n";

            }else{
            for (int i=1; i<tam; i++){
                    archivo<<"\t nodo_"<<i-1;
                    archivo<<"->";
                    archivo<<" nodo_"<<i<<"\n";

                    /*archivo<<"\t nodo_"<<i;
                    archivo<<"->";
                    archivo<<" nodo_"<<i-1<<"\n";

                }
                archivo<<"\t nodo_"<<tam-1;
                archivo<<"->nodo_0\n";

                archivo<<"\t nodo_0";
                archivo<<"->nodo_"<<tam-1<<"\n";*/

            }
            }

        archivo<<"}\n";
        archivo.close();

        system(generar.c_str());
        system(abrir.c_str());
        this->archi++;
        }


}

