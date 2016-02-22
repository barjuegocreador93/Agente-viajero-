
import point3D as r3
import fts_menu as ftsm

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