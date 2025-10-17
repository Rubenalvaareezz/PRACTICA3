from entrenos import *
from datetime import datetime



if __name__ == "__main__":
    entrenamientos = lee_entrenos("data/entrenos.csv")
    for r in entrenamientos[:3  ]: 
        print(r)

    for r in entrenamientos[-3: ]: 
        print(r)

   
    orden = tipo_entreno(entrenamientos)
    print(f"Tipos de entreno: {orden}")

    # d = int(input("Introduce una duración de entreno: "))
    # tiempo_entrenos = duracion_entreno(entrenamientos,d)
    # for r in tiempo_entrenos:
    #     print(f"Los entrenos de mayor duracion que d son : {r}")

    
    # f_inicial = input("Introduzca una fecha inicial (dd/mm/YYYY): ")
    # f_final = input("Introduzca una fecha final (dd/mm/YYYY): ")
    # fecha_inical = datetime.strptime(f_inicial, "%d/%m/%Y").date()
    # fecha_final = datetime.strptime(f_final, "%d/%m/%Y").date()   
    # entrenos_fecha= suma_calorias(entrenamientos, fecha_inical, fecha_final)

    mayor_duracion = mas_km(entrenamientos)
    
      
                                   
    
   