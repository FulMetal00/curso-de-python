# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:36:28 2024

@author: wpomp
"""

####################
## PROBLEM SET 1 a
####################
#Cuantos meses se tarda en ahorrar la entrada del pago de comprar casa#


annual_salary = float(input("ingrese su salario anual "))
portion_saved = float(input("ingrese el porcentaje del salario que va a ahorrar en decimales "))
total_cost = float(input("ingrese el valor de su casa "))

portion_down_payment = 0.25 * total_cost
#asumo que el porcentaje del pago icicial para comprar la casa es 25% #

current_savings = 0
#asumo que el ahorro inicial es 0 

##Inversion del ahorro#  #investments = current_savings*r/12
r = 0.04 
#Asumo que r es retorno de inversion anual con 4%
investments = 0

monthly_salary = annual_salary/12
#salario mensual

saved = portion_saved*monthly_salary
#Ahorro de salario

n = 0  
#### n es Number of months (contador)#


while portion_down_payment > current_savings :
        current_savings += investments + saved 
        #Incremento del ahorro a final de mes
        
        investments = current_savings*r/12
        n = n + 1

print("el numero de meses para ahorrar el pago inicial es ", n)