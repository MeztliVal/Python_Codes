#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:53:30 2021
Ejercicio de Herencia Curos Python Udemy
@author: meztli
"""
class Producto:     #Creando la clase madre
    def __init__(self,referencia,nombre,precio,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}""".format(self.referencia,self.nombre,self.precio,self.descripcion)

class Adorno(Producto): #Creando la subclase Adorno, y para indicar que es hija de producto, sele pasa como parametro
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.precio,self.descripcion,self.productor,self.distribuidor)

class Libro(Producto):
    autor= ""
    isbn = ""
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
AUTOR\t\t{}
ISBN\t\t{}""".format(self.referencia,self.nombre,self.precio,self.descripcion,self.autor,self.isbn)


a = Adorno(2034, "vaso adornado",15,"vaso de porcelana adornado con arboles")
print(a)

al = Alimento(1067,"Botella de aceite de oliva",5,"Botella de 250 ml extra")
al.productor="La aceitera"
al.distribuidor="Distribuciones SA"
print(al)
li = Libro(1048,"Cocina mediterranea",9,"Recetas de cocina vegana")
li.autor="Mario Gomez Vargas"
li.isbn = "0-123-543-22-8"
print(li)

#Agrupando objetos en una lista
productos = [a,al]
print(productos)
productos.append(li)
print(productos)
for p in productos:
    print(p,"\n")
for p in productos:
    print(p.referencia,p.nombre,"\n")
for p in productos:
    print(p.autor,"\n") #Esta linea da error porque no existe en atributo autor en adorno