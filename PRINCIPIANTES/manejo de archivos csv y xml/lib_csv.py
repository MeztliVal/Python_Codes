#Liberias para que pueda funcionar el código
import os
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black,blue,red,purple,pink

#Función que llama a las funciones escribe_csv y lee_csv
def crear_reporte_existencias():
    nombre=input("Teclea el archivo a reportar:")
    escribe_csv(nombre)
    resp = input("¿Deseas agregar un comentario al archivo?[Yes/No]:")
    comentario(resp)
    lee_csv('Reporte Existencias Porrua.csv',resp)
    print("Reporte de Existencias creado con exito")


#Funcion para leer archivo csv
def lee_csv(archivo,resp):
    c=canvas.Canvas("Reporte_Existencias_Porrua.pdf",pagesize= letter)
    c.setFont('Courier-BoldOblique',10)
    c.setFillColor(black)
    c.drawString(30,760,'REPORTE DE :')
    c.setFillColor(purple)
    c.drawString(230,760,'Titulos en Existencia')
    c.line(225,757,380,757)
    c.setFillColor(blue) 
    c.drawImage("tulipanes.png",50,150,width=100,height=100)
    cont=1
    cont_dig= cont2=0
    with open(archivo) as csv_arch:
        entrada = csv.reader(csv_arch,skipinitialspace=True, strict=True)
        for reg in entrada:
            cont+=1
            if cont<2:
                pass
            else:
                if reg[2]=="DIGITAL":
                    cont_dig+=1
                c.drawString(30,700-cont2,reg[0])
                c.drawString(56,700-cont2,reg[1])
                c.drawString(296,700-cont2,reg[2])
                c.drawString(480,700-cont2,reg[3])
                
                cont2+=12
        cf=str(cont-2-cont_dig)
        cd=str(cont_dig)
        c.setFillColor(red)
        c.drawString(30,700-(cont2+12),"Total de Libros Físicos:")
        c.drawString(215,700-(cont2+12),cf)
        c.drawString(30,700-(cont2+24),"Total de Libros Digitales:")
        c.drawString(215,700-(cont2+24),cd)
    if resp =="Yes" or resp=="YES" or resp=="yes":
        c.setFillColor(black)
        c.drawString(30,700-(cont2+36),"Comentarios:")
        archivo = open("/home/meztli/Documentos/CODIGOS_PYTHON/archivos/comentarios.txt", "r")
        c.setFillColor(purple)
        contenido = archivo.read()
        a=0
        b=90
        cont3 = cont2+48
        if len(contenido)>120:
            long = int(len(contenido)/90)
            for numero in range(long):
                renglon = contenido[a:b]
                print(renglon,a,b)
                c.drawString(30,700-cont3,renglon)
                a=b+1
                b+=91
                cont3+=12
        else:
            c.drawString(30,700-cont3,contenido)
    
    c.save()


#Función para escribir archivo csv que será desplegado en el archivo PDF
def escribe_csv(archivo):
    with open(archivo) as csv_arch:
        entrada = csv.reader(csv_arch,delimiter=',')
        csv_salida = open('Reporte Existencias Porrua.csv','w',newline='')
        salida = csv.writer(csv_salida,delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
        conta=0
        for registro in entrada:
            if conta==0:
                salida.writerow([registro[0],registro[1],registro[7],registro[12]])
            elif conta>=1 and registro[7]=="FISICO": 
                k = int(registro[10])-int(registro[11])
                registro[12]=str(k)
                salida.writerow([registro[0],registro[1],registro[7],registro[12]])
            elif conta>=1 and registro[7]=="DIGITAL":
                registro[12]="NA"
                salida.writerow([registro[0],registro[1],registro[7],registro[12]])
            
            conta+=1
        csv_salida.close()


#Función para escribir un comentario dentro del archivo PDF
def comentario(resp):
    if resp=="Yes" or resp=="YES" or resp=="yes" or "y":
        print("Cuando termines de agregar el comentario presiona la tecla -enter- ")
        comenta=input("Ahora Teclea el comentario a agregar:")
        arch_comentarios = open("/home/meztli/Documentos/CODIGOS_PYTHON/archivos/comentarios.txt", "w")
        arch_comentarios.write(comenta)
        arch_comentarios.close

