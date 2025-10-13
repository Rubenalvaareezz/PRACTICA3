from entrenos import lee_entrenos
from entrenos import tipo_entreno


entrenamientos = lee_entrenos("data/entrenos.csv")
for r in entrenamientos[:3  ]: 
    print(r)

for r in entrenamientos[-3: ]: 
    print(r)

tipo_entrenos = tipo_entreno("data/entrenos.csv")
orden = tipo_entrenos(tipo_entreno)
orden.sort()
print(orden)