#modificando archivos
#importando libreria nuestra para manejo de archivos
import lib20
print("Rellenando archivos...")
nombre = input("Teclea el nombre del archivo con extension .txt al que deseas agregar un registro:")
resp = 's'
while resp == 'S' or resp == 's':
    print("Ingresa los siguientes datos:")
    ncontrol = input('Teclea el No.de Control:') + '-'
    paterno = input('Teclea el Apellido Paterno:') + '-'
    materno = input('Teclea el Apellido Materno:') + '-'
    nombre_alumno = input('Teclea el Nombre(s):')
    agrega = ncontrol +  paterno + materno + nombre_alumno
    lib20.modifica_archivo(nombre, agrega)    
    resp = input('Deseas añadir mas registros al archivo?[S/n]')