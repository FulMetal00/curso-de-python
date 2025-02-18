# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:48:34 2024

@author: wpomp
"""

#######resolver una ecuación de segundo grado (ax² + bx + c = 0) usando Python#######

import math

# Solicitar los coeficientes al usuario
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Verificar si el discriminante es negativo, cero o positivo
if discriminante < 0:
    print("La ecuación no tiene soluciones reales.")
elif discriminante == 0:
    x = -b / (2*a)
    print(f"La ecuación tiene una solución: {x}")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"La ecuación tiene dos soluciones: {x1} y {x2}")
    
    
    
#######otra forma de resolver ecuaciones cuadraticas#####
from math import sqrt

A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))
x1= 0
x2= 0

if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)

# texto añadido desde local en la rama master
#texto añadido desde local a github
#texto añadido en la nube
