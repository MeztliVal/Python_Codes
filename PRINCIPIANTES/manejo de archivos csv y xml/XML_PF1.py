#Inportando libreria para XML
import xml.etree.ElementTree as ET
tree = ET.parse('contactos.xml')
root = tree.getroot()

def child(name):
    return name.attrib

def imprime(name):
    return  name.tag, name.text

print("\nPF imprimiendo años")
print(list(map(imprime,root.iter('year'))))

print("\nPF imprimiendo RANK")
print(list(map(imprime,root.iter('rank'))))

print("\nPF imprimiendo COUNTRY")
print(list(map(child,root.iter('country'))))

print("\nPF imprimiendo TELEFONOS")
print(list(map(child,root.iter('telephone'))))
