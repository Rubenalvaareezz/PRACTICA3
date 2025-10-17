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
    tipos = {entrenos[0] for entrenos in lista_entrenos}
    return sorted(tipos)

def duracion_entreno(lista_entrenos,d):
    lista_mas_duracion_d = []
    for entreno in lista_entrenos:
        if entreno.duracion > d:
            lista_mas_duracion_d.append(entreno)
    return lista_mas_duracion_d

def suma_calorias(lista_entrenos,f_inicial,f_final):
    calorias = 0
    lista_entrenamientos_fechas = []
    for entreno in lista_entrenos:
        if entreno[1] >= f_inicial and entreno[1]<= f_final:
            lista_entrenamientos_fechas.append(entreno)
            calorias += entreno[4]
    return print(f"La suma de las calorias de todos los entrenos es:{calorias} calorias")
        
def mas_km(lista_entrenos):
    lista_entrenamiento_mas_km = lista_entrenos[0]
    for entreno in lista_entrenos:
        if entreno[5] > lista_entrenamiento_mas_km[5]:
            lista_entrenamiento_mas_km = entreno
        else:
            lista_entrenamiento_mas_km = lista_entrenamiento_mas_km
    return print(f"El entrenamiento de mayor duracion es: {lista_entrenamiento_mas_km}")
    
    
    



            


        
