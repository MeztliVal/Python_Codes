#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:02:21 2021
Ejercicio de herencia Multiple udemy
@author: meztli
"""
class A:
    def __init__(self):
        print("Soy de Clase A")
        
    def a(self):
        print("Este método lo heredo de A")
        
class B:
    def __init__(self):
        print("Soy de Clase B")
        
    def b(self):
        print("Este método lo heredo de B")

class C(A,B): #Esta clase hereda de Ay B al mismo tiempo
    
    def c(self):
        print("Este método es de único de C")

class D(B,A): #Esta clase hereda de Ay B al mismo tiempo
    pass

c = C()   #Creando instancia de clase C
d = D()
print(c)
print(d)
print("Obteniendo acceso a metodos del objeto c")
print(c.a())
print(c.b())
print(c.c())