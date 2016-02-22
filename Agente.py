#@autor: Camilo Barbosa

import os
import libs.fts_menu as ftsm
import random, string
import libs.funs_agente as fag

#to linux "clear" to windows "cls"
ftsm._CLEAR_="clear"


def clear():
    os.system(ftsm._CLEAR_)


        

a=[0,0]
m=ftsm.fts_menu()

m.addMenu("Menu principal","Determine:",[["Destinos","Entrar Destinos"],["Salir"]])
m.addMenu("Entrar Destinos","Los datos van a ser modificados desde cero, que desea hacer:",[["Continuar","Menu principal"],["Atras","Menu principal"]])

numeroDeDestinos=0
destinos=[]
numeroDeVariables=0
variablesDeDestinos=[]

while(a!=m.fanselected("Menu principal","Salir")):
    a=m.run()

    if(a==m.fanselected("Entrar Destinos","Continuar")):
        clear()
        numeroDeDestinos=0
        destinos=[]
        numeroDeVariables=0
        variablesDeDestinos=[]
        
        numeroDeDestinos=int(input("Ingrese el numero de destinos a ingresar: "))
        numeroDeVariables=int(input("Ingrese el numero de variables a evaluar: "))
        namesvar=[]
        j=0
        while(j<numeroDeVariables):
            namev=["","",""]
            clear()
            print "Formato de variables para cada destino: "
            print " "
            namev[0]=raw_input("Nombre de la variable "+str(j+1)+": ")
                     
            op=[["string"],["float"],["int"]]
            namev[1]=ftsm.validator("Tipo de dato de variable","Determine el tipo de dato para la variable "+namev[0]+": ",op)
            namev[2]=raw_input("Unidades de la variable "+str(j+1)+": ")           
            namesvar.append(namev)            
            j+=1
       
        if(numeroDeDestinos>0):
            i=0
            while(i<numeroDeDestinos):
                clear()
                destino={}
                destino["nombre"]=raw_input("Entre el nombre del destino "+str(i+1)+": ")
                destino["vars"]=[]                
                j=0
                while(j<numeroDeVariables):
                    var={}                    
                    var["nombre"]=namesvar[j][0]
                    var["tipo"]=namesvar[j][1]
                    var["Unidades"]=namesvar[j][2]
                    if(namesvar[j][1]=="string"):
                        var["data"]=raw_input("Entre el dato cadena en "+namesvar[j][2]+" de "+namesvar[j][0]+": ")
                    elif(namesvar[j][1]=="float"):
                        var["data"]=float(input("Entre el dato real "+namesvar[j][2]+" de "+namesvar[j][0]+": "))
                    elif(namesvar[j][1]=="int"):
                        var["data"]=int(input("Entre el dato entero "+namesvar[j][2]+" de "+namesvar[j][0]+": "))
                    destino["vars"].append(var)
                    j+=1

                destinos.append(destino)
                i+=1
        m.addMenu("Menu principal","Determine:",[["Destinos","Entrar Destinos"],["Agente"],["Mostrar Destinos"],["Salir"]])
    if(a==m.fanselected("Menu principal","Mostrar Destinos")):
        clear()
        op=[]
        for destino in destinos:
            op.append([destino["nombre"]])
        op.append(["Atras"])
        k=ftsm.fts_menu()
        k.addMenu("Destinos","Seleccione un destino: ",op)
        r=[-1,-1]
        while(r!=k.fanselected("Destinos","Atras")):
            r=k.run()
            if(r[1]>-1 and r[1]<len(op)):
                clear()
                print "Nombre de destino: ", destinos[r[1]-1]["nombre"]
                for var in  destinos[r[1]-1]["vars"]:
                    print "Nombre de variable: ", var["nombre"]
                    print "Tipo: ", var["tipo"]
                    print "Unidades: ", var["Unidades"]
                    print "Informacion: ",var["data"]
                    print "***"
                raw_input("presiona una tecla para continuar...")
    if(a==m.fanselected("Menu principal","Agente")):
        random.shuffle(destinos)        
        results=fag.agente_finish(fag.agente_distance(destinos,fag.agente_protocolo(destinos)))
        fag.agente_optimus(results,destinos)


        
        
