#Importando libreria para XML
import xml.etree.ElementTree as ET

tree = ET.parse('contactos.xml')
root = tree.getroot()
print(root)

print("\nImprimiendo hijos con Atributos")
for child in root:
    print(child.tag, child.attrib)
    
print("\nImprimiendo RANKS por tag")
for rank in root.iter('rank'):
    print(rank.text)

print("\nImprimiento Contactos")
for name in root.iter('contact'):
    print(name.text)