#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:09:34 2021
Mi primer Diccionario
@author: meztli
"""
colores={'amarillo':'yellow','cafe':'brown','negro':'black','naranja':'orange'}
print(colores)
for color_esp in colores:
    print(color_esp)
del(colores['cafe'])
print(colores)
for color_esp in colores:
    print(color_esp)