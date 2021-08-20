#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:23:45 2021
Ejercicio de Herencia Curos Python Udemy
@author: meztli
"""
class Producto:
    def __init__(self,referencia,tipo,nombre,precio,descripcion,productor=None,
                 distribuidor=None,isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor
    
adorno = Producto ("000A", "adorno", "vaso adornado", 12, "vaso de porcelana con dibujos")

print(adorno)
print(adorno.tipo)
