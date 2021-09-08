#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:55:22 2021
Abriendo xml y extrayendo informacion con P.Funcional
@author: meztli
"""
import xml.etree.ElementTree as ET
tree = ET.parse('SPA PIEL ORIGINAL.xml')
root = tree.getroot()
h,m=0,0
def nombres(cliente):
    return cliente.attrib

def hombre(x):
    if x.text == "H":
        return "H"
    else:
        return "M"

def fechas(fecha):
    return fecha.text

def serv(tipo):
    return tipo.text
    
print("\t === REPORTE DE CLIENTES === \n")
clientes=list(map(nombres,root.iter('cliente')))
sexos=list(map(hombre,root.iter('sexo')))
date=list(map(fechas,root.iter('fecha')))
servicios = list(map(serv,root.iter('servicio')))
print(servicios)
print("Total de clientes varones:",h)
#print("Total de clientes mujeres:",m)
