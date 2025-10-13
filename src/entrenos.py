import csv
from collections import namedtuple
from datetime import datetime


Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
 



def lee_entrenos(ruta_csv):
    with open (ruta_csv, encoding = "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        lista_entrenos = []
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M" ).date()
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            if compartido == "S":
                compartido = True
            else: 
                compartido = False
            
            tupla=  Entreno(tipo, fechahora, ubicacion,duracion, calorias, distancia, frecuencia, compartido)
            lista_entrenos.append(tupla)

    return lista_entrenos


def tipo_entreno(lista_entrenos):
    tipos = []
    for entrenos in lista_entrenos:
        tipos.append(entrenos['tipo'])
    return tipos
        
    
    
    
    



            


        
