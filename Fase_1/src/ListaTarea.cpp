#include "ListaTarea.h"
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
ListaTarea::ListaTarea(){
    this->First = NULL;
    this->Last = 0;
    this->id =1;
    this->tam=0;
    this->archi=1;
}

int ListaTarea::getSize(){
    NodoTarea *aux = First;
    int counter = 0;

    while(aux != NULL){
        counter++;
        //tam++;
        aux = aux->getNext();
    }
    delete aux;
    return counter;
}

bool ListaTarea::isEmpty(){
    return this->First == NULL;
}

void ListaTarea::getList(){
    NodoTarea *aux = First;
    while(aux != NULL){
        cout<<" ID: "<<aux->getid()<<" Carnet: "<<aux->getcarnet()<<"\t Descripcion: "<<aux->getdescrip()<<endl;
        cout<<"\t Materia: "<<aux->getmateria()<<"\t Fecha: "<<aux->getfecha()<<" Estado: "<<aux->getestado()<<" \n"<<endl;
        aux = aux->getNext();
    }
    delete aux;
}

void ListaTarea::getListReverse(){
    NodoTarea *aux = Last;
    if (Last != NULL){
            do{
        cout<<" ID: "<<aux->getid()<<" Carnet: "<<aux->getcarnet()<<"\t Descripcion: "<<aux->getdescrip()<<endl;
        cout<<"\t Materia: "<<aux->getmateria()<<"\t Fecha: "<<aux->getfecha()<<" Estado: "<<aux->getestado()<<" \n"<<endl;
        aux = aux->getPrevious();
            }while(aux!=Last);
        cout<<" ID: "<<aux->getid()<<" Carnet: "<<aux->getcarnet()<<"\t Descripcion: "<<aux->getdescrip()<<endl;
        cout<<"\t Materia: "<<aux->getmateria()<<"\t Fecha: "<<aux->getfecha()<<" Estado: "<<aux->getestado()<<" \n"<<endl;
    }else{
            cout<<" La lista esta vacia!\n ";
    }

    delete aux;
}

void ListaTarea::insertList(string carnet_,string nombre_, string descrip_, string materia_, string fecha_,string hora_, string estado_,int index_){
    int idaux;
    if (carnet_=="-1"){
        idaux= -1;
    }else{

        idaux=this->id;
        this->id++;
    }
    NodoTarea *newNode = new NodoTarea(idaux,carnet_,nombre_,descrip_,materia_,fecha_,hora_,estado_,index_, NULL, NULL);
    this->tam++;
    if(isEmpty()){
        this->First = newNode;
        this->Last = this->First;
    }
    else {
        this->Last->setNext(newNode);
        newNode->setPrevious(this->Last);
        this->Last = newNode;
    }
}

void ListaTarea::deleteValue(string carnet) {
    NodoTarea *aux = this->First;
    while(this->First != NULL){
        if(this->First->getcarnet() == carnet){
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
void ListaTarea::ModificarNodo(string id) {
    NodoTarea* actual = new NodoTarea();
    actual = this->First;
    bool encontrado = false;
    //int DPI = 0;
    cout<<"Ingrese el ID de la tarea a buscar "<<endl;
    cin>> id;
    if (this->First != NULL){

        while (actual!=NULL && encontrado!=true){

            if (actual->getid() ==stoi(id)){
                cout<<"Tarea Encontrada "<<endl;


            }

        }
    }



}


void ListaTarea::generaTarea(){
        //this->getList();
        NodoTarea *aux = First;
        int tam = this->tam;
        string generar = "dot -Tbmp archivoTarea.dot -o tarea"+to_string(this->archi)+".bmp";
        string abrir = "start tarea"+to_string(this->archi)+".bmp ";
        // verificando que la lista este vacia
        if (isEmpty()){
            cout<<"\n La lista esta vacia!\n "<<endl;
        }else{
            ofstream archivo;
            archivo.open("archivoTarea.dot",ios::out);
            //iniciando comandos para el grafo
            archivo<<"digraph D { \n";
            archivo<<"\t rankdir =LR \n";
            archivo<<"\t graph [dpi=300]; \n";
            archivo<<"\t nodo_inicio [shape = point]; \n";


            int contador=0;
            do{
                    string info= "ID: "+to_string(aux->getid())
                    +"\\n Carnet: "+ aux->getcarnet()
                    +"\\n Nombre: "+aux->getnombre()
                    +"\\n Descripcion : "+aux->getdescrip()
                    +"\\n Materia: "+aux->getmateria()
                    +"\\n Fecha: "+aux->getfecha()
                    +"\\n Estado: "+aux->getestado();
            archivo<<"\t nodo_"<<contador<<"[shape=box, label= \"";
            archivo<<info;
            archivo<<"\"];\n";


            aux = aux->getNext();
            contador++;

            }while(aux!=NULL);
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
               /* archivo<<"\t nodo_"<<tam-1;
                archivo<<"->nodo_0\n";

                archivo<<"\t nodo_0";
                archivo<<"->nodo_"<<tam-1<<"\n";*/


            }

        archivo<<"}\n";
        archivo.close();

        system(generar.c_str());
        system(abrir.c_str());
        this->archi++;
        }


}


void ListaTarea::generaTarea1(){
    NodoTarea *aux = First;
    int contadornodo=0;
    int contadorgraficas=0;
    while (contadorgraficas<3){
    string node_data = "";
    string edge_data = "";
    string graph = "digraph List {\nrankdir=LR;\n node [shape = record, color=blue , style=filled,fillcolor=darkseagreen1];\n";
    string abrir = "start tarea"+to_string(contadorgraficas)+".svg ";
    int counter = 0;
    if (contadorgraficas!=0){
        counter = 1;
    }
    while(aux != NULL && contadornodo<450){
        //cout<<aux->getnombre()<<endl;
        node_data += "Node" + to_string(counter) + "[label=\""+" ID: " + to_string(aux->getid())+ "\\n Carnet: " + aux->getcarnet() +"\\n Nombre: "+ aux->getnombre()+"\\n Descripcion: "+ aux->getdescrip()+"\\n Materia: "+aux->getmateria()+"\\n Fecha: "+aux->getfecha()+ "\\n Hora: " + aux->gethora() +":00"+"\\n Estado: "+aux->getestado()+"\\n Index: "+to_string(aux->getindex())+ "\"];\n";
        if(aux->getPrevious()!=NULL){
            edge_data += "Node" + to_string(counter-1) + "->Node" + to_string(counter) + ";\n";
            edge_data += "Node" + to_string(counter) + "->Node" + to_string(counter-1) + ";\n";
        }
        counter++;
        contadornodo++;
        aux = aux->getNext();
    }
    graph += node_data;
    graph += edge_data;
    graph += "\n}";
    //-------------------------------------
    try{
        //Esta variable debe ser modificada para agregar su path de creacion de la Grafica
        //string generar = "dot -Tbmp archivoTarea.dot -o tarea"+to_string(this->archi)+".bmp";
        //string abrir = "start tarea"+to_string(this->archi)+".bmp ";
        string path = "Path_a_graficar";

        ofstream file;
        file.open("Graph"+to_string(contadorgraficas)+".dot",std::ios::out);

        if(file.fail()){
            exit(1);
        }
        file<<graph;
        file.close();
        string command = "dot -Tsvg Graph"+to_string(contadorgraficas)+".dot -o  tarea"+to_string(contadorgraficas)+".svg";
        system(command.c_str());
        system(abrir.c_str());

        contadornodo=0;
    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    contadorgraficas++;
    }



    delete aux;
}
