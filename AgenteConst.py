
import os
import libs.funs_agente as fag
import random, string


destinos=[
{
	"nombre":"a","vars":[
	{
		"nombre":"Temperatura","tipo":"float","Unidades":"c","data":25.0
	}
	]
},
{
	"nombre":"b","vars":[
	{
		"nombre":"Temperatura","tipo":"float","Unidades":"c","data":32.0
	}
	]
},
{
	"nombre":"c","vars":[
	{
		"nombre":"Temperatura","tipo":"float","Unidades":"c","data":10.2
	}
	]
}
]


protocolo=[["Temperatura","float","c",0.0]]

random.shuffle(destinos) 
fag.agente_optimus(fag.agente_finish(fag.agente_distance(destinos,protocolo)),destinos)