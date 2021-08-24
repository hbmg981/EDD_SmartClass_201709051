#include <iostream>
#include  <windows.h>
#include <sstream>
#include <fstream>
#include <string>
#include <string.h>
# include <conio.h>
# include <ListaU.h>
# include <ClaseCola.h>
# include <ListaTarea.h>
# include <NodoMatriz.h>
#include<regex>
using namespace std;
int menuprincipal();
int ingresomanual();
int menuUsuario();
int menuTarea();
int menuReporte();
int rutae();
int getIndiceMes(string);
int getIndiceHora(string);
string obtenerListaGraphviz();
ClaseCola *ClaseC = new ClaseCola();
ListaU *estudiantes = new ListaU();
ListaTarea *tareas = new ListaTarea();
void cargarArchivo();
void cargarTarea();
void ReporteUsuarios();
void ReporteErrores();
void ReporteTareas();
void AgregarUsuario(string,string,string,string,string,string,string,string);
void AgregarTarea(string,string,string,string,string,string,string,int);
int main()
{
    try{
    int opmenu=0;
    string ruta;
    do{ // Menu Principal
        opmenu=menuprincipal();
        switch (opmenu){
                case 1:{ // Carga de Estudiantes
                    cargarArchivo();
                    }break;
                case 2:{// Carga de Tareas
                    cargarTarea();
                }break;
                case 3: // Ingreso Manual de Usuarios o Tareas
                    {   int opmanual =0;
                        do  {
                            opmanual = ingresomanual();
                            switch (opmanual){
                        case 1: // Ingreso manual de estudiantes
                            {
                                int opU =0;
                                do  {
                                    opU = menuUsuario();
                                    switch (opU){
                                    case 1: // Agregar Usuario
                                    {
                                        string nombre,carrera,correo,pass,carnet,dpi,creditos,edad;
                                        cout<<" *  Ingrese el numero de Carnet *\n"<<endl;
                                        cin.ignore();
                                        getline(cin,carnet);
                                        cout<<" *  Ingrese el numero de DPI *\n"<<endl;
                                        getline(cin,dpi);
                                        cout<<" *  Ingrese el Nombre        *\n"<<endl;
                                        getline(cin,nombre);
                                        cout<<" *  Ingrese la Carrera       *\n"<<endl;
                                        getline(cin,carrera);
                                        cout<<" *  Ingrese el Correo        *\n"<<endl;
                                        getline(cin,correo);
                                        cout<<" *  Ingrese la Password      *\n"<<endl;
                                        getline(cin,pass);
                                        cout<<" *  Ingrese el numero de Creditos *\n"<<endl;
                                        getline(cin,creditos);
                                        cout<<" *  Ingrese la edad              *\n"<<endl;
                                        getline(cin,edad);
                                        AgregarUsuario(carnet,dpi,nombre,carrera,correo,pass,creditos,edad);
                                    }
                                    break;
                                    case 2:// Modificar Usuario
                                        {
                                        string dpi;
                                        cin.ignore();
                                        cout<<" *  Ingrese el numero de DPI del usuario a modificar *\n"<<endl;
                                        getline(cin,dpi);

                                        estudiantes->ModificarNodo(dpi);

                                        }

                                    break;
                                    case 3:// Eliminar Usuario
                                       {
                                        string dpie;
                                        string oper;
                                        int op;
                                        cout<<" *  Ingrese el numero de DPI del estudiante a eliminar *\n"<<endl;
                                        cin.ignore();
                                        getline(cin,dpie);
                                        cout<<" *  Esta seguro de eliminar el estudiante? *\n"<<endl;
                                        cout<<" *  Ingrese la opcion: *"<<endl;
                                        cout<<" *  1.- Si      2.- No *"<<endl;
                                        //cin.ignore();
                                        cin>>op;
                                        //getline(cin,oper);
                                       // istringstream(oper)>>op;
                                        if (op == 1){
                                           estudiantes->deleteValue(dpie);
                                           cout<<" * Estudiante Eliminado *\n"<<endl;
                                        }else {
                                        cout<<" * El estudiante no fue eliminado *\n"<<endl;
                                        }
                                       }
                                    break;
                                    default:
                                    cout<<" *  Datos mal ingresados *\n"<<endl;
                                    };
                                    }
                                while (opU != 4);
                            }
                            break;
                        case 2:// Ingreso manual de Tareas
                            {
                                int opT =0;
                                do  {
                                    opT = menuTarea();
                                    switch (opT){
                                    case 1: // Agregar Tarea
                                    {   int diax,mesx,horax;

                                        int index;
                                        cout<<" *  Ingrese el Mes de la Tarea *\n"<<endl;
                                        cin>>mesx;
                                        cout<<" *  Ingrese el Dia de la tarea *\n"<<endl;
                                        cin>>diax;
                                        cout<<" *  Ingrese la hora de la tarea *\n"<<endl;
                                        cin>>horax;
                                        int mes1=getIndiceMes(to_string(mesx));
                                        int hora1= getIndiceHora(to_string(horax));
                                        int dia1 = diax-1;
                                        index = hora1+9*((dia1)+30*(mes1));

                                        string carnet, descrip,nombre,materia,fecha,hora,estado;
                                        cin.ignore();
                                        cout<<" *  Ingrese el numero de Carnet *\n"<<endl;
                                        getline(cin,carnet);
                                        cout<<" *  Ingrese el nombre de la tarea *\n"<<endl;
                                        getline(cin,nombre);
                                        cout<<" *  Ingrese la descripcion *\n"<<endl;
                                        getline(cin,descrip);
                                        cout<<" *  Ingrese la Materia *\n"<<endl;
                                        getline(cin,materia);
                                        cout<<" *  Ingrese la Fecha en formato dd/mm/aaaa*\n"<<endl;
                                        getline(cin,fecha);
                                        cout<<" *  Ingrese la Hora *\n"<<endl;
                                        getline(cin,hora);
                                        cout<<" *  Ingrese el estado de la tarea *\n"<<endl;
                                        getline(cin,estado);

                                        if (estudiantes->buscarUsuarioCarnet(carnet)==true){
                                        cout << "\n El carnet es valido" << endl;
                                        if (tareas->ValorOcupado()==false){
                                            tareas->ModificarNodo(carnet,nombre,descrip,materia,fecha,hora,estado,index);
                                        }else{
                                        cout << "\n Ya existe una tarea en la posicion indicada" << endl;
                                        }

                                        }else{
                                        cout << "\n No se encontro estudiante con el numero  de carnet" << endl;
                                        ClaseC->insertList(" No hay estudiante con el # de carnet: "+carnet+"\n Ref. Index: "+to_string(index), "Tarea",2,1);
                                            }
                                    }break;
                                    case 2:// Modificar Tarea
                                        {
                                        int index;
                                        cout<<" *  Ingrese el ID de la tarea a Modificar *\n"<<endl;
                                        cin>>index;

                                        string carnet, descrip,nombre,materia,fecha,hora,estado;
                                        cin.ignore();
                                        cout<<" *  Ingrese el numero de Carnet *\n"<<endl;
                                        getline(cin,carnet);
                                        cout<<" *  Ingrese el nombre de la tarea *\n"<<endl;
                                        getline(cin,nombre);
                                        cout<<" *  Ingrese la descripcion *\n"<<endl;
                                        getline(cin,descrip);
                                        cout<<" *  Ingrese la Materia *\n"<<endl;
                                        getline(cin,materia);
                                        cout<<" *  Ingrese la Fecha en formato dd/mm/aaaa*\n"<<endl;
                                        getline(cin,fecha);
                                        cout<<" *  Ingrese la Hora *\n"<<endl;
                                        getline(cin,hora);
                                        cout<<" *  Ingrese el estado de la tarea *\n"<<endl;
                                        getline(cin,estado);

                                        if (estudiantes->buscarUsuarioCarnet(carnet)==true){
                                        cout << "\n El carnet es valido" << endl;
                                        tareas->ModificarNodo(carnet,nombre,descrip,materia,fecha,hora,estado,index);
                                        }else{
                                        cout << "\n No se encontro estudiante con el numero  de carnet" << endl;
                                        //ClaseC->insertList(" No hay estudiante con el # de carnet: "+carnet+"\n Ref. Index: "+to_string(index), "Tarea",2,1);
                                        }



                                        }

                                    break;
                                    case 3:// Eliminar Tarea
                                        {
                                        int index;
                                        int op;
                                        cout<<" *  Ingrese el ID de la tarea a eliminar *\n"<<endl;
                                        cin>>index;
                                        cout<<" *  Esta seguro de eliminar la tarea?: "+to_string(index)+" *\n"<<endl;
                                        cout<<" *  Ingrese la opcion: *"<<endl;
                                        cout<<" *  1.- Si      2.- No *"<<endl;
                                        //cin.ignore();
                                        cin>>op;
                                        //getline(cin,oper);
                                       // istringstream(oper)>>op;
                                        if (op == 1){
                                           tareas->deleteValue(index);
                                           cout<<" * Tarea Eliminada *\n"<<endl;
                                        }else {
                                        cout<<" * LA tarea no fue eliminada *\n"<<endl;
                                        }
                                       }

                                    break;
                                    case 4:// Regresar

                                    break;
                                    default:
                                    cout<<" *  Datos mal ingresados *\n"<<endl;
                                    };
                                    }
                                while (opT != 4);
                            }
                            case 3: // correccion de errores
                            {   string datomalo, datonuevo,dpie;
                                int index;
                                if (ClaseC->isEmpty()==false){
                                        if (ClaseC->ErrorUsuario()==true){
                                            cin.ignore();
                                            cout<<" *  Ingrese el numero de DPI del estudiante que contiene error *\n"<<endl;
                                            getline(cin,dpie);

                                            if (ClaseC->TipoError()==11){

                                            cout<<" *  Primer error Estudiante, carnet*\n"<<endl;
                                            cout<<" *  Ingrese el # de carnet correcto, (9 digitos) *\n"<<endl;
                                            getline(cin,datonuevo);
                                            estudiantes->ModificarDato(datonuevo,11,dpie);
                                            ClaseC->Desencolar();
                                            }else if (ClaseC->TipoError()==12){
                                            cout<<" *  Primer error Estudiante, dpi*\n"<<endl;
                                            cout<<" *  Ingrese el # de DPI correcto, (13 digitos) *\n"<<endl;
                                            getline(cin,datonuevo);
                                            estudiantes->ModificarDato(datonuevo,12,dpie);
                                            ClaseC->Desencolar();
                                            }else if (ClaseC->TipoError()==13){
                                            cout<<" *  Primer error Estudiante, correo*\n"<<endl;
                                            cout<<" *  Ingrese un email correcto, (user@dominio.(com|es|org) *\n"<<endl;
                                            getline(cin,datonuevo);
                                            estudiantes->ModificarDato(datonuevo,13,dpie);
                                            ClaseC->Desencolar();
                                            }else if (ClaseC->TipoError()==14){
                                            cout<<" *  Primer error Estudiante, Duplicado*\n"<<endl;
                                            ClaseC->Desencolar();
                                        }
                                        }else if (ClaseC->ErrorTarea2()==true){
                                            //
                                            cout<<" *  Ingrese el index de la tarea que contiene error *\n"<<endl;
                                            cin>>index;
                                            if (ClaseC->TipoError()==21){

                                            cout<<" *  Primer error Tarea, carnet*\n"<<endl;
                                            cin.ignore();
                                            cout<<" *  Ingrese el # de carnet correcto, (9 digitos) para la tarea*\n"<<endl;
                                            getline(cin,datonuevo);
                                            ClaseC->Desencolar();
                                            }else if (ClaseC->TipoError()==22){
                                            cout<<" *  Primer error Tarea, Fecha*\n"<<endl;
                                            cout<<" *  Ingrese fecha valida dd/mm/aaaa para la tarea*\n"<<endl;
                                            getline(cin,datonuevo);
                                            ClaseC->Desencolar();
                                            }

                                        }else if (ClaseC->TipoError()==3){
                                            cout<<" *  Primer error Fuera de rango*\n"<<endl;
                                            ClaseC->Desencolar();
                                        }else{
                                        cout<<" *  Primer error Datos erroneos*\n"<<endl;
                                        ClaseC->Desencolar();
                                        }


                                }else{
                                    cout<<" *  Lista de Errores Vacia *\n"<<endl;
                                }

                                /*int cont=1;
                                if (ClaseC->isEmpty()==false){
                                    // error de tipo estudiante
                                    NodoCola *aux = new NodoCola;

                                    if (ClaseC->ErrorUsuario()==true){
                                        string dpi;
                                        cin.ignore();
                                        cout<<" *  Ingrese el numero de DPI del usuario con error para modificar *\n"<<endl;
                                        getline(cin,dpi);

                                        estudiantes->ModificarNodo(dpi);
                                        ClaseC->Desencolar();
                                    }else if (ClaseC->ErrorTarea2()==true){

                                        cout<<" *  Error en la tarea *\n"<<endl;
                                        int index;
                                        cout<<" *  Ingrese el ID de la tarea a Modificar *\n"<<endl;
                                        cin>>index;

                                        string carnet, descrip,nombre,materia,fecha,hora,estado;
                                        cin.ignore();
                                        cout<<" *  Ingrese el numero de Carnet *\n"<<endl;
                                        getline(cin,carnet);
                                        cout<<" *  Ingrese el nombre de la tarea *\n"<<endl;
                                        getline(cin,nombre);
                                        cout<<" *  Ingrese la descripcion *\n"<<endl;
                                        getline(cin,descrip);
                                        cout<<" *  Ingrese la Materia *\n"<<endl;
                                        getline(cin,materia);
                                        cout<<" *  Ingrese la Fecha en formato dd/mm/aaaa*\n"<<endl;
                                        getline(cin,fecha);
                                        cout<<" *  Ingrese la Hora *\n"<<endl;
                                        getline(cin,hora);
                                        cout<<" *  Ingrese el estado de la tarea *\n"<<endl;
                                        getline(cin,estado);


                                        tareas->ModificarNodo(carnet,nombre,descrip,materia,fecha,hora,estado,index);

                                        ClaseC->Desencolar();

                                    }else if(ClaseC->ErrorTarea3()==true){
                                        cout<<" *  Error de rango *\n"<<endl;
                                        ClaseC->Desencolar();
                                    }

                                }else{
                                    cout<<" *  Lista de Errores Vacia *\n"<<endl;
                                }*/
                            }
                            break;
                            case 4:
                            break;

                        default:
                        cout<<" *  Datos mal ingresados *\n"<<endl;
                        };
                        }
                        while (opmanual != 4);
                            }
                        break;

                case 4 : // Apartado para Reportes
                    {
                        int opR =0;
                        do  {
                        opR = menuReporte();
                        switch (opR){
                            case 1: // Reporte de Usuarios
                                {
                                ReporteUsuarios();
                                }
                            break;
                            case 2:// Reporte Tareas
                                {
                                ReporteTareas();
                                }
                            break;
                            case 3: // Busqueda de tarea
                                {   string mes, hora;
                                    int dia;
                                    cin.ignore();
                                    cout<<"\N ********  BUSQUEDA DE TAREA ******** *\n"<<endl;
                                    cout<<" *  Ingrese el Mes *\n"<<endl;
                                    getline(cin,mes);
                                    cout<<" *  Ingrese el Dia *\n"<<endl;
                                    cin>>dia;
                                    cin.ignore();
                                    cout<<" *  Ingrese la Hora *\n"<<endl;
                                    getline(cin,hora);
                                    tareas->BuscarTarea(getIndiceMes(mes),dia,getIndiceHora(hora));

                                }
                            break;
                            case 4:// Busqueda de posicion
                                   {
                                    string mes, hora,dia;
                                    //int ;
                                    cin.ignore();
                                    cout<<" ********  CALCULO DE POSICION *********\n"<<endl;
                                    cout<<" *  Ingrese el Mes *\n"<<endl;
                                    getline(cin,mes);
                                    cout<<" *  Ingrese el Dia *\n"<<endl;
                                    getline(cin,dia);
                                    cout<<" *  Ingrese la Hora *\n"<<endl;
                                    getline(cin,hora);
                                    //int posicion=0;
                                    int mes1=getIndiceMes(mes);
                                    int hora1= getIndiceHora(hora);
                                    int dia1;
                                    istringstream(dia)>>dia1;
                                    int pos = hora1+9*((dia1-1)+30*(mes1));
                                    cout<<"\n ********  La tarea se encuentra en la posicion: ********* "<<pos<<endl;
                                    //(i+5*(j+30*k))

                                   }

                            break;
                            case 5:// Reporte Errores
                                {
                                ReporteErrores();
                                }
                            break;
                            case 6:// Reporte txt
                            {
                                estudiantes->generatxt();
                                tareas->generatxt();
                            }

                            break;
                            case 7:
                            break;
                            default:
                                    cout<<" *  Datos mal ingresados *\n"<<endl;

                            }}while (opR != 7);
                    }
                case 5:
                break;
                default:
                    cout<<" *  Datos mal ingresados *\n"<<endl;
    }; }

    while(opmenu!=5);

    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    return 0;
}

int menuprincipal(){
        cout<<"\n ";
        cout<<"**************MENU*************"<<endl;
        cout<<" *  1.-  Carga de Estudiantes  *"<<endl;
        cout<<" *  2.-  Carga de Tareas       *"<<endl ;
        cout<<" *  3.-  Ingreso Manual        *"<<endl;
        cout<<" *  4.-  Reportes              *"<<endl;
        cout<<" *  5.-  Salir                 *"<<endl;
        cout<<" *******************************\n"<<endl;
        cout<<endl;
        cout<<" * Ingrese el Numero de Opcion: *   "<<endl;
        int opmenu;
        cin >> opmenu ;
        return opmenu;
}
int ingresomanual(){
        cout<<"\n ";
        cout<<" ********INGRESO MANUAL********"<<endl;
        cout<<" *  1.-  Estudiantes          *"<<endl;
        cout<<" *  2.-  Tareas               *"<<endl ;
        cout<<" *  3.-  Corregir Error       *"<<endl;
        cout<<" *  4.-  Regresar             *"<<endl;
        cout<<" ******************************\n"<<endl;
        cout<<endl;
        cout<<" * Ingrese el Numero de Opcion:  *  "<<endl;
        int opmanual;
        cin >> opmanual;
        return opmanual;

}
int menuReporte(){
        cout<<"\n ";
        cout<<" **************REPORTES***************"<<endl;
        cout<<" *  1.-  Lista de Estudiantes         *"<<endl;
        cout<<" *  2.-  Lista de Tareas              *"<<endl ;
        cout<<" *  3.-  Busqueda de Tarea            *"<<endl;
        cout<<" *  4.-  Busqueda de posicion         *"<<endl;
        cout<<" *  5.-  Cola de Errores              *"<<endl;
        cout<<" *  6.-  Codigo de Salida             *"<<endl;
        cout<<" *  7.-  Regresar                     *"<<endl;
        cout<<" **************************************\n"<<endl;
        cout<<endl;
        cout<<" * Ingrese el Numero de Opcion:  *  "<<endl;
        int opmanual;
        cin >> opmanual;
        return opmanual;

}
int menuUsuario(){
        cout<<"\n ";
        cout<<" ********INGRESO MANUAL********"<<endl;
        cout<<" *  1.-  Agregar Usuario      *"<<endl;
        cout<<" *  2.-  Modificar Usuario    *"<<endl ;
        cout<<" *  3.-  Eliminar Usuario     *"<<endl;
        cout<<" *  4.-  Regresar             *"<<endl;
        cout<<" ******************************\n"<<endl;
        cout<<endl;
        cout<<" * Ingrese el Numero de Opcion:  *  "<<endl;
        int opmanual;
        cin >> opmanual;
        return opmanual;

}
int menuTarea(){
        cout<<"\n ";
        cout<<" ********INGRESO MANUAL********"<<endl;
        cout<<" *  1.-  Agregar Tarea        *"<<endl;
        cout<<" *  2.-  Modificar Tarea      *"<<endl ;
        cout<<" *  3.-  Eliminar Tarea       *"<<endl;
        cout<<" *  4.-  Regresar             *"<<endl;
        cout<<" ******************************\n"<<endl;
        cout<<endl;
        cout<<" * Ingrese el Numero de Opcion:  *  "<<endl;
        int opmanual;
        cin >> opmanual;
        return opmanual;

}
int rutae(){
        cout<<"\n ";
        cout<<" ********RUTA DE ESTUDIANTES********"<<endl;
        cout<<" *  1.-  Estudiantes          *"<<endl;
        cout<<" *  2.-  Tareas               *"<<endl ;
        cout<<" *  3.-  Regresar             *"<<endl;
        cout<<" ******************************\n"<<endl;
        cout<<endl;
        cout<<" * Ingrese el Numero de Opcion:  *  "<<endl;
        int opmanual;
        cin >> opmanual;
        return opmanual;

}
void cargarArchivo(){

         string ruta;
         ifstream archivo;
         cout << "Ingrese la ruta del archivo de estudiantes\n";
         //Concatenar string para la ruta completa
         cin.ignore();
         getline(cin, ruta);
         cout<<" ruta copiada:  "<<ruta<<"\n"<<endl;
         archivo.open(ruta,ios::in);
         string linea;
         char delimitador = ',';
        // Leemos la primer línea para descartarla, pues es el encabezado
        getline(archivo, linea);
        // Leemos todas las líneas
        if (!archivo.fail()){
        while (getline(archivo, linea))
        {

        stringstream stream(linea); // Convertir la cadena a un stream
        string  nombre, carrera, correo, pass,carnet, dpi,creditos,edad;


        // Extraer todos los valores de esa fila
        getline(stream, carnet, delimitador);
        getline(stream, dpi, delimitador);
        getline(stream, nombre, delimitador);
        getline(stream, carrera, delimitador);
        getline(stream, pass, delimitador);
        getline(stream, creditos, delimitador);
        getline(stream, edad, delimitador);
        getline(stream, correo, delimitador);
        // insertando a la lista doble
        AgregarUsuario(carnet,dpi,nombre,carrera,correo,pass,creditos,edad);
        }


        }else {
        cout << " La ruta del archivo es incorrecta: " << endl;
        }
        archivo.close();



}
void ReporteUsuarios(){
        estudiantes->generaDot();
        //cout << "\n ************ LISTA DE ESTUDIANTES INGRESADOS ************ " << endl;
        //estudiantes->getList();
        cout << "\n ************ GENERANDO GRAFICO... ************ " << endl;
        //estudiantes->getListReverse();


}
void ReporteTareas(){
        tareas->generaTarea1();
        //cout << "\n ************ LISTA DE ESTUDIANTES INGRESADOS ************ " << endl;
        //estudiantes->getList();
        //cout << "\n ************ GENERANDO GRAFICO... ************ " << endl;
        //estudiantes->getListReverse();


}
void ReporteErrores(){
        cout << "\n ****** LISTA DE ERRORES ****** " << endl;
        ClaseC->generaError();
       // ClaseC->getList();
}
void AgregarUsuario(string carnet, string dpi, string nombre, string carrera,string correo, string pass, string creditos,string edad){

        if (estudiantes->validarCarnet(carnet) == false){
            ClaseC->insertList(" El Carnet "+carnet+" es invalido,\n Ref. DPI: "+dpi, "Estudiante",1,1);
        }

        if(estudiantes->validarDpi(dpi) == false){
            ClaseC->insertList(" El DPI "+dpi+" es invalido", "Estudiante",1,2);
        }

        if(estudiantes->validarCorreo(correo) == false){
            ClaseC->insertList(" El correo "+correo+" es invalido,\n Ref. DPI: "+dpi, "Estudiante",1,3);
        }

        if (estudiantes->buscarUsuarioCarnet(carnet)==false){
           if (estudiantes->buscarUsuarioDPI(dpi)==false){
           // cout << "\n El estudiante fue encontrado, tarea asignada" << endl;
            estudiantes->insertList(carnet,dpi,nombre,carrera,correo,pass,creditos,edad);
        }else{
            cout << "\n El estudiante con numero de DPI: "+dpi+" ya existe" << endl;
            ClaseC->insertList(" El DPI:  "+dpi+" ya esta registrado", "Estudiante",1,4);
        }
        }else{
            cout << "\n El estudiante con numero de Carnet: "+carnet+" ya existe" << endl;
            ClaseC->insertList(" El Carnet:  "+carnet+" ya esta registrado\n Ref. DPI:"+dpi, "Estudiante",1,4);
        }




}
void cargarTarea(){

    //Variables para extracción de infomación
    string path = "";
    string data = "";
    string item = "";

    //Matriz con el nodo MatrixNode
    NodoMatriz *matrix[5][30][9];

    //Inicializacion de la matriz
    for(int i=0;i<5;i++){
        for(int j=0; j<30; j++){
           for(int k=0; k<9; k++){
            matrix[i][j][k] = NULL;
        }
        }
    }
    //Lectura del archivo
    ifstream archivo;
    cin.ignore();
    cout<<"Ingrese direccion del archivo de Tareas a leer: "<<endl;
    getline(cin, path);

    archivo.open(path, ios::in);
        string linea;
        char delimitador = ',';
        // Leemos la primer línea para descartarla, pues es el encabezado
        getline(archivo, linea);
        // Leemos todas las líneas
    if(!archivo.fail()){
            while (getline(archivo, linea))
        {

        stringstream stream(linea); // Convertir la cadena a un stream
        string  mes, dia1, hora,carnet,nombre,descrip,materia,fecha,estado;


        // Extraer todos los valores de esa fila
        getline(stream, mes, delimitador);
        getline(stream, dia1, delimitador);
        getline(stream, hora, delimitador);
        getline(stream, carnet, delimitador);
        getline(stream, nombre, delimitador);
        getline(stream, descrip, delimitador);
        getline(stream, materia, delimitador);
        getline(stream, fecha, delimitador);
        getline(stream, estado, delimitador);
        int dia;
        istringstream(dia1)>>dia;

        if (getIndiceMes(mes)!= -1){
                    if (dia>0 && dia<=30){
                            if (getIndiceHora(hora)!= -1){
                                    matrix[getIndiceMes(mes)][dia-1][getIndiceHora(hora)] = new NodoMatriz(carnet,nombre,descrip,materia,fecha,hora,estado);
                                    //counter = 0;
                            }else{
                                cout<<"hora "+hora+" fuera de rango: "<<endl;
                                ClaseC->insertList("Hora "+hora+" fuera de rango","Tarea",3,0);
                            }

                    }else{
                       cout<<"Dia "+ to_string(dia) +" fuera de rango: "<<endl;
                       ClaseC->insertList("Dia "+ to_string(dia) +" fuera de rango","Tarea",3,0);

            }}else{
            cout<<"Mes "+mes+" fuera de rango: "<<endl;
            ClaseC->insertList("Mes "+mes+" fuera de rango","Tarea",3,0);
            }


        }

    }
    archivo.close();

    //Recorrido de la matriz
    for(int i=0; i<5; i++){
        for(int j=0; j<30; j++){
            for(int k=0; k<9; k++){
            if(matrix[i][j][k]!=NULL){
               // cout<<matrix[i][j][k]->getnombre()<<endl;
            }
        }
        }
    }
    // rellenando la matriz
    for(int i=0; i<5; i++){
        for(int j=0; j<30; j++){
            for(int k=0; k<9; k++){
            if(matrix[i][j][k]!=NULL){
                // insertar los datos del nodo matriz a la lista de tareas
               //tareas->insertList(matrix[i][j][k]->getcarnet(),matrix[i][j][k]->getnombre(), matrix[i][j][k]->getdescrip(),matrix[i][j][k]->getmateria(),matrix[i][j][k]->getfecha(),matrix[i][j][k]->getestado(), (i+5*(j+30*k)));hora1+9*((dia1-1)+30*(mes1));
                AgregarTarea(matrix[i][j][k]->getcarnet(),matrix[i][j][k]->getnombre(), matrix[i][j][k]->getdescrip(),matrix[i][j][k]->getmateria(),matrix[i][j][k]->getfecha(),matrix[i][j][k]->gethora(),matrix[i][j][k]->getestado(), (k+9*(j+30*i)));

            }
            else {
               //insertar valores nulos a la matriz
               //hora1+9*((dia1-1)+30*(mes1));
            tareas->insertList("-1","-1", "-1","-1","-1","-1","-1", (k+9*(j+30*i)));
            }
        }}
    }



}
int getIndiceMes(string mes){
    int mes1;
    istringstream(mes)>>mes1;
    switch(mes1){
        case 7:
            return 0;
        break;
        case 8:
            return 1;
        break;
        case 9:
            return 2;
        break;
        case 10:
            return 3;
        break;
        case 11:
            return 4;
        break;
        default:
            return -1;
    }
}
int getIndiceHora(string hora){
    int hora1;
    istringstream(hora)>>hora1;
    switch(hora1){
        case 8:
            return 0;
        break;
        case 9:
            return 1;
        break;
        case 10:
            return 2;
        break;
        case 11:
            return 3;
        break;
        case 12:
            return 4;
        break;
        case 13:
            return 5;
        break;
        case 14:
            return 6;
        break;
        case 15:
            return 7;
        break;
        case 16:
            return 8;
        break;
        default:
            return -1;
    }
}
void AgregarTarea(string carnet, string nombre, string descrip, string materia,string fecha,string hora, string estado, int index){
            string dia, mes, a, nuevaFecha, fe;
            if (tareas->validarFecha(fecha)==true){
            string fechaF[3] = {"","",""};
            string dato = "";
            int contador =0;
            for (int i=0;i<fecha.length(); i++){
                if (fecha[i]!= '/'){
                    dato+=fecha[i];
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
            //cout << "\n Nueva Fecha: "+fe<< endl;

            }else{
                ClaseC->insertList(" La fecha: "+fecha+" No tiene el formato valido,\n Ref. Index:"+to_string(index), "Tarea",2,2);
            }


            if (estudiantes->buscarUsuarioCarnet(carnet)==true){
                    cout << "\n El estudiante fue encontrado, tarea asignada" << endl;
                    tareas->insertList(carnet,nombre,descrip,materia,fecha,hora,estado,index);
                   /* if (tareas->validarFecha(fecha)==true){
                    tareas->insertList(carnet,nombre,descrip,materia,fe,hora,estado,index);}
                    else{

                    }*/
            }else{
            cout << "\n No se encontro estudiante con el numero  de carnet" << endl;
            ClaseC->insertList(" No hay estudiante con el # de carnet: "+carnet+"\n Ref. Index: "+to_string(index), "Tarea",2,1);
            tareas->insertList(carnet,nombre,descrip,materia,fecha,hora,estado,index);
                    /*if (tareas->validarFecha(fecha)==true){
                    tareas->insertList(carnet,nombre,descrip,materia,fe,hora,estado,index);}
                    else{
                    tareas->insertList(carnet,nombre,descrip,materia,fecha,hora,estado,index);
                    }*/
            }


}

