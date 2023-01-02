#include "ListaTarea.h"
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <regex>
#include <ListaU.h>
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

bool ListaTarea::buscarIndex(int index){
    if (this->isEmpty()!=true){
    NodoTarea* actual = new NodoTarea();
    actual = this->First;
    do{
        if (actual->getindex() ==index){
                return true;
        }
        actual = actual->getNext();
    }while(actual!=NULL);


    }
    return false;

}
bool ListaTarea::ValorOcupado(){
    if (this->isEmpty()!=true){
    NodoTarea* actual = new NodoTarea();
    actual = this->First;
    do{
        if (actual->getcarnet() !="-1"){
                return true;
        }
        actual = actual->getNext();
    }while(actual!=NULL);


    }
    return false;

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

void ListaTarea::deleteValue(int index) {
    NodoTarea* aux = this->First;
    while(aux != NULL){
        if(aux->getindex() == index){
            cout<<"Tarea Encontrada "<<endl;
            aux->setcarnet("-1");
            aux->setnombre("-1");
            aux->setdescrip("-1");
            aux->setmateria("-1");
            aux->setfecha("-1");
            aux->setestado("-1");
            aux->sethora("-1");
         cout<<"Tarea Eliminada "<<endl;
        }
        aux = aux->getNext();
    }
   // this->First = aux;
}
void ListaTarea::ModificarNodo(string carnet_,string nombre_, string descrip_, string materia_, string fecha_,string hora_, string estado_,int index) {
    NodoTarea* actual = new NodoTarea();
    actual = this->First;
    bool encontrado = false;
    if (this->First != NULL){
        do{
             if (actual->getindex() ==index){
                cout<<"Tarea Encontrada "<<endl;
                encontrado=true;
                actual->setcarnet(carnet_);
                actual->setnombre(nombre_);
                actual->setdescrip(descrip_);
                actual->setmateria(materia_);
                actual->setfecha(fecha_);
                actual->sethora(hora_);
                actual->setestado(estado_);
                actual->setid(this->id);
                cout<<"Tarea Modificada con exito "<<endl;
        }
        actual = actual->getNext();

        }
        while (actual!=NULL && encontrado!=true);

        if(!encontrado){
            cout<<"Tarea no encontrada\n "<<endl;
        }

    }else {
    cout<<" * La lista esta vacia!!  *\n"<<endl;
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
                    string info=" Carnet: "+ aux->getcarnet()
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

void ListaTarea::BuscarTarea(int mes, int dia, int hora){
    //i+5*(j+30*k)
    NodoTarea *aux = First;
    while(aux != NULL){//hora1+9*((dia1-1)+30*(mes1))
        if(aux->getindex() == hora+9*((dia-1)+30*mes)){
            cout<<"***************** Tarea Encontrada **************"<<endl;
            cout<<" Carnet: "<<aux->getcarnet()<<" -- Nombre  "<<aux->getnombre()<<" -- Descripcion: "<<aux->getdescrip()<<endl;
            cout<<" Materia: "<<aux->getmateria()<<" -- Fecha "<<aux->getfecha()<<" -- Estado "<<aux->getestado()<<endl;
            break;
        }
        aux = aux->getNext();
    }
    delete aux;
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
        node_data += "Node" + to_string(counter) + "[label=\""+" ID: " + to_string(aux->getindex())+ "\\n Carnet: " + aux->getcarnet() +"\\n Nombre: "+ aux->getnombre()+"\\n Descripcion: "+ aux->getdescrip()+"\\n Materia: "+aux->getmateria()+"\\n Fecha: "+aux->getfecha()+ "\\n Hora: " + aux->gethora() +":00"+"\\n Estado: "+aux->getestado()+"\\n Id2: "+to_string(aux->getid())+ "\"];\n";
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

void ListaTarea::ModificarDato(string dato, int tipoerror, int index){
    if (this->isEmpty()!=true){
    NodoTarea* actual = new NodoTarea();
    actual = this->First;
    do{
        if (actual->getindex() ==index){
                cout<<" Tarea Encontrada!\n "<<endl;
                if(tipoerror ==21){
                actual->setcarnet(dato);
                cout<<" Carnet Cambiado!\n "<<endl;
                }else if(tipoerror ==22){
                actual->setfecha(dato);
                cout<<" Fecha Cambiada!\n "<<endl;
                }
        }

        actual = actual->getNext();
    }while(actual!=NULL);


    }
    //return false;


}


void ListaTarea::generatxt(){
        string abrir = "start repo6.txt";
        if (isEmpty()){
            cout<<"\n La lista esta vacia!\n "<<endl;
        }else{
            ofstream archivo;
            archivo.open("repo6.txt",ios::app);
            //iniciando comandos para el grafo
            //archivo<<"¿Elements?\n";
            NodoTarea *aux = First;
            int contador=0;


            do{
                if (aux->getid() != -1){
                        //split de la fecha para txt
            string dia, mes, a, nuevaFecha, fe;
            if (this->validarFecha(aux->getfecha())==true){
            string fechaF[3] = {"","",""};
            string dato = "";
            int contador =0;
            for (int i=0;i<aux->getfecha().length(); i++){
                if (aux->getfecha()[i]!= '/'){
                    dato+=aux->getfecha()[i];
                }else{
                    fechaF[contador]=dato;
                    dato ="";
                    contador++;
                }
            }
            fechaF[contador]=dato;
            dia = fechaF[2];
            mes = fechaF[1];
            a = fechaF[0];
            nuevaFecha= dia+"/"+mes+"/"+a;
            fe=nuevaFecha;
            }else{
            nuevaFecha=aux->getfecha();
            }
                    string info= "\t ¿element type=\"task\"? \n \t \t ¿item Carnet=\""+aux->getcarnet()+"\" $?"
                    +"\n \t \t ¿item Nombre=\" "+aux->getnombre()+"\" $?"
                    +"\n \t \t ¿item Descripcion=\" "+ aux->getdescrip()+"\" $?"
                    +"\n \t \t ¿item Materia=\" "+aux->getmateria()+"\" $?"
                    +"\n \t \t ¿item Fecha=\" "+nuevaFecha+"\" $?"
                    +"\n \t \t ¿item Hora=\" "+aux->gethora()+":00"+"\" $?"
                    +"\n \t \t ¿item Estado=\" "+aux->getestado()+"\" $?";
            archivo<<info;
            archivo<<"\n \t ¿$element?\n";

            }


            aux = aux->getNext();
            contador++;

            }while(aux != NULL);
            archivo<<"\n";
            archivo<<"¿$Elements?\n";
            archivo.close();


            }



       //system(generar.c_str());
        system(abrir.c_str());
       // this->archi++;


}


bool ListaTarea::validarFecha(const string& fecha_){
    //Regex para la fecha
    const regex expReg("^[0-9]{4}/[0-9]{2}/[0-9]{2}$");
    if (regex_match(fecha_,expReg)){
            string fechaF[3] = {"","",""};
            string dato = "";
            int contador =0;
            for (int i=0;i<fecha_.length(); i++){
                if (fecha_[i]!= '/'){
                    dato+=fecha_[i];
                }else{
                    fechaF[contador]=dato;
                    dato ="";
                    contador++;

                }

            }
            fechaF[contador]=dato;
            //int dia1;  istringstream(dia)>>dia1;
            int dia, mes, a;
            istringstream(fechaF[0])>>a;
            istringstream(fechaF[1])>>mes;
            istringstream(fechaF[2])>>dia;
            if (a!= 2021){
                return false;
            }else if (mes<7 || mes >11){
                return false;
            }else if (dia <1 || dia>30){
                return false;
            }




    }else{
        return false;
    }
    return true;
}
void ListaTarea::CambiarFecha(string fecha_){
            string fechaF[3] = {"","",""};
            string dato = "";
            int contador =0;
            for (int i=0;i<fecha_.length(); i++){
                if (fecha_[i]!= '/'){
                    dato+=fecha_[i];
                }else{
                    fechaF[contador]=dato;
                    dato ="";
                    contador++;

                }

            }
            fechaF[contador]=dato;
            string dia, mes, a, nuevaFecha;
            nuevaFecha= dia+"/"+mes+"/"+a;
           // return nuevaFecha;
}
