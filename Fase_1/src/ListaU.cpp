#include "ListaU.h"
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include<regex>
ListaU::ListaU(){
    this->First = NULL;
    this->Last = 0;
    this->id =1;
    this->tam=0;
    this->archi=1;
}

int ListaU::getSize(){
    NodoU *aux = First;
    int counter = 0;

    while(aux != NULL){
        counter++;
        //tam++;
        aux = aux->getNext();
    }
    delete aux;
    return counter;
}

bool ListaU::isEmpty(){
    return this->First == NULL;
}
bool ListaU::buscarUsuarioDPI(string DPI){
   if (this->isEmpty()!=true){
    NodoU* actual = new NodoU();
    actual = this->First;
    do{
        if (actual->getdpi() ==DPI){
                return true;
        }
        actual = actual->getNext();
    }while(actual!=this->First);


    }
    return false;
}
bool ListaU::buscarUsuarioCarnet(string Carnet){
    if (this->isEmpty()!=true){
    NodoU* actual = new NodoU();
    actual = this->First;
    do{
        if (actual->getcarnet() ==Carnet){
                return true;
        }
        actual = actual->getNext();
    }while(actual!=this->First);


    }
    return false;


}
void ListaU::ModificarDato(string dato){
    if (this->isEmpty()!=true){
    NodoU* actual = new NodoU();
    actual = this->First;
    do{
        if (actual->getcarnet() ==dato){

                actual->setcarnet(dato);
                cout<<" Carnet Cambiado!\n "<<endl;
        }else if(actual->getdpi() ==dato){
                actual->setdpi(dato);
                cout<<" Dpi Cambiado!\n "<<endl;
        }else if(actual->getcorreo() ==dato){
                actual->setcorreo(dato);
                cout<<" Correo Cambiado!\n "<<endl;
        }else{
            cout<<" No se encontro el dato !\n " + dato <<endl;
        }

        actual = actual->getNext();
    }while(actual!=this->First);


    }
    //return false;


}

void ListaU::getList(){
    NodoU *aux = First;
    if (First != NULL){
            do{
       // string nombre,carrera,correo,pass,carnet,dpi,creditos,edad;
        cout<<" ID: "<<aux->getid()<<" Carnet: "<<aux->getcarnet()<<"\t DPI: "<<aux->getdpi()<<"\t Nombre: "<<aux->getnombre()<<"\t Carrera: "<<aux->getcarrera()<<endl;
        cout<<" Correo: "<<aux->getcorreo()<<"\t PassWord: "<<aux->getpass()<<"\t Creditos: "<<aux->getcreditos()<<"\t Edad : "<<aux->getedad()<<" \n"<<endl;
        aux = aux->getNext();
            }while(aux!=First);
        cout<<" ID: "<<aux->getid()<<" Carnet: "<<aux->getcarnet()<<"\t DPI: "<<aux->getdpi()<<"\t Nombre: "<<aux->getnombre()<<"\t Carrera: "<<aux->getcarrera()<<endl;
        cout<<" Correo: "<<aux->getcorreo()<<"\t PassWord: "<<aux->getpass()<<"\t Creditos: "<<aux->getcreditos()<<"\t Edad : "<<aux->getedad()<<" \n"<<endl;
    }else{
            cout<<" La lista esta vacia!\n "<<endl;
    }
    delete aux;
}

void ListaU::getListReverse(){
    NodoU *aux = Last;
    if (Last != NULL){
            do{
        cout<<" ID: "<<aux->getid()<<" Carnet: "<<aux->getcarnet()<<"\t DPI: "<<aux->getdpi()<<"\t Nombre: "<<aux->getnombre()<<"\t Carrera: "<<aux->getcarrera()<<endl;
        cout<<" Correo: "<<aux->getcorreo()<<"\t PassWord: "<<aux->getpass()<<"\t Creditos: "<<aux->getcreditos()<<"\t Edad : "<<aux->getedad()<<" \n"<<endl;
        aux = aux->getPrevious();
            }while(aux!=Last);
        cout<<" ID: "<<aux->getid()<<" Carnet: "<<aux->getcarnet()<<"\t DPI: "<<aux->getdpi()<<"\t Nombre: "<<aux->getnombre()<<"\t Carrera: "<<aux->getcarrera()<<endl;
        cout<<" Correo: "<<aux->getcorreo()<<"\t PassWord: "<<aux->getpass()<<"\t Creditos: "<<aux->getcreditos()<<"\t Edad : "<<aux->getedad()<<" \n"<<endl;
    }else{
            cout<<" La lista esta vacia!\n ";
    }

    delete aux;
}

