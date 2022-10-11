# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:57:54 2022

@author: Patricio Haro
"""

class Casa:
    def __init__(self,var,var1,var2,var3,var4):
        self.propietario=var
        self.modelo=var1
        self.color=var2
        self.precio=var3
        self.tiempoconstruccion=var4
    def estadocasa(self,estado):
        print("Estado de la casa:",estado)
        
Casa_nueva=Casa("Patricio Haro","Casa 2 pisos, con pisina","Blanco franjas celestes","$80.000,00 dolares","2 Meses")
print("Propietario:",Casa_nueva.propietario)
print("Modelo:",Casa_nueva.modelo)
print("Color:",Casa_nueva.color)
print("Precio:",Casa_nueva.precio)
print("Tiempo de Contruccion:",Casa_nueva.tiempoconstruccion)
Casa_nueva.estadocasa("Terminando de construir(Nueva)\n")

Casa_seminueva=Casa("Medardo Gonzalez","Casa 1 piso, con parqueadero","Amarillo franjas blancas","$50.000,00 dolares","10 años")
print("Propietario:",Casa_seminueva.propietario)
print("Modelo:",Casa_seminueva.modelo)
print("Color:",Casa_seminueva.color)
print("Precio:",Casa_seminueva.precio)
print("Tiempo de Contruccion:",Casa_seminueva.tiempoconstruccion)
Casa_seminueva.estadocasa("Medio uso\n")

Casa_vieja=Casa("Jairo Pedrasa","Casa 3 pisos,pisina y parqueadero","verde, blanco franjas negras","$60.000,00 dolares","35 años")
print("Propietario:",Casa_vieja.propietario)
print("Modelo:",Casa_vieja.modelo)
print("Color:",Casa_vieja.color)
print("Precio:",Casa_vieja.precio)
print("Tiempo de Contruccion:",Casa_vieja.tiempoconstruccion)
Casa_vieja.estadocasa("Muchos años de construccion(Vieja)")