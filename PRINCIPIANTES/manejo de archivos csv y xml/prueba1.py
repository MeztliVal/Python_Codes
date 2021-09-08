#importando libreria nuestra para manejo de archivos
import lib20

#Menu de creacion de archivos
r = 's'           #variable de control de ciclo
while r == 's' or r == 'S':
    print("Bienvenido al menu del programa para creacióon y modificación de archivos\n\n")
    print( '============== MENU ==============\n')
    print('1)Crear Archivo\n')
    print('2)Agergar Información\n')
    print('3)Visualizar Contenido del Archivo\n')
    print('4)Salir del Menú\n')

    opcion = int(input('Teclea una opción:'))
    if opcion == 1:
        nombre = input("Teclea el nombre del archivo con extension .txt:")
        archivo = lib20.crear_archivo(nombre)
    elif opcion == 2:
        nombre = input("Teclea el nombre del archivo con extension .txt al que deseas agregar un registro:")
        resp = 's'
        while resp == 'S' or resp == 's':
            ncontrol = input('Teclea el No.de Control:') + '-'
            paterno = input('Teclea el Apellido Paterno:') + '-'
            materno = input('Teclea el Apellido Materno:') + '-'
            nombre_alumno = input('Teclea el Nombre(s):')
            agrega = ncontrol +  paterno + materno + nombre_alumno
            lib20.modifica_archivo(nombre, agrega)    
            resp = input('Deseas añadir mas registros al archivo?[S/n]')
    elif opcion == 3:
        nombre = input("Teclea el nombre del archivo con extension .txt que deseas ver:")
        lib20.leer_archivo(nombre)
    
    elif opcion ==4:
         print('Saliendo del menú....')
    else:
        print('Opción incorrecta.... BYE')
    r = input('Desea regresar al menu?[S/n]:')