void ListaU::insertList(string carnet_,string dpi_,string nombre_,string carrera_,string correo_,string pass_,string creditos_,string edad_){

    NodoU *newNode = new NodoU(this->id,carnet_,dpi_,nombre_,carrera_,correo_,pass_,creditos_,edad_, NULL, NULL);
    this->id++;
    this->tam++;
    if(isEmpty()){
        this->First = newNode;
        this->First->setNext(this->First) ;
        this->First->setPrevious(this->First);
        this->Last = this->First;
    }
    else {
        this->Last->setNext(newNode);
        newNode->setNext(this->First);
        newNode->setPrevious(this->Last);
        this->Last = newNode;
        this->First->setPrevious(this->Last);
    }







    /*if(this->First==NULL){
    cout<<" insertando primer nodo!\n " <<endl;



    }else{
        cout<<" verificando nodo!\n " <<endl;
    if(this->buscarUsuarioDPI(dpi_)== false){
        cout<<" no se encontraron dpi repetidos!\n " <<endl;
            if(this->buscarUsuarioCarnet(carnet_)==false){
            cout<<" no se encontraron carnet repetidos!\n " <<endl;
    NodoU *newNode = new NodoU(this->id,carnet_,dpi_,nombre_,carrera_,correo_,pass_,creditos_,edad_, NULL, NULL);
    this->id++;
    this->tam++;
    if(isEmpty()){
        this->First = newNode;
        this->First->setNext(this->First) ;
        this->First->setPrevious(this->First);
        this->Last = this->First;
    }
    else {
        this->Last->setNext(newNode);
        newNode->setNext(this->First);
        newNode->setPrevious(this->Last);
        this->Last = newNode;
        this->First->setPrevious(this->Last);
    }
    }else {
        cout<<" El usuario ya existe, Carnet o DPI Repetido!\n " <<endl;
    } }else{
            cout<<" El usuario ya existe, Carnet o DPI Repetido!\n " <<endl;
    }}*/




}

void ListaU::deleteValue(string dpi) {
    NodoU *aux = this->First;
    while(this->First != NULL){
        if(this->First->getdpi() == dpi){
            if(aux == this->First){
                aux = this->First->getNext();
                aux->setPrevious(NULL);
                this->id-=1;
                this->tam-=1;
                break;
            }
            else if (this->First == this->Last){
                this->Last = this->First->getPrevious();
                this->Last->setNext(NULL);
                this->id-=1;
                this->tam-=1;
                break;
            }
            else {
                this->First->getNext()->setPrevious(this->First->getPrevious());
                this->First->getPrevious()->setNext(this->First->getNext());
                this->id-=1;
                this->tam-=1;
                break;
            }
        }
        this->First = this->First->getNext();
    }
    this->First = aux;
}
void ListaU::ModificarNodo(string DPI) {
    NodoU* actual = new NodoU();
    actual = this->First;
    bool encontrado = false;
    if (this->First != NULL){
        do{
            if (actual->getdpi() ==DPI){
                cout<<"\n Estudiante Encontrado\n "<<endl;

                string nombre,carrera,correo,pass,carnet,dpi,creditos,edad;
                //cin.ignore();
                cout<<" *  Ingrese el numero de Carnet *\n"<<endl;
                getline(cin,carnet);
                if (this->validarCarnet(carnet)== true){
                    actual->setcarnet(carnet);
                }else{
                //while(this->validarCarnet(carnet)== false){
                cout<<" *  Ingrese un numero de Carnet valido (9 digitos) *\n"<<endl;
                getline(cin,carnet);
                    if (this->validarCarnet(carnet)== true){
                    actual->setcarnet(carnet);}
               // }
                }
                cout<<" *  Ingrese el numero de DPI *\n"<<endl;
                getline(cin,dpi);
                if (this->validarDpi(dpi)== true){
                    actual->setdpi(dpi);
                }else{
                cout<<" *  Ingrese un numero de DPI valido (13 digitos) *\n"<<endl;
                getline(cin,dpi);
                    if (this->validarDpi(dpi)== true){
                    actual->setdpi(dpi);}
                    }
                cout<<" *  Ingrese el Nombre        *\n"<<endl;
                getline(cin,nombre);
                actual->setnombre(nombre);
                cout<<" *  Ingrese la Carrera       *\n"<<endl;
                getline(cin,carrera);
                actual->setcarrera(carrera);
                cout<<" *  Ingrese el Correo        *\n"<<endl;
                getline(cin,correo);
                if (this->validarCorreo(correo)== true){
                    actual->setcorreo(correo);
                }else{
                cout<<" *  Ingrese un correo valido user@dominio.[com|es|org] *\n"<<endl;
                getline(cin,correo);
                    if (this->validarCorreo(correo)== true){
                    actual->setcorreo(correo);}
                    }
                cout<<" *  Ingrese la Password      *\n"<<endl;
                getline(cin,pass);
                actual->setpass(pass);
                cout<<" *  Ingrese el numero de Creditos *\n"<<endl;
                getline(cin,creditos);
                actual->setcreditos(creditos);
                cout<<" *  Ingrese la edad              *\n"<<endl;
                getline(cin,edad);
                actual->setedad(edad);
                encontrado=true;
                cout<<"Estudiante Modificado con exito \n"<<endl;



        }
        actual = actual->getNext();

        }
        while (actual!=First && encontrado!=true);

        if(!encontrado){
            cout<<"Estudiante no encontrado\n "<<endl;
        }

    }else {
    cout<<" * La lista esta vacia!!  *\n"<<endl;
    }



}
string ListaU:: obtenerListaGraphviz(){
    NodoU *aux = First;
    if (First != NULL){
            do{
                    string id =" "+aux->getid();
                    cout<<" ID: "<<id;

             aux = aux->getNext();
            }while(aux!=First);
            string id =" "+aux->getid();
            cout<<" ID: "<<id;
    }else{
            cout<<" La lista esta vacia!\n ";
    }
    delete aux;
}
void ListaU::generaDot(){
        //this->getList();
        int tam = this->tam;
        string generar = "dot -Tsvg archivo.dot -o graf"+to_string(this->archi)+".svg";
        string abrir = "start graf"+to_string(this->archi)+".svg ";
        // verificando que la lista este vacia
        if (isEmpty()){
            cout<<"\n La lista esta vacia!\n "<<endl;
        }else{
            ofstream archivo;
            archivo.open("archivo.dot",ios::out);
            //iniciando comandos para el grafo
            archivo<<"digraph D { \n";
            archivo<<"\t rankdir =LR \n";
            //archivo<<"\t graph [dpi=600]; \n";
            archivo<<"\t node [shape = record, color=blue , style=filled,fillcolor=thistle1]; \n";

            NodoU *aux = First;
            int contador=0;
            do{
                    string info= "Carnet: "+aux->getcarnet()
                    +"\\n DPI: "+ aux->getdpi()
                    +"\\n Nombre: "+aux->getnombre()
                    +"\\n Carrera : "+aux->getcarrera()
                    +"\\n Password: "+aux->getpass()
                    +"\\n Creditos: "+aux->getcreditos()
                    +"\\n Edad: "+aux->getedad()
                    +"\\n Correo: "+aux->getcorreo();
            archivo<<"\t nodo_"<<contador<<"[shape=box, label= \"";
            archivo<<info;
            archivo<<"\"];\n";

            aux = aux->getNext();
            contador++;

            }while(aux != First);
            archivo<<"\n";

            if (tam==1){
            archivo <<"\t nodo_0 -> nodo_0 \n";

            }else{
                for (int i=1; i<tam; i++){
                    archivo<<"\t nodo_"<<i-1;
                    archivo<<"->";
                    archivo<<" nodo_"<<i<<"\n";

                    archivo<<"\t nodo_"<<i;
                    archivo<<"->";
                    archivo<<" nodo_"<<i-1<<"\n";

                }
                archivo<<"\t nodo_"<<tam-1;
                archivo<<"->nodo_0\n";

                archivo<<"\t nodo_0";
                archivo<<"->nodo_"<<tam-1<<"\n";


            }

        archivo<<"}\n";
        archivo.close();

        system(generar.c_str());
        system(abrir.c_str());
        this->archi++;
        }


}

