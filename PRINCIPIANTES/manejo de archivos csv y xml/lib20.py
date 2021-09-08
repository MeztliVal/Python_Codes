#LIBRERIA PARA MANIPULACION DE ARCHIVOS 
import os    #libreria para manipulacion del sistema

#Funcion para crear archivos
def crear_archivo(archivo):
    direccion = '/home/meztli/Documentos/CODIGOS_PYTHON/archivos/'
    direccion_completa = direccion + archivo
    file = open(direccion_completa, "w+")
    print('Archivo: ' + archivo + ' ha sido creado correctamente')
    return file

#Funcion que modifica un archivo
def modifica_archivo(archivo,agrega):
    direccion = '/home/meztli/Documentos/CODIGOS_PYTHON/archivos/'
    direccion_completa = direccion + archivo
    file = open(direccion_completa, "a+")
    file.write(agrega + os.linesep)
    print('Archivo ' + archivo + ' modificado')
    cerrar_archivo(file)
    
#Funcion para cerrar archivos
def cerrar_archivo(file):
    file.close()
    print('\nArchivo cerrado correctamente')

#Funcion para visualizar contenido de un archivo
def leer_archivo(archivo):
    direccion = '/home/meztli/Documentos/CODIGOS_PYTHON/archivos/'
    direccion_completa = direccion + archivo
    file = open(direccion_completa, "r+")
    print('Imprimiendo contenido de archivo\n')
    i = 0
    for linea in file:
        linea = linea.rstrip("\n")
        print(linea)
        i+=1
    cerrar_archivo(file)    