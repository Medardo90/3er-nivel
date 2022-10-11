# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:23:33 2022

@author: Patricio Haro
"""

class Celular:
    def __init__(self,var,var1,var2,var3,var4):
        self.propietario=var
        self.modelo=var1
        self.color=var2
        self.precio=var3
        self.tiempouso=var4
    def estadocell(self,estado):
        print("Estado Smarphone:",estado)
        
Celular_nuevo=Celular("Pablo Oña","Samsung Galaxi S9","Negro","$600,00 dolares","1 Mes")
print("Propietario:",Celular_nuevo.propietario)
print("Modelo:",Celular_nuevo.modelo)
print("Color:",Celular_nuevo.color)
print("Precio:",Celular_nuevo.precio)
print("Tiempo de uso:",Celular_nuevo.tiempouso)
Celular_nuevo.estadocell("(Nueva)\n")

Celular_viejo=Celular("Patricio Haro","Samsung Galaxi A50","Blanco","$450,00 dolares","10 años")
print("Propietario:",Celular_viejo.propietario)
print("Modelo:",Celular_viejo.modelo)
print("Color:",Celular_viejo.color)
print("Precio:",Celular_viejo.precio)
print("Tiempo de uso:",Celular_viejo.tiempouso)
Celular_viejo.estadocell("(Viejo)\n")

Celular_mediouso=Celular("Ricardo Ferraño","Samsung Galaxi S10 NOTE-PLUS","Aura Glass","$700,00 dolares","2 años")
print("Propietario:",Celular_mediouso.propietario)
print("Modelo:",Celular_mediouso.modelo)
print("Color:",Celular_mediouso.color)
print("Precio:",Celular_mediouso.precio)
print("Tiempo de uso:",Celular_mediouso.tiempouso)
Celular_mediouso.estadocell("(Medio uso)\n")