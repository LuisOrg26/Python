# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:41:12 2021

@author: ACER PC
"""

#%%Ciclo While

"""Solicitar una contraseña y la confirmacion de ella y dar
la bienvenida al ususario cuando coincida (si importa el orden M y m)
"""
errores = 0
password = input("Ingrese la contrasela que desea utilizar: ")
passconfirm = input("Confirme su contraseña: ")

while (password != passconfirm):
    passconfirm = input("La contraseña no coincide, vuelva a ingresarla: ")
    errores += 1
    if (errores >= 3):
        print("se equivoco muchas veces por lo tanto solicite ayuda")
        break

if (errores < 3):
    numerror = "errores"
    if (errores == 1):
        str.replace("errores","error")
        
    
        
    print("Se ha dado de alta exitosamente con ", errores, numerror)
#%%Fibonashe
