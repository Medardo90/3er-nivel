# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:09:51 2022

@author: lab
"""

class vehiculo:
    
    def __init__(self,var,var1): # metodo constructor
       self.placa=var1
       self.marca=""
       self.modelo=""
       self.color=var
    def aceleracion(self,estado):
        print("estado actual del vehiculoes:", estado)

# ceacond de objetos

obj_vehiculo1 = vehiculo("rojo", "1231312")
print("color",obj_vehiculo1.color)

print("placa",obj_vehiculo1.placa)
obj_vehiculo1.aceleracion("estacionado\n")

vehiculo_joel= vehiculo("amarillo","309473974")
print("color",vehiculo_joel.color)
print("placa",vehiculo_joel.placa)
vehiculo_joel.aceleracion("70km/h")

vehiculo_pedro= vehiculo("verde", "405984085")
print("color",vehiculo_pedro.color)
print("placa",vehiculo_pedro.placa)
vehiculo_pedro.aceleracion("40km/h")


