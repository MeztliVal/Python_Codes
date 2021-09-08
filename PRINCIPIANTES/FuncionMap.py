#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:57:15 2021
Utilizando funcion map con PF
@author: meztli
"""
def doblar(numero): 
    return numero*2
numeros = [2,5,20,65,110]
print("Lista Original:",numeros)
print("Lista con dobles:", list(map(doblar,numeros)))