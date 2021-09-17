#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:33:36 2021
Diccionario 4
@author: meztli
"""
personajes = [{'Nombre':'Draco Malfoy','status':'sangre pura','varita':'avellano'}]

harry={'Nombre':'Harry Potter','status':'meztizo','varita':'roble'}
hermione = {'Nombre':'Hermione Granger','status':'sangre sucia','varita':'fresno'}
ron = {'Nombre':'Ronald Weasley','status':'sangre pura','varita':'arce'}

personajes.append(harry)
personajes.append(hermione)
personajes.append(ron)


for personaje in personajes:
    print(personaje['Nombre'],personaje['status'],personaje['varita'])