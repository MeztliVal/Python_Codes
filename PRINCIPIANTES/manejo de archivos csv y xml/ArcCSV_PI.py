import csv
nombre="/home/meztli/Documentos/CODIGOS_PYTHON/archivos/pato.csv"
with open(nombre) as csv_arch:
    entrada = csv.reader(csv_arch,delimiter=',')
    for registro in entrada:
        print (registro)