from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black,blue,red,purple,pink
import xml.etree.ElementTree as ET
tree = ET.parse('contactos.xml')
root = tree.getroot()
    
def lee_xml():
    rank_list,name_list,year_list,tel_list=[],[],[],[]
    telefono_dic = {}
    for rank in root.iter('rank'):
        rank_list.append(rank.text)
    for name in root.iter('contact'):
       name_list.append(name.text)
    for year in root.iter('year'):
        year_list.append(year.text)
    for tel in root.iter('telephone'):
        telefono_dic=tel.attrib
        tel_list.append(telefono_dic)
        
       
    c=canvas.Canvas("Reporte de Contactos.pdf",pagesize= letter)
    c.setFont('Courier-BoldOblique',10)
    c.setFillColor(black)
    c.drawString(30,760,'REPORTE DE :')
    c.setFillColor(purple)
    c.drawString(130,760,'Contactos')
    c.line(115,757,220,757)
    c.drawImage("wonder_tux.jpeg",500,700,width=100,height=100)
    a,x=12,0
    for child in root:
        atrib_pais = child.attrib
        c.setFillColor(blue) 
        c.drawString(150,650-a,'Pais:')
        c.drawString(190,650-a,atrib_pais['name'])
        c.drawString(300,650-a,'Continente:')
        c.drawString(390,650-a,atrib_pais['continent'])
        c.setFillColor(black) 
        c.drawString(170,640-a,'Nombre del Contacto:')
        c.drawString(310,640-a,name_list[x])
        c.drawString(170,630-a,'Rank:')
        c.drawString(310,630-a,rank_list[x])
        c.drawString(410,630-a,'Año:')
        c.drawString(460,630-a,year_list[x])
        c.drawString(170,620-a,'Telefono:')
        c.drawString(310,620-a,tel_list[x]['number'])
        c.drawString(410,620-a,'Ciudad:')
        c.setFillColor(red) 
        c.drawString(460,620-a,tel_list[x]['city'])
        x+=1
        a+=50
        
        
    
    c.save()
    
lee_xml()