# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:17:55 2021

@author: ACER PC
"""

nombres = ["Zoro", "Sanji", "Ussop", "Nami"]

#Imprimir desde el inicio hasta el indicado
print(nombres[:3])

#Desde el indice seleccionado hasta el final
print(nombres[1:])

#Modificar el valor de una lista
nombres[2] = "Daniela"
nombres[0] = "Benito Juarez"

for nombre in nombres:
    print(nombres)
else:
    print("No existen nombres en la lista")

#%% Largo de una lista
print(len(nombres)) #Len permite saber el tamaño de una lista

#%%Agregar elemento a la lista
nombres.append("Jaime Krauss") #Agrega al final de la lista un elemento

#%% Ejemplo de 3 listas
cliente = ["Maribel", "Daniela", "Isabella", "Haide"]
edad = [18,18,18,18]
direccion = ["Campestre", "Cañada", "G. Jardin", "R. Naranjos"]

for i in range(len(cliente)
    print(f'Cliente : {cliente[i]} Direccion : {direccion[i]} Edad: {edad[i]};')

#%% En una lista Vacia guarda las calificaciones de un alumno, indicando numero de calificaciones 

calificaciones = []
promedio = 0
nCalif = int(input("¿Cuantas calificaciones desea guardar?\n"))

for i in range(nCalif):
    calif = float (input(f'Calificacion \n'))
    calificaciones.append(calif)
    promedio += calif
    
promedio = promedio/nCalif    
print(calificaciones, "Y su promedio es: ", promedio)



#%%
agregar = "no"
usuarios =[]# nombres
edades = [] # edades
estados = [] # mayor o menor

agregar = input("Desea agregar un usuario nuevo? Responda si o no")

while(agregar == "si"):
    nombre = input("Cual es el nombre?")
    usuarios.append(nombre)
    edad = int(input("Cual es la edad?"))
    edades.append(edad)
    if (edad >=18):
        print("Mayor")
        estados.append("Mayor")
    else: 
        print("Menor")
        estados.append("Menor")
    agregar = input("Desea agregar otro usuario nuevo? Responda si o no")  
    
print(f'')





