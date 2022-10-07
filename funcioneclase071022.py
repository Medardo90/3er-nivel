# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#funciones
# def funcion():
#     print("hola")
#     for i in range(5):
#         print(i)
        
# funcion()  
# funcion() 
# funcion()
# funcion() 

# con parmetros invocar la funcion ejemplo var 

# def funcion(var):
#     print("hola")
#     for i in range(var):
#         print(i)
        
# funcion(2)
# funcion(5)
# funcion(9)
# funcion(100)

# con 2 en var parmetros invocar la funcion ejemplo var 

# def funcion(var1,var2):
#     print("hola")
#     for i in range(var1, var2):
#         print(i)
        
# funcion(2,5)
# funcion(7,9)
# funcion(1,4)
# funcion(10,13)

# 

# def funcion(var1,var2):
#     print("hola")
#     for i in range(var1, var2):
#         print(i)
        
# funcion(2,5)
# funcion(9,4) #no se va imprimir por que el nueve es mayor 
# # que el 4 debe ser siempre mayor el primer munero
# funcion(1,4)
# funcion(10,13)

# sumar el total de las var 

# def funcion(var1,var2):
#     ac=0
#     print("hola")
#     for i in range(var1, var2):
#         print(i)
#         ac=ac+i
#     print("acumulado", ac)
        
# funcion(2,5)
# funcion(9,4) #no se va imprimir por que el nueve es mayor 
# # que el 4 debe ser siempre mayor el primer munero
# funcion(1,4)
# funcion(10,13)


# def funcion(var1,var2):
#     ac=0
#     print("hola")
#     for i in range(var1, var2):
#         print(i)
#         ac=ac+i
#     print("acumulado dentro", ac)
#     return ac
        
# ac= funcion(2,5)
# print("ac fuera de la funcion", ac)
# ac= funcion(9,14) #no se va imprimir por que el nueve es mayor 
# print("ac fuera de la funcion", ac)


def funcion(var1,var2):
    ac=0
    print("hola")
    for i in range(var1, var2):
        print(i)
        ac=ac+i
    print("acumulado dentro", ac)
    return ac
        
pepito = funcion(2,5)
print("ac fuera de la funcion", pepito)
ac= funcion(9,14) #no se va imprimir por que el nueve es mayor 
print("ac fuera de la funcion", ac)


