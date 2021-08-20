
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:53:30 2021
Ejercicio de Herencia Curos Python Udemy3
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
    if(isinstance(p,Adorno)):
        print(p.referencia,p.nombre)
    elif(isinstance(p,Alimento)):
        print(p.referencia,p.nombre,p.productor)
    elif(isinstance(p,Libro)):
        print(p.referencia,p.nombre,p.isbn)
        

def rebajar_producto(p,rebaja):
    """Devuelve el producto con una rebaja en porcentaje de su precio"""
    p.precio = p.precio - (p.precio/100*rebaja)
    return p

al_rebajado = rebajar_producto(al,10)
print(al_rebajado)

#INTENGO DE COPIAR UN OBJETO CON EL SIMBOLO DE IGUAL

copia_al = al
copia_al.referencia=1983
print("====Imprimiento la copia de al ====\n",copia_al)

print("Imprimiento el original de al despues de haber sido copiado con el simbolo =\n",al)
"""No se puede hacer una copia del objeto con el simbolo de = ya que solo estamos haciendo una
   asignación simple del objeto"""
   
#COMO SE DEBE COPIAR CORRECTAMENTE UNA LISTA
lista1=[1,2,3]
lista2= lista1
lista2.append(4)
print("Contenido de lista1 \n",lista1)
print("Contenido de lista2 \n",lista2)
#Para copiarlo correctamente hacemos esto:
l3 = lista1[:]
l3.append(5)
print("Copiando lista1 a lista3",l3)
print("Contenido de lista1 \n",lista1)
print("Contenido de lista3 \n",l3)

#Para copiar un objeto hay ue importar el modulo copy

import copy

copia_ad=copy.copy(a)
print(copia_ad)
copia_ad.precio = 106
print("Imprimiendo Copia de Objeto Adorno \n",copia_ad)
print("Imprimiendo Objeto Adorno Original \n",a)