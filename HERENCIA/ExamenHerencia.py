#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:31:19 2021
Ejercicio de Examen de Herencia Udemy
@author: meztli
"""
class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format(self.color,self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ",{} km/hr , {} cc".format(self.velocidad,self.cilindrada)
    
class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga
        
    def __str__(self):
        return super().__str__() + ", {} Kg de carga".format(self.carga)
    
class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return super().__str__() + ", tipo {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} Km/hr , {} cc".format(self.velocidad,self.cilindrada)
    
vehiculos = [
        Coche("azul",4,150,1200),
        Camioneta("blanco",4,100,1300,1500),
        Bicicleta("verde",2,"urbana"),
        Motocicleta("negro",2,"deportiva",180,900)
]

def catalogar(lista):
    for v in lista:
        print("{}: {}".format(type(v).__name__, v))

print(catalogar(vehiculos))

def catalogar(lista):
    for v in lista:
        if ruedas == None:
            print("{}: {}".format(type(v).__name__, v))

print(catalogar(vehiculos))

