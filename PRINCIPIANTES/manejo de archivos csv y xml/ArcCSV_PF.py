import csv
def extrae(lista): 
    k= lista[0]+"IC"
    return k
nombre="/home/meztli/Documentos/CODIGOS_PYTHON/archivos/pato.csv"
with open(nombre) as csv_arch:
    print(list(map(extrae,csv.reader(csv_arch,delimiter='-'))))