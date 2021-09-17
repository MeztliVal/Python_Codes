#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:20:24 2021
Mi Tercer diccionario
@author: meztli
"""
usuarios={'nombre':'Mario','Apaterno':'Ruiz','edad':45,'telefono':'8751099','sexo':'M'}
nombre_completo=usuarios['nombre']+' '+usuarios['Apaterno']
#print(nombre_completo)
#print(usuarios['edad'])
#print(usuarios['telefono'])
#print(usuarios['sexo'])
for clave in usuarios:
    print(clave)
