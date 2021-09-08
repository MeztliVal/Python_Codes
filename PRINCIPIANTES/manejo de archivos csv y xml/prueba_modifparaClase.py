from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black,blue,red,purple,pink,green
import xml.etree.ElementTree as ET
tree = ET.parse('automotriz.xml')
root = tree.getroot()

def lee_xml():
    todos_list = []
    x,ch,cm = 0, 0,0
    for child in root:
        atrib_vendedor = child.attrib
        todos_list.append(atrib_vendedor)
  
    for sexo in root.iter('sexo'):
        if sexo.text == 'M':
            todos_list[x]['sexo']= 'M'
            cm+=1
        else:
            ch+=1
            todos_list[x]['sexo']= 'H'
        x+=1
        
    a,b=12,0    
    c=canvas.Canvas("Reporte de Vendedores.pdf",pagesize= letter)
    c.setFont('Courier-BoldOblique',10)
    c.setFillColor(black)
    c.drawString(30,760,'REPORTE DE :')
    c.setFillColor(purple)
    c.drawString(130,760,'Vendedores')
    c.line(115,757,220,757)
    c.drawImage("wonder_tux.jpeg",500,700,width=100,height=100)
    c.drawString(100,720-a,'Total de Mujeres:')
    c.drawString(210,720-a,str(cm))
    c.drawString(300,720-a,'Total de Hombres:')
    c.drawString(420,720-a,str(ch))
    c.drawString(30,696-a,'NP')
    c.drawString(65,696-a,'Paterno')
    c.drawString(185,696-a,'Materno')
    c.drawString(315,696-a,'Nombre')
    c.setFillColor(green)
    x=0
    for element in todos_list:
        sexo=todos_list[b]['sexo']
        if sexo=="M":
            x+=1
            c.drawString(30,684-a,str(x))
            c.drawString(65,684-a,todos_list[b]['paterno'])
            c.drawString(185,684-a,todos_list[b]['materno'])
            c.drawString(315,684-a,todos_list[b]['nombre'])
            a+=12
        b+=1
 
  
    c.save()
  
lee_xml()