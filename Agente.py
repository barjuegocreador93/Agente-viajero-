#@autor: Camilo Barbosa
import os
import libs.fts_menu as ftsm
import libs.point3D as r3
import random, string

#to linux "clear" to windows "cls"
ftsm._CLEAR_="clear"


def clear():
    os.system(ftsm._CLEAR_)


def agente_protocolo(destinos):
    print "Parametros a buscar: "
    protocolo=[]
    for var in destinos[0]["vars"]:
        data=[]
        data.append(var["nombre"])
        data.append(var["tipo"])
        data.append(var["Unidades"])
        var["optimo"]=""
        if(var["tipo"]=="string"):
            var["optimo"]=[raw_input("Entre el dato cadena en optimo(s[,]) "+data[2]+" de "+data[0]+": ").split(",")]
        elif(var["tipo"]=="float"):
            var["optimo"]=float(input("Entre el dato real optimo "+data[2]+" de "+data[0]+": "))
        elif(var["tipo"]=="int"):
            var["optimo"]=int(input("Entre el dato entero optimo "+data[2]+" de "+data[0]+": "))
        data.append(var["optimo"])
        protocolo.append(data)
    return protocolo


def agente_distance(destinos,protocolo):
    resultados=[]
    for des in destinos:
        i=0
        destino_resul={}
        destino_resul["nombre"]=des["nombre"]
        destino_resul["vars"]=[]
        for var in des["vars"]:
            resul={}
            resul["nombre_del_destino"]=des["nombre"]
            resul["nombre"]=(var["nombre"])
            resul["tipo"]=(var["tipo"])
            if(var["tipo"]=="float" or var["tipo"]=="int"):
                p=r3.Line3D(r3.Point3D(var["data"]),r3.Point3D(protocolo[i][3]))
                d=p.Distans()
                resul["result"]=(d)
                print d
                raw_input("presiona una tecla para continuar...")
            if(var["tipo"]=="string"):
                resul["result"]=[]
                for data in protocolo[i]["optimo"]:
                    if(var["data"]==data):
                        resul["result"].apped(data)

            destino_resul["vars"].append(resul)    
            i+=1
        resultados.append(destino_resul)
    return resultados

def agente_finish(resultados):
    destinosOptimosPorVariable=[]
    for var in resultados[0]["vars"]:        
        destinosOptimosPorVariable.append(var)    
    
    for res in resultados:
        i=0
        for var in res["vars"]:
            if(var["tipo"]=="float" or var["tipo"]=="int"):
                if(var["result"]<destinosOptimosPorVariable[i]["result"]):                     
                     print var["nombre_del_destino"]
                     raw_input("presiona una tecla para continuar...")
                     destinosOptimosPorVariable[i]=var
            i+=1

    return destinosOptimosPorVariable

def buscar_destino(destino_nombre, destinos):
    for des in destinos:
        if(des["nombre"]==destino_nombre):
            return des
    return []
def agente_optimus(destinosOptimosPorVariable, destinos):
    lista=[]
    for var in destinosOptimosPorVariable:
        lista.append([var["nombre"]])
    lista.append(["Atras"])
    a=[-1,-1]
    m=ftsm.fts_menu()
    m.addMenu("Resultados Optimos por variables","Seleccione para mirar: ",lista)
    while(a!=m.fanselected("Resultados Optimos por variables","Atras")):
        a=m.run()
        if(a!=[-1,-1] and a!=m.fanselected("Resultados Optimos por variables","Atras")):
            des=buscar_destino(destinosOptimosPorVariable[a[1]-1]["nombre_del_destino"],destinos)
            print "Nombre del destino: ",des["nombre"]
            for var in des["vars"]:
                print "nombre de variable: ",var["nombre"]
                print "tipo de variable: ",var["tipo"]
                print "Unidades de variable: ",var["Unidades"]
                print "Informacion: ",var["data"]
            print "timing: ",destinosOptimosPorVariable[a[1]-1]["result"]
            raw_input("presiona una tecla para continuar...")




        

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
        results=agente_finish(agente_distance(destinos,agente_protocolo(destinos)))
        agente_optimus(results,destinos)


        
