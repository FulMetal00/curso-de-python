# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:20:03 2024

@author: wpomp
"""

####################
## PROBLEM SET 1 b
####################
#Cuantos meses se tarda en ahorrar la entrada del pago de comprar casa#
#Si cada 6 meses suben el salario#

annual_salary = float(input("ingrese su salario anual "))
portion_saved = float(input("ingrese el porcentaje del salario que va a ahorrar en decimales "))
total_cost = float(input("ingrese el valor de su casa "))
semi_annual_raise = float(input("ingrese el porcentaje del aumento salarial en decimales "))

portion_down_payment = 0.25 * total_cost
#asumo que el porcentaje del pago icicial para comprar la casa es 25% #

current_savings = 0
#asumo que el ahorro inicial es 0 

##Inversion del ahorro#  #investments = current_savings*r/12
r = 0.04 
#Asumo que r es retorno de inversion anual con 4%
investments = 0
investments = current_savings*r/12
monthly_salary = annual_salary/12
#salario mensual

monthly_salary_actual = monthly_salary
#salario actual que se aumentara cada 6 meses

saved = portion_saved*monthly_salary_actual
#Ahorro de salario


n = 1  
#### n es Number of months (contador)#


while current_savings < portion_down_payment :
    if n % 6 == 0 :
        monthly_salary_actual *= (1 + semi_annual_raise)
    
    current_savings += investments + saved 
    #Incremento del ahorro a final de mes
    
    investments = current_savings*r/12
    saved = portion_saved*monthly_salary_actual    
             
    n = n + 1   
     
            
print("el numero de meses para ahorrar el pago inicial es ", n - 1)