from lxml import etree

doc = etree.parse('contactos.xml')
print etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")