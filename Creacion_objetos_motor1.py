# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:30:09 2022

@author: Patricio Haro
"""
class Motor:
    
     def __init__(self,var6,var,var1,var2,var3,var4,var5):
         self.nombre=var6
         self.numeroid=var1
         self.voltage=var
         self.potencia=var2
         self.corriente=var3
         self.frecuencia=var4
         self.factorpotencia=var5
         
     def velocidad(self,estado):
         print("Estado actual del motor:",estado)
         
Motor_Siemens=Motor("Siemens","440 Voltios","EASDFE567484-3","10 Kw","8 Amperios","60 Htz","0.97 Cosfi")
print("Nombre Motor:",Motor_Siemens.nombre)
print("Numero ID:", Motor_Siemens.numeroid)
print("Voltage:",Motor_Siemens.voltage)
print("Potencia:",Motor_Siemens.potencia)
print("Corriente:",Motor_Siemens.corriente)
print("Frecuencia:",Motor_Siemens.frecuencia)
print("Factor de Potencia:",Motor_Siemens.factorpotencia)
Motor_Siemens.velocidad("Motor fuera de funcionamiento\n")

Motor_abb=Motor("ABB","220 Voltios","ADDFE5I56-5","20 Kw","15 Amperios","60 Htz","0.94 Cosfi")
print("Nombre Motor:",Motor_abb.nombre)
print("Numero ID:", Motor_abb.numeroid)
print("Voltage:",Motor_abb.voltage)
print("Potencia:",Motor_abb.potencia)
print("Corriente:",Motor_abb.corriente)
print("Frecuencia:",Motor_abb.frecuencia)
print("Factor de Potencia:",Motor_abb.factorpotencia)
Motor_Siemens.velocidad("Motor en velocidad al 50 %\n")

Motor_lenz=Motor("Lenz","110 Voltios","YTUIO4533DF-8","3 Kw","1.5 Amperios","50 Htz","0.98 Cosfi")
print("Nombre Motor:",Motor_lenz.nombre)
print("Numero ID:", Motor_lenz.numeroid)
print("Voltage:",Motor_lenz.voltage)
print("Potencia:",Motor_lenz.potencia)
print("Corriente:",Motor_lenz.corriente)
print("Frecuencia:",Motor_lenz.frecuencia)
print("Factor de Potencia:",Motor_lenz.factorpotencia)
Motor_Siemens.velocidad("Motor encendido al 40 %\n")
        
    