void ListaU::generatxt(){
        // verificando que la lista este vacia
        if (isEmpty()){
            cout<<"\n La lista esta vacia!\n "<<endl;
        }else{
            ofstream archivo;
            archivo.open("repo6.txt",ios::out);
            //iniciando comandos para el grafo
            archivo<<"¿Elements?\n";
            NodoU *aux = First;
            int contador=0;
            do{
                    string info= "\t ¿element type=\"user\"? \n \t \t ¿item Carnet=\""+aux->getcarnet()+"\" $?"
                    +"\n \t \t ¿item DPI=\" "+ aux->getdpi()+"\" $?"
                    +"\n \t \t ¿item Nombre=\" "+aux->getnombre()+"\" $?"
                    +"\n \t \t ¿item Carrera=\" "+aux->getcarrera()+"\" $?"
                    +"\n \t \t ¿item Password=\" "+aux->getpass()+"\" $?"
                    +"\n \t \t ¿item Creditos=\" "+aux->getcreditos()+"\" $?"
                    +"\n \t \t ¿item Edad=\" "+aux->getedad()+"\" $?"
                    +"\n \t \t ¿item Correo=\" "+aux->getcorreo()+"\" $?";
            //archivo<<"\t nodo_"<<contador<<"[shape=box, label= \"";
            archivo<<info;
            archivo<<"\n \t ¿$element?\n";

            aux = aux->getNext();
            contador++;

            }while(aux != First);
            archivo<<"\n";



            }

       // archivo<<"}\n";
      //  archivo.close();

       // system(generar.c_str());
       // system(abrir.c_str());
       // this->archi++;



}

bool ListaU::validarCarnet(const string& carnet){
    //Regex para el Carnet
    const regex expReg("[0-9]{9}");
    return regex_match(carnet,expReg);
}
bool ListaU:: validarDpi(const string& dpi){
    //Regex para el Dpi
    const regex expReg("[0-9]{13}");
    return regex_match(dpi,expReg);
}
bool ListaU::validarCorreo(const string& correo){
    //Regex para el Correo
    const regex expReg("^[^@]+@[^@]+\.(es|org|com)$");
    return regex_match(correo,expReg);
}

