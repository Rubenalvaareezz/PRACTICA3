import csv
from collections import namedtuple
from datetime import datetime


entrenos = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
 
ruta_csv = "data/entrenos.csv.csv"


def lee_entrenos(ruta_csv):
    with open (ruta_csv, encoding = "utf-8") as f:
        lector = csv.reader(f)
        lista_entrenos = []
        for entreno , tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = str(tipo)
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M" ).date()
            ubicacion = str(ubicacion)
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
        
