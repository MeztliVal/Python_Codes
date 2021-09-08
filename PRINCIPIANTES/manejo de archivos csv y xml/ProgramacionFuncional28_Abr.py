#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:16:34 2021
Funcion Map con Lambda y doble lista
@author: meztli
"""
a = [1,2,3,4,5,6,7,8,9,10]
b = [4,4,4,4,4,4,4,4,4,4]
print(list(map(lambda x,y: x*y, a,b)))