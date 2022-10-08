# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:13:01 2022

@author: Patricio Haro
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:09:51 2022

@author: lab
"""


class Vehiculo: #Propiedades-atributos
    
    def __init__(self,var,var1,var2,var3,var4): # metodo constructor
       self.placa=var1
       self.marca=var2
       self.modelo=var3
       self.color=var
       self.propietario=var4
    def aceleración(self,estado): #Conportamiento-Metodos
        print("El estado actual del vehiculo:",estado)
        

""" Creación de objetos"""


obj_Vehiculo1 = Vehiculo("ROJO", "PCV-3598" ,"MAZDA", "CX-3","PATRICIO HARO")
print("Propietario:",obj_Vehiculo1.propietario)
print("Color:",obj_Vehiculo1.color)
print("Placa:",obj_Vehiculo1.placa)
print("Marca:",obj_Vehiculo1.marca)
print("Modelo:",obj_Vehiculo1.modelo)
obj_Vehiculo1.aceleración("ESTACIONADO\n")

Vehiculo_Joel= Vehiculo("AMARILLO","PFG-5678","TOYOTA","HILUX 4X4","JOEL GONZALEZ")
print("Propietario:",Vehiculo_Joel.propietario)
print("Color:",Vehiculo_Joel.color)
print("Placa:",Vehiculo_Joel.placa)
print("Marca:",Vehiculo_Joel.marca)
print("Modelo:",Vehiculo_Joel.modelo)
Vehiculo_Joel.aceleración("EN ACELERACIÓN, 70 km/h\n")

Vehiculo_Pedro= Vehiculo("Verde", "TRS-1243","FORD","F-250","PEDRO FUENTES")
print("Propietario:",Vehiculo_Pedro.propietario)
print("Placa:",Vehiculo_Pedro.placa)
print("Marca:",Vehiculo_Pedro.marca)
print("Modelo:",Vehiculo_Pedro.modelo)
Vehiculo_Pedro.aceleración("EN ACELERACIÓN, 40 km/h\n")

