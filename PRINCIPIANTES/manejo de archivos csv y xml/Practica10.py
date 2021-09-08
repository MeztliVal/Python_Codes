from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black,blue,red,purple,pink
import xml.etree.ElementTree as ET

def haciendo_pdf(autor,formato,editorial, precio,inventario):
    print('Creando archivo PDF')
    c=canvas.Canvas("Reporte de Libros.pdf",pagesize= letter)
    c.setFont('Courier-BoldOblique',10)
    c.setFillColor(black)
    c.drawString(30,760,'REPORTE DE :')
    c.setFillColor(red)
    c.drawString(130,760,'Libros')
    c.line(115,757,220,757)
    c.drawImage("wonder_tux.jpeg",500,700,width=100,height=100)
    x,a=0,0
    for child in root:
        libro = child.attrib
        c.setFillColor(purple)
        c.drawString(100,720-a,'Nombre del Libro:')
        c.drawString(220,720-a,libro['nombre'])
        c.line(210,717-a,480,717-a)
        c.setFillColor(blue)
        c.drawString(100,700-a,'Idioma:')
        c.drawString(220,700-a,libro['idioma'])
        c.line(210,698-a,270,698-a)
        c.drawString(350,700-a,'Formato:')
        c.drawString(420,700-a,formato[x])
        c.line(410,698-a,480,698-a)
        c.drawString(100,680-a,'Autor:')
        c.drawString(220,680-a,autor[x])
        c.line(210,678-a,330,678-a)
        c.drawString(350,680-a,'Precio:')
        precio_modif = '$' + precio[x]+'.00'
        c.drawString(420,680-a,precio_modif)
        c.line(410,678-a,480,678-a)
        c.drawString(100,660-a,'Editorial:')
        c.drawString(220,660-a,editorial[x])
        c.line(210,658-a,330,658-a)
        c.drawString(350,660-a,'Existencias:')
        total=str(int(inventario['almacen'])-int(inventario['vendidos']))
        c.drawString(440,660-a,total)
        c.line(420,658-a,480,658-a)
        x+=1
        a+=100
    c.save()

tree = ET.parse('libreria.xml')
root = tree.getroot()
autor_list, formato_list, editorial_list, precio_list= [],[],[],[]
inv, libros = {}, {}
for autor in root.iter('autor'): 
    autor_list.append(autor.text)
for formato in root.iter('formato'):
    formato_list.append(formato.text)
for editorial in root.iter('editorial'):
    editorial_list.append(editorial.text)
for precio in root.iter('precio'):
    precio_list.append(precio.text)
for inventario in root.iter('inventario'):
    inv = inventario.attrib
    
haciendo_pdf(autor_list,formato_list,editorial_list,precio_list,inv)
    

    