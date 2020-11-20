#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:43:18 2020

@author: camilanahuel
"""

import preguntas as p


p1 = p.Preguntas(1)
n1 = p1.Preguntas_nivel(1)

if n1 == True:
    p2 = p.Preguntas(2)
    n2 = p2.Preguntas_nivel(2)
    if n2 == True:
        p3 = p.Preguntas(3)
        n3 = p3.Preguntas_nivel(3)
        if n3 == True:
            print("show final screen")
else:
    a = input("If you want to start over press enter ")
    if a == "":
        print("Restart")
    else:
        print("Bye")
        
            




